def calculate_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * calculate_factorial(n-1)

def main():
    num = int(input("Enter a number to calculate factorial: "))
    result = calculate_factorial(num)
    print(f"Factorial of {num} is: {result}")

if __name__ == "__main__":
    main()
    