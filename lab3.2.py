import multiprocessing
import time

def sum_of_squares_process(chunk, result_queue):
    result = sum(x ** 2 for x in chunk)
    result_queue.put(result)

def multiprocessing_sum_of_squares(numbers, num_processes):
    chunk_size = len(numbers) // num_processes
    processes = []
    result_queue = multiprocessing.Queue()

    for i in range(num_processes):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_processes - 1 else len(numbers)
        process = multiprocessing.Process(target=sum_of_squares_process, args=(numbers[start_index:end_index], result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = 0
    while not result_queue.empty():
        total_sum += result_queue.get()

    return total_sum

if __name__ == '__main__':
    numbers = [i for i in range(1, 1000001)]  
    num_processes = 4
    start_time = time.time()
    result = multiprocessing_sum_of_squares(numbers, num_processes)
    end_time = time.time()
    print(f"Multiprocessing result: {result}, Time taken: {end_time - start_time:.5f} seconds")
