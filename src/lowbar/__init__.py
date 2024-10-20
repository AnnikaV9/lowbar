"""
The simplest no-nonsense progress bar for python.
"""

import shutil


class lowbar:
    """
    The main lowbar class.
    """
    def __init__(self, bar_iter: range | int = 0, desc: str = "",
                 load_fill: str = "#", blank_fill: str = "-",
                 remove_ends: bool = False, keep_receipt: bool = False) -> None:
        """
        Checks and initializes the bar with the given
        parameters.
        """
        if not isinstance(load_fill, str) or len(load_fill) != 1:
            raise TypeError("arg load_fill should be a single char str")

        if not isinstance(blank_fill, str) or len(blank_fill) != 1:
            raise TypeError("arg blank_fill should be a single char str")

        if not isinstance(desc, str):
            raise TypeError("arg desc should be type str")

        if not isinstance(remove_ends, bool):
            raise TypeError("arg remove_ends should be type bool")

        if not isinstance(keep_receipt, bool):
            raise TypeError("arg keep_receipt should be type bool")

        if not isinstance(bar_iter, range):
            if not isinstance(bar_iter, int):
                raise TypeError("arg bar_iter should be either type range or int")

            bar_iter = range(bar_iter)

        self.bar_iter = bar_iter
        self.completion = 1
        self.load_fill = load_fill
        self.blank_fill = blank_fill
        self.desc = desc
        self.bar_ends = ("[", "]") if not remove_ends else (" ", " ")
        self.keep_receipt = keep_receipt

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
        print() if self.keep_receipt else self.clear()

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
            print() if self.keep_receipt else self.clear()

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
        desc = self.desc if len(self.desc) + 20 < self._get_columns() else ""
        label = f"{desc}  {str(self.completion)}" if self.completion < 10 else f"{desc} {str(self.completion)}"
        size = self._get_columns() - (len(label) + 7)
        load_size = int(size * (self.completion / 100))
        bar_blank_fill = size - load_size
        self._print(f"\r{label} % {self.bar_ends[0]}{load_size * self.load_fill}{bar_blank_fill * self.blank_fill}{self.bar_ends[1]} ")

    def _overwrite_bar(self, text: str = "") -> None:
        """
        Overwrite the loading bar with optional text.
        """
        overwrite = " " * (self._get_columns() - len(text))
        self._print(f"\r{text}{overwrite}")

    def update(self, percentage: int) -> None:
        """
        Sets the current completion percentage.
        """
        if not isinstance(percentage, int):
            raise TypeError("arg percentage should be type int")

        if percentage < 0 or percentage > 100:
            raise ValueError("arg percentage out of range (0-100)")

        self.completion = percentage
        self._update_bar()

    def add(self, percentage: int) -> None:
        """
        Adds to the current completion percentage.
        """
        if not isinstance(percentage, int):
            raise TypeError("arg percentage should be type int")

        self.completion += percentage
        self.completion = 100 if self.completion > 100 else self.completion
        self.completion = 0 if self.completion < 0 else self.completion
        self._update_bar()

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
