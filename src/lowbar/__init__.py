"""
The simplest no-nonsense progress bar for python.
https://github.com/AnnikaV9/lowbar/issues
"""

#
# MIT License
#
# Copyright (c) 2022 AnnikaV9
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import shutil
import time


class LowBar:
    
    """
    The main lowbar class
    """

    def __init__(self, bar_load_fill: str="#", bar_blank_fill: str="-"):

        """
        Initializes a few variables
        """

        if not isinstance(bar_load_fill, str):
            raise TypeError("bar_load_fill should be type str")

        if not isinstance(bar_blank_fill, str):
            raise TypeError("bar_blank_fill should be type str")

        self.completion: int = 1
        self.bar_load_fill: str = bar_load_fill
        self.bar_blank_fill: str = bar_blank_fill

    def __enter__(self):

        """
        Context manager setup for the bar - automatically display bar
        without requiring update()
        """

        self.update(0)

        return self

    def __exit__(self, type, value, traceback):

        """
        Context manager exit to clear the bar automatically
        without requiring clear()
        """

        if type == AttributeError:
            raise AttributeError(f"{value}\nValid functions: update() update_smooth() log() clear()") from None

        self._overwrite_bar()

    def _print_internal(self, text: str):

        """
        Writes data to stdout
        """

        print(text, end='', flush=True)

    def _get_terminal_columns(self) -> int:

        """
        Returns the number of columns in the running console
        """

        return shutil.get_terminal_size().columns

    def _update_bar(self):

        """
        Refreshes the current bar with new values
        """

        completion_string: str = f" {str(self.completion)}" if self.completion < 10 else str(self.completion)
        bar_size: int = self._get_terminal_columns() - (len(completion_string) + 6)
        bar_loaded_size: int = int(bar_size * (self.completion / 100))
        bar_blank_fill: int = bar_size - bar_loaded_size
        self._print_internal(f"\r{completion_string} % [{bar_loaded_size * self.bar_load_fill}{bar_blank_fill * self.bar_blank_fill}] ")

    def _overwrite_bar(self, text: str=""):

        """
        Overwrite the loading bar with optional text
        """

        overwrite: str = (" " * (self._get_terminal_columns() - len(text)))
        self._print_internal(f"\r{text}{overwrite}")

    def update(self, percentage: int):

        """
        Increases or decreases the completed percentage and
        calls _update_bar()
        """

        if not isinstance(percentage, int):
            raise TypeError("percentage should be type int")

        self.completion = percentage
        self._update_bar()

    def update_smooth(self, percentage: int):

        """
        Same as update(), but with a smoother but slower animation
        Cannot decrease the completed percentage with this function
        """

        if not isinstance(percentage, int):
            raise TypeError("percentage should be type int")

        distance: int = percentage - self.completion
        for i in range(distance):
            del i
            self.completion += 1
            self._update_bar()
            time.sleep(0.005)

    def log(self, text: str):

        """
        Log text to the console without affecting the bar
        """

        if not isinstance(text, str):
            raise TypeError("text should be type str")

        self._overwrite_bar(f"{text}")
        print()
        self._update_bar()

    def clear(self):

        """
        Clears the bar completely from the console
        """

        self._overwrite_bar()
