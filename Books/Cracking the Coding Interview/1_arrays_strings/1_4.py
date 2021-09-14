def is_palim_perm(s: str) -> bool:
	s.replace(' ', '')
	amount = {}
	apply_even_rule = len(s) % 2 == 0

	for char in s:
		if char not in amount:
			amount[char] = 1
		else:
			amount[char] += 1

	has_one_odd = False

	for char in amount:
		test = amount[char] % 2 == 0
		
		if apply_even_rule and not test:
			return False

		if not apply_even_rule:
			if not test:
				if has_one_odd:
					return False
				else:
					has_one_odd = True

	return True

if __name__ == '__main__':
	print(is_palim_perm(' al la   '))
