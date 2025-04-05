class IncompleteOrderException(Exception):
    def __init__(self, message="Order detail is incomplete."):
        super().__init__(message)
