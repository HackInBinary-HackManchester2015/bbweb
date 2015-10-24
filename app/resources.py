from flask import jsonify
from . import models, schemas
from flask.ext.restful import Resource


class MonsterResource(Resource):
    """
    Monster Resource
    """
    monster_schema = schemas.MonsterSchema()

    def get(self, id):
        monster = models.Monster.query.get(id)
        if monster:
            result = self.monster_schema.dump(monster)
            return jsonify(result.data)
        else:
            return jsonify(result='Not found')
