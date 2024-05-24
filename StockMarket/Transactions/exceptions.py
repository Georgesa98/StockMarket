from django.core.exceptions import ValidationError


class InsufficientStockQuantityException(ValidationError):
    pass
