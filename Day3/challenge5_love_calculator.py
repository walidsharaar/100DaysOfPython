'''
write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in
the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
'''
print("Welcome to love machine")

first_partner = input("Enter your name: ").lower()
second_partner = input("Enter your partner name: ").lower()
attribute = "love"
# check true within the names
t=(first_partner.count("t")+second_partner.count("t"))
r=(first_partner.count("r")+second_partner.count("r"))
u=(first_partner.count("u")+second_partner.count("u"))
e=(first_partner.count("e")+second_partner.count("e"))

# check love within the names

l=(first_partner.count("l")+second_partner.count("l"))
o=(first_partner.count("o")+second_partner.count("o"))
v=(first_partner.count("v")+second_partner.count("v"))
e=(first_partner.count("e")+second_partner.count("e"))

# count of characters
score = (t+r+u+e+l+o+v+e)

if score <=40 or score >=90 :
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
    print(f"Your score is {score}, you are alright.")



