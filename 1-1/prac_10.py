def returnFileList(path):
    import os
    try:
        return os.listdir(path)
    except FileNotFoundError:
        return "경로 없음"
path = "C:/"
print(returnFileList(path))
path = "D:/"
print(returnFileList(path))
def readFileLines(path): #리스트 안  for문
    try:
        with open(path) as f:
            return [line.strip("\n") for line in f] # return_list = [] ; for line in f : return_list.append(line.strip("\n")) ; return return_list
    except FileNotFoundError:
        path = input("다시 입력: ")
        return readFileLines(path)
print(readFileLines("prac_09.ini"))
print(readFileLines("NoFile"))

            
