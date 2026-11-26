from Lab4_Q10_BinaryMatrixExponentiation_372 import BinaryMatrixExponentiation_372

def CountGraphWalks_372(adjacency_372, edges_372, start_372, end_372, modulus_372):
    size_372 = len(adjacency_372)
    if edges_372 < 0 or modulus_372 <= 0:
        raise ValueError("Edge count must be non-negative and modulus positive.")
    if not (0 <= start_372 < size_372 and 0 <= end_372 < size_372):
        raise ValueError("Start and end vertices must be valid matrix indexes.")
    powered_372 = BinaryMatrixExponentiation_372(adjacency_372, edges_372, modulus_372)
    return powered_372[start_372][end_372]

if __name__ == "__main__":
    adjacency_372 = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]
    print("Walks of exactly 2 edges from vertex 0 to 2:", CountGraphWalks_372(adjacency_372, 2, 0, 2, 100))
