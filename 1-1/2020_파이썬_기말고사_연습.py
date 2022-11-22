import sys
file_name = "python.txt"#input("파일 이름을 입력하세요: ")
while not file_name:
    file_name = input("파일 이름을 다시 입력하세요: ")
search_str = "언어"#input("검색할 문자열을 입력하세요: ")
while not search_str:
    search_str = input("검색할 문자열을 다시 입력하세요: ")
def fileToList(file_name): #예외처리 필요
    returnlst = []
    try:
        with open(file_name) as file:
            for line in list(file.readlines()):
                returnlst.append(line.strip("\n"))
        return returnlst
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        sys.exit()
    except UnicodeDecodeError:
        with open(file_name, encoding = "utf-8") as file:
            for line in list(file.readlines()):
                returnlst.append(line.strip("\n"))
        return returnlst


def strFinder(line, search_str):
    idxtuple = []
    if line.find(search_str) != -1 and len(line) >= len(search_str):
        for idx in range(0,len(line)-len(search_str)+2):
            if line[idx:idx+len(search_str)] == search_str:
                idxtuple.append(idx+1)
    return tuple(idxtuple)
dic = {}
lst = []
for line in fileToList(file_name):
    if strFinder(line, search_str):
        lst.append([strFinder(line, search_str), line])
print("lst",lst)
for lsts in lst:
    dic[fileToList(file_name).index(lsts[1])+1] = lsts
print("dic",dic)
if dic:
    for idx in range(len(dic)):
        print(f"{list(dic.keys())[idx]}", ":", f"{list(dic.values())[idx][0]}", ":", f"{list(dic.values())[idx][1]}")        
