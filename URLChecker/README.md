# URL Checker with Multithreading
## Description:

Implement a system to check a list of URLs in parallel using threads. If the URL responds with a 200 status, save the response body to a file, otherwise write "Not reachable".

## Topics: 
Multithreading, HTTP, File I/O, Error handling.

## Key Points

1. **Handling Response Content in File Writing:**

    - `response.content` returns the data in `byte` format. There are two main approaches to convert byte into str or write this byte content directly into a file:

        - **Option 1:** Use `response.text` to directly write the string version of the byte data.

        - **Option 2:** Use `.decode()` to **decode** the byte content into a specific format (like `utf-8`), and write it in `w` mode:

        - **Option 3:** Open the file in `wb` mode if you plan to write `response.content` without conversion.
    
2. **Exception Handling with `exp.args`:**

    - In the event of an error, `exp.args` is a tuple that contains information related to the exception.

        - `exp.args[0]` typically holds the **primary error message or code**. 

        - Use `str(exp.args)` to safely convert the tupple to a string format for logging or writing to a file. This is necessary because `.decode()` works on bytes, but `exp.args` is usually a string.

## ThreadPoolExecutor vs Thread

1. Thread Management:

    - **Thread:** When using the `Thread` class directly, we have to manually create and manage each thread, including starting, joining, and tracking its completion. If we have a lot of URLs, this can be cumbersome.

    - **ThreadPoolExecutor:** It abstracts away much of this complexity by managing a pool of threads for we. We submit tasks and it automatically distributes them among available threads, handles their lifecycle, and provides useful utilities like `submit()` and `map()` for task execution.

2. Reusability and Thread Pooling:

    - **Thread:** With Thread, every time you need a new task to run, we have to create a new thread instance. Threads are not reused, which can be inefficient for handling many tasks.

    - **ThreadPoolExecutor:** It reuses threads from a pool, reducing the overhead of constantly creating and destroying threads. This improves performance, especially when the overhead of creating threads is non-trivial.

3. Graceful Shutdown:

    - **Thread:** Manually managing thread lifecycles can be error-prone, and we must ensure all threads have finished executing or handle cleanup manually.

    - **ThreadPoolExecutor:** It provides shutdown() methods to gracefully shut down all worker threads after they complete their current tasks, ensuring clean resource management.