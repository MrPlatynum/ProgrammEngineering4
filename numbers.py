def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))

    sum1 = num1 + num2
    sum2 = num3 + num4

    result = sum1 / sum2
    print(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()