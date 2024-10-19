"""
The simplest no-nonsense progress bar for python.
"""

import shutil


class lowbar:
    """
    The main lowbar class.
    """
    def __init__(self, bar_iter: range | int = 0, bar_load_fill: str = "#",
                 bar_blank_fill: str = "-", bar_desc: str = "",
                 remove_ends: bool = False, no_clear: bool = False,
                 smooth_iter = False  # backwards compatibility (no effect)
                 ) -> None:
        """
        Checks and initializes the bar with the given
        parameters.
        """
        if not isinstance(bar_load_fill, str):
            raise TypeError("arg bar_load_fill should be type str")

        if not isinstance(bar_blank_fill, str):
            raise TypeError("arg bar_blank_fill should be type str")

        if not isinstance(bar_desc, str):
            raise TypeError("arg bar_desc should be type str")

        if not isinstance(remove_ends, bool):
            raise TypeError("arg remove_ends should be type bool")

        if not isinstance(no_clear, bool):
            raise TypeError("arg no_clear should be type bool")

        if not isinstance(bar_iter, range):
            if not isinstance(bar_iter, int):
                raise TypeError("arg bar_iter should be either type range or int")

            bar_iter = range(bar_iter)

        if len(bar_load_fill) != 1:
            raise TypeError("arg bar_load_fill should be a single char")

        if len(bar_blank_fill) != 1:
            raise TypeError("arg bar_blank_fill should be a single char")

        self.bar_iter = bar_iter
        self.completion = 1
        self.bar_load_fill = bar_load_fill
        self.bar_blank_fill = bar_blank_fill
        self.bar_desc = bar_desc
        self.bar_ends = ("[", "]") if not remove_ends else (" ", " ")
        self.no_clear = no_clear

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
        print() if not self.no_clear else self.clear()

    def __iter__(self) -> object:
        """
        Iterable manager that automatically runs new() at the
        start and clear() at the end
        """
        self.new()
        div = 100 / len(self.bar_iter)
        add = div
        try:
            for item in self.bar_iter:
                yield item
                self.update(int(div))
                div += add

        finally:
            self.clear() if not self.no_clear else print()

    def _print(self, text: str) -> None:
        """
        Writes data to stdout
        """
        print(text, end='', flush=True)

    def _get_columns(self) -> int:
        """
        Returns the number of columns in the running console.
        """
        return shutil.get_terminal_size().columns

    def _update_bar(self) -> None:
        """
        Refreshes the current bar with new values, and a
        possibly resized console.
        """
        temp_desc = self.bar_desc if len(self.bar_desc) + 20 < self._get_columns() else ""
        completion_string = f"{temp_desc}  {str(self.completion)}" if self.completion < 10 else f"{temp_desc} {str(self.completion)}"
        bar_size = self._get_columns() - (len(completion_string) + 7)
        bar_loaded_size = int(bar_size * (self.completion / 100))
        bar_blank_fill = bar_size - bar_loaded_size
        self._print(f"\r{completion_string} % {self.bar_ends[0]}{bar_loaded_size * self.bar_load_fill}{bar_blank_fill * self.bar_blank_fill}{self.bar_ends[1]} ")

    def _overwrite_bar(self, text: str = "") -> None:
        """
        Overwrite the loading bar with optional text.
        """
        overwrite = " " * (self._get_columns() - len(text))
        self._print(f"\r{text}{overwrite}")

    def update(self, percentage: int) -> None:
        """
        Increases or decreases the completed percentage and
        calls _update_bar().
        """
        if not isinstance(percentage, int):
            raise TypeError("arg percentage should be type int")

        self.completion = percentage
        self._update_bar()

    update_smooth = update  # backwards compatibility

    def new(self) -> None:
        """
        Alias for update(0)
        """
        self.update(0)

    def log(self, text: str) -> None:
        """
        Log text to the console without affecting the bar.
        """
        if not isinstance(text, str):
            raise TypeError("arg text should be type str")

        self._overwrite_bar(text)
        print()
        self._update_bar()

    def clear(self) -> None:
        """
        Clears the bar completely from the console.
        """
        self._overwrite_bar()


# backwards compatibility
LowBar = lowbar
