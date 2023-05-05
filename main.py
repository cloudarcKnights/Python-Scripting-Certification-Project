# 1
# def count_factors(given_number):
#   factor = 1
#   count = 1
#   if given_number == 0:
#     return 0

#   while factor < given_number:
#     if given_number % factor == 0:
#       count += 1
#     factor += 1
#   return count
 
# print(count_factors(0)) # Count value will be 0
# print(count_factors(3)) # Should count 2 factors (1x3)
# print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
# print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8,
# # and 4x6). 


# 2


# def addition_table(given_number):
 
#     iterated_number = 1
#     my_sum = 1

#     while iterated_number <= 5:
 
#         my_sum = given_number + iterated_number

#         if my_sum > 20:
#             break
#         print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
        
#         iterated_number += 1

# addition_table(5)
# addition_table(17)
# addition_table(30)

# 3

# def is_power_of_two(number):

#   while number % 2 == 0:
#     number = number / 2
#     break
#   if number >= 1 and number < 9:
#     return True
#   return False
    
  

# # Calls to the function
# print(is_power_of_two(0)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False

# 4

# def multiplication_table(number):
#     # Initialize the appropriate variable
#     multiplier = 1
#     result = 1

#     # Complete the while loop condition.
#     while multiplier < result:
#         number 
#         result = number * multiplier
#         if  result > 25:
#             # Enter the action to take if the result is greater than 25
#             break    
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
#         # Increment the appropriate variable
#         multiplier += 1


# multiplication_table(3) 
# # Should print: 
# # 3x1=3 
# # 3x2=6 
# # 3x3=9 
# # 3x4=12 
# # 3x5=15

# multiplication_table(5) 
# # Should print: 
# # 5x1=5
# # 5x2=10
# # 5x3=15
# # 5x4=20
# # 5x5=25

# multiplication_table(8) 
# # Should print:
# # 8x1=8
# # 8x2=16
# # 8x3=24


# 5

# teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
# for home_team in teams:
#     for away_team in teams:
#         if home_team != away_team:
#             print(home_team + ' vs ' + away_team)

# 6

# def matrix(initial_number, end_of_first_row):
 
#     n1 = initial_number 
#     n2 = end_of_first_row+1  # include the upper range value with +1

#     # The first for loop will create the columns.
#     for column in range(n1, n2):
#         # print(column)

#         # The nested for loop will create the rows.
#         for row in range(n1, n2):
              
 
#               print(column*row, end=" ")
#         print()

# matrix(1, 10)
# # Should print:
# # 1 2 3 4 
# # 2 4 6 8 
# # 3 6 9 12 
# # 4 8 12 16 


# 7


# def X_figure(salary):
    
   
#     tally = 0


#     if salary == 0:
#         tally += 1
#     while salary >= 1:
#         salary = salary/10
#         tally += 1
#     return tally
 
# print("The CEO has a " + str(X_figure(23000000)) + "-figure salary.")

# # Should print"The CEO has a 7-figure salary."

# 8

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))