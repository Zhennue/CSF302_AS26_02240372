def IdentityMatrix_372(size_372):
    if size_372 < 1:
        raise ValueError("Matrix size must be at least 1.")
    return [[1 if row_372 == col_372 else 0 for col_372 in range(size_372)] for row_372 in range(size_372)]

if __name__ == "__main__":
    for row_372 in IdentityMatrix_372(3):
        print(row_372)
