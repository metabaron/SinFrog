import urllib2

version = "0.02"
url = ('http://metabaron.dyndns.org/SinFrog/version.php')
f = urllib2.urlopen(url)
data = f.read() # read all data in a single, blocking operation
if data != version:
	print "New version available"
else:
	print "Latest version"