def containsDup(nums):
    if len(nums)==len(set(nums)):
        return True
    return False
print(containsDup([1,2,3,4,0]))