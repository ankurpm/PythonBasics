'''
“Given a list of numbers, interchange first and last number”

Example:
Input = [12,35,56,4,67]
Output = [67,35,56,4,12]
'''
nums = [12, 35, 56, 4, 67]
print("Before swap",nums)

# swap first and last
nums[0], nums[-1] = nums[-1], nums[0]

print("After swap",nums)
