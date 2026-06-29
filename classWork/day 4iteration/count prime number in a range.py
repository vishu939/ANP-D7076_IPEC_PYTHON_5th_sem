# Function to check prime using iteration
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):   # loop till sqrt(n)
        if n % i == 0:
            return False
    return True

# Input range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0
print(f"Prime numbers between {start} and {end} are:")

# iterate through range
for num in range(start, end + 1):
    if is_prime(num):   # check prime by iteration
        print(num, end=" ")
        count += 1

# print total count
print(f"\nTotal prime numbers found: {count}")
