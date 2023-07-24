import os
import glob
import hashlib



def get_list_folder():
    PATH = glob.glob('/home/root/USPD/module_*//')
    return PATH

def get_list_file():
    FILE_LIST = []
    for i in get_list_folder():
        if os.path.isdir(i+'lib'):
            PATH_FILE_LIST = glob.glob(i+'lib/module_*')
            FILE_LIST.append(PATH_FILE_LIST)
        else:
            PATH_FILE_LIST = glob.glob(i+'*')
            FILE_LIST.append(PATH_FILE_LIST)
    
    return FILE_LIST

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def hash_sum():
    HASH_LIST = []
    for i in get_list_file():
        digest = ''
        for j in i:
            digest += md5(j)
        if len(i) == 1:
            HASH_LIST.append([digest, i[0]])
        else:
            HASH_LIST.append([hashlib.md5(digest.encode()).hexdigest(), i[0]])
    return HASH_LIST

if __name__ == '__main__':

    # print(*get_list_folder(), sep ='\n')
    with open('heshsum.log', 'a') as f:
        print(*hash_sum(), sep ='\n', file=f)