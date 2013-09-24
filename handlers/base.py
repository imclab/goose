# -*- coding: utf-8 -*-

import tornado.web
import boto
import boto.s3
from boto.s3.key import Key
from PIL import Image
from settings import settings
import StringIO
import os

from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.goosepics

AWS_ACCESS_KEY_ID = settings['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = settings['aws_secret_access_key']

bucket_name = AWS_ACCESS_KEY_ID.lower() + 'goosepics'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
			AWS_SECRET_ACCESS_KEY)


class BaseHandler(tornado.web.RequestHandler): 
	def get_current_user(self):
		return self.get_secure_cookie("username")


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.get_secure_cookie('username')
        self.render('index.html')


class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('login.html')

	def post(self):
		password = self.get_argument('password')

		if password == 'pizzatime':
			self.set_secure_cookie('username', 'friend');
			self.redirect('/')


class SubmitHandler(tornado.web.RequestHandler):
	def post(self):
		story = self.get_argument('story')
		file_name = self.request.files['picture'][0]['filename']
		file_body = self.request.files['picture'][0]['body']
		file_path = os.path.realpath(str("./static/img/" + file_name))
		img = Image.open(StringIO.StringIO(file_body))
		img.save(file_path, img.format)
		bucket = conn.get_bucket('goosepics')
		key = Key(bucket)
		key.set_contents_from_filename(file_path)

		id = db.pics.insert({
			'file_name': file_name,
			'url': 'https://s3.amazonaws.com/goosepics/' + key.key,
			'story': story,
			'comments': []
			})

		os.remove(file_path)
		self.redirect('/pic/'+str(id))

class PicHandler(tornado.web.RequestHandler):
	def get(self, input):
		doc = db.pics.find_one({'_id': ObjectId(input)})
		url = doc['url']
		story = doc['story']
		comments = doc['comments']
		self.render('pic.html', url=url, 
			story=story, comments=comments)


class GalleryHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		pics = db.pics.find()
		pics = pics[:]
		self.render('gallery.html', pics=pics)

