__author__ = 'Victor'
from urllib.request import *
import re
url = 'http://www.ratemyprofessors.com/ShowRatings.jsp?tid=306975'

def crawlURL(addedURL):
    url = addedURL
    html = urlopen(url).read()

    teacherData = re.findall(r'\">(.*?)</',html)

    output = ''
    addStuff = 0
    for x in xrange(len(teacherData)):
        if teacherData[x] == 'Submit a Correction':
            output = 'professor: '
            for y in xrange(4):
                output += teacherData[x-8+y] + ' '
            addStuff = 1
        elif teacherData[x] == 'Helpfulness' and addStuff == 1:
            output += ': Overall quality: '+ str(teacherData[x-2]) + ': Average grade: ' + str(teacherData[x-1]) + ': Helpfulness: ' + teacherData[x+1]
        elif teacherData[x] == 'Easiness' and addStuff == 1:
            output += ': Easiness: ' + str(teacherData[x+1])
            addStuff = 0
            break
    print (output)
crawlURL(url)
