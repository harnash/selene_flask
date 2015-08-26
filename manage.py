# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import current_app
from flask.ext.script import Manager, prompt_choices, Server
from flask.ext.script.commands import ShowUrls, Clean
import nose
import pprint


from main import app
from config import CONFIG


def create_app(debug, config=None):
    app.debug = False
    print("CONFIG", config)

    if config is not None:
        app.config.from_pyfile(config)
    else:
        app.config.from_object(CONFIG)

    app.debug = debug

    return app

manager = Manager(create_app)

@manager.command
def test():
    """Run tests"""
    nose.run(argv=["-w ."])



@manager.command
def dumpconfig():
    """Dumps config"""
    pprint.pprint(current_app.config)

manager.add_option("-c", "--config",
                   dest="config",
                   help="config file",
                   required=False)
manager.add_option("-d", "--debug",
                   dest="debug",
                   help="run in debug mode",
                   default=False)

manager.add_command("runservernoreload", Server(use_reloader=False))
manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())

if __name__ == "__main__":
    manager.run()
