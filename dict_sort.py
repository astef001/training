def read_dicts(file):
    dictionaries=[]
    with open(file, "r") as f:
        while True:
            temp_dict = {}
            inf = f.readline()
            if not inf:
                break
            inf = inf.rstrip("\n\r")
            inf = str.split(inf,' ')
            for i in range(0,len(inf)-1,2):
                temp_dict[inf[i]] = inf[i+1]
            dictionaries.append(temp_dict)
    return dictionaries


def sort_dicts(input_file):
    sorting = True
    dictionaries = read_dicts(input_file);
    while sorting:
        sorting = False
        for x in range(len(dictionaries)-1):
            if dictionaries[x][min(dictionaries[x])] > dictionaries[x+1][min(dictionaries[x+1])]:
                dictionaries[x], dictionaries[x+1] = dictionaries[x+1],dictionaries[x]
                sorting = True
    print(dictionaries)
