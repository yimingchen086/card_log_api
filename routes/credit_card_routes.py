from flask_smorest import Blueprint, abort
from exts import db
from models.credit_card_db import CreditCard
from models.schemas import CreditCardSchema
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# 確保 url_prefix 正確設定在 Blueprint
credit_card_bp = Blueprint("credit_card", __name__, url_prefix="/api/credit_card", description="卡片相關 API")


@credit_card_bp.route("", methods=["POST"])
@credit_card_bp.arguments(CreditCardSchema)
@credit_card_bp.response(201, CreditCardSchema)
def create_card(card_data):
    """新增信用卡"""
    try:
        new_card = CreditCard(**card_data)
        db.session.add(new_card)
        db.session.commit()
        return new_card
    except IntegrityError:
        db.session.rollback()
        abort(400, message="資料庫完整性錯誤，請確認輸入資料是否唯一")
    except Exception as e:
        abort(500, message=f"內部伺服器錯誤: {str(e)}")


@credit_card_bp.route("/<int:card_id>", methods=["GET"])
@credit_card_bp.response(200, CreditCardSchema)
def get_card(card_id):
    """取得特定信用卡資訊"""
    card = CreditCard.query.get(card_id)
    if not card:
        abort(404, message="找不到該信用卡")
    return card


@credit_card_bp.route("/<int:card_id>", methods=["PUT"])
@credit_card_bp.arguments(CreditCardSchema)
@credit_card_bp.response(200, CreditCardSchema)
def update_card(card_data, card_id):
    """更新特定信用卡資訊"""
    card = CreditCard.query.get(card_id)
    if not card:
        abort(404, message=f"找不到ID {card_id}信用卡")
    try:
        for key, value in card_data.items():
            setattr(card, key, value)
        db.session.commit()
        return card
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, message="無法更新信用卡資料")


@credit_card_bp.route("/<int:card_id>", methods=["DELETE"])
@credit_card_bp.response(204)
def delete_card(card_id):
    """刪除特定信用卡"""
    card = CreditCard.query.get(card_id)
    if not card:
        abort(404, message="找不到該信用卡")
    try:
        db.session.delete(card)
        db.session.commit()
        return "", 204
    except SQLAlchemyError:
        db.session.rollback()
        abort(500, message="無法刪除信用卡資料")


@credit_card_bp.route("", methods=["GET"])
@credit_card_bp.response(200, CreditCardSchema(many=True))
def get_cards():
    """取得所有信用卡列表"""
    try:
        cards = CreditCard.query.all()
        return cards
    except SQLAlchemyError:
        abort(500, message="無法取得信用卡資料")