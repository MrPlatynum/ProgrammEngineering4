def main():
    angle = float(input("Enter the angle in degrees: "))

    hours = int(angle / 30)

    minutes = int((angle - (hours * 30)) / 0.5)

    print(f"Full Hours: {hours}")
    print(f"Full Minutes: {minutes}")

if __name__ == "__main__":
    main()



