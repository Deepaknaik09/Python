#list
# nums = [1, 2, 3, 4, 5, 6]

# for val in nums:
#     print(val)


# String
# str = "Deepak"

# for char in str:
#     print(char)


# Finding number X in tuple
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0
for ele in nums:
    if(ele == x):
        print("Number is found at index",idx)
        break
    idx += 1