# -*- coding: utf-8 -*-

import os.path

from tornado.options import define


define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

settings = {}

settings["debug"] = True
settings["cookie_secret"] = "askdfjpo83q47r9haskldfjh8"
settings["login_url"] = "/login"
settings["static_path"] = os.path.join(os.path.dirname(__file__), "static")
settings["template_path"] = os.path.join(os.path.dirname(__file__), "templates")
settings["xsrf_cookies"] = False

settings['aws_access_key_id'] = 'AKIAJVUP27XRFLHEL3BA'
settings['aws_secret_access_key'] = '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'