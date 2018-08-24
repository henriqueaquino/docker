#!/usr/bin/python

print("Content-type: text/html \n")

import subprocess

subprocess.call(['/home/service/set_stats.sh'])

file = open("/home/service/service_stats.log", "r")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<title>Container</title>")
print("</head>")
print("<body style='margin: 5%; font-size: 2em'>")
print("<div>--- Container ---</div> <br />")
print("<div style='font-size: 2em'>")
print(file.read())
print("</div>")
print("</body>")
print("</html>")

