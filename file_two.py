

print("File TWO's '__name__' is set to {}".format(__name__))


def function_three(x):
    print(x)


if __name__ == '__main__': 

    print("File TWO is the main program being executed")

else: 

    print("File TWO is being imported")