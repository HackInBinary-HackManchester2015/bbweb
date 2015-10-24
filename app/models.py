from . import db


class Monster(db.Model):
    """
    Monster class
    """

    __tablename__ = 'monsters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    imgPath = db.Column(db.String(60))

    def __repr__(self):
        return '<Monster {}>'.format(self.id)
