import multiprocessing
import io
import datetime


# 0:00:01.425764  #  время -линейный запуск
# 0:00:00.644853 # время - при многопроцесном подходе
def read_info(name):
    all_data = []

    with open(name, 'r') as file:
        m = True
        while m:
            line = file.read()
            all_data.append(line)
            if (len(line) == 0):
                m = False




if __name__ == "__main__":

    for i in range(1,5):
        filenames = [f'./file {number}.txt' for number in range(1, 5)]


    # #Линейный запуск
    start = datetime.datetime.now()
    for name in filenames:
        read_info(name)
    stop = datetime.datetime.now()
    print(stop - start)


    # start = datetime.datetime.now()
    # with multiprocessing.Pool(processes=4) as pool:
    #     pool.map(read_info, filenames)
    #     stop = datetime.datetime.now()
    # print(stop - start)
    #



