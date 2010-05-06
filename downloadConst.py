import re,sys

matcher = re.compile('"/wiki/(.*?UK_Parliament_constituency\))"')

consts = set()
for line in open(sys.argv[1],'r').readlines():
    for match in matcher.findall(line):
        consts.add(match)

for match in consts:
    print "http://en.wikipedia.org/wiki/" + match

