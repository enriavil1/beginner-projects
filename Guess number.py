from random import randint


user_num =  input("How many numbers do you want to guess \n")
user_num_int = int(user_num)

number_list = list(range(0, user_num_int + 1))
number_randomly_generated = randint(0, user_num_int + 1)


user_guess = int(input("Guess a number! \n"))

counter = 0
counter_limit = (4 * user_num_int/10)
if type(counter_limit) != int():
    counter_limit = round(counter_limit)


if user_guess == number_randomly_generated:
    print("Congratulations, you guessed it on your first try \n")
else:
        while(user_guess is not number_randomly_generated):
            if counter > counter_limit:
                print("you have reached the limit in tries. You have lost!")
                break
            if user_guess < number_randomly_generated:
                counter += 1
                print("too low, try again \n")
                counter_limit = counter_limit - 1
                print("you have this many guesses left: {} \n".format(counter_limit))
                user_guess = int(input("Guess a number!"))
            if(user_guess > number_randomly_generated):
                counter += 1
                print("too high, try again \n")
                counter_limit = counter_limit - 1
                print("you have this many guesses left: {} \n".format(counter_limit))
                user_guess = int(input("Guess a number!"))  
            if(user_guess == number_randomly_generated):
                print("Congratulations you guessed the number in {}".format(counter))
                break

















