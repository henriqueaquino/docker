#!/usr/bin/python

print("Content-type: text/html \n")

import subprocess

subprocess.call(['/home/service/set-stats'])

file = open("/home/service/log/stats.log", "r")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<title>Container</title>")
print("</head>")
print("<body style='margin: 3%; font-size: xx-large; text-align: center;'>")
print("<h3> #---# Container #---# </h3>")
print("<div>")
print("<h4> --- Stats --- </h4> <br />")
print("<ul>")

for line in file:
	print("<li> ",line," </li>")	

print("</ul>")
print("</div>")
print("</body>")
print("</html>")

file.close()
