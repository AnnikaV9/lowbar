"""
pytest test cases
"""

from pytest import raises
from unittest.mock import patch
from os import terminal_size
from io import StringIO

from lowbar import lowbar


@patch("shutil.get_terminal_size")
@patch("sys.stdout", new_callable=StringIO)
def test_update_add_log(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    bar = lowbar()
    bar.new()
    bar.update(20)
    bar.update(50)
    bar.log("Test log message")
    bar.add(50)
    bar.clear()
    output = mock_stdout.getvalue()
    assert "Test log message" in output
    assert "\r  0 % [-------------------------------------------] " in output
    assert "\r 20 % [########-----------------------------------] " in output
    assert "\r 50 % [#####################----------------------] " in output
    assert "\r 100 % [##########################################] " in output
    assert "\r                                                     " in output


@patch("shutil.get_terminal_size")
@patch("sys.stdout", new_callable=StringIO)
def test_add_over_100(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    bar = lowbar()
    bar.new()
    bar.add(150)
    assert "\r 100 % [##########################################] " in mock_stdout.getvalue()


@patch("shutil.get_terminal_size")
@patch("sys.stdout", new_callable=StringIO)
def test_add_under_0(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    bar = lowbar()
    bar.new()
    bar.add(-50)
    assert "\r  0 % [-------------------------------------------] " in mock_stdout.getvalue()


@patch("shutil.get_terminal_size")
@patch("sys.stdout", new_callable=StringIO)
def test_tasks_in_next(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    bar = lowbar()
    bar.new()
    bar.next(5)
    output = mock_stdout.getvalue()
    assert "\r  0 % [-------------------------------------------] " in output
    assert "\r 20 % [########-----------------------------------] " in output


@patch("shutil.get_terminal_size")
@patch("sys.stdout", new_callable=StringIO)
def test_tasks_in_constructor(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    bar = lowbar(5)
    bar.new()
    bar.next()
    output = mock_stdout.getvalue()
    assert "\r  0 % [-------------------------------------------] " in output
    assert "\r 20 % [########-----------------------------------] " in output


@patch("shutil.get_terminal_size")
@patch("sys.stdout", new_callable=StringIO)
def test_desc(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    bar = lowbar(desc="Downloading")
    bar.new()
    bar.update(100)
    output = mock_stdout.getvalue()
    assert "\rDownloading  0 % [--------------------------------] " in output
    assert "\rDownloading 100 % [###############################] " in output


@patch("shutil.get_terminal_size")
@patch("sys.stdout", new_callable=StringIO)
def test_desc_too_long(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    bar = lowbar(desc="A very long description that will not fit in the terminal")
    bar.new()
    bar.update(100)
    output = mock_stdout.getvalue()
    assert "\r  0 % [-------------------------------------------] " in output
    assert "\r 100 % [##########################################] " in output


@patch("shutil.get_terminal_size")
@patch('sys.stdout', new_callable=StringIO)
def test_iterable(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    for _ in lowbar(3, keep_receipt=True):
        pass

    output = mock_stdout.getvalue()
    assert "\r  0 % [-------------------------------------------] " in output
    assert "\r 33 % [##############-----------------------------] " in output
    assert "\r 66 % [############################---------------] " in output
    assert "\r 100 % [##########################################] \n" in output


@patch("shutil.get_terminal_size")
@patch('sys.stdout', new_callable=StringIO)
def test_iterable_no_receipt(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    for _ in lowbar(3):
        pass

    output = mock_stdout.getvalue()
    assert "\r  0 % [-------------------------------------------] " in output
    assert "\r 33 % [##############-----------------------------] " in output
    assert "\r 66 % [############################---------------] " in output
    assert "\r 100 % [##########################################] " in output
    assert "\r                                                     " in output


@patch("shutil.get_terminal_size")
@patch('sys.stdout', new_callable=StringIO)
def test_context_manager(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    with lowbar(keep_receipt=True) as bar:
        bar.update(100)

    output = mock_stdout.getvalue()
    assert "\r  0 % [-------------------------------------------] " in output
    assert "\r 100 % [##########################################] \n" in output


@patch("shutil.get_terminal_size")
@patch('sys.stdout', new_callable=StringIO)
def test_context_manager_no_receipt(mock_stdout, mock_terminal_size):
    mock_terminal_size.return_value = terminal_size((53, 20))
    with lowbar() as bar:
        bar.update(100)

    output = mock_stdout.getvalue()
    assert "\r  0 % [-------------------------------------------] " in output
    assert "\r 100 % [##########################################] " in output
    assert "\r                                                     " in output


def test_errors():
    with raises(TypeError):
        lowbar("invalid iterable type")

    with raises(TypeError):
        lowbar(load_fill="invalid load fill length")

    with raises(TypeError):
        lowbar(blank_fill="invalid blank fill length")

    with raises(TypeError):
        lowbar(desc=list("invalid desc type"))

    with raises(TypeError):
        lowbar(remove_ends="invalid remove ends type")

    with raises(TypeError):
        lowbar(keep_receipt="invalid keep receipt type")

    with raises(ValueError):
        bar = lowbar()
        bar.update(101)

    with raises(ValueError):
        bar = lowbar()
        bar.update(-1)

    with raises(TypeError):
        bar = lowbar()
        bar.log(1)
