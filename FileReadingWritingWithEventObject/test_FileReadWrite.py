import unittest, threading
# from threading import Thread, Event
from unittest.mock import patch, mock_open, MagicMock
from FileReadWrite import FileReadingWrting


class TestFileReadWrite(unittest.TestCase):

    def setUp(self):
        self.fileReadWriter = FileReadingWrting()

    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open, read_data='line1\nline2\nline3\nline4\nline5\n')
    def test_reader(self, mock_file, mock_print):

        def mock_read_lines(file):
            self.fileReadWriter.data = ['line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5\n']
            self.fileReadWriter.isFileFinish = True  # Simulate file finish after 1 call
        
        # Patch the `read_lines` function to control its behavior
        with patch.object(self.fileReadWriter, 'read_lines', side_effect=mock_read_lines):
            # Call the reader function
            self.fileReadWriter.reader("src.txt")

        mock_file.assert_called_once_with('src.txt', 'r')
        self.assertEqual(self.fileReadWriter.data, ['line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5\n'])
        self.assertTrue(self.fileReadWriter.e.is_set())

    @patch('builtins.print')
    def test_read_lines_1(self, mock_print):
        mock_file = MagicMock()
        mock_file.readline.side_effect = ['line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5\n', '']

        self.fileReadWriter.read_lines(mock_file)

        self.assertEqual(self.fileReadWriter.data, ['line1\n', 'line2\n', 'line3\n', 'line4\n', 'line5\n'])

        self.assertFalse(self.fileReadWriter.isFileFinish)

        mock_print.assert_called_with("Reading file")
    
    @patch('builtins.print')
    def test_read_lines_2(self, mock_print):
        mock_file = MagicMock()
        mock_file.readline.side_effect = ['line1\n', 'line2\n', 'line3\n', '']

        self.fileReadWriter.read_lines(mock_file)

        self.assertEqual(self.fileReadWriter.data, ['line1\n', 'line2\n', 'line3\n'])

        self.assertTrue(self.fileReadWriter.isFileFinish)

        mock_print.assert_called_with("Reading file")
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('time.sleep', return_value=None)  
    @patch('builtins.print') 
    def test_write_lines(self, mock_print, mock_sleep, mock_file):
    # Add some dummy data to self.data to simulate data being written
        self.fileReadWriter.data = ['line1\n', 'line2\n', 'line3\n']
        
        with patch.object(self.fileReadWriter, 'data', self.fileReadWriter.data):
            mock_file_handle = mock_file()
            
            self.fileReadWriter.write_lines(mock_file_handle)

            mock_file_handle.write.assert_any_call('line1\n')
            mock_file_handle.write.assert_any_call('line2\n')
            mock_file_handle.write.assert_any_call('line3\n')


            self.assertEqual(self.fileReadWriter.data, [])


if __name__=="__main__":
    unittest.main()
