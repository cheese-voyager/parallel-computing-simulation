from multiprocessing import Process, Queue

def matrix_add(A, B, q):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    print("Addition process result =", result)
    q.put(("Addition", result))

def matrix_subtract(C, D, q):
    result = []
    for i in range(len(C)):
        row = []
        for j in range(len(C[0])):
            row.append(C[i][j] - D[i][j])
        result.append(row)
    print("Subtraction process result =", result)
    q.put(("Subtraction", result))

if __name__ == "__main__":
    A = [
        [1, 2],
        [3, 4]
    ]
    B = [
        [5, 6],
        [7, 8]
    ]

    C = [
        [9, 8],
        [7, 6]
    ]
    D = [
        [1, 1],
        [2, 2]
    ]

    q = Queue()

    p1 = Process(target=matrix_add, args=(A, B, q))
    p2 = Process(target=matrix_subtract, args=(C, D, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("\nMIMD Final Results:")
    for _ in range(2):
        print(q.get())