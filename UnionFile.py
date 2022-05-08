def union(file_list: list):
    for file in file_list:
        with open(file, 'r') as f:
            str_list = f.readlines()
            str_list.insert(0, str(len(str_list)))
            str_list.insert(1, '\n')
            str_list.insert(0, '\n'f'{file}''\n')
        with open(file, 'w') as fw:
            fw.writelines(str_list)


file_list = ['1.txt', '2.txt', '3.txt']

union(file_list)


with open('mainfile.txt', 'w') as fwm:
    for fname in file_list:
        with open(fname) as f:
            for line in f:
                fwm.writelines(line)


