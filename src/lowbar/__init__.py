#
# https://github.com/AnnikaV9/lowbar/issues
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <https://unlicense.org>
#

# import necessary modules
import sys
import shutil
import time


# the main class
class lowbar:

    # initialize a few variables
    def __init__(self, bar_load_fill: str="#", bar_blank_fill: str="-"):
        self.completion: int = 1
        self.bar_load_fill: str = bar_load_fill
        self.bar_blank_fill: str = bar_blank_fill

    # writing data to stdout
    def _print_internal(self, text: str):
        sys.stdout.write(text)
        sys.stdout.flush()

    # obtaining the number of columns in the running console
    def _get_terminal_columns(self) -> int:
        return shutil.get_terminal_size().columns

    # refresh the current bar with new values
    def _update_bar(self):
        completion_string: str = str(self.completion)
        bar_size: int = self._get_terminal_columns() - (len(completion_string) + 6)
        bar_loaded_size: int = int(bar_size * (self.completion / 100))
        bar_blank_fill: int = bar_size - bar_loaded_size
        self._print_internal(f"\r{self.completion} % [{bar_loaded_size * self.bar_load_fill}{bar_blank_fill * self.bar_blank_fill}] ")

    # overwrite the loading bar with optional text
    def _overwrite_bar(self, text: str=""):
        overwrite: str = (" " * (self._get_terminal_columns() - len(text)))
        self._print_internal(f"\r{text}{overwrite}")

    # increase or decrease the completed percentage and call _update_bar()
    def update(self, percentage: int):
        self.completion = percentage
        self._update_bar()

    # same as update(), but with a smoother but slower animation
    # cannot decrease the completed percentage with this function
    def update_smooth(self, percentage: int):
        distance: int = percentage - self.completion
        for i in range(distance):
            self.completion += 1
            self._update_bar()
            time.sleep(0.005)

    # log text to the console without affecting the bar
    def log(self, text: str):
        self._overwrite_bar(f"{text}")
        print()
        self._update_bar()

    # clear the bar completely from the console
    def clear(self):
        self._overwrite_bar()
