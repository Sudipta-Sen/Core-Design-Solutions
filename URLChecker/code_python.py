import requests, logging, threading, time
from concurrent.futures import ThreadPoolExecutor

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_url_list(file_path: str = 'urllist.txt') -> list:

    try:
        with open(file_path, 'r') as f:
            urllist = [line.strip() for line in f.readlines()]
        return urllist
    except FileNotFoundError:
        logging.error(f"File Not found {file_path}")
        return []
    
def fetch_url_content(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status() # catch any non-200 status codes
        return response.content.decode('utf-8')
    except Exception as exp:
        logging.error(f"Failed to fetch URL-{url}: {exp.args}\n")
        return str(exp.args)

def write_to_file(content: str, file_name: str) -> None:
    try:
        with open(file_name, 'w') as f:
            f.write(content)
    except Exception as exp:
        logging.error(f"Failed to write into file {file_name}: {exp.args}\n")

def process_url(url: str, idx: int) -> None:
    logging.info(f"Processing Url {url}")
    content = fetch_url_content(url)
    file_name = f"file-{idx}.html"
    write_to_file(content, file_name)

def process_url_file_with_thread_method(file_path: str = 'urllist.txt') -> None:
    urllist = get_url_list(file_path)
    threads = []
    if urllist:
        for idx, url in enumerate(urllist):
            thread = threading.Thread(target=process_url, args=(url, idx))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
    else:
        logging.warning(f'url list is empty')

def process_url_file_with_ThreadPoolExecutor(file_path: str = 'urllist.txt') -> None:
    urllist = get_url_list(file_path)
    
    if urllist:
        with ThreadPoolExecutor(max_workers=3) as executor:
            for idx, url in enumerate(urllist):
                executor.submit(process_url, url, idx)
    else:
        logging.warning(f'url list is empty')

if __name__ == "__main__":
    start_time = time.perf_counter()

    process_url_file_with_thread_method()
    # process_url_file_with_ThreadPoolExecutor()
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    logging.info(f"\nExecution time - {execution_time}")

        