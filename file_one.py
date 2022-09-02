import file_two



print("File ONE's '__name__' variable is set to {}".format(__name__))


if __name__ == "__main__": 
    print("File ONE is the main program being executed")
    file_two.function_three('What?')

else: 
    print("File ONE is being imported")