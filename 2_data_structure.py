def add_book(library, title, author):
    if (title, author) not in library:
        library.append((title, author))
        print(title, "by", author, "has been added")
    else:
        print(title, "by", author, "already exists")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

print("")
add_book(library, "1984", "George Orwell")
print("")
add_book(library, "Star Wars", "George Lucas")
print("")
add_book(library, "Lavish Closet Living", "Harry Potter")
print("")

print("----------------------------------------")
print("")
print(library)