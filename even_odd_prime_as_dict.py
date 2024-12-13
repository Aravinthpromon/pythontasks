
import math
def is_prime(num):
   
    if num < 2:
        return False  
    for i in range(2, int(math.sqrt(num)) + 1):

        if num % i == 0:  
            return False
    return True  

def categorize_numbers(start, end):
   
    even_numbers = []
    odd_numbers = []
    prime_numbers = []

    for num in range(start, end + 1): 
        if num % 2 == 0:
            even_numbers.append(num)  
        else:
            odd_numbers.append(num)  

        if is_prime(num):
            prime_numbers.append(num)  

    
    return {
        "Even": even_numbers,
        "Odd": odd_numbers,
        "Prime": prime_numbers
    }

start_range = int(input("Enter the start of of the range: "))
end_range = int(input("Enter the end of the range: "))

numbers_dict = categorize_numbers(start_range, end_range)
print("\nNumbers categorized:")
for category, numbers in numbers_dict.items():
    print(f"{category}: {numbers}")



   
         

    




