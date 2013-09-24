# -*- coding: utf-8 -*-

from handlers import base

url_patterns = [
    (r"/", base.MainHandler),
    (r"/login", base.LoginHandler),
    (r"/submit", base.SubmitHandler),
    (r"/pic/(\w+)", base.PicHandler),
    (r"/gallery", base.GalleryHandler),
]