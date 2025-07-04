class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			cur = self.head
			while cur.next:
				cur = cur.next
			cur.next = new_node

	def insert_after(self, prev_node: Node, data):
		if prev_node is None:
			print("Попереднього вузла не існує.")
			return
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete_node(self, key: int):
		cur = self.head
		if cur and cur.data == key:
			self.head = cur.next
			cur = None
			return
		prev = None
		while cur and cur.data != key:
			prev = cur
			cur = cur.next
		if cur is None:
			return
		prev.next = cur.next
		cur = None

	def search_element(self, data: int) -> Node | None:
		cur = self.head
		while cur:
			if cur.data == data:
				return cur
			cur = cur.next
		return None

	def reverse_list(self):
		prev = None
		curr = self.head
		if not curr:
			return None
		while curr:
			next_node = curr.next
			curr.next = prev
			prev = curr
			curr = next_node
		self.head = prev

	def print_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next
	
	def len_link(self):
		count = 0
		current = self.head
		while current:
			count += 1
			current = current.next
		return count


	def insertion_sort(self):
		sorted_head = None
		current = self.head

		while current:
			next_node = current.next
			if not sorted_head or current.data < sorted_head.data:
				current.next = sorted_head
				sorted_head = current
			else:
				sorted_current = sorted_head
				while sorted_current.next and sorted_current.next.data < current.data:
					sorted_current = sorted_current.next
				current.next = sorted_current.next
				sorted_current.next = current
			current = next_node

		self.head = sorted_head

	def merge_2_lists(self, otherList):
		otherList.insertion_sort()
		self.insertion_sort()
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = otherList.head
		self.insertion_sort()







print('First List')
llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)
llist.reverse_list()
print("Reversed 1st Linked List:")
llist.print_list()
llist.insertion_sort()
print("Sorted 1st Linked List:")
llist.print_list()

print('2 merged and sorted lists')
last = LinkedList()
last.insert_at_beginning(19)
last.insert_at_beginning(20)
last.insert_at_beginning(2)
last.insert_at_end(73)
last.insert_at_end(17)
last.merge_2_lists(llist)
last.print_list()