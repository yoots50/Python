def solution(new_id):
    new_id = new_id.lower() #1
    for string in new_id: #2
        if not(string.isalnum() or string == '.' or string == '_' or string == '-'):
            new_id = new_id.replace(string,'')
    for idx in range(len(new_id)): #3
        try:
            if new_id[idx] == '.':
                while new_id[idx+1] == '.':
                    new_id = new_id[:idx+1] + new_id[idx+2:]
        except:
            pass
    new_id = new_id.strip('.') #4
    if new_id == '': #5re
        new_id = 'a'
    if len(new_id) >= 16: #6re
        new_id = new_id[:15].rstrip('.')
    if len(new_id) <= 2: #7re
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id
