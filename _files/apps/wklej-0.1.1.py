#!/usr/bin/env python

""" Simple wklej.org paste script
license: gplv2

version 0.1.1
"""

from optparse import OptionParser
import commands
import sys
import xmlrpclib

syntaxes = [ 
'apache', 'bash', 'bat', 'c', 'cpp', 'csharp', 'css', 'd', 'diff',
'dylan', 'erlang', 'gas', 'haskell', 'html', 'html+django', 'html+genshi', 'html+mako', 'html+myghty',
'html+php', 'irb', 'irc', 'java', 'js', 'jsp', 'lua', 'minid', 'ocaml', 'perl', 'pycon', 'pytb', 'python',
'rhtml', 'rst', 'ruby', 'scheme', 'smarty', 'sourceslist', 'sql', 'squidconf', 'tex', 'text', 'vim', 'xml'
]

syntaxy = ""

def getAuthor():
    try:
        author = commands.getoutput('whoami')
    except:
        author = 'Anonim'
    return author

def checkSyntax(syn):
    if syn in syntaxes:
        pass
    else:
        print "WRONG SYNTAX"
        sys.exit(1)

def getTresc(input):
    if input:
        tresc = input
    else:
        print "Input is empty!"
        sys.exit(1)
    return tresc

for i in syntaxes:
    syntaxy = syntaxy + " " + i

usage = """
To paste something: 
$ echo 'something' | wklej -s syntax
$ cat file | wklej -s syntax
$ wklej -s syntax"""
parser = OptionParser(usage=usage)
parser.add_option("-s", "--syntax", dest="syntax", help="Choose one:" + syntaxy, default="text")
parser.add_option("-a", "--author", dest="author", help="", default=getAuthor())





def main(args=sys.argv):
    
    (options, args) = parser.parse_args()
    checkSyntax(options.syntax)

    tresc = getTresc(sys.stdin.read())

    rpc_srv = xmlrpclib.ServerProxy("http://wklej.org/xmlrpc/")
    result = rpc_srv.dodaj_wpis(tresc, options.syntax, options.author)
    print "http://wklej.org%s" % result
    
    sys.exit(0)


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
