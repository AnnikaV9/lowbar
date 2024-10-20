"""
Test cases
"""

import unittest
from unittest.mock import patch
from os import terminal_size
from io import StringIO

from lowbar import lowbar


class TestLowbar(unittest.TestCase):
    @patch("shutil.get_terminal_size")
    @patch("sys.stdout", new_callable=StringIO)
    def test_update_add_log(self, mock_stdout, mock_terminal_size):
        mock_terminal_size.return_value = terminal_size((53, 20))
        bar = lowbar()
        bar.new()
        bar.update(20)
        bar.update(50)
        bar.log("Test log message")
        bar.add(50)
        bar.clear()
        self.assertIn("Test log message", mock_stdout.getvalue())
        self.assertIn("\r  0 % [-------------------------------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 20 % [########-----------------------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 50 % [#####################----------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 100 % [##########################################] ", mock_stdout.getvalue())
        self.assertIn("\r                                                     ", mock_stdout.getvalue())

    @patch("shutil.get_terminal_size")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_over_100(self, mock_stdout, mock_terminal_size):
        mock_terminal_size.return_value = terminal_size((53, 20))
        bar = lowbar()
        bar.new()
        bar.add(150)
        self.assertIn("\r 100 % [##########################################] ", mock_stdout.getvalue())

    @patch("shutil.get_terminal_size")
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_under_0(self, mock_stdout, mock_terminal_size):
        mock_terminal_size.return_value = terminal_size((53, 20))
        bar = lowbar()
        bar.new()
        bar.add(-50)
        self.assertIn("\r  0 % [-------------------------------------------] ", mock_stdout.getvalue())

    @patch("shutil.get_terminal_size")
    @patch("sys.stdout", new_callable=StringIO)
    def test_desc(self, mock_stdout, mock_terminal_size):
        mock_terminal_size.return_value = terminal_size((53, 20))
        bar = lowbar(desc="Downloading")
        bar.new()
        bar.update(100)
        self.assertIn("\rDownloading  0 % [--------------------------------] ", mock_stdout.getvalue())
        self.assertIn("\rDownloading 100 % [###############################] ", mock_stdout.getvalue())

    @patch("shutil.get_terminal_size")
    @patch("sys.stdout", new_callable=StringIO)
    def test_desc_too_long(self, mock_stdout, mock_terminal_size):
        mock_terminal_size.return_value = terminal_size((53, 20))
        bar = lowbar(desc="A very long description that will not fit in the terminal")
        bar.new()
        bar.update(100)
        self.assertIn("\r  0 % [-------------------------------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 100 % [##########################################] ", mock_stdout.getvalue())

    @patch("shutil.get_terminal_size")
    @patch('sys.stdout', new_callable=StringIO)
    def test_iterable(self, mock_stdout, mock_terminal_size):
        mock_terminal_size.return_value = terminal_size((53, 20))
        for _ in lowbar(3, keep_receipt=True):
            pass

        self.assertIn("\r  0 % [-------------------------------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 33 % [##############-----------------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 66 % [############################---------------] ", mock_stdout.getvalue())
        self.assertIn("\r 100 % [##########################################] \n", mock_stdout.getvalue())

    @patch("shutil.get_terminal_size")
    @patch('sys.stdout', new_callable=StringIO)
    def test_iterable_no_receipt(self, mock_stdout, mock_terminal_size):
        mock_terminal_size.return_value = terminal_size((53, 20))
        for _ in lowbar(3):
            pass

        self.assertIn("\r  0 % [-------------------------------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 33 % [##############-----------------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 66 % [############################---------------] ", mock_stdout.getvalue())
        self.assertIn("\r 100 % [##########################################] ", mock_stdout.getvalue())
        self.assertIn("\r                                                     ", mock_stdout.getvalue())

    @patch("shutil.get_terminal_size")
    @patch('sys.stdout', new_callable=StringIO)
    def test_context_manager(self, mock_stdout, mock_terminal_size):
        mock_terminal_size.return_value = terminal_size((53, 20))
        with lowbar(keep_receipt=True) as bar:
            bar.update(100)

        self.assertIn("\r  0 % [-------------------------------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 100 % [##########################################] \n", mock_stdout.getvalue())

    @patch("shutil.get_terminal_size")
    @patch('sys.stdout', new_callable=StringIO)
    def test_context_manager_no_receipt(self, mock_stdout, mock_terminal_size):
        mock_terminal_size.return_value = terminal_size((53, 20))
        with lowbar() as bar:
            bar.update(100)

        self.assertIn("\r  0 % [-------------------------------------------] ", mock_stdout.getvalue())
        self.assertIn("\r 100 % [##########################################] ", mock_stdout.getvalue())
        self.assertIn("\r                                                     ", mock_stdout.getvalue())

    def test_errors(self):
        with self.assertRaises(TypeError):
            bar = lowbar("invalid iter type")

        with self.assertRaises(TypeError):
            bar = lowbar(load_fill="invalid load fill length")

        with self.assertRaises(TypeError):
            bar = lowbar(blank_fill="invalid blank fill length")

        with self.assertRaises(TypeError):
            bar = lowbar(desc=list("invalid desc type"))

        with self.assertRaises(TypeError):
            bar = lowbar(remove_ends="invalid remove ends type")

        with self.assertRaises(TypeError):
            bar = lowbar(keep_receipt="invalid keep receipt type")

        with self.assertRaises(ValueError):
            bar = lowbar()
            bar.update(101)

        with self.assertRaises(ValueError):
            bar = lowbar()
            bar.update(-1)

        with self.assertRaises(TypeError):
            bar = lowbar()
            bar.log(1)


if __name__ == '__main__':
    unittest.main()
