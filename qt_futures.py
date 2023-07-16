from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
from os import listdir
from os.path import isfile, join
import shutil
import random

from design_window_two import Ui_MainWindow

# Добавил
import pandas as pd
import mplfinance as mpf


index_file = 0
main_dir_name = "directory_pamp"
one_dir_name = "directory_standart"
two_dir_name = "directory_hard"
three_dir_name = "directory_smooth"


def check_dir(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


check_dir(main_dir_name)
check_dir(one_dir_name)
check_dir(two_dir_name)
check_dir(three_dir_name)


only_files = [f for f in listdir(main_dir_name) if isfile(join(main_dir_name, f))]
count_files = len(only_files)


def show_graph(file_name):
    file_name = f"{main_dir_name}/{file_name}"

    data = pd.read_csv(file_name)
    data['Time'] = data['Open time']
    data = data.set_index('Time')
    data.index = pd.to_datetime(data.index, unit = 'ms')
    data = data.astype(float)

    mpf.plot(data, type='candle', style='yahoo', volume=True)
    mpf.show()

    '''
    with open(file_name) as file:
        data = file.read().split('\n')
        # print(data)

    data_open = [float(elem.split(',')[1]) for elem in data[1:] if elem]
    data_close = [float(elem.split(',')[4]) for elem in data[1:] if elem]
    data_high = [float(elem.split(',')[2]) for elem in data[1:] if elem]
    data_low = [float(elem.split(',')[3]) for elem in data[1:] if elem]
    data_volume = [float(elem.split(',')[5]) for elem in data[1:] if elem]

    # data_volume = rand_list[index_file]
    times = [ii for ii in range(len(data_close))]

    # main_w.sc.set_value_hist_bar(data_volume, data_open, data_close, data_high, data_low)

    # plot data: x, y values
    main_w.graphWidget.clear()
    main_w.graphWidget.plot(times, data_close)
    main_w.graphWidget_2.clear()
    main_w.graphWidget_2.plot(times, data_volume)
'''

def func_one():
    global index_file
    index_file += 1
    if count_files > index_file:
        file_name = only_files[index_file]
        main_w.label.setText(file_name)
        show_graph(file_name)

    else:
        main_w.label.setText("Больше нет")

def func_two():
    global index_file
    index_file += 1
    if count_files > index_file:
        file_name = only_files[index_file]
        main_w.label.setText(file_name)
        show_graph(file_name)
        if not os.path.exists(f"{one_dir_name}/{file_name}"):
            shutil.copyfile(f"{main_dir_name}/{file_name}", f"{one_dir_name}/{file_name}")

    else:
        main_w.label.setText("Больше нет")



def func_three():
    global index_file
    index_file += 1
    if count_files > index_file:
        file_name = only_files[index_file]
        main_w.label.setText(file_name)
        show_graph(file_name)
        if not os.path.exists(f"{two_dir_name}/{file_name}"):
            shutil.copyfile(f"{main_dir_name}/{file_name}", f"{two_dir_name}/{file_name}")

    else:
        main_w.label.setText("Больше нет")



def func_four():
    global index_file
    index_file += 1
    if count_files > index_file:
        file_name = only_files[index_file]
        main_w.label.setText(file_name)
        show_graph(file_name)
        if not os.path.exists(f"{three_dir_name}/{file_name}"):
            shutil.copyfile(f"{main_dir_name}/{file_name}", f"{three_dir_name}/{file_name}")

    else:
        main_w.label.setText("Больше нет")


app = QtWidgets.QApplication(sys.argv)

main_window = QtWidgets.QMainWindow()
main_w = Ui_MainWindow()
main_w.setupUi(main_window)
main_w.label.setText(only_files[index_file])
main_w.pushButton.clicked.connect(func_one)
main_w.pushButton_2.clicked.connect(func_two)
main_w.pushButton_3.clicked.connect(func_three)
main_w.pushButton_4.clicked.connect(func_four)
show_graph(only_files[index_file])
main_window.show()

sys.exit(app.exec_())
