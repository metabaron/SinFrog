import time, threading, urllib2, json

class SpeedClass(threading.Thread):
    def report(start, size, text, displayTarget):
        total = time.time() - start
        displayTarget.DisplayCtrl.AppendText("\n" + "%s reading took %d seconds, transfer rate %.2f KBPS" % (text, total, (size / 1024.0) / total))
        #print "%s reading took %d seconds, transfer rate %.2f KBPS" % (text, total, (size / 1024.0) / total)

    def __init__(self, url, displayTarget = None,  user = None):
        self.url = url
        self.user = user
        self.displayTarget = displayTarget
        threading.Thread.__init__(self)
        
    def run(self):
        f = urllib2.urlopen(self.url)
        start = time.time()
        
        self.displayTarget.DisplayCtrl.AppendText("\n" + "Chuncked reading from " + self.url)
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
        
        url = ('http://sinfrog.metabaron.net/rate.php')
        data = json.dumps({"userID": self.user, "target": self.url, "type": text, "rate": (len(data) / 1024.0) / total})
        clen = len(data)
        req = urllib2.Request(url, data, {'Content-Type': 'application/json', 'Content-Length': clen})
        f = urllib2.urlopen(req)
        f.close()
        
        g = urllib2.urlopen(self.url)
        start = time.time()
        self.displayTarget.DisplayCtrl.AppendText("\n" + "Reading in one block from " + self.url)
        text = 'All data'
        data = g.read() # read all data in a single, blocking operation
        g.close()
            
        total = time.time() - start
        self.displayTarget.DisplayCtrl.AppendText("\n" + "%s reading took %d seconds, transfer rate %.2f KBPS" % (text, total, (len(data) / 1024.0) / total))
        self.displayTarget.DisplayCtrl.AppendText("\n" + "Done. Please close this window")
        
        url = ('http://sinfrog.metabaron.net/rate.php')
        data = json.dumps({"userID": self.user, "target": self.url, "type": text, "rate": (len(data) / 1024.0) / total})
        clen = len(data)
        req = urllib2.Request(url, data, {'Content-Type': 'application/json', 'Content-Length': clen})
        f = urllib2.urlopen(req)
        f.close()