__author__ = 'Shiva'


def palin(str):
    revstr = str[::-1]
    print str
    print revstr
    if str == revstr:
        print 'Given string is palindrom'
    else:
        print 'Given string is not palindrom'


def main():
    str = raw_input('Enter the string');
    palin(str)

main()
