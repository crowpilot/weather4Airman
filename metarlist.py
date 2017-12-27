import io
import os
import urllib2
import re
import datetime
import shutil
from HTMLParser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag=False
        self.metar=""
        self.lastdata=""
        self.codeCK=""
        self.code=""
        
    def handle_starttag(self, tag, attrs):
        if tag=='body':
            self.flag=True
        if tag=='a':
            self.flag=False
            
    def handle_data(self, data):
        if self.flag:
            self.metar+=str(data)
    
    def handle_endtag(self, tag):
        if tag=='body':
            self.flag=False
            if self.metar:
                print self.metar
                self.lastdata=self.metar[1:5]
                print self.lastdata
                f=open("./metarlist/"+self.lastdata,"w")
                f.write(self.metar)
                f.close                
                
            elif self.lastdata:
                f=open("./metarlist/"+self.lastdata,"a")
                f.write(self.metar)
                f.close
            self.metar=""

def parseData():
    file=os.listdir("./metardata/")
    for name in file:
        f=open('./metardata/'+name,'r')
        parse=MyParser()
        parse.feed(f.read())

def checkData():
    return

if __name__=='__main__':
    parseData()
    checkData()