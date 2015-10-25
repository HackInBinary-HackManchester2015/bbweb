import random
from flask import jsonify
from . import models, schemas
from flask.ext.restful import Resource, reqparse


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


class MonsterListResource(Resource):

    monster_list_schema = schemas.MonsterSchema(many=True)

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('userlevel')

    def get(self):
        args = self.parser.parse_args()
        if args['userlevel']:
            userlevel = args['userlevel']

            monsters = models.Monster.query.filter(
                    models.Monster.level >= int(userlevel) - 1,
                    models.Monster.level <= int(userlevel) + 1
                    ).all()

            if monsters:
                selected = random.choice(monsters)
                result = MonsterResource.monster_schema.dump(selected)
                return jsonify(result.data)
            else:
                return jsonify(result='not yet implemented')
        else:
            number_of_monsters = models.Monster.query.count()
            return jsonify(numMonsters=number_of_monsters)
