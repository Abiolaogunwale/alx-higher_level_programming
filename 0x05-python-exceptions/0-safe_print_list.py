#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
       m = 0
        for s in range(x):
            print(my_list[s], end='')
            m += 1
        print()
    except IndexError:
        print()
    return (m)

