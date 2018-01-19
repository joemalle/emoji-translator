import json
import sys

def dict2map(fname):
    f = open(fname)
    d = {}
    while 1:
        line = f.readline()
        if line == "":
            break
        fp = line.index(' ')
        emoji = line[:fp]
        words = line[fp:].strip().split()
        for word in words:
            d[word] = emoji
    return d


if __name__ == "__main__":
    d = dict2map(sys.argv[1])
    print d
