'''
data_list is a custom data structure to be used with the pyserial-based interface for arduino lcbci

@author: Chanha Kim
@date:   07/02/2020
'''

class data_list:
	def __init__(self, capacity = 100):
		self.capacity = capacity
		self.data = [None for i in range(self.capacity)]
		self.start_index = 0
		self.size = 0

	def remove(self):
		'''Removes value at start_index and shifts start_index by 1'''
		self.data[self.start_index] = None
		self.start_index = (self.start_index + 1) % self.capacity

	def is_full(self):
		'''Returns true if list is full'''
		return None not in self.data

	def add(self, value):
		'''Adds value to list to first index available after self.start_index'''
		if self.is_full():
			self.remove()
			self.data[(self.start_index - 1) % self.capacity] = value
		else:
			self.data[(self.start_index + self.size) % self.capacity] = value
			self.size += 1

	def __list__(self):
		'''Returns the list'''
		return self.data[self.start_index:] + self.data[:self.start_index-self.capacity]

	def __iter__(self):
		'''Returns an iterator'''
		if self.is_full():
			return iter(self.data[self.start_index:] + self.data[:self.start_index-self.capacity])
		else:
			return iter(self.data[0:self.size])