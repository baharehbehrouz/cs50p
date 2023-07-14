import sys
if len(sys.argv)<2:
   sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
   sys.exit("Too many command-line arguments")
elif sys.argv[1][-2:] != "py":
   sys.exit("Not a Python file")
   # print(sys.argv[1])
else:
    try:
        counter = 0
        with open(sys.argv[1], newline='') as pythonfile:
            lines = pythonfile.readlines()
            for line in lines:
                if len(line.lstrip()) > 0:
                    if line.lstrip()[0] == "#":
                        pass
                    else:
                        counter += 1
        print(counter)
    except FileNotFoundError:
            sys.exit("File does not exist")
             