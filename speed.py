import time, urllib2, threading

class SpeedClass(threading.Thread):
    def report(start, size, text, displayTarget):
        total = time.time() - start
        displayTarget.DisplayCtrl.AppendText("\n" + "%s reading took %d seconds, transfer rate %.2f KBPS" % (text, total, (size / 1024.0) / total))
        #print "%s reading took %d seconds, transfer rate %.2f KBPS" % (text, total, (size / 1024.0) / total)

    def __init__(self, url, displayTarget = None):
        self.url = url
        self.displayTarget = displayTarget
        threading.Thread.__init__(self)
        
    def run(self):
        f = urllib2.urlopen(self.url)
        start = time.time()
        
        data = ''
        text = 'Chunked'
        while True:
            chunk = f.read(4096) # read a chunk
            if not chunk:
                break
            data = data + chunk
        f.close()
        total = time.time() - start
        self.displayTarget.DisplayCtrl.AppendText("\n" + "%s reading took %d seconds, transfer rate %.2f KBPS" % (text, total, (len(data) / 1024.0) / total))
        
        g = urllib2.urlopen(self.url)
        start = time.time()
        text = 'All data'
        data = g.read() # read all data in a single, blocking operation
        g.close()
            
        total = time.time() - start
        self.displayTarget.DisplayCtrl.AppendText("\n" + "%s reading took %d seconds, transfer rate %.2f KBPS" % (text, total, (len(data) / 1024.0) / total))