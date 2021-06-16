def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} does not exist")        



  

readFile('1.txt')
readFile('exception_handling/Chapter_11/2.txt')
readFile('exception_handling/Chapter_11/3.txt')
readFile('exception_handling/Chapter_11/4.txt')