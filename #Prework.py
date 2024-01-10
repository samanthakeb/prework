#Prework

# 1. Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print(f"hello_" + user_name)

get_username = input("Please enter your username...")
hello_name(get_username)

# 2. Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds():
    for number in range(1, 101, 2):
        print(number)

first_odds()

# 3. Please write a python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    return max(a_list)

numbers = [2, 6, 9, 20, 85, 5]
result = max_num_in_list(numbers)
print(result)


# 4. Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean.
def is_leap_year(a_year):
    return (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 ==0)

year = int(input("Please enter a year... "))
answer = is_leap_year(year)
print(answer)

# 5. Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive, but [1,2,4,5] are not. The return should be boolean.
def is_consecutive(a_list):
    sorted_list = sorted(a_list)

    for i in range(len(sorted_list) - 1):
        if sorted_list[i] + 1 != sorted_list[i + 1]:
            return False
        
        else:
            return True
        
nums = [1,3,4,5,6]
results = is_consecutive(nums)
print(results)
