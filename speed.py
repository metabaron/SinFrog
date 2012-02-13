import urllib2
import time

def report(start, size, text):
    total = time.time() - start
    print "%s reading took %d seconds, transfer rate %.2f KBPS" % (
            text, total, (size / 1024.0) / total)

start = time.time()
url = ('http://itc.conversationsnetwork.org/audio/download/ITC.SO-Episode69-2009.09.29.mp3')
f = urllib2.urlopen(url)
start = time.time()
data = f.read() # read all data in a single, blocking operation
report(start, len(data), 'All data')
f.close()

f = urllib2.urlopen(url)
start = time.time()
while True:
    chunk = f.read(4096) # read a chunk
    if not chunk:
        break
report(start, len(data), 'Chunked')
f.close()
