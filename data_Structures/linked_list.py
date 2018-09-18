#Node class (The user never interacts with this class)
class Node(object):
	def __init__(self, value=None):
		self.value = value
		#double linked list
		self.next = None
		self.prev = None

#Linked_List class (uses Node class)
class Linked_List(object):
	def __init__(self):
		#empty head object
		self.head = Node()
		self.size = 0

	def add_node(self, arg=None):
		if arg:
			new_node = Node(arg)
			cur = self.head #start with the head node
			#keep looping until we reach at the end of the list
			while cur.next:
				cur = cur.next
			cur.next = new_node
			cur.next.prev = cur
			self.size += 1

	def search_val(self, value=None):
	    cur = self.head
	    while cur.next:
	      cur = cur.next
	      if cur.value == value:
	        return cur
	    return False

	def print_reverse(self, value):
	    if value:
	      rev_elem = []
	      start_node = self.search_val(value)
	      if start_node:
	        while start_node.prev:
	          rev_elem.append(start_node.value)
	          start_node = start_node.prev
	        return rev_elem
	      else:
	        return False

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
print(my_list.print_reverse(4))




