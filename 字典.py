mydict = {
    'apple': ['a round fruit with red skin', '苹果'],
    'banana': ['a long fruit with yellow skin', '香蕉'],
    'watermelon':['a large, round fruit with green skin', '西瓜']
    }
def list_all_words():
    print('Your word list \n')
    for key, value in mydict.items():
        print('{}({})\n{}'.format(key,value[1],value[0]))
def test_yourself():
    quit_the_test = False
    point = 0
    incorrect_word_list =[]
    for key, value in mydict.items():
        while True:
            answer = input('\nWhich word matches the definition? or [c]hinese,[p]ass,[q]uit\n{}'.format(value[0]))
            if answer == 'c':
                print(value[1])
            elif answer == 'p':
                print('The correct answer is {}'.format(key))
                incorrect_word_list.append(key)
                break
            elif answer =='q':
                quit_the_test = True
                break
            elif answer == key:
                point = point + 1
                print('correct')
                break
            else:
                print('It\'s not correct')

        if quit_the_test == True:
            break

    print('\nScore {}/{}'.format(point, len(mydict)))
    print('Incorrect words list:')
    for key in incorrect_word_list:
        value = mydict[key]
        print('{}({})\n{}'.format(key,value[1],value[0]))

def run():
    while True:
        cmd = input("""\nWelcome to your dictionary!
1)Test yourself!
2)List all words
3)exit\n""")
        if cmd == '1':
            test_yourself()
        elif cmd == '2':
            list_all_words()
        elif cmd == '3':
            break

run()
