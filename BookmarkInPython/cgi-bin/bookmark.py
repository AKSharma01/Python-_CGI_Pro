#!/usr/bin/python
import cgi,os,sys
from classfile import *
from urllib3 import request



sys.stdout.write('Content-type: text/html\r\n\r\n')
sys.stdout.write("""<!DOCTYPE html>
								<html>
									<head>
										<title> Bookmark </title>
										<meta charset="utf-8">
										<meta name="viewport" content="width=device-width, initial-scale=1">
										<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
										<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
										<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
										<link rel="stylesheet" href="bootstrap/bootstrap.min.css">
										<script src="bootstrap/jquery.min.js"></script>
										<script src="bootstrap/bootstrap.min.js"></script>
									</head>
									<body>""")
test=dbQuery()
form = cgi.FieldStorage()
if os.environ['REQUEST_METHOD'] == 'POST':
	# print '<h1>hello2</h1>'
	link = form["link"].value
	# print '<h1>hello3</h1>'
	if form["submit"].value == "ADD":
		title = form["title"].value		
		button="Add"
		# print '<h1>hello4</h1>'
		test.insert(link, title, button)
		sys.stdout.write(test.Query())
	else:
		# print '<h1>hello5</h1>'
		button = "Delete"
 		test.delete(link, button)
		sys.stdout.write(test.Query())
# print '<h1>hello6</h1>'

sys.stdout.write(""" <h1>BookMark</h1>
									<div class="container" style="text-align: center">
										<form action="bookmark.py"  method="post" class="form-inline">
											<div class="form-group">
												<input type="text" name="link" class="form-control" required placeholder="http://www.example.com"/>	
											</div>
											<div class="form-group">
												<input type="text" name="title" class="form-control" required placeholder="example"/>	
											</div>
											<input type="submit" class="btn btn-default" name="submit" value="ADD"/>
										</form>
									</div>""")



test.show()
rows = test.Query()
if rows is None:
	sys.stdout.write('<script>alert("There is no Link saved")</script>')
else:
	print ("""<div class="container">
									<table class="table table-striped" style="width:100%">
										<thead>
											<tr><th>Serial No.</th>
											    <th>Web Link</th>
											    <th>Created At</th>
											    <th>Delete Option</th></tr>
										</thead>""")
	for row in rows:
		sys.stdout.write("""			<tbody>
											<form action="bookmark.py" method="post">
												<tr> 
													<input type="hidden" name="link" value="%s"/>
													<td> %d </td> 
													<td><a href="%s" return false;" target="_blank"> %s </a></td> 
													<td> %s </td> 
													<td><input type="submit" class="btn btn-default" name="submit" value="DELETE"/></td> 
												</tr>
											</form>
										</tbody>"""%(row[1],row[0],row[1],row[2],row[3]))
	sys.stdout.write('</table></div>')



sys.stdout.write('					</body>\
								</html>')
