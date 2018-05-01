#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from urllib.request import urlopen
import sys

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""

    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement (self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                self.linea = "Title: " + self.theContent + ".<br/>"
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
                archivo = open("barrapunto.html","a")
                archivo.write("<a href='" + self.theContent + "'>" + self.linea + "</a></br>")
                archivo.close()
                self.inContent = False
                self.theContent = ""
                archivo.close()

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

#Main

if len(sys.argv) < 1:
    print ("Usage Error")
    sys.exit(1)

theParser = make_parser()
theHandler = myContentHandler()
theParser.setContentHandler(theHandler)

archivo = open("barrapunto.html","w")
archivo.write("<h1>TITULARES</h1>")
archivo.close()
url = "http://barrapunto.com/index.rss"
archivoXML = urlopen(url)
theParser.parse(archivoXML)

print ("Parse complete")
