from threading import Thread, Event
import string, random, time

class FileReadingWrting:
    def __init__(self):
        self.data = []
        self.e = Event()
        self.isFileFinish = False
        
    def reader(self, srcFile):
        with open(srcFile, 'r') as f:
            while not self.isFileFinish:
                while not self.e.is_set():
                    self.read_lines(f)
                    self.e.set()
                    while not self.isFileFinish and self.e.is_set(): time.sleep(2)
        print("Reader thread fiishes")
    
    def read_lines(self, file):
        print("Reading file")
        while len(self.data) < 5:
            line = file.readline()
            if not line:
                self.isFileFinish = True
                break
            self.data.append(line)


    def writer(self, dstFile):
        with open(dstFile, 'w') as f:
            while not self.isFileFinish:
                self.e.wait()
                self.write_lines(f)
                self.e.clear()
        print("Writer thread finishes")
    
    def write_lines(self, file):
        print("Writing into file")
        if self.data:
            time.sleep(5) # Simulate some work
            for line in self.data: file.write(line)
            self.data.clear()


    def start(self, srcFile, dstFile):
        t1 = Thread(target=self.reader, args=(srcFile,))
        t2 = Thread(target=self.writer, args=(dstFile,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    def generate_file(self, filename, num_lines):
        """Generates a file with the given number of random text lines."""
        with open(filename, 'w') as file:
            for i in range(1, num_lines+1):
                line = ' '.join(
                            ''.join(random.choices(string.ascii_letters + string.digits, k=random.randrange(4, 10)))
                            for _ in range(random.randrange(3, 11))
                        )
                formatted_line = f"Line-{i} {line}\n"
                file.write(formatted_line)
        print(f"File '{filename}' with {num_lines} lines generated.")



if __name__ == "__main__":
    srcFile = "src.txt"
    dstFile = "dst.txt"
    fileReadWrite = FileReadingWrting()
    fileReadWrite.generate_file(srcFile, 5)
    fileReadWrite.start(srcFile, dstFile)