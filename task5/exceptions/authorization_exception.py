class AuthorizationException(Exception):
    def __init__(self, message="User does not have permission."):
        super().__init__(message)
