# Import packages
from string import ascii_letters  # this is a list of letters in the English alphabet

# open "feature_file.txt" with read permission
f = open("feature_file.txt", "r")
# get contents of file
data = f.read()
f.close()

# We need to do two things:
# 1) replace every space with "-"
# 2) replace every third letter with "*"

# Replace every space with "-"
data = data.replace(" ", "-")

# There are several complications with the second part
# 1) You can't assign new values to strings; they are considered constants. We have to build a new string.
# 2) The specifications say every third _letter_, not every third _character_. We need to check every character.
new_data = ""
letter_counter = 0
for char in data:
    # Check if the character is a letter
    if char in ascii_letters:
        letter_counter += 1
    # Check if this is the third letter
    if letter_counter == 3:
        # Third letter; reset counter, substitute the *
        letter_counter = 0
        new_data += "*"
    else:
        new_data += char

# Write out results
f = open("updated_feature.txt", "w")
f.write(new_data)
f.close()
