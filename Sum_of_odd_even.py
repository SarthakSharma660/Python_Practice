sum_odd=0
sum_even=0
total=0
# sum of 1st 100 even integers
for number in range(2,101, 2):
    sum_even += number
print(f"Sum of 1st 100 even numbers is :{sum_even}")
#  sum of 1st odd integers
for number in range(1,101,2):
    sum_odd += number
print(f"Sum of 1st 100 odd numbers is:{sum_odd}")
# sum of 1st 100 integers
for number in range(1, 101):
    total += number
print(f"Sum of 1st 100 numbers is :{total}")
