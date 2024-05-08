import json
import os
## Create Class for creating new dictionaries here
class Book():
    def __init__(self, name, year, author, genre):
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre
    def __str__(self):
        return f"{self.name}, {self.year}, {self.author}, {self.genre}" 


with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

while True:
        name = input("Book name: ")
        year = int(input("Book year: "))
        author = input("Author: ")
        genre = input("Book genre: ")
        book = Book(name, year, author, genre)
        data.append(book.__dict__)
        continue_adding_books = input("Add books: Y/N ")
        if continue_adding_books.upper() != "Y":
            break
   

#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")