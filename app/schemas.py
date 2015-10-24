from marshmallow import Schema, fields


class MonsterSchema(Schema):
    """
    Schema for the Monster
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
    level = fields.Int()
    health = fields.Int()
    imgPath = fields.Str()
