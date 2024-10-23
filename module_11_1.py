import multiprocessing
from PIL import Image
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        line = f.readline()
        while line:
            line = line.rstrip('\n')
            all_data.append(line)
            line = f.readline()


if __name__ == '__main__':
    filenames = [f'./files/file {number}.txt' for number in range(1, 5)]
    start = datetime.now()
    for i in filenames:
        read_info(i)
    end = datetime.now()
    print(f'{end - start}(Линейный)')

    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'{end - start}(Vногопоточный)')
