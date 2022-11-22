import math
lists,list1,results,listxy,linenum = [],[],[],[],0
with open('C:/Users/yooTs/Downloads/MP08/MP08data.txt',encoding = 'cp949') as text :
    for line in text :
        lists.append(line.strip('\n'))
for words in lists :
    if words == '삼각형' or words == '사각형' or words == '원':
        if words == '사각형':
            listxy1 = lists[linenum+1:linenum+5]
            for num in listxy1 :
                num = int(num)
                listxy.append(num)
            x1,y1,x2,y2=listxy
            tuplexy = (x1,y1,x2,y2)
            S = (x1 - x2) * (y1 - y2)
            if S < 0 :
                S *= -1
        elif words == '삼각형':
            listxy1 = lists[linenum+1:linenum+7]
            for num in listxy1 :
                num = int(num)
                listxy.append(num)
            x1,y1,x2,y2,x3,y3 = listxy
            tuplexy = (x1,y1,x2,y2,x3,y3)
            a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
            c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
            s = (a+b+c)/2
            S = math.sqrt(s*(s-a)*(s-b)*(s-c))
        else :
            listxy1 = lists[linenum+1:linenum+4]
            for num in listxy1 :
                num = int(num)
                listxy.append(num)
            x,y,r=listxy
            tuplexy = (x,y,r)
            S = r**2*math.pi
        results.append(words)
        list1.append(words)
        results.append(S)
        list1.append(tuplexy)
        listxy,list1,tuplexy = [],[],()
    linenum += 1
for line in results:
    print(line)
