from marshmallow import Schema, fields, validate

class CreditCardSchema(Schema):
    # 欄位定義
    card_id = fields.Int(dump_only=True)  # 僅用於輸出
    card_name = fields.Str(required=True, validate=validate.Length(min=1, max=50))  # 卡片名稱，必填，長度限制
    bank = fields.Str(required=True, validate=validate.Length(min=1, max=50))  # 發卡銀行，必填，長度限制
    maxconsume = fields.Int(allow_none=True)  # 最大消費額度，可選
    curramount = fields.Int(allow_none=True)  # 目前消費金額，可選
    description = fields.Str(allow_none=True)  # 描述，可選
    store = fields.Str(allow_none=True)  # 適用商店，可選
    rewardstype = fields.Str(allow_none=True, validate=validate.Length(max=50))  # 獎勵類型，可選，長度限制
    daterange_start = fields.Date(allow_none=True)  # 優惠開始日期，可選
    daterange_end = fields.Date(allow_none=True)  # 優惠結束日期，可選
    postingdate = fields.Str(allow_none=True, validate=validate.Length(max=10))  # 發布日期，可選，長度限制

    class Meta:
        model_name = "CreditCardSchema"  # 設定唯一名稱
        fields = (
            'card_id',
            'card_name',
            'bank',
            'maxconsume',
            'curramount',
            'description',
            'store',
            'rewardstype',
            'daterange_start',
            'daterange_end',
            'postingdate'
        )
        ordered = True  # 保持欄位順序