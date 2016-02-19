import xml.etree.ElementTree as et
import datetime
import sys, os


def main():
    tree = et.parse(os.curdir + '/crime-reporter.xml')
    print ''
    for child in tree.getroot():
        print ''
        print "#################################"
        print "Date:", child.attrib['datetime']
        print "Type:", child.attrib['type']
        for info in child:
            print '     ', info.tag + ":", info.text






if __name__ == '__main__':

    main()