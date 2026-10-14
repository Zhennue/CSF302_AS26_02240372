print("Square Matrix Multiplication")
print("----------------------------")

n372 = int(input("Enter matrix size (2, 4, 8, 16...): "))

if n372 < 2 or (n372 & (n372 - 1)) != 0:
    print("Please enter 2, 4, 8, 16, etc.")
else:
    print("\nEnter Matrix A:")

    a372 = []

    for i372 in range(n372):
        row372 = []
        for j372 in range(n372):
            num372 = int(input("Enter number: "))
            row372.append(num372)
        a372.append(row372)

    print("\nEnter Matrix B:")

    b372 = []

    for i372 in range(n372):
        row372 = []
        for j372 in range(n372):
            num372 = int(input("Enter number: "))
            row372.append(num372)
        b372.append(row372)

    # Create result matrix
    c372 = []

    for i372 in range(n372):
        row372 = []
        for j372 in range(n372):
            row372.append(0)
        c372.append(row372)

    # Matrix multiplication
    steps372 = 0

    for i372 in range(n372):
        for j372 in range(n372):
            for k372 in range(n372):
                c372[i372][j372] = c372[i372][j372] + a372[i372][k372] * b372[k372][j372]
                steps372 += 1

    # Display result
    print("\nResultant Matrix:")

    for i372 in range(n372):
        print(c372[i372])

    print("\nBasic operation count:", steps372)