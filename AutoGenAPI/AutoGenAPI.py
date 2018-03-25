#!/bin/python

def c_files_remove_annotation(file_buff):
    new_lines = []
    idx = 0
    is_multi_annot = False
    while(idx < len(file_buff)):
        line = file_buff[idx].strip()
        idx = idx + 1
        if len(line) == 0:
            continue
        elif (is_multi_annot):
            if ('*/' in line):
                is_multi_annot = False
            continue
        elif ('//' == line[0:2]):
            continue
        elif ('/*' == line[0:2]):
            if not ('*/' in line): 
                is_multi_annot = True
            continue
        elif ('#' == line[0]):
            continue
        #print(line)
        new_lines.append(line)
    return new_lines

def read_file(header_file):
    file_object = open(header_file)
    read_buff = []
    try:
        read_buff = file_object.readlines()
    finally:
        file_object.close()
    return read_buff

all_text  = read_file("api_test.h")
all_text = c_files_remove_annotation(all_text)
print(all_text)
