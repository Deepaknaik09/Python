# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
    
# cal_fact(5)

#Recursion
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)

def fact(n):
    if(n == 1 or n ==0):
        return 1
    return fact(n-1) * n

print(fact(5))

