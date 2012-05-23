import time, threading, urllib2, json, os, fileinput
from datetime import datetime, timedelta

class SpeedClass(threading.Thread):
    def report(start, size, text, displayTarget):
        total = time.time() - start
        displayTarget.DisplayCtrl.AppendText("\n" + "%s reading took %d seconds, transfer rate %.2f KBPS" % (text, total, (size / 1024.0) / total))

    def __init__(self, displayTarget = None,  user = None):
        self.user = user
        self.displayTarget = displayTarget
        threading.Thread.__init__(self)
        
    def run(self):
        #http://www.thinkbroadband.com/download.html
        #http://www.speedtest.com.sg/speedtest.php
        self.displayTarget.DisplayFrame_statusbar.SetStatusText("Download speed: Start")
        
        if(os.path.exists(r'speedList.txt')):
            statinfo = os.stat('speedList.txt')
        else:
            u = urllib2.urlopen('http://sinfrog.metabaron.net/speedList.php')
            localFile = open('speedList.txt', 'w')
            localFile.write(u.read())
            localFile.close()
            statinfo = os.stat('speedList.txt')
        if (datetime.fromtimestamp(time.time()) - datetime.fromtimestamp(statinfo.st_mtime)) > timedelta (days = 7):
            #Retrieve list of servers to test download speed from
            u = urllib2.urlopen('http://sinfrog.metabaron.net/speedList.php')
            localFile = open('speedList.txt', 'w')
            localFile.write(u.read())
            localFile.close()
        #loading file line by line and not at once in memory
        for line in fileinput.input(['speedList.txt']):
        #urlList = ["http://ipv4.download.thinkbroadband.com/5MB.zip", "http://www.speedtest.com.sg/test_random_10mb.zip"]
            self.test(line.strip(' \t\n\r'))
        self.displayTarget.DisplayFrame_statusbar.SetStatusText("Download speed: Done")
    
    def test(self, url):
        self.url = url
        f = urllib2.urlopen(self.url)
        print("ok")
        start = time.time()
        print("ok")
        
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
        
        url = ('http://sinfrog.metabaron.net/rate.php')
        data = json.dumps({"userID": self.user, "target": self.url, "type": text, "rate": (len(data) / 1024.0) / total})
        clen = len(data)
        req = urllib2.Request(url, data, {'Content-Type': 'application/json', 'Content-Length': clen})
        f = urllib2.urlopen(req)
        f.close()