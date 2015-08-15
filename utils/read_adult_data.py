"""
read adult dataset
"""

# !/usr/bin/env python
# coding=utf-8

# Read data and read tree fuctions for INFORMS data
# attributes ['age', 'workcalss', 'final_weight', 'education', 'education_num',
# 'matrital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain',
# 'capital_loss', 'hours_per_week', 'native_country', 'class']
# QID ['age', 'workcalss', 'education', 'matrital_status', 'race', 'sex', 'native_country']
# SA ['occopation']

from utils.utility import cmp_str

ATT_NAME = ['age', 'workcalss', 'final_weight', 'education',
            'education_num', 'marital_status', 'occupation', 'relationship',
            'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
            'native_country', 'class']
QI_INDEX = [0, 1, 4, 5, 6, 8, 9, 13]
IS_CAT = [False, True, False, True, True, True, True, True]
SA_INDEX = -1
__DEBUG = False


def read_data():
    """
    read microda for *.txt and return read data
    """
    QI_num = len(QI_INDEX)
    data = []
    # oder categorical attributes in intuitive order
    # here, we use the appear number
    intuitive_order = []
    intuitive_number = []
    for i in range(QI_num):
        intuitive_order.append(dict())
        intuitive_number.append(0)
    data_file = open('data/adult.data', 'rU')
    for line in data_file:
        line = line.strip()
        # remove empty and incomplete lines
        # only 30162 records will be kept
        if len(line) == 0 or '?' in line:
            continue
        # remove double spaces
        line = line.replace(' ', '')
        temp = line.split(',')
        ltemp = []
        for i in range(QI_num):
            index = QI_INDEX[i]
            if IS_CAT[i]:
                try:
                    ltemp.append(intuitive_order[i][temp[index]])
                except KeyError:
                    intuitive_order[i][temp[index]] = intuitive_number[i]
                    ltemp.append(intuitive_number[i])
                    intuitive_number[i] += 1
            else:
                ltemp.append(int(temp[index]))
        ltemp.append(temp[SA_INDEX])
        data.append(ltemp)
    return data


# def read_data():
#     """
#     read microda for *.txt and return read data
#     """
#     QI_num = len(QI_INDEX)
#     data = []
#     result = []
#     # oder categorical attributes in intuitive order
#     # here, we use the appear number
#     intuitive_order = []
#     for i in range(QI_num):
#         intuitive_order.append(dict())
#     data_file = open('data/adult.data', 'rU')
#     for line in data_file:
#         line = line.strip()
#         # remove empty and incomplete lines
#         # only 30162 records will be kept
#         if len(line) == 0 or '?' in line:
#             continue
#         # remove double spaces
#         line = line.replace(' ', '')
#         temp = line.split(',')
#         ltemp = []
#         for i in range(QI_num):
#             index = QI_INDEX[i]
#             if IS_CAT[i]:
#                 try:
#                     intuitive_order[i][temp[index]] += 1
#                 except KeyError:
#                     intuitive_order[i][temp[index]] = 1
#             ltemp.append(temp[index])
#         ltemp.append(temp[SA_INDEX])
#         data.append(ltemp)
#     order = []
#     for i in range(QI_num):
#         order.append(sorted(intuitive_order[i].keys(), cmp=cmp_str))
#     for temp in data:
#         ltemp = []
#         for i in range(QI_num):
#             if IS_CAT[i]:
#                 ltemp.append(order[i].index(temp[i]))
#             else:
#                 ltemp.append(int(temp[i]))
#         ltemp.append(temp[-1])
#         result.append(ltemp)
#     return result
