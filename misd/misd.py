from multiprocessing import Process, Queue

def matrix_sum(matrix, q):
    total = sum(sum(row) for row in matrix)
    print("Sum process result =", total)
    q.put(("Sum", total))

def matrix_transpose(matrix, q):
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("Transpose process result =", transpose)
    q.put(("Transpose", transpose))

def scalar_multiply(matrix, q):
    result = [[element * 2 for element in row] for row in matrix]
    print("Scalar x2 process result =", result)
    q.put(("Scalar x2", result))

if __name__ == "__main__":
    A = [
        [1, 2],
        [3, 4]
    ]

    q = Queue()

    p1 = Process(target=matrix_sum, args=(A, q))
    p2 = Process(target=matrix_transpose, args=(A, q))
    p3 = Process(target=scalar_multiply, args=(A, q))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("\nMISD Final Results:")
    for _ in range(3):
        print(q.get())