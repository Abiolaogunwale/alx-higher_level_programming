#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    m = 0
    for s in range(x):
        try:
            print("{:d}".format(my_list[s]), end='')
            m += 1
        except (TypeError, ValueError):
            continue
    print()
    return (m)

