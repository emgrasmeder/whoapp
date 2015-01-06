'''
    script_downloader.py makes quick use of Python's webscraping abilities
    to downlaod all the Doctor Who scripts to my local computer.

    Script source: http://www.chakoteya.net/doctorwho/index.htm
    Initially, I am agnostic to the accuracy and completeness of these
    scripts. I consider deviations from the official script to be normally
    distributed and therefore won't interfere with the integrity of this
    vital, vital research.

    The script is written in python2.7, until I know that all the dependencies
    will work with python3
'''


import urllib3
import time

url = 'http://www.chakoteya.net/doctorwho/34-1.html'

http = urllib3.PoolManager()
testr = http.request('GET', 'http://www.chakoteya.net/doctorwho/34-1.html')
print("accomplished step 1")



#response = urllib3.request.urlopen(url)
#raw = response.read().decode('utf8')
#print("raw = %s" % raw[:75])
