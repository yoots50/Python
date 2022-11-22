def solution(array, commands):
    answer = []
    if type(commands[0]) != list:
        lst = array[commands[0]:commands[1]+1]
        lst.sort
        return lst[commands[2]]
    else :    
        for i in commands:
            lst = array[i[0]-1:i[1]]
            lst.sort()
            answer.append(lst[i[2]-1])
        return answer
