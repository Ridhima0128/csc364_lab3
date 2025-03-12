import threading
import time
from queue import Queue

def sum_of_squares(chunk, result_queue):
    result = sum(x ** 2 for x in chunk)
    result_queue.put(result)

def threaded_sum_of_squares(numbers, num_threads):
    chunk_size = len(numbers) // num_threads
    threads = []
    result_queue = Queue()

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_threads - 1 else len(numbers)
        thread = threading.Thread(target=sum_of_squares, args=(numbers[start_index:end_index], result_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = 0
    while not result_queue.empty():
        total_sum += result_queue.get()

    return total_sum

numbers = [i for i in range(1, 1000001)]  # List of numbers from 1 to 1 million
num_threads = 4
start_time = time.time()
result = threaded_sum_of_squares(numbers, num_threads)
end_time = time.time()
print(f"Threaded result: {result}, Time taken: {end_time - start_time:.5f} seconds")
