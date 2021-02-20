stroka = str(input())

list = stroka.split(' ')
print(list)

if list[4] == 'nit':
    print('9')
elif list[4] == 'diff':
    if list[0] == '1965':
        print('8')
    elif list[0] == '2012':
        if list[1] == '1986':
            print('0')
        elif list == '2013':
            print('1')
    elif list[0] == '2000':
        if list[1] == '1986':
            if list[2] == 'glsl':
                print('2')
            elif list[2] == 'sass':
                print('3')
            elif list[2] == 'edn':
                print('4')
        elif list[1] == '2013':
            if list[2] == 'glsl':
                print('5')
            elif list[2] == 'sass':
                print('6')
            elif list[2] == 'edn':
                print('7')
