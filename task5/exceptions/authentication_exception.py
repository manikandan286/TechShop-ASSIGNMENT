class AuthenticationException(Exception):
    def __init__(self, message="User is not authenticated."):
        super().__init__(message)
