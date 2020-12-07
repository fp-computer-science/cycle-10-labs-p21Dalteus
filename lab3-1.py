#Author DA (AMDG) 12/7/2020

def sum_to(n):
    total = 0
    iteration = 1
    while iteration < n+1:
        total += iteration
        iteration += 1
    return total


num = input("Please input an interger: ")

result = sum_to(int(num))
print(result)
