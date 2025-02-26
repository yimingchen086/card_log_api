from .credit_card_schema import CreditCardSchema
from .transaction_create_schema import TransactionCreateSchema
from .transaction_schema import TransactionSchema
from .transaction_update_schema import TransactionUpdateSchema
from .transaction_method_schema import TransactionMethodSchema
from .category_schema import CategorySchema

SCHEMA_CATEGORIES = {
    "credit_card": ["CreditCardSchema"],
    "transaction": ["TransactionCreateSchema", "TransactionSchema", "TransactionUpdateSchema"],
    "category": ["CategorySchema"]
}

__all__ = [
    *SCHEMA_CATEGORIES["credit_card"],
    *SCHEMA_CATEGORIES["transaction"],
    *SCHEMA_CATEGORIES["category"]
]
