# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
Christian = {'age': '22', 'first_name': 'Christian', 'last_name': 'Goddard', 'city': 'Chicago'}
print(Christian['age'])
print(Christian['first_name'])
print(Christian['last_name'])
print(Christian['city'])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program
Christian = {'favorite_number': '3'}
Leslie = {'favorite_number': '11'}
Danielle = {'favorite_number': '22'}
Riley = {'favorite_number': '76'}
Justin = {'favorite_number': "545"}
print(Justin['favorite_number'])
print(Leslie['favorite_number'])
print(Christian['favorite_number'])
print(Danielle['favorite_number'])
print(Riley['favorite_number'])

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output
glossary = {
'HTML': 'hyper link text markup language',
'.py': 'python filename',
'1MB': '1024 bytes',
'GB': 'gigabyte',
'TB': 'Terabyte',
'KB': 'Kilobyte',
'OS': 'Operating System',
'SSD': 'Solid State Drive',
'HDMI': 'high definition multimedia interface',
'PDF': 'Portable Document Format'
}
print(glossary)

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.
for key, value in glossary.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 6-6. Polling: Use the code in favorite_languages.py (page 104).
#  Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
#  Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'mike d': 'ruby',
    'jasper': 'python'
    }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.
fluffy = {'animal_type': 'guinea_pig', 'owner': 'Wyatt'}
toasty = {'animal_type': 'rat', 'owner': 'Justin'}
spooky = {'animal_type': 'cat', 'owner': 'Leslie'}
pets = [fluffy, toasty, spooky]
for pet in pets:
    print(pet)

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.
favorite_numbers = {
    'Danielle': [22, 10],
    'Justin': [545, 32],
    'Riley': [76, 42],
    'Christian': [3, 9],
    'Leslie': [11, 2]
    }
for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))

# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program or improving the formatting of the output



# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”
car = input("What kind of car would you like? ")
print("Let me see if I can find you a " + car.title() + ".")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.
party_size = input("How many people are in your dinner group tonight? ")
party_size = int(party_size)

if party_size > 8:
    print("I'm terribly sorry, you'll have to wait for a table.")
else:
    print("Your table is prepared.")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
number = input("Can I have a number?: ")
number = int(number)
if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value


# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
sandwich_orders = ['meatball', 'BLT', 'salami', 'roast beef']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm preparing your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.
place_prompt = "If you could visit one place in the world, where would you go? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
responses = {}
while True:
    place = input(place_prompt)
    responses[name] = place
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")

# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
def display_message():
    """Display a message about what I'm learning."""
    msg = "I'm learning about functions."
    print(msg)
display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")
favorite_book('House to House')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message
def make_shirt(size='large', message='I love Python.'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')
make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Python is fun.')

# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value
# that’s returned.
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())
city = city_country('santiago', 'chile')
print(city)
city = city_country('moscow', 'russia')
print(city)
city = city_country('jalalabad', 'afghanistan')
print(city)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict
title_prompt = "\nWhat album? "
artist_prompt = "What artist? "
print("Enter 'quit' to stop.")
while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)
print("\nThanks for responding!")

# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)
def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)
magicians = ['Ben', 'Justin', 'Ryan']
show_magicians(magicians)
print("\n")
make_great(magicians)
show_magicians(magicians)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times, using a different number
# of arguments each time.
def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI make a killer sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Here is your food")
make_sandwich('roasted garlic powder', 'dank cheese', 'lettuce', 'honey dijon')
make_sandwich('salami', 'salt', 'honey bbq sauce')
make_sandwich('extra meat', 'mayo')

# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict
my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)
my_k10 = make_car('chevrolet', 'K10', year=1986, color='black')
print(my_k10)

# 8-15. Printing Models: Put the functions for the example print_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of print_models.py, and modify the file to use the imported functions

# printing_functions.py:
"""Functions related to printing 3d models."""
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)