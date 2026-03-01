import numpy as np

if __name__ == "__main__":
    data = np.array([1, 2, 3, 4, 5])

    result = data * 2

    print("Original Data :", data)
    print("SIMD Result   :", result)