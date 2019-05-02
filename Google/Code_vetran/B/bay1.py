from __future__ import print_function, division

import sys

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))

def read_in(infile):
    data = infile.readlines()
    amount = int(data[0])
    content = data[1:]
    assert amount == len(content)
    return [s.strip() for s in content]

def do_output(number, output, outfiles):
    for f in outfiles:
        print('Case #%d: ' % number, output, file=f)

def main():
    for i, content in enumerate(read_in(infile)):
        do_output(i+1, do_task(content), outfiles)

def do_task(content):
    # Parse input string
    sex, mom, dad = content.split()
    child = -5 if sex == 'G' else 5
    def to_inches(s):
        feet, ins = s.split("'")
        inches = ins.split('"')[0]
        return int(feet) * 12 + int(inches)
    height = (to_inches(mom) + to_inches(dad) + child) / 2
    if height == int(height):
        range = 4
    else:
        range = 3.5

    def to_string(h):
        assert int(h) == h
        h = int(h)
        return '''{}'{}"'''.format(h // 12, h % 12)

    return '{} to {}'.format(to_string(height-range), to_string(height+range))

if __name__=='__main__':
    main()
