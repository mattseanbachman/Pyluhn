
def luhn(cc):
	scc = str(cc)
	isum = 0
	if not len(scc) % 2 : # even numbered cards
		count = 1
		tmp = list(scc)
		for each in tmp:
			if not count % 2: # even
				isum += int(each)
#				print(each)
			else:
				ttemp = int(each) * 2
#				print(ttemp)
				if ttemp >= 10:
					ttemp -= 9
				isum += ttemp
			count += 1
	else: # odd numbered cards
		count = 1
		tmp = list(scc)
		for each in tmp:
			if not count % 2:
				ttemp = int(each) * 2
				if ttemp >= 10:
					ttemp -= 9
				isum += ttemp
			else:
				isum += int(each)
			count += 1
#	print(isum)
	if not isum % 10:
		return True
	return False


print(luhn(4408041234567893))

print(luhn(4417123456789112))
