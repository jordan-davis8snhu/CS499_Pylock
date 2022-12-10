This is pylock, a command-line service for storing passwords in a single place, hidden behind a master password and encryption. 
To begin the service, you will of course need to first install the requirements. Then, navigate to the location of the program in a terminal and execute:
 python3 master.py
If it is your first time running the service, you will be prompted to create a master password. 
This is the single password you will use to access the program's functionality. 
After setting the master password, you will be asked for it everytime you start the service.

I will briefly demonstrate here how the program is used. There are 5 possible commands:
[generate][manual][get][update][delete]

[generate] and [manual] are our 'create' commands. 

[GENERATE] will randomly generate a password for you when given a service, username and desired password length. 

Format: [generate][service][username][password length]

The command would look like this on the command-line:

'generate gmail jordand 32' 

this command would generate a 32-character password for the username jordand for the service gmail.

[MANUAL] is the command to use if you want to insert a username/password that alrady exists. It is similar to generate, 
but you will enter your password itself rather than a desired length to generate. for example:

Format: [manual][service][username][password]

'manual gmail jordand badpassword'

[GET] is simply a read command. It will copy the password you retrieve straight to the clipboard and not display it.
Format: [get][service][username]

'get gmail jordand'

[UPDATE] will update an existing entry. 

Format: [update][service][username][new password]

'update gmail jordand newpassword'

[DELETE] will delete an entry. 

Format: [delete][service][username]

'delete gmail jordand'

finally you MUST use the exit command to quit the program for now. This command executes the final encryption.