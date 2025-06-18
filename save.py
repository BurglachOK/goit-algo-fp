'This code is an attempt to implement insertion sort on a linked list using index access. '
'It is not the most efficient way to do it, but it serves as a reminder of the approach I tried'

class LinkedList:
	def __init__(self):
		self.head = None

	def get_index(self, index):
		current = self.head
		for i in range(index):
			current = current.next
		return current	

	def insertion_sort(self):
		for i in range(1, self.len_link()):
			key = self.get_index(i).data
			j = i-1
			while j >=0 and key < self.get_index(j).data:
				temp = self.get_index(j+1)
				temp2 = self.get_index(j)
				temp2.next = temp.next
				temp.next = temp2
				j -= 1
			self.get_index(j+1).data = key

