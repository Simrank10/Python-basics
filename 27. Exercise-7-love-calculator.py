"""
Friendship Score Calculator

Instructions:
1. Ask two people for their names.
2. Convert the names to lowercase.
3. Count the occurrences of the letters in the word "friend":
   - f, r, i, e, n, d
4. Count the occurrences of the letters in the word "ship":
   - s, h, i, p
   (Note that the letter "i" appears in both words and is counted twice.)
5. Concatenate the two counts to form the friendship score.
6. Display a message based on the score:
   - If the score is less than 10 or greater than 90:
         "Your friendship score is X%, you are best friends forever!"
   - If the score is between 40 and 60:
         "Your friendship score is X%, you are pretty solid pals!"
   - Otherwise, simply display the friendship score.
"""


print("Let's check the friendship score!")
print()

# Get user names
name_1 = input("Enter the first name: ")
print()
name_2 = input("Enter the second name: ")

# Convert names to lowercase for uniform counting
name_1 = name_1.lower()
name_2 = name_2.lower()

# Count letters for the word "friend"
f = name_1.count("f") + name_2.count("f")
r = name_1.count("r") + name_2.count("r")
i = name_1.count("i") + name_2.count("i")
e = name_1.count("e") + name_2.count("e")
n = name_1.count("n") + name_2.count("n")
d = name_1.count("d") + name_2.count("d")
friend_count = f + r + i + e + n + d

# Count letters for the word "ship"
s = name_1.count("s") + name_2.count("s")
h = name_1.count("h") + name_2.count("h")
# Count "i" again for the word "ship"
i_ship = name_1.count("i") + name_2.count("i")
p = name_1.count("p") + name_2.count("p")
ship_count = s + h + i_ship + p

# Create the friendship score by concatenating the two counts
friendship_score = int(str(friend_count) + str(ship_count))

print()
# Display different messages based on the friendship score
if friendship_score < 10 or friendship_score > 90:
    print(f"Your friendship score is {friendship_score}%, you are best friends forever!")
elif 40 <= friendship_score <= 60:
    print(f"Your friendship score is {friendship_score}%, you are pretty solid pals!")
else:
    print(f"Your friendship score is {friendship_score}%")

print()
print("Remember, true friendship goes beyond numbers!")
