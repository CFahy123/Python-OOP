
# Library --> display books, loan books, add new books
class Library:
	
	def __init__(self,bookList):
		self.availableBooks = bookList

	def display_books(self):
		print()
		print("Here are the available books: ")
		for book in self.availableBooks:
			print(book)

	def lend_a_book(self,requestedBook):
		if requestedBook in self.availableBooks:
			print("You have now borrowed the book")
			self.availableBooks.remove(requestedBook)
		else: 
			print("Sorry, The book was not available")


	def add_a_book(self,returnedBook):
		self.availableBooks.append(returnedBook)
		print("Thanks for returning the book!")


# Patron --> borrow books, return books	
class Patron:

	def borrow_book(self):
		print("Please enter the book you would like to borrow: \n")
		self.book = input()
		return self.book

	
	def return_book(self):
		print("Please enter the book you are returning: ")
		self.book = input() 
		return self.book



library1 = Library(['Demon Box','Neuromancer','The Perl'])
patron1 = Patron()
while True:
	print("Enter 1 to display the available books")
	print("Enter 2 to borrow a book")
	print("Enter 3 to return a book")
	print("Enter 4 to exit")
	userChoice = int(input())
	if userChoice is 1:
		library1.display_books()
	elif userChoice is 2:
		requestedBook = patron1.borrow_book()
		library1.lend_a_book(requestedBook)
	elif userChoice is 3:
		returnedBook = patron1.return_book()
		library1.add_a_book(returnedBook)	
	else:
		quit()


'''
library1.add_a_book("Dune")
library1.add_a_book("Momo")
library1.add_a_book("No Logo")


patron1.borrow_book('Demon Box')
library1.display_books()

print(patron1.patron_books)
'''






