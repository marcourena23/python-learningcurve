class Book:
	def __init__(self, title, author, num_pages):
		self.title = title
		self.author = author
		self.num_pages = num_pages

	def __str__(self):
		return f"{self.title} by {self.author}"

	def __eq__(self, other): # Other is the second object (book)
    		return self.title == other.title and self.author == other.author

	def __lt__(self, other):
		return self.num_pages < other.num_pages

	def __gt__(self, other):
		return self.num_pages > other.num_pages

	def __add__(self, other):
		return self.num_pages + other.num_pages

	def __contains__(self, keyword):
		return keyword in self.title

	def __getitem__(self, key):
		if key in "title":
			return self.title
		elif key in "author":
			return self.author
		elif key in "num_pages":
			return self.num_pages
		else: 
			return f"Key {key} was not found"

book1 = Book("The Hobbit", "J.R.R Tolkien", 312)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K Roling", 223)

print(book1)
print(book1 == book2)
print(book1 < book2)
print(book1 > book2)
print(book1 + book2)
print("Hobbit" in book1)
print(book1['title'])
print(book1['author'])
print(book1['num_pages'])
print(book1['audio'])
