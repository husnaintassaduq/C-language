def calculate_sum(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum += i
        else:
            sum -= i
    return sum

def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def print_numbers(n):
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1

# Flowgraph:
#       ______
#      |      |
#      v      |
# calculate_sum ---> find_maximum ---> print_numbers

# Cyclomatic Complexity = E - N + 2P
# E = Number of edges
# N = Number of nodes
# P = Number of connected components (1 for a single function)

# For the code fragment above:
# E = 9 (Number of edges)
# N = 7 (Number of nodes)
# P = 1 (Number of connected components)

# Cyclomatic Complexity = 9 - 7 + 2(1) = 4

# Independent paths:
# 1. calculate_sum -> find_maximum -> print_numbers
# 2. calculate_sum -> find_maximum -> return
# 3. calculate_sum -> return

# Test the functions
n = 10
sum_result = calculate_sum(n)
print(f"Sum of numbers from 1 to {n}: {sum_result}")

numbers = [5, 2, 9, 1, 7]
max_number = find_maximum(numbers)
print(f"Maximum number in the list: {max_number}")

print("Printing numbers:")
print_numbers(15)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

def main_function():
    num_to_sum = 10
    sum_result = calculate_sum(num_to_sum)
    print(f"Sum of numbers from 1 to {num_to_sum}: {sum_result}")

    number_list = [5, 2, 9, 1, 7]
    max_number = find_maximum(number_list)
    print(f"Maximum number in the list: {max_number}")

    print("Printing numbers:")
    print_numbers(15)

    start_range = 1
    end_range = 20
    prime_count = count_primes_in_range(start_range, end_range)
    print(f"Number of prime numbers between {start_range} and {end_range}: {prime_count}")

main_function()
# Flowgraph:
  #    |      |
  #    |      |
  #    |      |
  #    v      |
# calculate_sum ---> find_maximum ---> print_numbers
   #   |
    #  v
  #is_prime ---> count_primes_in_range
 #     |
  #    v
# main_function
#calculate_sum -> find_maximum -> print_numbers -> is_prime -> count_primes_in_range -> main_function
#calculate_sum -> find_maximum -> print_numbers -> is_prime -> count_primes_in_range -> return
#calculate_sum -> find_maximum -> return
#calculate_sum -> return


