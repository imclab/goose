# -*- coding: utf-8 -*-

from handlers import base

url_patterns = [
    (r"/gallery", base.GalleryHandler),
    (r"/login", base.LoginHandler),
    (r"/submit", base.SubmitHandler),
    (r"/pic/(\w+)", base.PicHandler),
    (r"/upload", base.UploadHandler),
    (r"/comment/(\w+)", base.CommentHandler),
]