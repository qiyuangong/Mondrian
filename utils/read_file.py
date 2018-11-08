# !/usr/bin/env python
'''
read csv data, 
support numeric, category, time date

author : Liu Kun
date   : 2018-10
'''

from datetime import datetime


__DEBUG = False

def read_csv(file_path, 
        QI_INDEX,
        IS_CAT,
        IS_DATETIME,
        SA_INDEX, 
        header=False, delimiter=',', encoding="utf-8",
        TIME_FORMAT_STR="%Y-%m-%d %H:%M:%S"
    ):
    """
    read microdata for *.txt and return read data

    # Note that Mondrian can only handle numeric attribute
    # So, categorical attributes should be transformed to numberic attributes
    # before anonymization. For example, Male and Female shold be transformed
    # to 0, 1 during pre-processing. Then, after anonymization, 0 and 1 should
    # be transformed to Male and Female.
    """
    QI_num = len(QI_INDEX)
    data = []
    # oder categorical attributes in intuitive order
    # here, we use the appear number
    intuitive_dict = []
    intuitive_order = []
    intuitive_number = []
    for i in range(QI_num):
        intuitive_dict.append(dict())
        intuitive_number.append(0)
        intuitive_order.append(list())
    with open(file_path, 'r', encoding=encoding) as data_file:
        if header:
            headers = data_file.readline()
        for line in data_file:
            if len(line) == 0 or '?' in line:
                continue
            temp = [item.strip() for item in line.split(delimiter)]
            ltemp = []
            if not all(temp):
                continue
            for i in range(QI_num):
                index = QI_INDEX[i]
                if IS_DATETIME[i]:
                    t = datetime.strptime(temp[index], TIME_FORMAT_STR)
                    ltemp.append(t)
                elif IS_CAT[i]:
                    try:
                        ltemp.append(intuitive_dict[i][temp[index]])
                    except KeyError:
                        intuitive_dict[i][temp[index]] = intuitive_number[i]
                        ltemp.append(intuitive_number[i])
                        intuitive_number[i] += 1
                        intuitive_order[i].append(temp[index])
                else:
                    ltemp.append(float(temp[index]))
            ltemp.append(temp[SA_INDEX])
            data.append(ltemp)
        return data, intuitive_order

