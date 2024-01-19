PLACEHOLDER = "[name]"


with open("./Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    print(names)
   
with open("./Mail Merge Project Start/input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
