def convert_int(str):
    while str.find(',') != 0:
        str = str[:str.find(',')]+str[str.find(',')+1:]
    else:
        return str
print(convert_int('12,12,12,1,21,2'))
