def readFileLines(path): #list안 for문
    with open(path) as f:
        opened_file = f.readlines()
        return [i.strip("\n") for i in opened_file]
def readFileLines2(path):
    lst = []
    with open(path) as f:
        opened_file = f.readlines()
        for i in opened_file:
            lst.append(i)
    return lst
prac_09 = readFileLines("prac_09.ini")
prac_09_1 = readFileLines("prac_09.ini")
print(prac_09)
print(prac_09_1)
lst = [prac_09[0],prac_09[1:3]]
print(lst)
