# property = Decorator used to define method as a property (it can be accessed like an attribute)
#		Benefit: Add additional logic when read, read, write or delete attributes
#		Gives you getter, setter and deleter method

class Rectangle:
	def __init__(self, width, height):
		self._width = width
		self._height = height

	@property
	def get_width(self):
		return f"{self._width:.1f}cm"

	@property
	def get_height(self):
		return f"{self._height:.1f}cm"

rectangle = Rectangle(3, 4)

print(rectangle.get_width)
print(rectangle.get_height)
