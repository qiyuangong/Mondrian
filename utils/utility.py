# !/usr/bin/env python
# coding:utf-8
"""
public functions
"""

from datetime import datetime
import time

def cmp(x, y):
    if x > y:
        return 1
    elif x==y:
        return 0
    else:
        return -1


def cmp_str(element1, element2):
    """
    compare number in str format correctley
    """
    try:
        return cmp(int(element1), int(element2))
    except ValueError:
        return cmp(element1, element2)

def cmp_value(element1, element2):
    if isinstance(element1, str):
        return cmp_str(element1, element2)
    else:
        return cmp(element1, element2)


def value(x):
    '''Return the numeric type that supports addition and subtraction'''
    if isinstance(x, (int, float)):
        return float(x)
    elif isinstance(x, datetime):
        return time.mktime(x.timetuple())
        # return x.timestamp() # not supported by python 2.7
    else:
        try:
            return float(x)
        except Exception as e:
            return x


def merge_qi_value(x_left, x_right, connect_str='~'):
    '''Connect the interval boundary value as a generalized interval and return the result as a string
    return:
        result:string
    '''
    if isinstance(x_left, (int, float)):
        if x_left == x_right:
            result = '%d' % (x_left)
        else:
            result = '%d%s%d' % (x_left, connect_str, x_right)
    elif isinstance(x_left, str):
        if x_left == x_right:
            result = x_left
        else:
            result = x_left + connect_str + x_right
    elif isinstance(x_left, datetime):
        # Generalize the datetime type value
        begin_date = x_left.strftime("%Y-%m-%d %H:%M:%S")
        end_date = x_right.strftime("%Y-%m-%d %H:%M:%S")
        result = begin_date + connect_str + end_date
    return result


def covert_to_raw(result, intuitive_order, delimiter='~'):
    """
    During preprocessing, categorical attrbutes are covert to
    numeric attrbute using intutive order. This function will covert
    these values back to they raw values. For example, Female and Male
    may be coverted to 0 and 1 during anonymizaiton. Then we need to transform
    them back to original values after anonymization.
    """
    covert_result = []
    qi_len = len(intuitive_order)
    for record in result:
        covert_record = []
        for i in range(qi_len):
            if len(intuitive_order[i]) > 0:
                vtemp = ''
                if delimiter in record[i]:
                    temp = record[i].split(delimiter)
                    raw_list = []
                    for j in range(int(temp[0]), int(temp[1]) + 1):
                        raw_list.append(intuitive_order[i][j])
                    vtemp = delimiter.join(raw_list)
                else:
                    vtemp = intuitive_order[i][int(record[i])]
                covert_record.append(vtemp)
            else:
                covert_record.append(record[i])
        if isinstance(record[-1], str):
            covert_result.append(covert_record + [record[-1]])
        else:
            covert_result.append(covert_record + [delimiter.join(record[-1])])
    return covert_result

