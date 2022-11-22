#202210947 유태석
import sys
def readData(filename):
    return_dic = dict()
    try:
        with open(filename) as f:
            for line in f.readlines():
                lst = line.strip("\n").split(",")
                return_dic[lst[0]] = [lst[1],int(lst[2])]
        return return_dic
    except FileNotFoundError:
        print(f"{filename}이 없습니다.")
        sys.exit()        
#print(readData("items.cp949.txt"))
#print(readData("없는 파일"))
d = readData("items.cp949.txt")
def printItem(d, itemName):
    cnt = 0
    for idx in d.keys():
        try:
            if idx.count(itemName):
                print(f"상품명 : {idx}, 분류 : {d[idx][0]}, 가격 : {d[idx][1]}")
                cnt = 1
        except:
            pass
    if not cnt:
        print(f"상품 {itemName}이 없습니다.")
#print(printItem(d,"주걱"))
#print(printItem(d,"없는 상품"))
def printCategory(d, category):
    cnt = 0
    for idx in d:
        if d[idx][0].lower() == category.lower():
            print(f"상품명 : {idx}, 분류 : {d[idx][0]}, 가격 : {d[idx][1]}")
            cnt = 1
    if not cnt:
        print(f"분류항목 {category}가 없습니다.")
#print(printCategory(d, "Food"))
#print(printCategory(d,"없는 카테고리"))
def printPriceInRange(d, price1, price2):
    cnt = 0
    try:
        price1 = int(price1)
        price2 = int(price2)
        for idx in d:
            if price1 <= d[idx][1] and d[idx][1] < price2:
                print(f"상품명 : {idx}, 분류 : {d[idx][0]}, 가격 : {d[idx][1]}")
                cnt = 1
        if not cnt:
            print(f"가격이 {price1} ~ {price2} 에 해당되는 물품이 없습니다.")
    except BaseException:
        print("가격은 정수로 입력하세요.")
#print(printPriceInRange(d, 100, 5000))
#print(printPriceInRange(d, 0, 3000))
#print(printPriceInRange(d,"가","나"))
def main(filename):
    d = readData(filename)
    inp= input("\"명령:데이터\" 형태로 입력하세요: ")
    if inp[:inp.find(":")] == "item":
        return printItem(d, inp[inp.find(":")+1:])
    elif inp[:inp.find(":")] == "category":
        return printCategory(d, inp[inp.find(":")+1:])
    elif inp[:inp.find(":")] == "price":
        price1 = inp[inp.find(":")+1:inp.find("~")]
        price2 = inp[inp.find("~")+1:]
        return printPriceInRange(d, price1, price2)
    else:
        pass
main("items.cp949.txt")
            
