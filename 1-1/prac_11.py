lst = [ "국어",90, "수학",80, "영어",95, "과학",100, "역사",90 ]
def lstToDic(lst): #zip
    return dict(zip(lst[::2], lst[1::2]))
def lstToDic2(lst): # range(0,len(lst),2)로 하면 if 필요없음
    return_dic = {}
    for idx in range(len(lst)):
        if not idx % 2:
            return_dic[lst[idx]] = lst[idx+1]
    return return_dic
print(lstToDic(lst))
print(lstToDic2(lst))
string = "aaabbbccccccc12121546445"
#굳이 set을 만드는 것이 아닌 if else가 간편
# def countAlpha(string):
#   return_dic = {}
#   for alpha in string:
#       if alpha in return_dic:
#           return_dic[alpha] += 1
#       else:
#           return_dic[alpha] = 1
#   return return_dic
def countAlpha(string): 
    return_dic = dict()
    str_set = set(string)
    for alpha in str_set:
        if alpha.isalpha():
            return_dic[alpha] = string.count(alpha)
    return return_dic
print(countAlpha(string))
def countAlnum(string):
    return_dic = dict()
    str_set = set(string)
    for alnum in str_set:
        if alnum.isalnum():
            return_dic[alnum] = string.count(alnum)
    return return_dic
print(countAlnum(string))
Seoul_dic = {"A" : 1, "B" : 1, "C" : 3}
search = input("인구수를 알아볼 서울의 자치구 명을 입력하세요. (서울에 있는 자치구: %s): " %list(Seoul_dic.keys()))
while not search in Seoul_dic:
    search = input("다시 입력하세요. (서울에 있는 자치구: %s): " %list(Seoul_dic.keys()))
else:
    print("인구수는",Seoul_dic[search],"입니다.")
