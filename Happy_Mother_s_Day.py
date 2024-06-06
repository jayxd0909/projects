import getpass
import random
import string

while True:
    print("Happy Mother's Day Mom! I have programmed a Mad Libs program for you. Hope you enjoy!")

    name1 = input("\nEnter a name: ")
    gender = input("\nIs this person a boy or a girl? ")
    place1 = input("\nEnter a place: ")
    thing1 = input("\nEnter a noun (plural): ")
    place2 = input("\nEnter a place: ")
    relative1 = input("\nEnter a familial relation: ")
    name2 = input("\nEnter a name: ")
    number1 = input("\nEnter a number: ")
    enemyp = input("\nEnter the enemy of the hero (plural): ")
    Cenemyp = enemyp.title()
    enemys = input("\nEnter the enemy of the hero (singular): ")
    vehicle = input("\nEnter a vehicle: ")
    number2 = input("\nEnter a number: ")
    name3 = input("\nEnter a name: ")
    store = input("\nEnter a store: ")
    name4 = input("\nEnter a name: ")

    if gender == "boy":
        pronoun1 = "his"
        Cpronoun1 = "His"
        pronoun2 = "he"
        Cpronoun2 = "He"
        pronoun3 = "gentleman"
        pronoun4 = "him"
    else:
        pronoun1 = "her"
        Cpronoun1 = "Her"
        pronoun2 = "she"
        Cpronoun2 = "She"
        pronoun3 = "gentlewoman"
        pronoun4 = "her"

    if enemys[0] in "aeiou":
        article = "an"
        Carticle = "An"
    else:
        article = "a"
        Carticle = "A"

    print("\nOk, all done! Ready for your beautiful story? I don't know if you are. This could be rough. Well, here we go. Press Enter to continue.")
    getpass.getpass("")
    readingStory = True
    while(readingStory):
        makingChoice = False
        loss = False
        evil = False
        explosion = False
        LarryHater = False
        prison = False
        win = False
        print("The legendary hero's name is", name1 + ".")
        getpass.getpass("")
        print(name1, "comes from", place1 + ".")
        getpass.getpass("")
        print(name1, "loves", thing1 + ".")
        getpass.getpass("")
        print(name1, "heard from", pronoun1, relative1, name2, "that there is a lot of", thing1, "in", place2 + ".")
        getpass.getpass("")
        print("So, naturally,", name1, "has only one dream in", pronoun1, "life: to go to", place2 + ".")
        getpass.getpass("")
        print("This has been", name1 + "'s dream for", number1, "years.")
        getpass.getpass("")
        print("This morning, when our hero awoke, they knew today was the day. The day they would make the long journey to", place2 + ".")
        getpass.getpass("")
        print("This journey will be difficult. There are many", enemyp, "that want to get all the", thing1, "in", place2, "for themselves!")
        getpass.getpass("")
        print("Those jerks! The", thing1, "belong to", name1 + "!")
        getpass.getpass("")
        print("Yup,", name1, "has had enough of this. Today is the day.")
        getpass.getpass("")
        print("With these thoughts in", pronoun1, "mind,", name1 + ", with", pronoun1, "fabulous", vehicle + ", rode away from", place1 + ". Who knows when", name1, "will return. Maybe never. Maybe never ever. But", pronoun2, "could. But also might not. Who knows?")
        getpass.getpass("")
        print("After", number2, "hours of travel,", name1, "encountered", pronoun1, "first obstacle. The", enemyp, "have set up a roadblock on the only path to", place2 + "!")
        getpass.getpass("")
        print(Carticle, enemys, "stops you at the gate. What does", name1, "do?\n")
        print("1 | Punch him in the face")
        print("2 | Turn around and go back to", place1 + ".")
        print("3 | Ask nicely. It might work.\n")
        choice1 = input()
    
        makingChoice = True
        while(makingChoice):
            if choice1 == "1":
                makingChoice = False
                evil = True
                LarryHater = True
                print("\nThe", enemys, "falls over. He wails \"WHYYYYY?!?\" as he falls to the ground.")
                getpass.getpass("")
                print("\"You--\" he coughs. \"You... didn't have to do that.\"")
                getpass.getpass("")
                print("\"You could have... asked nicely.\"")
                getpass.getpass("")
                print("\"I... would have let you through... bruh...\"")
                getpass.getpass("")
                print("\"You have blood on your hands now.\"")
                getpass.getpass("")
                print("\"BLOOD!!!\"")
                getpass.getpass("")
                print("\"ON YOUR HANDS!!!\"")
                getpass.getpass("")
                print("He dies.")
                getpass.getpass("")
                print(name1, "did not expect this.")
                getpass.getpass("")
                print(name1, "feels kind of bad.")
                getpass.getpass("")
                print("But oh well, it is worth it for the", thing1 + ".", name1, "continues on.")
                getpass.getpass("")
            elif choice1 == "2":
                loss = True
                makingChoice = False
                print("\nWhy would you choose this option? You loser! Don't you care about", thing1 + "?!? Disguting. You lose. Press Enter to restart the story. Do better next time, geez!")
                getpass.getpass("")
            elif choice1 == "3":
                makingChoice = False
                print("\n\"Hello sir, would you mind letting me pass through?\"")
                getpass.getpass("")
                print("\"You seem like an upstanding", pronoun3 + ". Absolutely!\"")
                getpass.getpass("")
                print("The gate opens and you are let through. That was easier than expected. Are these bad guys really bad?", name1, "continues on.")
                getpass.getpass("")
            else:
                choice1 = input("\nInvalid input. Try again: ")

        if(loss):
            continue

        print("It wasn't long before", name1, "encountered", pronoun1, "next trial.")
        getpass.getpass("")

        sign = 1
        right = []
        for i in range(11):
            r = random.randint(0,1)
            if r == 0:
                right.append("l")
            else:
                right.append("r")
        #right = ["l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l", "l"]

        while(sign<11):
            print("There is a sign with a '" + str(sign) + "'. There is also a fork in the road. Do you want to go left (l) or right (r)?")
            direction = getpass.getpass("")
            if direction == right[sign]:
                sign = sign + 1
            else:
                sign = 1

        print("You made it! The journey continues.")
        getpass.getpass("")
        print(name1, "has made it to the midpoint of", pronoun1, "journey.")
        getpass.getpass("")
        print(Cpronoun2, "recognizes the area", pronoun2, "is in.", Cpronoun2, "has a friend here named", name3, "who owns a nearby", store + ".")
        getpass.getpass("")
        print(Cpronoun2, "decides to visit.")
        getpass.getpass("")
        print("\"Hello", name1 + "!\" welcomes", name3 + ". What would you like to purchase?")
        print("You have $100. The items at", store, "are listed below.")
        print("1 | Cookie | Cost: $1")
        print("2 | Bomb | Cost: $50")
        print("3 | Dog | Cost: $100")
        print("4 | Exit\n")
        choice2 = input()
    
        makingChoice = True
        cookies = 0
        bombs = 0
        dogCount = 0
        money = 100
        while(makingChoice and money > 0):
            if choice2 == "1":
                if(money >= 1):
                    cookies = cookies + 1
                    money = money - 1
                    print("\nOoh, a cookie! Yum!")
                    if(money != 0):
                        print("Money: $" + str(money))
                        choice2 = input("Anything else? ")
                        continue
                    else:
                        print("\nNo more money! Time to leave.")
                        getpass.getpass("")
                else:
                    choice2 = input("\nInsufficient funds. Anything else? ")
                    continue
            elif choice2 == "2":
                if(money >= 50):
                    bombs = bombs + 1
                    money = money - 50
                    print("\nDo", store + "'s in real life sell bombs? Probably not. Good thing this isn't real life.")
                    if(money != 0):
                        print("Money: $" + str(money))
                        choice2 = input("Anything else? ")
                        continue
                    else:
                        print("\nNo more money! Time to leave.")
                        getpass.getpass("")
                else:
                    choice2 = input("\nInsufficient funds. Anything else? ")
                    continue
            elif choice2 == "3":
                if(money >= 100):
                    dogCount = dogCount + 1
                    money = 0
                    makingChoice = False
                    print("\nIs this really the time to be buying a dog? Well, he is cute...")
                    getpass.getpass("")
                    dog = input("What is his name? ")
                    print("\n" + dog + ", huh? Hope we didn't need anything else...")
                    getpass.getpass("")
                else:
                    choice2 = input("\nInsufficient funds. Anything else? ")
                    continue
            elif choice2 == "4":
                makingChoice = False
                print()
            else:
                choice2 = input("Invalid input. Try again: ")

        print("\"Farewell", name1 + ", good luck on your quest.\"")
        getpass.getpass("")
        print(number2, "more hours pass. We are almost to", place2 + ".")
        getpass.getpass("")
        print("All of a sudden you are brought to a halt.")
        getpass.getpass("")
        print("A nerdy voice calls out, \"Eureka! it's a success! My Gravitron Capacitance Reactor 4000 has captured a moving target!\"")
        getpass.getpass("")
        print("\"BRO! I'm trying to get to", place2 + "! Let me go!\"")
        getpass.getpass("")
        if bombs > 0:
            if gender == "boy":
                print(name1, "thinks about using", pronoun1, "bombs, but realizes the gravity would just make the bomb come back to", pronoun4 + ".")
                getpass.getpass("")
            else:
                print(name1, "thinks about using", pronoun1, "bombs, but realizes the gravity would just make the bomb come back to", pronoun1 + ".")
                getpass.getpass("")
        if evil:
            print("\"Oh, I know all about you,", name1 + ". News travels fast, I heard about you killing Larry over at the eastern roadblock. Not cool bro.\"")
            getpass.getpass("")
            print("\"Bro, he died in one punch! I didn't know he was that weak!\"")
            getpass.getpass("")
            print("\"Whatever makes you feel better about yourself, murderer.\"")
            getpass.getpass("")
        else:
            print("\"Oh, I know all about you,", name1 + ".\"")
            getpass.getpass("")
            print("\"How?\"")
            getpass.getpass("")
            print("\"Once you get to my intellectual level, you can do things that seem like magic to simpletons like yourself.\"")
            getpass.getpass("")

        print("\"bruh. what do you want from me then?\"")
        getpass.getpass("")
        print("\"Your company. It can get lonely sometimes, being a genius like myself :(\"")
        getpass.getpass("")
        print("\"My name is", name4, "by the way.\"")
        getpass.getpass("")
        print("\"I have devised a word game for you to play. If you win, I'll let you pass. If you fail, you will be sent back in time and teleported back to", place1 + ".\"")
        getpass.getpass("")
        print("\"You will have to guess a five-letter word. For each letter, I will tell you whether that letter is in the word in the right position, is in the word in the wrong position, or not in the word at all. I call it... Wordel.\"")
        getpass.getpass("")
        print("\"Isn't that Wordle?\"")
        getpass.getpass("")
        print("\"Yes, I told you already, it's Wordel\"")
        getpass.getpass("")
        print("\"Uh... nevermind...\"")
        getpass.getpass("")
        guess = input("\"Alright, let's begin! Please type guesses in all caps. First guess?\": ")

        count = 0
        word = "APPLE"
        while(count < 7):
            charcount = 0
            correct = 0
            Acount = 0
            Pcount = 0
            Lcount = 0
            Ecount = 0
            count = count + 1
            for char in guess:
                 if(char == 'A'):
                    Acount  = Acount + 1
                 if(char == 'P'):
                    Pcount  = Pcount + 1
                 if(char == 'L'):
                    Lcount  = Lcount + 1
                 if(char == 'E'):
                    Ecount  = Ecount + 1

            if(len(guess) == 5):
                for char in guess:
                    if(char in word):
                        if(char == word[charcount]):
                            print(char, "is in the correct spot.")
                            correct = correct + 1
                        else:
                            if(char == 'A'):
                                if(Acount > 1):
                                    print(char, "is not in the word.")
                                    Acount = Acount - 1
                                else:
                                    print(char, "is in the word, but not in the correct spot.")
                            if(char == 'P'):
                                if(Pcount > 2):
                                    print(char, "is not in the word.")
                                    Pcount = Pcount - 1
                                else:
                                    print(char, "is in the word, but not in the correct spot.")
                            if(char == 'L'):
                                if(Lcount > 1):
                                    print(char, "is not in the word.")
                                    Lcount = Lcount - 1
                                else:
                                    print(char, "is in the word, but not in the correct spot.")
                            if(char == 'E'):
                                if(Ecount > 1):
                                    print(char, "is not in the word.")
                                    Ecount = Ecount - 1
                                else:
                                    print(char, "is in the word, but not in the correct spot.")
                    else:
                        print(char, "is not in the word.")

                    charcount = charcount + 1
        
                if(correct == 5):
                    print("You got it! Newton thought up his theory of gravity from observing an apple falling you know. However, contrary to popular belief, it did not hit him on his head. Interesting how rumors spread. Thank you for your time. \nYou may pass.")
                    getpass.getpass("")
                    break
                if(count == 6):
                    loss = True
                    print("\nOut of guesses, sorry. Better luck next time. Bye.")
                    getpass.getpass("")
                elif(count == 5):
                    guess = input("\n\"Last guess. Make it count.\": ")
                else:
                    guess = input("\n\"Next guess?\": ")
            else:
                guess = input("\nInvalid input. Try again: ")
                count = count - 1

        if (loss):
            continue

        print("After many hours of travel,", name1, "has finally made it to", place2 + ".")
        getpass.getpass("")
        print("As expected, there is a hoard of", enemyp, "guarding the", thing1 + ".")
        getpass.getpass("")
        if(bombs != 0 or dogCount != 0):
            print("What does", name1, "do?\n")
            print("1 | Attack the enemy with fists!")
            if(bombs != 0):
                print("2 | Attack the enemy with a bomb!\n")
            else:
                print("2 | Send", dog, "after them!\n")
            choice4 = input()

            makingChoice = True
            while(makingChoice):
                if choice4 == "1":
                    makingChoice = False
                    print()
                    print(name1, "charges in on the enemy, fists ablazing.")
                    getpass.getpass("")
                    print("The fight seems to be going alright at first, but as it went on it was clear that", name1, "was beginning to get overwhelmed.")
                    getpass.getpass("")
                    print("The", enemyp, "just don't stop coming!")
                    getpass.getpass("")
                    print("Could this be it? Is the dream dead? Is this the end of", name1 + "?")
                    getpass.getpass("")
                elif choice4 == "2":
                    makingChoice = False
                    if(bombs != 0):
                        explosion = True
                        evil = True
                        print("\nThe bomb decimates all of the enemies surrounding the", thing1 + ".")
                        getpass.getpass("")
                        print("\"WAHOO!\"", name1, "exclaims as", pronoun2, "rushes towards the", thing1 + ".", Cpronoun1, "dream is finally about to become a reality.")
                        getpass.getpass("")
                    else:
                        print("\n" + dog, "charges in on the enemy, furiously barking.")
                        getpass.getpass("")
                        print("The fight seems to be going alright at first, but as it went on it was clear that", dog, "was beginning to get overwhelmed.")
                        getpass.getpass("")
                        print(name1, "joins the fight, fists ablazing.")
                        getpass.getpass("")
                        print("It helps, but it still isn't enough.")
                        getpass.getpass("")
                        print("The", enemyp, "just don't stop coming!")
                        getpass.getpass("")
                        print("Could this be it? Is the dream dead? Is this the end of", name1, "and", dog + "?")
                        getpass.getpass("")
                else:
                    choice4 = input("\nInvalid input. Try again: ")
        else:
            print(name1, "charges in on the enemy, fists ablazing.")
            getpass.getpass("")
            print("The fight seems to be going alright at first, but as it went on it was clear that", name1, "was beginning to get overwhelmed.")
            getpass.getpass("")
            print("The", enemyp, "just don't stop coming!")
            getpass.getpass("")
            print("Could this be it? Is the dream dead? Is this the end of", name1 + "?")
            getpass.getpass("")

        if explosion or not evil:
            print("\"STOP!\", a familiar voice shouts.\"")
            getpass.getpass("")

            if explosion:
                print(name1, "turns around.")
                getpass.getpass("")
            else:
                print("The fighting stops.", name1, "turns towards the direction of the voice.")
                getpass.getpass("")

            print("It's...", relative1, name2 + "!")
            getpass.getpass("")

            if explosion:
                print("\"I have worked too hard for this", name1 + ". You cannot have the", thing1 + ".\"")
                getpass.getpass("")
                print("\"The", enemyp + "? Were you behind them", relative1 + "?\"")
                getpass.getpass("")
                print("\"Yes. I did what I had to. It has been my lifelong dream to get all of the", thing1, "in", place2 + ".\"")
                getpass.getpass("")
                print("\"It was foolish of me to tell you about it. I should have known it would make you want the", thing1, "too.\"")
                getpass.getpass("")
                print("\"I... can't believe this... how could you?\"")
                getpass.getpass("")
                print("\"You would have done the same were you in my shoes. You know how strong the pull of", thing1, "is.\"")
                getpass.getpass("")
                print("\"You are already heading down the path. Using a bomb to kill all those", enemyp+".\"")
                getpass.getpass("")
                if LarryHater:
                    print("\"Killing Larry.\"")
                    getpass.getpass("")
                print("\"You will just get in the way.\"")
                getpass.getpass("")
                print("\"" + Cenemyp + "!\" More", enemyp, "approach the", thing1 + ". Prepare to attack.")
                getpass.getpass("")
            else:
                print("\"I have worked too hard for this", name1 + ". You cannot have the", thing1 + ".\"")
                getpass.getpass("")
                print("\"The", enemyp + "? Were you behind them", relative1 + "?\"")
                getpass.getpass("")
                print("\"Yes. I did what I had to. It has been my lifelong dream to get all of the", thing1, "in", place2 + ".\"")
                getpass.getpass("")
                print("\"It was foolish of me to tell you about it. I should have known it would make you want the", thing1, "too.\"")
                getpass.getpass("")
                print("\"I... can't believe this... how could you?\"")
                getpass.getpass("")
                print("\"I know, I know. But you know how strong the pull of", thing1, "is.\"")
                getpass.getpass("")
                print("\"I just can't let you destroy what I've been working so hard for.\"")
                getpass.getpass("")
                print("\"" + Cenemyp + "!\" More", enemyp, "approach the", thing1 + ". \"Prepare to capture", name1, "and put", pronoun4, "in the prison.\"")
                prison = True
                getpass.getpass("")
        else:
            if bombs != 0:
                yn = input("You still have a bomb. Do you want to use it? Type Y or N: ")
                makingDecision = True
                while(makingDecision):
                    if yn == "Y":
                        makingDecision = False
                        print("\nThe bomb decimates all of the enemies surrounding the", thing1 + ".")
                        getpass.getpass("")
                        print("\"WAHOO!\"", name1, "exclaims as", pronoun2, "rushes towards the", thing1 + ".", Cpronoun1, "dream is finally about to become a reality.")
                        getpass.getpass("")
                        print("\"STOP!\", a familiar voice shouts.\"")
                        getpass.getpass("")
                        print(name1, "turns around.")
                        getpass.getpass("")
                        print("It's...", relative1, name2 + "!")
                        getpass.getpass("")
                        if evil:
                            print("\"I have worked too hard for this", name1 + ". You cannot have the", thing1 + ".\"")
                            getpass.getpass("")
                            print("\"The", enemyp + "? Were you behind them", relative1 + "?\"")
                            getpass.getpass("")
                            print("\"Yes. I did what I had to. It has been my lifelong dream to get all of the", thing1, "in", place2 + ".\"")
                            getpass.getpass("")
                            print("\"It was foolish of me to tell you about it. I should have known it would make you want the", thing1, "too.\"")
                            getpass.getpass("")
                            print("\"I... can't believe this... how could you?\"")
                            getpass.getpass("")
                            print("\"You would have done the same were you in my shoes. You know how strong the pull of", thing1, "is.\"")
                            getpass.getpass("")
                            print("\"You are already heading down the path. Using a bomb to kill all those", enemyp+".\"")
                            getpass.getpass("")
                            if LarryHater:
                                print("\"Killing Larry.\"")
                                getpass.getpass("")
                            getpass.getpass("")
                            print("\"You will just get in the way.\"")
                            getpass.getpass("")
                            print("\"" + Cenemyp + "!\" More", enemyp, "approach the", thing1 + ". Prepare to attack.")
                            getpass.getpass("")
                        else:
                            print("\"I have worked too hard for this", name1 + ". You cannot have the", thing1 + ".\"")
                            getpass.getpass("")
                            print("\"The", enemyp + "? Were you behind them", relative1 + "?\"")
                            getpass.getpass("")
                            print("\"Yes. I did what I had to. It has been my lifelong dream to get all of the", thing1, "in", place2 + ".\"")
                            getpass.getpass("")
                            print("\"It was foolish of me to tell you about it. I should have known it would make you want the", thing1, "too.\"")
                            getpass.getpass("")
                            print("\"I... can't believe this... how could you?\"")
                            getpass.getpass("")
                            print("\"I know, I know. But you know how strong the pull of", thing1, "is.\"")
                            getpass.getpass("")
                            print("\"I just can't let you destroy what I've been working so hard for.\"")
                            getpass.getpass("")
                            print("\"" + Cenemyp + "!\" More", enemyp, "approach the", thing1 + ". \"Prepare to capture", name1, "and put", pronoun4, "in the prison.\"")
                            prison = True
                            getpass.getpass("")
                    elif yn == "N":
                        makingDecision = False
                        loss = True
                        print("\nYou needed to use it. You are dead. The story will restart.")
                        getpass.getpass("")
                    else:
                        yn = input("\nInvalid input. Try again: ")
            else:
                if evil:
                    print("Yes, yes it is. You could have made better decisions. The story will restart.")
                    getpass.getpass("")
                    continue
                else:
                    print("\"I have worked too hard for this", name1 + ". You cannot have the", thing1 + ".\"")
                    getpass.getpass("")
                    print("\"The", enemyp + "? Were you behind them", relative1 + "?\"")
                    getpass.getpass("")
                    print("\"Yes. I did what I had to. It has been my lifelong dream to get all of the", thing1, "in", place2 + ".\"")
                    getpass.getpass("")
                    print("\"It was foolish of me to tell you about it. I should have known it would make you want the", thing1, "too.\"")
                    getpass.getpass("")
                    print("\"I... can't believe this... how could you?\"")
                    getpass.getpass("")
                    print("\"I know, I know. But you know how strong the pull of", thing1, "is.\"")
                    getpass.getpass("")
                    print("\"I just can't let you destroy what I've been working so hard for.\"")
                    getpass.getpass("")
                    print("\"" + Cenemyp + "!\" More", enemyp, "approach the", thing1 + ". \"Prepare to capture", name1, "and put", pronoun4, "in the prison.\"")
                    prison = True
                    getpass.getpass("")
    
        if(loss):
                continue
    
        print("What does", name1, "do?\n")
        print("1 | Offer to share the", thing1 + ".")
        print("2 | Surrender.")
        if cookies > 0:
            print("3 | Offer some cookies.")
            if bombs > 0:
                print("4 | Use a bomb.\n")
                choice3 = input()
    
                makingChoice = True
                while(makingChoice):
                    if choice3 == "1":
                        makingChoice = False
                        if evil:
                            print("No, I don't think you are a good person. I don't want to share.\n")
                            choice3 = input()
                        else:
                            makingChoice = False
                            print("\n\"The", thing1, "don't have to belong to only me or only you. We can share!\"")
                            getpass.getpass("")
                            print("\"...share?\"") 
                            getpass.getpass("")
                            print("\"Share...\"") 
                            getpass.getpass("")
                            print("\"Share!\"") 
                            getpass.getpass("")
                            print("\"That sounds wonderful.\"")
                            getpass.getpass("")
                            print("\"" + name1, "and", pronoun1, relative1, name2, "owning all the", thing1 + "... together! Let's do it!\"")
                            getpass.getpass("")
                            print("You have achieved the \"Negotiator\" ending.")
                            win = True
                            getpass.getpass("")
                    elif choice3 == "2":
                        makingChoice = False
                        if prison:
                            print()
                            print("You have been thrown in the gulag.")
                            getpass.getpass("")
                            print("You have achieved the \"Sent to the Gulag\" ending.")
                            win = True
                            getpass.getpass("")
                        else:
                            print("You lose. The story will restart.")
                            getpass.getpass("")
                    elif choice3 == "3":
                        makingChoice = False
                        print()
                        print("\"Want some cookies?\"")
                        getpass.getpass("")
                        if evil:
                            print("No, I don't think you are a good person. I don't want anything from you.\n")
                            makingChoice = True
                            choice3 = input()
                        else:
                            print("\"Strange proposition... But how many are we talking?\"")
                            getpass.getpass("")
                            print("\"I have", str(cookies) + ".\"")
                            getpass.getpass("")
                            if cookies < 50:
                                print("\"Sorry, not enough for me.\"")
                                makingChoice = True
                                choice3 = input()
                            elif cookies < 100:
                                print("\"Ok, now we're talking.\"")
                                getpass.getpass("")
                                print("\"If you give me 50, I will let you go back to", place1 + ".\"\n")
                                yn2 = input("Do you want to give 50 cookies? Type Y or N: ")
                                makingDecision = True
                                while(makingDecision):
                                    if yn2 == "Y":
                                        makingDecision = False
                                        print("\n\"You are free to go.\"")
                                        getpass.getpass("")
                                        print("You have achieved the \"Escapee\" ending.")
                                        win = True
                                        getpass.getpass("")
                                    elif yn2 == "N":
                                        makingDecision = False
                                        makingChoice = True
                                        print("\n\"Well that was a waste of time.\"\n")
                                        choice3 = input()
                                    else:
                                        yn2 = input("\nInvalid input. Try again: ")
                            else:
                                print("\"Ooh, 100! Wow! How many are you willing to give?\"")
                                getpass.getpass("")
                                donation = input("How many do you want to give? ")
                                makingDecision = True
                                while(makingDecision):
                                    if(donation.isdigit()):
                                        if int(donation) < 50:
                                            makingDecision = False
                                            makingChoice = True
                                            print("\n\"Well that was a waste of time.\"")
                                            choice3 = input()
                                        elif int(donation) >= 50 and int(donation) < 100:
                                            makingDecision = False
                                            print("\n\"With that amount, you are free to go.\"")
                                            getpass.getpass("")
                                            print("You have achieved the \"Escapee\" ending.")
                                            win = True
                                            getpass.getpass("")
                                        elif int(donation) == 100:
                                            makingDecision = False
                                            print("\n\"Wow! How generous!\"")
                                            getpass.getpass("")
                                            print("\"For that, I will share the", thing1, "with you.\"")
                                            getpass.getpass("")
                                            print("\"Only someone special would willingly give 100 cookies.\"")
                                            getpass.getpass("")
                                            print("You have achieved the \"Philanthropist\" ending.")
                                            win = True
                                            getpass.getpass("")
                                        else:
                                            donation = input("You don't have that many. How many do you want to give? ")
                                    else:
                                        donation = input("You don't have that many. How many do you want to give? ")
                    elif choice3 == "4":
                        makingChoice = False
                        print("\n\"Take this", relative1 + "!\"")
                        getpass.getpass("")
                        print("BOOM!")
                        getpass.getpass("")
                        print("Well, you got what you wanted. But at what cost? You killed your", relative1 + ".")
                        getpass.getpass("")
                        if LarryHater and explosion:
                            print("And Larry.")
                            getpass.getpass("")
                            print("Congratulations. At every decision, you chose to be as destructive as possible. You are the lowest of the low. Enjoy your", thing1 + ", you despicable monster.")
                            getpass.getpass("")
                            print("You have achieved the \"Evilest\" ending.")
                            win = True
                            getpass.getpass("")
                        else:
                            if LarryHater:
                                print("And Larry.")
                                getpass.getpass("")
                            print("Congratulations. You monster.")
                            getpass.getpass("")
                            print("You have achieved the \"Evil\" ending.")
                            win = True
                            getpass.getpass("")
                    else:
                        choice3 = input("\nInvalid input. Try again: ")
            else:
                print()
                choice3 = input()
    
                makingChoice = True
                while(makingChoice):
                    if choice3 == "1":
                        makingChoice = False
                        if evil:
                            print("No, I don't think you are a good person. I don't want to share.\n")
                            choice3 = input()
                        else:
                            makingChoice = False
                            print("\n\"The", thing1, "don't have to belong to only me or only you. We can share!\"")
                            getpass.getpass("")
                            print("\"...share?\"") 
                            getpass.getpass("")
                            print("\"Share...\"") 
                            getpass.getpass("")
                            print("\"Share!\"") 
                            getpass.getpass("")
                            print("\"That sounds wonderful.\"")
                            getpass.getpass("")
                            print("\"" + name1, "and", pronoun1, relative1, name2, "owning all the", thing1 + "... together! Let's do it!\"")
                            getpass.getpass("")
                            if(cookies == 100):
                                print("\"Glad we got that taken care of. Now I can finally start devouring some of these 100 cookies I bought.\"")
                                getpass.getpass("")
                                print("\"Why did you buy that many cookies? And can I have one?\"")
                                getpass.getpass("")
                                print("\"You're saying that if you could have 100 cookies, you wouldn't take the opportunity?\"")
                                getpass.getpass("")
                                print("\"Ridiculous question", relative1 +".\"")
                                getpass.getpass("")
                                print("\"And no, you can't have any.\"")
                                getpass.getpass("")
                                print("\"Wow, rude.\"")
                                getpass.getpass("")
                                print("You have achieved the \"Cookie Monster\" ending.")
                                win = True
                                getpass.getpass("")
                            else:
                                print("You have achieved the \"Negotiator\" ending.")
                                win = True
                                getpass.getpass("")
                    elif choice3 == "2":
                        makingChoice = False
                        if prison:
                            print()
                            print("You have been thrown in the gulag.")
                            getpass.getpass("")
                            print("You have achieved the \"Sent to the Gulag\" ending.")
                            win = True
                            getpass.getpass("")
                        else:
                            print("You lose. The story will restart.")
                            getpass.getpass("")
                    elif choice3 == "3":
                        makingChoice = False
                        print()
                        print("\"Want some cookies?\"")
                        getpass.getpass("")
                        if evil:
                            print("No, I don't think you are a good person. I don't want anything from you.\n")
                            makingChoice = True
                            choice3 = input()
                        else:
                            print("\"Strange proposition... But how many are we talking?\"")
                            getpass.getpass("")
                            print("\"I have", str(cookies) + ".\"")
                            getpass.getpass("")
                            if cookies < 50:
                                print("\"Sorry, not enough for me.\"")
                                makingChoice = True
                                choice3 = input()
                            elif cookies < 100:
                                print("\"Ok, now we're talking.\"")
                                getpass.getpass("")
                                print("\"If you give me 50, I will let you go back to", place1 + ".\"\n")
                                yn2 = input("Do you want to give 50 cookies? Type Y or N: ")
                                makingDecision = True
                                while(makingDecision):
                                    if yn2 == "Y":
                                        makingDecision = False
                                        print("\n\"You are free to go.\"")
                                        getpass.getpass("")
                                        print("You have achieved the \"Escapee\" ending.")
                                        win = True
                                        getpass.getpass("")
                                    elif yn2 == "N":
                                        makingDecision = False
                                        makingChoice = True
                                        print("\n\"Well that was a waste of time.\"\n")
                                        choice3 = input()
                                    else:
                                        yn2 = input("\nInvalid input. Try again: ")
                            else:
                                print("\"Ooh, 100! Wow! How many are you willing to give?\"")
                                getpass.getpass("")
                                donation = input("How many do you want to give? ")
                                makingDecision = True
                                while(makingDecision):
                                    if(donation.isdigit()):
                                        if int(donation) < 50:
                                            makingDecision = False
                                            makingChoice = True
                                            print("\n\"Well that was a waste of time.\"\n")
                                            choice3 = input()
                                        elif int(donation) >= 50 and int(donation) < 100:
                                            makingDecision = False
                                            print("\n\"With that amount, you are free to go.\"")
                                            getpass.getpass("")
                                            print("You have achieved the \"Escapee\" ending.")
                                            win = True
                                            getpass.getpass("")
                                        elif int(donation) == 100:
                                            makingDecision = False
                                            print("\n\"Wow! How generous!\"")
                                            getpass.getpass("")
                                            print("\"For that, I will share the", thing1, "with you.\"")
                                            getpass.getpass("")
                                            print("\"Only someone special would willingly give 100 cookies.\"")
                                            getpass.getpass("")
                                            print("You have achieved the \"Philanthropist\" ending.")
                                            win = True
                                            getpass.getpass("")
                                        else:
                                            donation = input("You don't have that many. How many do you want to give? ")
                                    else:
                                        donation = input("\nInvalid input. Try again: ")
                    else:
                        choice3 = input("\nInvalid input. Try again: ")
        elif bombs > 0:
            print("3 | Use a bomb.\n")
            choice3 = input()
    
            makingChoice = True
            while(makingChoice):
                if choice3 == "1":
                    makingChoice = False
                    if evil:
                        print("No, I don't think you are a good person. I don't want to share.\n")
                        choice3 = input()
                    else:
                        makingChoice = False
                        print("\n\"The", thing1, "don't have to belong to only me or only you. We can share!\"")
                        getpass.getpass("")
                        print("\"...share?\"") 
                        getpass.getpass("")
                        print("\"Share...\"") 
                        getpass.getpass("")
                        print("\"Share!\"") 
                        getpass.getpass("")
                        print("\"That sounds wonderful.\"")
                        getpass.getpass("")
                        print("\"" + name1, "and", pronoun1, relative1, name2, "owning all the", thing1 + "... together! Let's do it!\"")
                        getpass.getpass("")
                        print("You have achieved the \"Negotiator\" ending.")
                        win = True
                        getpass.getpass("")
                elif choice3 == "2":
                    makingChoice = False
                    if prison:
                        print()
                        print("You have been thrown in the gulag.")
                        getpass.getpass("")
                        print("You have achieved the \"Sent to the Gulag\" ending.")
                        win = True
                        getpass.getpass("")
                    else:
                        print("You lose. The story will restart.")
                        getpass.getpass("")
                elif choice3 == "3":
                    makingChoice = False
                    print("\n\"Take this", relative1 + "!\"")
                    getpass.getpass("")
                    print("BOOM!")
                    getpass.getpass("")
                    print("Well, you got what you wanted. But at what cost? You killed your", relative1 + ".")
                    getpass.getpass("")
                    if LarryHater and explosion:
                        print("And Larry.")
                        getpass.getpass("")
                        print("Congratulations. At every decision, you chose to be as destructive as possible. You are the lowest of the low. Enjoy your", thing1 + ".")
                        getpass.getpass("")
                        print("You have achieved the \"Evilest\" ending.")
                        win = True
                        getpass.getpass("")
                    else:
                        if LarryHater:
                            print("And Larry.")
                            getpass.getpass("")
                        print("Congratulations. You monster.")
                        getpass.getpass("")
                        print("You have achieved the \"Evil\" ending.")
                        win = True
                        getpass.getpass("")
                else:
                    choice3 = input("\nInvalid input. Try again: ")
        elif dogCount > 0:
            print("3 | Offer", dog + ".\n")
            choice3 = input()
    
            makingChoice = True
            while(makingChoice):
                if choice3 == "1":
                    if evil:
                        print("No, I don't think you are a good person. I don't want to share.\n")
                        choice3 = input()
                    else:
                        makingChoice = False
                        print("\n\"The", thing1, "don't have to belong to only me or only you. We can share!\"")
                        getpass.getpass("")
                        print("\"...share?\"") 
                        getpass.getpass("")
                        print("\"Share...\"") 
                        getpass.getpass("")
                        print("\"Share!\"") 
                        getpass.getpass("")
                        print("\"That sounds wonderful.\"")
                        getpass.getpass("")
                        print("\"" + name1, "and", pronoun1, relative1, name2, "owning all the", thing1 + "... together! Let's do it!\"")
                        getpass.getpass("")
                        print("\"Glad you had a change of heart. Don't forget about", dog + " though.\"")
                        getpass.getpass("")
                        print("\"Oh, yeah, haha. Good boy.\"")
                        getpass.getpass("")
                        print("\"Ruff ruff.\"")
                        getpass.getpass("")
                        print("You have achieved the \"Dog Lover\" ending.")
                        win = True
                        getpass.getpass("")
                elif choice3 == "2":
                    makingChoice = False
                    if prison:
                        print()
                        print("You have been thrown in the gulag.")
                        getpass.getpass("")
                        print("You have achieved the \"Sent to the Gulag\" ending.")
                        win = True
                        getpass.getpass("")
                    else:
                        print("You lose. The story will restart.")
                        getpass.getpass("")
                elif choice3 == "3":
                    print("\nSorry, I'm not a dog person.", Cenemyp + "!\n")
                    choice3 = input()
                else:
                    choice3 = input("\nInvalid input. Try again: ")
        else:
            print()
            choice3 = input()

            makingChoice = True
            while(makingChoice):
                if choice3 == "1":
                    if evil:
                        print("No, I don't think you are a good person. I don't want to share.\n")
                        choice3 = input()
                    else:
                        makingChoice = False
                        print("\n\"The", thing1, "don't have to belong to only me or only you. We can share!\"")
                        getpass.getpass("")
                        print("\"...share?\"") 
                        getpass.getpass("")
                        print("\"Share...\"") 
                        getpass.getpass("")
                        print("\"Share!\"") 
                        getpass.getpass("")
                        print("\"That sounds wonderful.\"")
                        getpass.getpass("")
                        print("\"" + name1, "and", pronoun1, relative1, name2, "owning all the", thing1 + "... together! Let's do it!\"")
                        getpass.getpass("")
                        print("\"Glad you had a change of heart. Don't forget about Benjamin though.\"")
                        getpass.getpass("")
                        print("\"Who?\"")
                        getpass.getpass("")
                        print("\"Y'know, Benjamin Franklin! I've got $100 in my pocket.\"")
                        getpass.getpass("")
                        print("\"You're weird.\"")
                        getpass.getpass("")
                        print("You have achieved the \"Penny Pincher\" ending.")
                        win = True
                        getpass.getpass("")
                elif choice3 == "2":
                    makingChoice = False
                    if prison:
                        print()
                        print("You have been thrown in the gulag.")
                        getpass.getpass("")
                        print("You have achieved the \"Sent to the Gulag\" ending.")
                        win = True
                        getpass.getpass("")
                    else:
                        print("You lose. The story will restart.")
                        getpass.getpass("")
                else:
                    choice3 = input("\nInvalid input. Try again: ")
   
        if(win):
            print("There are 9 endings in total. Play again to discover more endings.")
            getpass.getpass("")
            choice5 = input("Press 'I' to input different words. Press 'S' to redo the story with the same input. ")

            makingChoice = True
            while(makingChoice):
                if choice5 == "I" or choice5 == "S":
                    makingChoice = False 
                    print()
                else:
                    choice5 = input("\nInvalid input. Try again: ")
            if choice5 == "I":
                readingStory = False      
         