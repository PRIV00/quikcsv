

class Error(Exception):
    """Base Error"""
    pass


class UnevenColumnError(Error):

    def __init__(self, data, message="Mock data columns are uneven. Check the length of your lists, they need to match."):  # noqa
        self.data = data
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.data} -> {self.message}'
