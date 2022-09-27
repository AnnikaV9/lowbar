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
import threading


class lowbar:

    """
    The main lowbar class.
    """

    def __init__(self, bar_iter: (range, int)=0, smooth_iter: bool=False, bar_load_fill: str="#", bar_blank_fill: str="-", bar_desc: str="", remove_ends: bool=False, no_clear: bool=False) -> None:

        """
        Checks and initializes a few variables.
        """

        if not isinstance(bar_load_fill, str):
            raise TypeError("arg bar_load_fill should be type str")

        if not isinstance(bar_blank_fill, str):
            raise TypeError("arg bar_blank_fill should be type str")

        if not isinstance(smooth_iter, bool):
            raise TypeError("arg smooth_iter should be type bool")

        if not isinstance(bar_desc, str):
            raise TypeError("arg bar_desc should be type str")

        if not isinstance(remove_ends, bool):
            raise TypeError("arg remove_ends should be type bool")

        if not isinstance(no_clear, bool):
            raise TypeError("arg no_clear should be type bool")

        if not isinstance(bar_iter, range):
            if not isinstance(bar_iter, int):
                raise TypeError("arg bar_iter should be either type range or int")

            bar_iter: range = range(bar_iter)

        if len(bar_load_fill) != 1:
            raise TypeError("arg bar_load_fill should be a single char")

        if len(bar_blank_fill) != 1:
            raise TypeError("arg bar_blank_fill should be a single char")

        self.bar_iter: range = bar_iter
        self.smooth_iter: bool = smooth_iter
        self.completion: int = 1
        self.bar_load_fill: str = bar_load_fill
        self.bar_blank_fill: str = bar_blank_fill
        self.bar_is_smoothing: bool = False
        self.bar_desc: str = bar_desc
        self.bar_ends: str = ("[", "]") if not remove_ends else (" ", " ")
        self.no_clear: bool = no_clear

    def __enter__(self) -> object:

        """
        Context manager setup to automatically display bar
        without requiring new().
        """

        self.new()

        return self

    def __exit__(self, *exc) -> None:

        """
        Context manager exit to clear the bar automatically
        without requiring clear().
        """

        if not self.no_clear:
            self.clear()

        else:
            print()

    def __iter__(self) -> object:

        """
        Iterable manager that automatically runs new() at the
        start and clear() at the end
        """

        self.new()

        div: float = 100 / len(list(self.bar_iter))
        add: float = div

        try:
            for item in self.bar_iter:
                yield item
                self.update(int(div)) if not self.smooth_iter else self.update_smooth(int(div))
                div += add

        finally:
            if not self.no_clear:
                self.clear()

            else:
                print()

    def _print_internal(self, text: str) -> None:

        """
        Writes data to stdout
        """

        print(text, end='', flush=True)

    def _get_terminal_columns(self) -> int:

        """
        Returns the number of columns in the running console.
        """

        return shutil.get_terminal_size().columns

    def _update_bar(self) -> None:

        """
        Refreshes the current bar with new values, and a
        possibly resized console.
        """

        temp_desc = self.bar_desc if len(self.bar_desc) + 20 < self._get_terminal_columns() else ""
        completion_string: str = f"{temp_desc}  {str(self.completion)}" if self.completion < 10 else f"{temp_desc} {str(self.completion)}"
        bar_size: int = self._get_terminal_columns() - (len(completion_string) + 7)
        bar_loaded_size: int = int(bar_size * (self.completion / 100))
        bar_blank_fill: int = bar_size - bar_loaded_size
        self._print_internal(f"\r{completion_string} % {self.bar_ends[0]}{bar_loaded_size * self.bar_load_fill}{bar_blank_fill * self.bar_blank_fill}{self.bar_ends[1]} ")

    def _overwrite_bar(self, text: str="") -> None:

        """
        Overwrite the loading bar with optional text.
        """

        overwrite: str = " " * (self._get_terminal_columns() - len(text))
        self._print_internal(f"\r{text}{overwrite}")

    def _update_bar_smooth(self, percentage: int) -> None:

        """
        Wraps _update_bar() with a smoother but slower animation.
        """

        self.bar_is_smoothing = True
        distance: int = percentage - self.completion
        for i in range(distance):
            del i
            self.completion += 1
            self._update_bar()
            time.sleep(0.002)

        self.bar_is_smoothing = False

    def _block_when_smoothing(self) -> None:

        """
        Blocks the main thread if bar is still running _update_bar_smooth()
        Only used if another function call is performed. If the bar is
        left to smooth properly without calling other functions, it will
        be non-blocking.
        """

        while True:
            if not self.bar_is_smoothing:
                break

    def update(self, percentage: int) -> None:

        """
        Increases or decreases the completed percentage and
        calls _update_bar().
        """

        if not isinstance(percentage, int):
            raise TypeError("arg percentage should be type int")

        self._block_when_smoothing()

        self.completion = percentage
        self._update_bar()

    def new(self) -> None:

        """
        Alias for update(0)
        """

        self.update(0)

    def update_smooth(self, percentage: int) -> None:

        """
        Increases the completed percentage and calls _update_bar_smooth()
        in a seperate thread so it's non-blocking.
        Cannot decrease the completed percentage with this function.
        """

        if not isinstance(percentage, int):
            raise TypeError("arg percentage should be type int")

        self._block_when_smoothing()

        threading.Thread(target=self._update_bar_smooth, args=[percentage]).start()

    def log(self, text: str) -> None:

        """
        Log text to the console without affecting the bar.
        """

        if not isinstance(text, str):
            raise TypeError("arg text should be type str")

        self._block_when_smoothing()

        self._overwrite_bar(f"{text}")
        print()
        self._update_bar()

    def clear(self) -> None:

        """
        Clears the bar completely from the console.
        """

        self._block_when_smoothing()

        self._overwrite_bar()


# Backwards compatibility with earlier versions
LowBar = lowbar
