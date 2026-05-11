"""
Demonstration of Python custom exceptions.

Custom exceptions allow for more specific error handling by creating
exception classes that inherit from built-in exception types.
"""


class ValidationError(ValueError):
    """Base validation error for application-specific validation failures."""
    pass


class AgeValidationError(ValidationError):
    """Error raised when age validation fails."""

    def __init__(self, age: int, message: str = None) -> None:
        self.age = age
        self.message = message or f"Invalid age: {age}"
        super().__init__(self.message)


class EmailValidationError(ValidationError):
    """Error raised when email validation fails."""

    def __init__(self, email: str) -> None:
        self.email = email
        self.message = f"Invalid email format: {email}"
        super().__init__(self.message)


class ResourceNotFoundError(Exception):
    """Error raised when a requested resource is not found."""

    def __init__(self, resource_type: str, resource_id: str) -> None:
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.message = f"{resource_type} with id '{resource_id}' not found"
        super().__init__(self.message)


def validate_age(age: int) -> None:
    """Validate that age is within acceptable range."""
    if age < 0:
        raise AgeValidationError(age, "Age cannot be negative")
    if age > 150:
        raise AgeValidationError(age, "Age cannot exceed 150")


def validate_email(email: str) -> None:
    """Validate basic email format."""
    if '@' not in email or '.' not in email:
        raise EmailValidationError(email)


def get_user(user_id: str) -> dict:
    """Get user by ID, raises if not found."""
    users = {'1': {'name': 'Alice'}, '2': {'name': 'Bob'}}
    if user_id not in users:
        raise ResourceNotFoundError("User", user_id)
    return users[user_id]


def main() -> None:
    # Custom exception inherits from built-in
    assert issubclass(ValidationError, ValueError)
    assert issubclass(AgeValidationError, ValidationError)
    assert issubclass(EmailValidationError, ValidationError)
    assert issubclass(ResourceNotFoundError, Exception)

    # Catching specific exception
    try:
        validate_age(-5)
        assert False, "Should have raised"
    except AgeValidationError as e:
        assert e.age == -5
        assert "negative" in e.message

    # Catching parent exception
    try:
        validate_email("invalid-email")
        assert False, "Should have raised"
    except ValidationError as e:
        assert "invalid-email" in str(e)

    # Resource not found
    try:
        get_user("999")
        assert False, "Should have raised"
    except ResourceNotFoundError as e:
        assert e.resource_type == "User"
        assert e.resource_id == "999"
        assert "not found" in e.message

    # Successful validation doesn't raise
    validate_age(25)  # No exception
    validate_email("test@example.com")  # No exception

    # Successful resource access
    user = get_user("1")
    assert user['name'] == 'Alice'

    # Exception chaining with 'from'
    try:
        try:
            validate_age(200)
        except AgeValidationError as original:
            raise RuntimeError("User creation failed") from original
    except RuntimeError as e:
        assert e.__cause__ is not None
        assert isinstance(e.__cause__, AgeValidationError)

    # Exception string representation
    error = AgeValidationError(999, "Way too old")
    assert str(error) == "Way too old"


if __name__ == "__main__":
    main()
