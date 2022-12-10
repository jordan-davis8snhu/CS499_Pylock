# contains main()/ command-line functionality
import mysql.connector
import sys
import os
import string
import random

import pyperclip

from initialize import initialize, get_master
from models.Locker import Locker
from models.Crypto import Crypto
from config import HOST, USER, PASS, MASTER_PASS_FILE, PASS_KEY_FILE, PASS_FILE


# Generate random password based on desired length
def gen_pass(length: int):
    """

    :param length: password length
    :return:
    """

    characters = string.ascii_letters + string.digits + string.punctuation

    return "".join((random.choice(characters)) for i in range(length))


def main():

    db = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASS,
    )

    # cursor object
    cursor = db.cursor()

    if not os.path.exists(MASTER_PASS_FILE):
        initialize(db, cursor)

    user_pass = input(str('master password: '))

    master_pass = get_master()

    if user_pass == master_pass:
        print('password accepted')

        pass_crypto = Crypto(PASS_FILE, PASS_KEY_FILE)

        try:
            r = pass_crypto.decrypt()
            if r == 'key is invalid':
                pass
        except FileNotFoundError:
            pass

        while True:

            arg = list(input('>>> ').split(' '))

            command = arg[0]
            # commands go in order of [command][service][username][password]
            if command in ('generate', 'manual', 'get', 'update', 'delete'):

                pass_locker = Locker(arg[1], arg[2], PASS_FILE)

                if command == 'generate':
                    if len(arg) == 4:
                        response = pass_locker.create(db, cursor, gen_pass(int(arg[3])))
                        print(response)
                    else:
                        print('command entered incorrectly')
                elif command == 'manual':
                    if len(arg) == 4:
                        response = pass_locker.create(db, cursor, arg[3])
                        print(response)
                    else:
                        print('command entered incorrectly')
                elif command == 'get':
                    if len(arg) == 3:
                        response = pass_locker.read()
                        if response == 'credentials invalid':
                            print(response)
                        else:
                            pyperclip.copy(response)
                            print('password copied to clipboard')
                    else:
                        print('command entered incorrectly')
                elif command == 'update':
                    if len(arg) == 4:
                        response = pass_locker.update(cursor, db, arg[3])
                        print(response)
                    else:
                        print('command entered incorrectly')
                elif command == 'delete':
                    if len(arg) == 3:
                        response = pass_locker.delete(cursor, db)
                        print(response)
                    else:
                        print('command entered incorrectly')

            elif command == 'exit':
                pass_crypto.encrypt()
                db.close()
                sys.exit()

            else:
                print(command + ' is not an accepted command')

    else:
        print('invalid password')
        sys.exit()


if __name__ == '__main__':
    main()
