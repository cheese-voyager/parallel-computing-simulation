from multiprocessing import Process, Queue

def square(x, q):
    result = x * x
    print(f"Square of {x} = {result}")
    q.put(("square", result))

def cube(x, q):
    result = x * x * x
    print(f"Cube of {x} = {result}")
    q.put(("cube", result))

def double(x, q):
    result = x * 2
    print(f"Double of {x} = {result}")
    q.put(("double", result))

if __name__ == "__main__":
    q = Queue()
    data = 5

    p1 = Process(target=square, args=(data, q))
    p2 = Process(target=cube, args=(data, q))
    p3 = Process(target=double, args=(data, q))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    results = [q.get() for _ in range(3)]
    print("Sum MISD =", results)