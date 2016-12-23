#!/usr/binn/python
import cgi, os, sys
import psycopg2

class Database:
	"""docstring for database"""
	def __init__(self):
		self.list={'database': 'akash',
		'user' : 'postgres',
		'password' : 'password',
		'host' : '127.0.0.1',
		'port' : '5432'}
		
	def connection(self):
		# conn = psycopg2.connect(self.list['database'],self.list['user'],password="password", host="127.0.0.1", port="5432")
		try:
			self.conn = psycopg2.connect(database="akash", user="postgres", password="password", host="127.0.0.1", port="5432")
			self.cursor = self.conn.cursor()
			# return '<script>alert("Connection !")</script>'
		except Exception as e:
			# return '<script>alert("Connection Error!")</script>'
			print "hello"


	def executeAddQurey(self,query):
		try:
			self.cursor.execute(query)
			self.conn.commit()
			return '<script>alert("Inserted")</script>'
		except Exception as e:
			return '<script>alert("%s!")</script>'%e
	
	def deleteExecuteQuery(self,query):
		try:
			self.cursor.execute(query)
			self.conn.commit()
			return '<script>alert("Deleteded")</script>'
		except Exception as e:
			return '<script>alert("%s!")</script>'%e		
		
	def checkQueryDuplication(self,link):
		self.cursor.execute("select * from bookmark where link = '%s'"%link)
		return self.cursor.fetchone()
	

	def checkTitleDuplication(self,title):
		self.cursor.execute("select * from bookmark where title = '%s'"%title)
		return self.cursor.fetchone()

	def executeShowQuery(self,query):
		self.cursor.execute(query)
		return self.cursor.fetchall()

