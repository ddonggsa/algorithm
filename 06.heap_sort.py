def heap(case):
	def soyeon(case, length, node):
		max = node
		left = 2 * node + 1
		right = 2 * node + 2
		if left < length and case[left] > case[max]:
			max = left
		if right < length and case[right] > case[max]:
			max = right
		if max != node:
			case[max], case[node] = case[node], case[max]
			soyeon(case, length, max)

	length = len(case)

	for a in range(length//2, -1, -1):
		soyeon(case, length, a)
	for a in range(length - 1, 0, -1):
		case[0], case[a] = case[a], case[0]
		soyeon(case, a, 0)

	return case

a = list(map(int,input().split()))
print(heap(a))

