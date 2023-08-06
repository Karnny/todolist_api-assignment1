
# เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial
# เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว

def main():
    try:
        num = int(input("Enter a number to find its factorial trailing zeroes: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(num)
            print(f"The factorial of {num} is: {result}")
            trailing_zeros = count_trailing_zeros(result)
            print(f"The number of trailing zeros in the factorial is: {trailing_zeros}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

def count_trailing_zeros(fr):
    factorial_result = fr
    count = 0
    while factorial_result % 10 == 0:
        factorial_result //= 10
        count += 1
    return count

if __name__ == "__main__":
    main()
