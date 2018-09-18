#Node class (The user never interacts with this class)
class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.next = None

#Linked_List class (uses Node class)
class Linked_List(object):
	def __init__(self):
		#empty head object
		self.head = Node()

	def add_node(self, arg=None):
		if arg:
			new_node = Node(arg)
			cur = self.head #start with the head node
			#keep looping until we reach at the end of the list
			while cur.next:
				cur = cur.next
			cur.next = new_node

	def print_list(self):
		elem = []
		cur = self.head
		while cur.next:
			cur = cur.next
			elem.append(cur.value)
		return elem

#linked_list_instance
my_list = Linked_List()
#add data
for i in range(2,7):
	my_list.add_node(i)
#prit the list
print(my_list.print_list())





