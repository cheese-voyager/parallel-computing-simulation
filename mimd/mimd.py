from multiprocessing import Process

def calculate_average(scores):
    avg = sum(scores) / len(scores)
    print(f"Average process: average score = {avg}")

def find_max(scores):
    maximum = max(scores)
    print(f"Max process: highest score = {maximum}")

if __name__ == "__main__":
    class_a_scores = [70, 80, 90]
    class_b_scores = [65, 85, 95]

    p1 = Process(target=calculate_average, args=(class_a_scores,))
    p2 = Process(target=find_max, args=(class_b_scores,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()