
class ChatficValidationError(Exception):
    """
    Exception raised for validation errors in the chatfic format.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
