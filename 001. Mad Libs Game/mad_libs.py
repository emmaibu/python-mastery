import textwrap

title = 'Mad Libs'
paragraph = 'Adventure In The Amazon Jungle'
prompt = 'Go Mad! Fill in the blank fields below'
print(title.center(50))
print(paragraph.center(50))
print(prompt.center(50))

def mad_libs():
    adj1 = input('Enter an adjective: ')
    plural_noun1 = input('Enter a plural noun: ')
    plural_noun2 = input('Enter a plural noun: ')
    noun1 = input('Enter a noun: ')
    adj2 = input('Enter an adjective: ')
    animal_sound = input('Enter an animal sound: ')
    name_of_person1 = input('Enter name of a person: ')
    adj3 = input('Enter an adjective: ')
    animal1 = input('Enter an animal: ')
    plural_noun3 = input('Enter a plural noun: ')
    name_of_person2 = input('Enter name of a person: ')
    adj4 = input('Enter an adjective: ')
    adj5 = input('Enter an adjective: ')
    animal2 = input('Enter an animal: ')
    food_item1 = input('Enter a food item: ')
    food_item2 = input('Enter a food item: ')
    adj6 = input('Enter an adjective: ')
    adj7 = input('Enter an adjective: ')
    adj8 = input('Enter an adjective: ')
    adj9 = input('Enter an adjective: ')
    name_of_person3 = input('Enter name of a person: ')
    verb = input('Enter a verb: ')
    adj10 = input('Enter an adjective: ')
    animal3 = input('Enter an animal: ')
    name_of_person4 = input('Enter name of a person: ')
    plural_noun4 = input('Enter a plural noun: ')
    plural_noun5 = input('Enter a plural noun: ')
    adj11 = input('Enter an adjective: ')
    name_of_person5= input('Enter name of a person: ')
    noun2 = input('Enter a noun: ')
    adj12 = input('Enter an adjective: ')
    input('Press enter to Go Mad!')

    story = f"""One sunny morning, a group of {adj1} adventurers set off on a journey into the wild, untamed Amazon jungle. They packed {plural_noun1}, {plural_noun2}, and a giant {noun1}, just in case they encountered a {adj2} problem. As they walked through the dense jungle, they suddenly heard a loud {animal_sound}. "What was that?!" yelled {name_of_person1}, looking around nervously. Out of the trees, a massive, {adj3} {animal1} appeared, covered in {plural_noun3}. "This is it!" screamed {name_of_person2}, "We're gonna get {adj4}!" But just then a {adj5} {animal2} swoooped down and stole their last bag of {food_item1}! "No! Not the {food_item2}!" cried the group. "We'll never survive the jungle without it!" They quickly followed the {adj6} creature into the jungle, which led them to a {adj7} waterfall. Beneath the water, they saw something shiny, a {adj8} treasure chest! "it's the legendary {adj9} treasure!" shouted {name_of_person3}. "Let's open it!" But as they touched the chest, the ground began to {verb}, and a giant {adj10} {animal3} burst from the earth! "RUN" yelled {name_of_person4}. The group sprinted through the jungle, dodging {plural_noun4} and {plural_noun5}, until they reached the safety of a {adj11} treehouse. Panting and out of breath, {name_of_person5} wiped their brow, "Well, at least we still have our {noun2}... and our {adj12} sense of adventure."
    """
    print('Processing\nGenerating...\nDone!')

    return textwrap.dedent(story)

while True:

    story = mad_libs()
    print(story)

    save_file = input('Do you want to save the story as a file?(y/n) ').lower().strip()
    while save_file not in ['y', 'n', 'yes', 'no']:
        save_file = input('Please enter yes or no: ')
    if save_file in ['y', 'yes']:
        with open('madlib.txt', 'a') as f:
            f.write(story + "\n" + "-"*50 + "\n")
        print('Story saved!')
    else:
        print('Story not saved.')

    user_response = input('Do you want to Go Mad Again?(y/n): ').lower().strip()
    while user_response not in ['y', 'n', 'yes', 'no']:
        user_response = input('Please type y or n: ')
    if user_response not in ['y', 'yes']:
        break

print('Bye!')