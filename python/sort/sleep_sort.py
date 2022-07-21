import threading
import time
import concurrent.futures

result = []
nums = [4, 2, 6, 3, 8, 1]
def thread_function(num):
    time.sleep(num)
    return num

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(thread_function, num) for num in nums]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

# threads = [threading.Thread(target=thread_function, args=(num,)) for num in nums]
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
