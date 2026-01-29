import glob

myfiles = glob.glob("filees/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())