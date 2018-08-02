# --- Define your functions below! ---
def introduction():
    print ("Hello! Welcome to Chatbot!")

def process_input(userInput):
    greetings = ["Hi", 'hi', "hello", "Hello", "hey", "Hey", "Hallo", "hallo", "good morning", "good afternoon", "ciao"]
    if userInput in greetings:
        return True
    else:
        return False

def game(yn):
    if yn == "yes":
        answer1 = input("Do you wear glasses?")
        if answer1 == "yes":
            print ("Me too!")
        elif answer1 == "no":
            print ("Ok; next question: ")
        answer2 = input("Do you wear a watch?")
        if answer2 == "yes":
            print ("Cool! Me too!")
        if answer2 == "no":
            print ("Ok; next question: ")
        answer3 = input("Do you have a twin?")
        if answer3 == "yes":
            print ("Cool! So do I!")
        if answer3 == "no":
            print ("Ok; next question: ")
        answer4 = input("Do you speak another language?")
        if answer4 == "yes":
            print ("A bilingual! Me too!")
        if answer4 == "no":
            print ("That's OK. Next question: ")
        answer5 = input("Do you play a sport?")
        if answer5 == "yes":
            print ("Good job!")
        if answer5 == "no":
            print ("Neither do I; next question: ")
        answer6 = input("Do you like to read?")
        if answer6 == "yes":
            print ("A fellow book worm!")
        if answer6 == "no":
            print ("Ok; next question: ")
        answer7 = input("Are you vegetarian?")
        if answer7 == "yes":
            print ("Nice! Next question:")
        if answer7 == "no":
            print ("That's OK. Next question: ")
        answer8 = input("Do you like dark chocolate?")
        if answer8 == "yes":
            print ("Lovely. Me too!")
        if answer8 == "no":
            print ("Ok; next question: ")
        answer9 = input("Do you have your driving permit or license?")
        if answer9 == "yes":
            print ("Nice! Me too!")
        if answer9 == "no":
            print ("It's Ok! Next question: ")
        answer10 = input("Do you like to take naps?")
        if answer10 == "yes":
            print ("Me too! They are the best!")
            print ("Ok, this is the end of 'Yes or No'. Thanks for playing with me.")
        if answer10 == "no":
            print ("Ok, this is the end of 'Yes or No'. Thank you for playing with me.")
    if yn == "no":
        print("OK then")
def game2(tot):
    if tot == "yes":
        print ("Please enter your responses with the exact spelling as in the question. Thank you.")
        answera = input("introvert or extrovert?")
        if answera == ("introvert"):
            print ("Me too!")
        if answera == "extrovert":
            print ("Ok, next question:")
        answerb = input("summer or winter?")
        if answerb == ("winter"):
                print ("Me too!")
        if answerb == ("summer"):
                print ("It's summer time! Next question:")
        answerc = input("indoors or outdoors?")
        if answerc == ("indoors"):
            print ("Me too!")
        if answerc == "outdoors":
            print ("Good for you! Next question:")
        answerd = input("mbta or driving?")
        if answerd == ("mbta"):
            print ("Me too!")
        if answerd == "driving":
            print ("Ok, next question:")
        answere = input("fries or chips?")
        if answere == "fries" or answere == "chips":
            print ("Cool! Next question:")
        answerf = input("cats or dogs?")
        if answerf == "cats" or answerf == "dogs":
            print("Cool! Next question:")
        answerg = input("tea or coffee?")
        if answerg == ("tea"):
            print ("Awesome!Me too!")
        if answerg == "coffee":
            print ("Cool! Next question:")
        answerh = input("peanut butter or nutella? Enter 'pb' or 'n'.")
        if answerh == ("pb"):
            print ("Me too!")
        if answerh == ("n"):
                print ("Sweet! Next question:")
        answeri = input("pancake or waffles?")
        if answeri == ("pancake") or answeri == ("waffles"):
            print ("Cool! Next question")
        answerj = input("sunrise or sunset?")
        if answerj == ("sunrise") or answerj == ("sunset"):
            print ("Beautiful!")
            print ("OK, this is the end of 'This or That'. Thanks for playing with me.")
    if tot == ("no"):
        print ("OK then")

# --- Put your main program below! ---
def main():
    introduction()
    while True:
        username = input("What's your name?")
        print ("My name is Q, the chatbot.")
        answer = input("(What will you say?)")
        valid = process_input(answer)
        if valid == True:
            print ("Hi!")
        if valid == False:
            print ("That's cool!")
        print("What do you want to chat about now?")
        print("I know! We can play 'Yes or No'.")
        yn = input("Do you want to play'Yes or No'?")
        game(yn)
        tot = input("Do you want to play 'This or That'?")
        game2(tot)
        print("I enjoyed chatting with you,", username+"! Now I know you much better. See you next time!")
        print("Bye!")
        break


# DON'T TOUCH! Setup code that runs your main() function.Start running from main()
if __name__ == "__main__":
  main()
