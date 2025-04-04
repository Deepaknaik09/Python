# i = 100
# while i >= 1 :
#     print(i)
#     i -= 1

# Multiplying
# n = int(input("Enter the number:"))
# i = 1
# while i <= 10 :
#     print(n*i)
#     i += 1

# Print the element of folowing list 
# [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]

# num = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1


# superheros = ["Ironman","Spiderman","Thor","Blackpanter","Hulk"]
# idx = 0
# while idx < len(superheros):
#     print(superheros[idx])
#     idx += 1

num = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100]
i = 0
x = 81
while i < len(num):
    if(num[i] == x):
        print("found at index",i)
    i += 1