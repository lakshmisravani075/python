def recursive_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):   
            total += recursive_sum(item)
        else:                       
            total += item
    return total

x = [1, 2, 3, [1, 2, 3], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]

print("Sum of all numbers:", recursive_sum(x))




#using recursion
def fabonicc(n):
    if n<=1:
        return n
    else:
        return fabonicc(n-1) + fabonicc(n-2)
for i in range(7):
 print(fabonicc(i))
 
