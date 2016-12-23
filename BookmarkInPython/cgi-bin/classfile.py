import psycopg2
import cgi,os,sys
from Database import *
from urllib3 import request


class dbQuery(Database):
	"""docstring for testQ"""
	def __init__(self):
		Database.__init__(self)
	
	def insert(self, link, title, button):
		self.title = title
		self.link = link
		self.button = button

	def delete(self, link, button):
		self.link = link
		self.button = button

	def show(self):
		self.button = None
		
	# def __str__():
	
	def Query(self):
		self.connection()
		if self.button == "Add":
			# return "akash"
			if self.checkQueryDuplication(self.link):
				return '<script>alert("Link Already Exist")</script>'

			elif self.checkTitleDuplication(self.title):
				return '<script>alert("Change Title")</script>'		 
			
			else:
				return self.executeAddQurey("insert into bookmark(link,title) values('%s','%s')"%(self.link,self.title))
		elif self.button == "Delete":
			return self.deleteExecuteQuery("delete from bookmark where link = '%s'"%self.link)
		else:
			return self.executeShowQuery("select * from bookmark")
			