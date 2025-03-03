# To manage exceptions in the program
import sys


def error_message_details(error, error_detail: sys):
    """Returns detailed error message including file name, line number, and error message."""
    _, _, exc_tb = error_detail.exc_info()  # This will return three values

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):  # Fixed spelling of "CustomException"
    """Custom exception class to format error messages properly."""

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)

    def __str__(self):
        return self.error_message

