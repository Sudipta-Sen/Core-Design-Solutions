# Design a Solution for File Reading and Writing with Threads

Design a solution where two threads work together to transfer the contents of one file to another:

1. **Reader Thread:** This thread reads the source file in chunks of 5 lines at a time.

2. **Writer Thread:** This thread receives the lines read by the reader and writes them into a destination file.

The reader thread continuously reads 5 lines and passes them to the writer thread, which then writes the lines to the destination file. This process repeats until all lines in the source file are processed. For the final read, if there are fewer than 5 lines, the remaining lines are transferred and written as the last batch.