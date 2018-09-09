#!/usr/bin/env python

print "Content-type: text/html \n"

import subprocess
subprocess.call(['/home/service/set-stats'])

file = open("/var/log/service/stats.log", "r")
delimiter = ';;;'

print """
<!DOCTYPE html>
<html>
<head>
	<title>Container</title>
	<style>
		body{
			margin-left: 5%;
			margin-right: 5%;
			font-size: large;
			font-weight: bold;
			text-align: center;
		}
		td{
			padding: 1%;
		}
		header{
			padding: 3%;
			background-color: #aa0000;
		}
	</style>

</head>
<body>
	<header>
	</header>
	<h3> CONTAINER - INFO </h3>
	<table>
"""

for line in file:
	print "<tr>"
	if delimiter in line:
		print "<td><br></td>"
		continue
	result = line.split()
	for i in result:
		print "<td>", i, "</td>"
	print "</tr>"

print """
	</table>"
</body>"
</html>
"""

file.close()
