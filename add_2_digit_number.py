# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number=input("Enter two digit number :\n")
# To check type of two_digit_number
print(type(two_digit_number))
# type is string so we need to subscript our string 
two_digit_number_1 = two_digit_number[0] 
two_digit_number_2 = two_digit_number[1]
# now we need to typecast two_digit_number_1 & two_digit_number_2 
two_digit_number_1 = int(two_digit_number[0]) 
two_digit_number_2 = int(two_digit_number[1])
# last step is to add both the numbers
sum=two_digit_number_1+two_digit_number_2
print(sum)