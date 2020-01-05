from random import choice, sample, random
from string import ascii_letters, digits, punctuation

def password_generator(how_many_numbers,how_many_points,letters_in_password):
    numbers = "".join([choice(digits) for i in range(int(how_many_numbers))])
    letters = "".join([choice(ascii_letters) for i in range(int(letters_in_password))])
    special_characters = "".join([choice(punctuation)for i in range(int(how_many_points))])
    together = numbers + letters + special_characters
    all_together = "".join(sample(together, len(together)))
    return print("this is your new password: " + all_together + "\n")



if __name__ == "__main__":

    print("\nWelcome to password generator!!\n")

    while(True):

        length_of_password = input("how long do you want your password to be?\n")
        how_many_numbers = input("how many numbers do you want in your password?\n")
        how_many_points = input("how many special characters do you want\n")
        letters_in_password = (int(length_of_password) -  int(how_many_numbers)) - int(how_many_points)


        if letters_in_password < 1:
            print("please make it so there is at least one letter\n")     
        else:
            if int(how_many_points) >= int(length_of_password) - int(how_many_numbers):
                length_change = input("wanna cxhange the length of your password")
                if length_change == "yes":
                    length_of_password = input("how long do you want your password to be?\n")
            else:
                if int(how_many_numbers) >= int(length_of_password) - int(how_many_points):
                    length_change = input("wanna change the length of your password")
                    if length_change == "yes":
                        length_of_password = input("how long do you want your password to be?\n")
                else:
                    password_generator(how_many_numbers, how_many_points, letters_in_password)
                    break






