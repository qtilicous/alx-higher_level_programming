#!/usr/bin/python3
def safe_print_list_integers(my_list=[], limit=0):
    nb_print = 0
    for i in range(limit):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_print += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            print()
            break
    print()
    return nb_print


my_list = [12, 7, 'abc', 45, 100, 'def']
nb_print = safe_print_list_integers(my_list, 2)
print("nb_print:", nb_print)
nb_print = safe_print_list_integers(my_list, 5)
print("nb_print:", nb_print)
nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print:", nb_print)
