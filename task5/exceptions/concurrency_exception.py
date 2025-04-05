class ConcurrencyException(Exception):
    def __init__(self, message="Concurrent update conflict occurred."):
        super().__init__(message)
