#!/usr/bin/env python

print "Content-type: text/html \n"

import subprocess
subprocess.call(['/home/service/set-stats'])

file = open("/var/log/service/stats.log", "r")
delimiter = ';;;'
resource = '@@@'

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
		table{
			border-collapse: collapse;
			width: 100%;
			text-align: center;
		}
		td{
			padding: 1%;
#			border-width: 1px;
#			border-style: solid;
#			border-color: #000000;
		}
		.resource{
			color: #ff0000;
			border: none;
		}
	</style>

</head>
<body>
	<h3> CONTAINER - INFO </h3>
	<table>
"""

for line in file:
	print "<tr>"

	if resource in line:
		name = line.split()
		print "<td class='resource'>", name[1], "</td>"
		continue
	elif delimiter in line:
		continue
	else:
		result = line.split()
		for i in result:
			print "<td>", i, "</td>"

	print "</tr>"

print """
	</table>
</body>
</html>
"""

file.close()
