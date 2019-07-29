"""                                                                              
usage:                                                                           
    python multi_wc2.py \                                                         
    http://xroads.virginia.edu/~drbr/gettysbu.html \                             
    http://history.eserver.org/gettysburg-address.txt                            
"""
import sys
import urllib.request
import subprocess
import re
import threading

if len(sys.argv) < 2: sys.exit("error: no url")

pat = re.compile(r'\d+')
sum = 0
s1 = s2 = ""

class wc_th(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.setDaemon(True)

    def run(self):
        global sum, s1, s2
        f = urllib.request.urlopen(self.url)
        s = f.read()
        f.close()
        p = subprocess.Popen(['wc', '-w'],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)
        out, err = p.communicate(s)
        ret = pat.search(str(out))
        nstr = ret.group()
        nint = int(nstr)
        sum += nint
        s1 += nstr + " + "
        s2 += "%7d %s\n" % (nint, self.url.split("/")[-1])

tl = []
for url in sys.argv[1:]:
    wc = wc_th(url)
    wc.start()
    tl.append(wc)

for t in tl:
    t.join()

print("Total:", s1[:-3])
print(s2, end='')