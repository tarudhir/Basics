m = int(input("Enter marks: "))

if 90 <= m <= 100:
    print("A grade")
elif 75 <= m < 90:
    print("B grade")
elif 40 <= m < 75:
    print("C grade")
elif 0 <= m < 40:
    print("F grade")
else:
    print("Invalid marks")
