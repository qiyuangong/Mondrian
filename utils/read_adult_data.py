#!/usr/bin/env python
# coding=utf-8

# Read data and read tree fuctions for INFORMS data
# attributes ['age', 'workcalss', 'final_weight', 'education', 'education_num', 'matrital_status', 'occupation',
# 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'class']
# QID ['age', 'workcalss', 'education', 'matrital_status', 'race', 'sex', 'native_country']
# SA ['occopation']

import pdb

gl_att_names = ['age', 'workcalss', 'final_weight', 'education',
                'education_num', 'matrital_status', 'occupation', 'relationship',
                'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'class']
gl_QI_index = [0, 1, 3, 5, 8, 9, 13]
gl_is_cat = [False, True, True, True, True, True, True]
gl_SA_index = 6

__DEBUG = False


def read_data():
    """
    read microda for *.txt and return read data
    """
    QI_num = len(gl_QI_index)
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
            index = gl_QI_index[i]
            if gl_is_cat[i]:
                try:
                    ltemp.append(intuitive_order[i][temp[index]])
                except:
                    intuitive_order[i][temp[index]] = intuitive_number[i]
                    ltemp.append(intuitive_number[i])
                    intuitive_number[i] += 1
            else:
                ltemp.append(int(temp[index]))
        ltemp.append(temp[gl_SA_index])
        data.append(ltemp)
    return (data, intuitive_order)
