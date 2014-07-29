#!/usr/bin/env python
#coding=utf-8

# store

import socket
import pickle
from datetime import datetime
from utils.ftp_upload import ftp_upload

def save_to_file(result, flag=0):
    print "Saving result...."
    hostname = socket.gethostname()
    file_tail = datetime.now().strftime('%Y-%m-%d-%H') + '.txt'
    file_path = 'output/'
    file_name = hostname + '-result' + file_tail
    if flag:
        # write file in text
        file_result = open(file_path + file_name,'w')
        for record in result:
            line = ';'.join(record) + '\n'
            file_result.write(line)
    else:
        # write file using pickle
        file_result = open(file_path + file_name,'wb')
        pickle.dump(result, file_result)
    file_result.close()
    # try:
    #     ftp_upload(file_name, file_path)
    # except:
    #     print "Upload Fail!"
    print "Save Complete!"
