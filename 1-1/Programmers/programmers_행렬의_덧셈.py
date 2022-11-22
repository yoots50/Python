def solution(arr1,arr2):
    lst1 = []
    for idx1 in range(len(arr1)):
        lst = []
        for idx2 in range(len(arr1[0])):
            lst.append(arr1[idx1][idx2]+arr2[idx1][idx2])
        lst1.append(lst)
    return lst1
