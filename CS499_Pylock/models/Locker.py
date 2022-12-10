# Where CRUD functions are stored, as well as functions for reading and setting data
import json

from database import db_tools as data


# Locker class contains the CRUD functions
class Locker:

    login_list = []

    def __init__(self, service: str, user: str,  path: str):
        """

        :param service:
        :param user: associated user name
        :param path: password path
        """
        self.path = path
        self.service = service
        self.user = user

    def get_logins(self):
        self.login_list = []
        with open(self.path, 'r') as f:
            for login in f:
                self.login_list.append(json.loads(login))

        return self.login_list

    def set_logins(self):
        with open(self.path, 'w') as f:
            for d in self.login_list:
                f.write(json.dumps(dict(d)))
                f.write('\n')

    def get_login_dict(self):
        for d in self.login_list:
            if self.service in d:
                if self.user in d[self.service]:
                    return d

    def create(self, db: str, cursor: str, password: str):
        """

        :param password: associated password
        :return:
        """
        self.get_logins()

        d = self.get_login_dict()
        if d is not None:
            response = 'credentials already exist'
            return response
        else:
            login = {
                self.service: {
                    self.user: password
                }
            }
            with open(self.path, 'a+') as f:
                f.write(json.dumps(dict(login)))
                f.write('\n')

            try:
                data.insert_data(cursor, db, self.service, self.user, password)
            except Exception as e:
                print(e)
                pass

            response = 'login created'
            return response

    def read(self):
        self.get_logins()

        d = self.get_login_dict()
        if d is None:
            response = 'credentials invalid'
            return response
        else:
            password = (d[self.service][self.user])
            return password

    def delete(self, cursor, db):
        self.get_logins()

        d = self.get_login_dict()
        if d is None:
            response = 'credentials invalid'
            return response
        else:
            del(d[self.service])
            self.set_logins()

            try:
                data.delete_data(cursor, db, self.service, self.user)
            except Exception as e:
                print(e)
                pass

            response = 'deletion successful'
            return response

    def update(self, cursor: str, db: str, new_pass: str):
        """

        :param new_pass: updated password
        :return:
        """
        self.get_logins()

        d = self.get_login_dict()
        if d is None:
            response = 'credentials invalid'
            return response
        else:
            d[self.service][self.user] = new_pass
            self.set_logins()

            data.update_data(cursor, db, self.service, self.user, new_pass)
            response = 'credentials updated'
            return response
