#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            x = 0
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            x = 0
        except IndexError:
            print("out of range")
            x = 0
        finally:
            new_list.append(x)
    return new_list
