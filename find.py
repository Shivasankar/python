__author__ = 'Shiva'


def main():
    one = two = three = four = five = six = seven = eight = nine = zero = 0
    val = [12, 13, 12, 14, 12, 444, 25, 66, 54, 90, 23, 11, 58]
    size = len(val)
    #print val
    print size
    for i in val:
        #print i
        lst_num = i % 10
        print lst_num
        if lst_num == 0:
            zero += 1
        elif lst_num == 1:
            one += 1
        elif lst_num == 2:
            two += 1
        elif lst_num == 3:
            three += 1
        elif lst_num == 4:
            four += 1
        elif lst_num == 5:
            five += 1
        elif lst_num == 6:
            six += 1
        elif lst_num == 7:
            seven += 1
        elif lst_num == 8:
            eight += 1
        elif lst_num == 9:
            nine += 1
    print('1', one)
    print('2', two)
    print('3', three)
    print('4', four)
    print('5', five)
    print('6', six)
    print('7', seven)
    print('8', eight)
    print('9', nine)
    print('0', zero)

if __name__ == '__main__':
    global val, one, two, three, four, five, six, seven, eight, nine, zero
    main()
