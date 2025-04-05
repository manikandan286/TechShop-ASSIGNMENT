from exceptions.invalid_data_exception import InvalidDataException

class Customer:
    def __init__(self, email):
        self._email = None
        self.Email = email

    @property
    def Email(self):
        return self._email

    @Email.setter
    def Email(self, value):
        if "@" not in value:
            raise InvalidDataException("Email must contain '@'.")
        self._email = value
