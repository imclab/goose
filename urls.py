# -*- coding: utf-8 -*-

from handlers import base

url_patterns = [
    (r"/gallery", base.GalleryHandler),
    (r"/login", base.LoginHandler),
    (r"/logout", base.LogoutHandler),
    (r"/submit", base.SubmitHandler),
    (r"/pic/(\w+)", base.PicHandler),
    (r"/", base.MainHandler),
    (r"/comment/(\w+)", base.CommentHandler),
]