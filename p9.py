"""
9.Write a Python program to display the size of every data type."""

import sys
print("size of interger: ",sys.getsizeof(int()))
print("size of float: ",sys.getsizeof(float()))
print("size of string: ",sys.getsizeof(str()))
print("size of list: ",sys.getsizeof(list()))
print("size of list: ",sys.getsizeof(set()))
print("size of list: ",sys.getsizeof(tuple()))


"""
size of interger:  24
size of float:  24
size of string:  49
size of list:  56
size of list:  216
size of list:  40
