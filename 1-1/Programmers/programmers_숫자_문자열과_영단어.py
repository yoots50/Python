def solution(s):
    answer = []
    returnanswer = ''
    if s.isnumeric():
        return int(s)
    for idx in range(len(s)):
        if list(s)[idx].isalpha():
            if list(s)[idx:idx+4] == ['z','e','r','o']:
                answer.append('0')
            elif list(s)[idx:idx+3] == ['o','n','e']:
                answer.append('1')
            elif list(s)[idx:idx+3] == ['t','w','o']:
                answer.append('2')
            elif list(s)[idx:idx+5] == ['t','h','r','e','e']:
                answer.append('3')
            elif list(s)[idx:idx+4] == ['f','o','u','r']:
                answer.append('4')
            elif list(s)[idx:idx+4] == ['f','i','v','e']:
                answer.append('5')
            elif list(s)[idx:idx+3] == ['s','i','x']:
                answer.append('6')
            elif list(s)[idx:idx+5] == ['s','e','v','e','n']:
                answer.append('7')
            elif list(s)[idx:idx+5] == ['e','i','g','h','t']:
                answer.append('8')
            elif list(s)[idx:idx+4] == ['n','i','n','e']:
                answer.append('9')
            else:
                pass
        else:
            answer.append(s[idx])
    for i in answer:
        returnanswer += i
    return int(returnanswer)
