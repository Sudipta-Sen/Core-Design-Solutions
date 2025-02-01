import unittest
from unittest.mock import patch, mock_open, MagicMock
import requests
from io import StringIO
from code_python import *

class TestURLProcessing(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="https://example.com\nhttps://google.co.in")
    def test_get_url_list(self, mock_file):
        urllist = get_url_list()
        self.assertEqual(urllist, ["https://example.com", "https://google.co.in"])
        mock_file.assert_called_with('urllist.txt', 'r')
    
    @patch('requests.get')
    def test_fetch_url_content_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content =  b"<html>Success</html>"
        mock_get.return_value = mock_response

        content = fetch_url_content("https://example.com")
        self.assertEqual(content, "<html>Success</html>")
        mock_get.assert_called_with("https://example.com")
    
    @patch('requests.get')
    def test_fetch_url_content_failure(self, mock_get):
        mock_get.side_effect = requests.ConnectionError("Failed to connect")

        content = fetch_url_content("https://badurl.com")
        self.assertIn("Failed to connect", content)
    
    @patch('builtins.open', new_callable=mock_open)
    def test_write_to_file(self, mock_file):
        content = "<html>Test Content</html>"
        write_to_file(content, "file-0.html")
        mock_file.assert_called_with("file-0.html", 'w')
        mock_file().write.assert_called_with(content)

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_process_url_file_with_ThreadPoolExecutor(self, mock_file, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content =  b"<html>Success</html>"
        mock_get.return_value = mock_response

        file_handles = {
            'urllist.txt': mock_open(read_data="https://example.com").return_value,
            'file-0.html': mock_open().return_value,
        }

        def side_effect(file_name, mode):
            return file_handles[file_name]
        
        mock_file.side_effect = side_effect

        process_url_file_with_ThreadPoolExecutor()

        mock_file.assert_any_call('urllist.txt', 'r')

        mock_file.assert_any_call('file-0.html', 'w')
        
        file_handles['file-0.html'].write.assert_called_once_with("<html>Success</html>")

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_process_url_file_with_thread_method(self, mock_file, mock_get):
    # Mock the HTTP response for requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html>Success</html>"
        mock_get.return_value = mock_response

        # Mock the 'open' behavior for reading and writing files
        file_handles = {
            'urllist.txt': mock_open(read_data="https://example.com").return_value,
            'file-0.html': mock_open().return_value,
        }
        
        def side_effect(file_name, mode):
            return file_handles[file_name]

        # Set the side effect to mock different files
        mock_file.side_effect = side_effect

        # Execute the function to test
        process_url_file_with_thread_method()

        # Assert that the file 'urllist.txt' was opened for reading
        mock_file.assert_any_call('urllist.txt', 'r')

        mock_file.assert_any_call('file-0.html', 'w')

        # Assert that 'file-0.html' was written with correct content
        file_handles['file-0.html'].write.assert_called_once_with("<html>Success</html>")

if __name__ == "__main__":
    unittest.main()