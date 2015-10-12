#!/usr/bin/env python

gradeFile = open('./grades.txt')

#print "Content-type: text/html"
print
print "<h1>Grades</h1>"

for line in gradeFile:
	if line[0] == '#':
		print "<p>"
		print "<h2>" + line + "</h2>"
		print "</p>"
	else:
		if len(line) > 1:
			#print str(len(line)) + "---------" + line
			#print "<p>"
			entry = line.split(' ', 1)
			name = entry[0]
			grade = entry[1].split()
			print name + " " + grade[0] + "<br>"
			#print "</p>"
