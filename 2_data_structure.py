#   Task 2:

# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.

#   [] list
#   () tuple
#   [()] tuple IN a list

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]





# list.append('item')

library = list(library)                 #   conv. tuple to a list so it can be added too
library.append('Add Book Title')        #   adding/inserting new book
library.append('Add Book Author')       #   adding/inserting new book
library = tuple(library)                #   conv back to a tuple
print(library)                          #   printing end result 







