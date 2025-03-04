#number = int(input("Введіть 4-х значне число:"))

#n1 = number // 1000
#n2 = (number // 100) % 10
#n3 = (number // 10) % 10
#n4 = number % 10

#print(n1)
#print(n2)
#print(n3)
#print(n4)

num = int(input("Please, write your number:"))

rev_num = 0

while num > 0:
    last_digit = num % 10
    rev_num = rev_num * 10 + last_digit
    num = num // 10

print("Revers number:", rev_num)