import random
#O(1)
def random_element(nums):
    index = random.randint(0, len(nums)-1)
    return nums[index]

print(random_element([1,2,3,4]))

#if you do something in a for loop, you could replace it with O(n)
#O(n)
def calculate_total(nums):
    total = 0
    for num in nums:
        total += num
    return total
print(calculate_total([1,2,3,4]))#it is going to access nums 4 times
#if this is a big o of n

#O(n^2) 
#this represents a loop inside of a loop
#this will become inefficient when you have bigger and bigger lists
def find_pair(nums, target):
    output = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target
            output.append((nums[i], nums[j]))
    return output
print(find_pair([1,2,3,4], 5)) #2,3 or 1,4