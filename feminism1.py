name = input("Insert strong, independent name (aka your name bc you're a strong, independent woman)\n")

print("Welcome " + name + "! This your life.\n\nYour mom wants you to be a doctor, but you've always wanted to be an engineer.\n")

q1 = input("Do you a: 'listen to your mom' or b: 'pursue your dreams'? (Please only press 'a' or 'b'!)\n")

# if choose to listen to mom
if q1 == "a":
    print("You will live an unhappy life.\n")
    # end game here; come back to this later lol

# if choose to pursue dreams
elif q1 == "b":
    print("You get it, girl!\n")
    print("While you are out here pursing your dreams, you also have a boyfriend of five years named Jake.")
    print("He feels threatened that you are a woman going into the engineering field; he is very unhappy.\n")

    q2 = input("Do you a: 'stay with him' or b: 'keep doing you and following your dreams'?\n")

# if choose stay with him
    if q2 == "a":
        print("You will live an unhappy life.\n")

    elif q2 == "b":
        print("Congratulations! You got rid of your obstacle. You didn't need him anyway!\n")

        print("You graduate from college at the top of your class and land an opportunity to intern at Apple!")
        print("However, you see that all the workers are old White men who don't understand what you're doing there as a woman.\n")

        q3 = input("Do you a: 'get intimidated and choose to never come back to the industry' or b: 'continue to persevere through the struggles', as you've been doing, girl?\n")

        if q3 == "a":
            print("You will live an unhappy life.\n")

        elif q3 == "b":
            print("You continue with the internship and eventually get a position at the company!\n")
            print("Five years later, you have a happy life with a supportive husband (or wife!!) who doesn't think you threaten his masculinity!")
            print("You are also now the CEO of your own company that teaches girls how to code!")
            print("Your daughter sees you as an example and now wants to be as strong as you.\n")
            print("You go, fam!!! You have succeeded in life, girl #empowerment")
