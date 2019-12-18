import requests
import argparse
import xml.etree.ElementTree
import re
import urllib
from os.path import isfile
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="The album's URL.")
    args = parser.parse_args()
    r = requests.get(args.url)
    urls = re.findall('https://www.nhaccuatui.com/flash/xml([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', r.content.decode('utf-8'))
    xmlfile = requests.get('https://www.nhaccuatui.com/flash/xml' + urls[0])
    e = xml.etree.ElementTree.fromstring(xmlfile.content.decode('utf-8'))
    for track in e.findall('track'):
        title = ''
        url = ''
        singer = ''
        for i in track:
            if i.tag == 'title':
                title = i.text.strip()
            elif i.tag == 'location':
                url = i.text.strip()
            elif i.tag == 'creator':
                signer = i.text.strip()
        print("Downloading file: "  title)
        mp3file = "./" + title + " - "+ signer +".mp3"
        if isfile(mp3file):
            print("File exists")	
            continue
        else:
            try:
                urllib.request.urlretrieve(url, mp3file )
            except (Exception) as e:
                print("Error. Download next file")
                continue



