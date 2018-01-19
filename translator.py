import sys
import re


def translate(fname, d):
    f = open(fname)
    s = f.read()
    for k in d:
        r = re.compile('([\n\s])' + k + '([\s\.\,])', re.IGNORECASE)
        s = r.sub('\g<1>' + d[k] + '\g<2>', s)
        r = re.compile('([\n\s])' + k + 'ing([\s\.\,])', re.IGNORECASE)
        s = r.sub('\g<1>' + d[k] + '\g<2>', s)
        r = re.compile('([\n\s])' + k + 'in\'([\s\.\,])', re.IGNORECASE)
        s = r.sub('\g<1>' + d[k] + '\g<2>', s)
        r = re.compile('([\n\s])' + k + 's([\s\.\,])', re.IGNORECASE)
        s = r.sub('\g<1>' + d[k] + '\g<2>', s)
    return s


if __name__ == "__main__":
    with open('simple.dict','r') as inp:
        d = eval(inp.read())
    res = translate(sys.argv[1], d)
    print res
