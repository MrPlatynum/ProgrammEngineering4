def main():
    expression = "4 * 100 - 54"

    correct_answer = 4*100-54

    user_answer = int(input(f"Solve the expression: {expression} = "))

    print(f"Correct answer: {correct_answer}")
    print(f"Your answer: {user_answer}")

if __name__ == "__main__":
    main()