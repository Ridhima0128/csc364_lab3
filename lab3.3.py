import threading
import multiprocessing
import time
import queue

def io_bound_task(task_id, result_queue):
    time.sleep(2) 
    result_queue.put(task_id)  

def threaded_io_bound_task(num_threads):
    threads = []
    result_queue = queue.Queue()  

    for i in range(num_threads):
        thread = threading.Thread(target=io_bound_task, args=(i, result_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    return results

def multiprocessing_io_bound_task(num_processes):
    processes = []
    result_queue = multiprocessing.Queue()

    for i in range(num_processes):
        process = multiprocessing.Process(target=io_bound_task, args=(i, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    return results

if __name__ == "__main__":
    num_threads = 4
    num_processes = 4

    start_time = time.time()
    threaded_io_bound_task(num_threads)
    end_time = time.time()
    print(f"Time taken for threaded I/O-bound task: {end_time - start_time:.5f} seconds")

    start_time = time.time()
    multiprocessing_io_bound_task(num_processes)
    end_time = time.time()
    print(f"Time taken for multiprocessing I/O-bound task: {end_time - start_time:.5f} seconds")
