import os
from os import getcwd
from random import shuffle
from math import floor

if __name__ == '__main__':

    datadir = os.path.join(getcwd() + '/data/VOC2007/JPEGImages')


    def get_file_list_from_dir(datadir):
        all_files = os.listdir(os.path.abspath(datadir))
        data_files = list(filter(lambda file: file.endswith('.jpg'), all_files))
        shuffle(data_files)
        return data_files


    def get_training_and_testing_sets(file_list):
        split = 0.8
        split_index = floor(len(file_list) * split)
        training = file_list[:split_index]
        testing = file_list[split_index:]
        return training, testing

    def txt_generator(train, test):
        path_train = os.path.join(getcwd() + '/data/VOC2007/ImageSets/Main/trainval.txt')
        path_test = os.path.join(getcwd() + '/data/VOC2007/ImageSets/Main/test.txt')
        if not os.path.exists(path_train):
            with open(path_train, 'w+') as f:
                for i in range(len(train)):
                    train[i] = train[i].replace('image', '')
                    train[i] = train[i].replace('.jpg', '')
                    f.write("%s\r\n" % (train[i]))
        if not os.path.exists(path_test):
            with open(path_test, 'w+') as f:
                for i in range(len(test)):
                    test[i] = test[i].replace('image', '')
                    test[i] = test[i].replace('.jpg', '')
                    f.write("%s\r\n" % (test[i]))
                f.close()
        else:
            print('trainval.txt already exists')
    file_list = get_file_list_from_dir(datadir)
    [train, test] = get_training_and_testing_sets(file_list)
    txt_generator(train, test)

'''
    
    number_list = []
    for i in file_list:
        i = i.replace('image', '')
        i = i.replace('.jpg', '')
        number_list.append(i)

    print(number_list)
'''