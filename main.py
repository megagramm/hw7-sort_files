def read_files(lst):
    data = {}
    for filename in lst:
        with open('sorted/'+filename) as f:
            lines = f.readlines()
            data[filename] = {'lines': lines, 'len': len(lines)}
    return data


def make_result_file(dct):
    lst = []
    for file, file_data in dct.items():
        lst.append(file_data['len'])
    lst.sort()
    with open('result.txt', 'w') as f:
        for ln in lst:
            for filename, file_data in dct.items():
                if ln == file_data['len']:
                    f.write(filename+'\n')
                    f.write(str(ln)+'\n')
                    for line in file_data['lines']:
                        f.write(line.strip('\n')+'\n')


files = ['1.txt', '2.txt', '3.txt']
make_result_file(read_files(files))
