
print("Welcome to the GK Quiz...")
print()

name = input("Enter your name here : ")
print()

want = input("If you want to play quiz type 'yes' here : ")
print()

if want=="yes":
    pass
else:
    print("I think you don't want to play. Try again to type 'yes' ")
    quit()

total = 0

print("Q.1. What is full-form of UN? ")

print("""
(a) Union of Nations
(b) Union of Nepal
(c) Union of Nato
(d) United Nations
""")

q1 = input("Enter your choice here : ")

if q1 == "d":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is d ")

print()

print("Q.2. Who is the President of USA? ")

print("""
(a) Donald Trump
(b) Joe Biden
(c) Steave Jobs
(d) Narender Modi
""")

q2 = input("Enter your choice here : ")

if q2 == "b":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is b ")
print()

print("Q.3. Who is the Prime Minister of India? ")

print("""
(a) Atal Bihari Vajpeyi
(b) Dr. APJ Abdul Kalam
(c) Narender Modi
(d) Pranab Mukherji
""")

q3 = input("Enter your choice here : ")

if q3 == "c":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is c")
print()

print("Q.4. What is the capital of India? ")

print("""
(a) Haidrabad
(b) Surat
(c) New Delhi
(d) Mumbai
""")

q4 = input("Enter your choice here : ")

if q4 == "c":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is c")
print()

print("Q.5. How many states in India? ")

print("""
(a) 20
(b) 29
(c) 28
(d) 27
""")

q5 = input("Enter your choice here : ")

if q5 == "c":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is c")
print()

print("Q.6. What is the biggest city in India? ")

print("""
(a) New Delhi
(b) Banglore
(c) Colkatta
(d) Mumbai
""")

q6 = input("Enter your choice here : ")

if q6 == "d":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is d")
print()

print("Q.7. What is the biggest state in India? ")

print("""
(a) Rajsthan
(b) Uttrakhand
(c) Bihar
(d) Haryana
""")

q7 = input("Enter your choice here : ")

if q7 == "a":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is a")
print()

print("Q.8. What is smallest state in India? ")

print("""
(a) Haryana
(b) Goa
(c) Arunachal Pradesh
(d) Jammu & Kashmir
""")

q8 = input("Enter your choice here : ")

if q8 == "b":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is b")
print()

print("Q.9. When India get Indepence? ")

print("""
(a) 15 August, 1857
(b) 26 January, 1950
(c) 26 January, 1955
(d) 15 August, 1947
""")

q9 = input("Enter your choice here : ")

if q9 == "d":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is d")
print()

print("Q.10. When India become repulic? ")

print("""
(a) 15 August, 1857
(b) 26 January, 1950
(c) 26 January, 1955
(d) 15 August, 1947
""")

q10 = input("Enter your choice here : ")

if q10 == "b":
    print("That's right!")
    total+=1
else:
    print("Oh! this is wrong answer. Right answer is b")
print()

if total<4:
    print("Hey! " + name + " You lost the game!!!")
    print("Your total score is : " , total)
    print("YOu can try again...")

elif total==10:
    print("Hey! " + name + " Great! you won the game!!!")
    print("YOu get the score of : " , total)

elif total>7:
    print("Hey! " + name + " That's great score ...")
    print("Your total score is : ", total)
    print("YOu have done great, but still you not won. try again and get 10 scores...")


else : 
    print("Hey! " + name + " You are average ")
    print("Your total score is : " , total)
    print("You can do more...try once more time ...")
print()

print(".........created by Vinay Kargwal.............")
