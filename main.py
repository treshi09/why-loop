#Write a program to find the sum of natural numbers.

term = int(input("Enter the last term: "))
sum=0
start=1
while start <= term:
    sum = sum + start
    start = start + 1
sum = 0
for start in range(1, term + 1):
    sum = sum + start
print("The sum of all the natural numbers is:", sum)