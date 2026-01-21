def find_permutations(arr):
    if len(arr)<2:
        return [arr]
    result = []
    for i in range(len(arr)):
        curr_ele = arr[i]
        remaining_arr = arr[:i]+arr[i+1:]

        for p in find_permutations(remaining_arr):
            result.append([curr_ele]+p)

    return result
print(find_permutations([1,1,2]))