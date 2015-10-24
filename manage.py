#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import create_app, db, models
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    """
    Make the shell context
    """
    return dict(app=app, db=db)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', Server(host='0.0.0.0'))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
