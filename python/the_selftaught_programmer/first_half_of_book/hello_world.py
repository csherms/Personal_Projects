import csv
# --------------------------------------------------------
# Writing to a text file
# with open("st.txt", "w") as f:
#   f.write("Hi from Python!")

# Reading a text file and saving it to a variable in python
# with open("st.txt", "r") as f:
#   print(f.read())
  
# my_list = list()

# with open("st.txt", "r") as f:
#   my_list.append(f.read())
  
# print(my_list)
# --------------------------------------------------------


# --------------------------------------------------------
# Writing to a csv file
# with open("st.csv", "w", newline='') as f:
#   w = csv.writer(f, delimiter=",")
#   w.writerow(["one","two","three"])
#   w.writerow(["four", "five","six"])

# Reading from a csv file
# with open("st.csv", "r") as f:
#   r = csv.reader(f, delimiter=",")
#   for row in r:
#     print(",".join(row))
# --------------------------------------------------------

# for i in range(10):
#     print("Hello World")

# home = "America"
# if home == "America":
#     print("Hello America!")
# else:
#     print("Hello World!")

# x = 2
# if x == 2:
#     print("The number is 2")
# if x % 2 == 0:
#     print ("The number is even.")
# if x % 2 != 0:
#     print("The number is odd.")

# # nested if statement
# x = 10
# y = 11
# if x == 10:
#     if y == 11:
#         print(x + y)

#age = 12
#if age < 10:
#    print("You're just a baby.")
#elif age > 10 and age < 20:
#    print("There's still time.")
#else:
#    print("You're fuckin' old.")

# def even_odd():
#     n = input("Enter a number: ")
#     n = int(n)
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# even_odd()
# even_odd()
# even_odd()
    
# try:
#     a = input("Enter number: ")
#     b = input("Enter another number: ")
#     a = int(a)
#     b = int(b)
#     print(a / b)
# except(ZeroDivisionError, ValueError):
#     print("Invalid input. ")

# this is a demonstation of a docstring inside of a function to tell others what the function does.
# def add(x,y):
#     """_summary_

#     Args:
#         x (_int_): _first number_
#         y (_int_): _second number_

#     Returns:
#         _int_: _sum of x and y_
#     """
#     return x + y


# rhymes = {"1": "fun",
#           "2": "blue",
#           "3": "me",
#           "4": "floor",
#           "5": "live"}

# n = input("Type a number: ")
# if n in rhymes:
#     """ This is like saying if the input number exists as a key in the dictionary, 
#     then get that keys value and print it."""
#     rhyme = rhymes[n]
#     print(rhyme)
# else:
#     print("Not found.")


# fav_musicians = ["Dave Matthews", "Eminem", "Dr. Dre", "David Gilmour"]
# places = []
# la = (123, 456)
# chicago = (789, 101112)

# places.append(la)
# places.append(chicago)

# print(places)


# This one was pretty interesting because I had never seen one where the "user" was asking me a question before.
# me = {"height": 5.5,
#       "fav_author": "J.K. Rowling",
#       "fav_color": "red"}

# answer = input("Type: height, fav_color, or fav_author: ")
# if answer in me:
#     result = me[answer]
#     print(result)


# qs = ["What is your name?: ",
#       "What is your fav. color?: ",
#       "What is your quest?: ",
#       "Answer another question: "]

# n = 0
# while True:
#   print("Type q to quit")
#   """This is really cool because it allows the quit statement to be available each time the question is posed."""

#   a = input(qs[n])
#   if a == "q":
#     break
#   n = (n + 1) % 4  
#   """The modulo number should be equal to the number of questions, allowing the loop to keep repeating and listing all questions. """
  
# ------------------------------------------ 
# All of this was part of the challenge of reading a writing python files. It worked very well to create a text file.
# n = open("another.txt", "w")
# n.write("Making some more notes to test out the challenges.\n")
# n.write("Lets see if we can make some updates to what I am doing.\n")
# n.write("Yes indeed, it works but I have to put a new line break on the end of each previous sentence.")
# n.close()

# with open("another.txt", "r") as f:
#   print(f.read())

# Another challenge from the book
# I can't believe this actually worked.
# answer = input("What is your favorite color?: ")
# with open("fav_color.txt", "w") as f:
#   f.write(answer)

# Another challenge (movies)
# (don't forget to import csv for this to work)
# movies = [["Top Gun", "Risky Business", "Minority Report", "Titanic", "The Revenant", "Inception"], ["Training Day", "Man of Fire", "Flight"]]

# movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
# with open("movies.csv", "w") as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=",")
#     for movie_list in movies:
#         spamwriter.writerow(movie_list)
# ------------------------------------------ 


