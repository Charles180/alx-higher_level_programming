#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nlist = []

    for x in range(list_length):
        try:
            nlist.append(my_list_1[x] / my_list_2[x])
        except ZeroDivisionError:
            nlist.append(0)
            print("division by 0")
            continue
        except IndexError:
            nlist.append(0)
            print("out of range")
            continue
        except TypeError:
            nlist.append(0)
            print("wrong type")
            continue
        finally:
            pass
    return nlist
