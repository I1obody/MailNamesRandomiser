import random
import string


def MailNamesAndPassRandomiser(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    rang_string = ''.join(random.sample(letters_and_digits, length))
    path = 'random_logins_and_pass.txt'
    random_logins_and_pass = open(path,'a')
    title = 'login: '
    titlle = ' password: '
    gmail =  '@outlook.com ' #u can change it on smt like  @gmail.com and etc
    random_logins_and_pass.write('\n' + title + rand_string + gmail + titlle + rang_string)
    random_logins_and_pass.close()

MailNamesAndPassRandomiser(10) #change ten on any other number for switch length
