import urllib2
import webbrowser
import xml.etree.ElementTree as ET
import sys

print "--------------------------------------------------"
print "Welcome to the Random Wikipedia Article Generator."
print "--------------------------------------------------"
print "Press 'n' for the next article."
print "Press 'y' to open the current article."
print "Press 'x' to quit the program."
print "--------------------------------------------------"

while True:
	request = urllib2.urlopen('https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=500&format=xml')
	tree = ET.parse(request)
	root = tree.getroot()
	for child in root[1][0]:
		id_val = child.attrib.get('id')
		title = child.attrib.get('title').encode('ascii', 'ignore')
		prompt_string = "Would you like to read about: " + title + "? "
		user_input = raw_input(prompt_string)
		while True:
			if (user_input == 'n'):
				break
			elif (user_input == 'x'):
				sys.exit()
			elif (user_input == 'y'):
				print "Now opening: " + title
				url = "http://en.wikipedia.org/wiki?curid=" + id_val
				webbrowser.open(url)
				user_input = raw_input("Press 'n' for next article, press 'x' to quit. ")
			else:
				user_input = raw_input("Invalid entry. Try again. ")
