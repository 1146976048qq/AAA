import pandas as pd
import numpy
import csv

# -*- coding: utf-8 -*-
import os
import re
import codecs
 
def replace_func(input_file):
#     p2 = re.compile(r'[(][: @ . , ？！\s][)]')
    p3 = re.compile(r'[「『]')
    p4 = re.compile(r'[\s+\/_$%^*(+\"\')]+|[+——()【】“”！，。？、~@#￥%……&*（） ; \-\ \[\ \]\ ]\...\ \....')
    outfile = codecs.open(input_file + ".txt", 'w', 'utf-8')
    with codecs.open(input_file, 'r', 'utf-8') as myfile:        
        for line in myfile:
            print(line)
#             line = p2.sub(r' ', line)
            line = p3.sub(r' ', line)
            line = p4.sub(r' ', line)
            t=0
            str = []
            for i in line.split(" "):
                if t < 30:
                    outfile.write(i)
                    outfile.write(" ")
                    t = t + 1
                
            outfile.write('\n')
                
            
            
    outfile.close()
 
def run():
    data_path = ''
    data_names = ['dataset/raw_data/books/review_negative', 'dataset/raw_data/books/review_positive',
                  'dataset/raw_data/books/review_unlabeled',

                  'dataset/raw_data/dvd/review_negative', 'dataset/raw_data/dvd/review_positive',
                  'dataset/raw_data/dvd/review_unlabeled',

                  'dataset/raw_data/electronics/review_negative', 'dataset/raw_data/electronics/review_positive',
                  'dataset/raw_data/electronics/review_unlabeled',

                  'dataset/raw_data/kitchen/review_negative', 'dataset/raw_data/kitchen/review_positive',
                  'dataset/raw_data/kitchen/review_unlabeled',

                  'dataset/raw_data/video/review_negative', 'dataset/raw_data/video/review_positive',
                  'dataset/raw_data/video/review_unlabeled',
                  
                  ]
    for data_name in data_names:
        replace_func(data_name)
        print('{0} has been processed !'.format(data_name))
        
if __name__ == '__main__':
    run()
