# Time: O(n). Memory: O(1)

def is_palim(linked_list: LinkedList):
	first =	linked_list.first
	last = linked_list.last

	while first != last and first.next != last:
		if first.value != last.value:
			return False

		first = first.next
		last = last.prev

	if first.value != last.value
		return False

	return True # Empty and one value linked lists will be considered palindromes
