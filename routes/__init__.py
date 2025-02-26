from .category_routes import category_bp
from .credit_card_routes import credit_card_bp
from .transaction_routes import transaction_bp
from flask_smorest import Api


def register_blueprints(api: Api):
    """
    統一註冊所有的 Blueprint
    """
    api.register_blueprint(credit_card_bp)
    api.register_blueprint(transaction_bp)
    api.register_blueprint(category_bp)
