def find_smallest(letters,target):
	""" Find the smallest letter greater than the target
		Input: letters = ["c","f","j"], target = "a"
		Output: "c"."""
	if target == 'z':
		return letters[0]
	left = 0
	right = len(letters)-1
	while left <= right:
		mid = (right+left) // 2
		if letters[mid]<=target:
			left = mid+1
		elif letters[mid]>target:
			right = mid-1
	return letters[left%len(letters)]

print(find_smallest(["c","f","j","k","n","r"],'s'))