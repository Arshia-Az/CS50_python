import random



def check_geuss(num):
    while True:
        user_guess = input("Guess: ")
        if user_guess.isdigit():
            if int(user_guess) >= 0:
                if num == int(user_guess):
                    print("Just right!")
                    break
                elif num > int(user_guess):
                    print("Too small!")
                else:
                    print("Too large!")
            else:
                 check_geuss()
        else:
             pass



def main():
    while True:
        try:
            level = int(input("Level: "))
            num = random.randint(1, level)
            check_geuss(num)
            break

        except ValueError:
            pass





if __name__ == "__main__":
     main()

