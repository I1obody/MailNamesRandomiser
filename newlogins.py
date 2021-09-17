import random
import string


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    rang_string = ''.join(random.sample(letters_and_digits, length))
    path = '/Users/I1obody/Desktop/random_logins_and_pass/random_logins_and_pass.txt'
    random_logins_and_pass = open(path,'a')
    title = 'login: '
    titlle = ' password: '
    gmail =  '@outlook.com '
    random_logins_and_pass.write('\n' + title + rand_string + gmail + titlle + rang_string)
    random_logins_and_pass.close()

generate_alphanum_random_string(10)