def solution(participant, completion):
    participant.sort()
    completion.sort()
    a = list(zip(participant,completion))
    for i in a:
        if i[0] != i[1]:
            return i[0]
    return participant[-1]
