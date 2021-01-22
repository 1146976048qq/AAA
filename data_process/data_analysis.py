'''
Data analysis for Amazon Dataset (four domains)
'''
import argparse
import json
import os
import re
import sys
import pandas as pd
# import numpy as np

# from allennlp.predictors.predictor import Predictor
# from lxml import etree
# from nltk.tokenize import TreebankWordTokenizer
# from tqdm import tqdm

book_neg = '/Users/mac/Desktop/raw_data/books/review_negative_depparse.json'
book_pos = '/Users/mac/Desktop/raw_data/books/review_positive_depparse.json'
dvd_neg = '/Users/mac/Desktop/raw_data/dvd/review_negative_depparse.json'
dvd_pos = '/Users/mac/Desktop/raw_data/dvd/review_positive_depparse.json'
electronics_neg = '/Users/mac/Desktop/raw_data/electronics/review_negative_depparse.json'
electronics_pos = '/Users/mac/Desktop/raw_data/electronics/review_positive_depparse.json'
kitchen_neg = '/Users/mac/Desktop/raw_data/kitchen/review_negative_depparse.json'
kitchen_pos = '/Users/mac/Desktop/raw_data/kitchen/review_positive_depparse.json'
video_neg = '/Users/mac/Desktop/raw_data/video/review_negative_depparse.json'
video_pos = '/Users/mac/Desktop/raw_data/video/review_positive_depparse.json'

# with open(book_neg,'r') as book_neg:
#     load_dict = json.load(book_neg)

# print(load_dict["tokens"])



## book domain ###
import json
deprel = pd.DataFrame()

with open(book_neg) as f:
    book_neg_data = json.load(f)
    for dict in book_neg_data:
        sentences = dict['sentence']
        tokens = dict['tokens']
        tags = dict['tags']
        # get the syntax relations of each sentence
        dep = dict['predicted_dependencies']
        deprel = deprel.append(dep)

# print(len(deprel) # 100183
print(deprel[0].value_counts())


with open(book_pos) as f:
    book_pos_data = json.load(f)
    for dict in book_pos_data:
        sentences = dict['sentence']
        tokens = dict['tokens']
        tags = dict['tags']

        # get the syntax relations of each sentence
        dep = dict['predicted_dependencies']

        # get the syntax relation dataframe
        deprel = deprel.append(dep)

# print(len(deprel)) #99322
print(deprel[0].value_counts())


### dvd domain ###
import json
deprel = pd.DataFrame()

with open(dvd_neg) as f:
    dvd_neg_data = json.load(f)
    for dict in dvd_neg_data:
        sentences = dict['sentence']
        tokens = dict['tokens']
        tags = dict['tags']
        # get the syntax relations of each sentence
        dep = dict['predicted_dependencies']
        deprel = deprel.append(dep)

# print(len(deprel)) #100553
print(deprel[0].value_counts())


with open(dvd_pos) as f:
    dvd_pos_data = json.load(f)
    for dict in dvd_pos_data:
        sentences = dict['sentence']
        tokens = dict['tokens']
        tags = dict['tags']

        # get the syntax relations of each sentence
        dep = dict['predicted_dependencies']

        # get the syntax relation dataframe
        deprel = deprel.append(dep)

# print(len(deprel)) #198947
print(deprel[0].value_counts())


### electronics domain ###
import json
deprel = pd.DataFrame()

with open(electronics_neg) as f:
    electronics_neg_data = json.load(f)
    for dict in electronics_neg_data:
        sentences = dict['sentence']
        tokens = dict['tokens']
        tags = dict['tags']
        # get the syntax relations of each sentence
        dep = dict['predicted_dependencies']
        deprel = deprel.append(dep)

# print(deprel.duplicated().count()) #99290

# deprel = pd.DataFrame(deprel)

# get number of each syntax relation
print(deprel[0].value_counts())


with open(electronics_pos) as f:
    electronics_pos_data = json.load(f)
    for dict in electronics_pos_data:
        sentences = dict['sentence']
        tokens = dict['tokens']
        tags = dict['tags']

        # get the syntax relations of each sentence
        dep = dict['predicted_dependencies']

        # get the syntax relation dataframe
        deprel = deprel.append(dep)

# print(len(deprel)) #196151
print(deprel[0].value_counts())


# ### kitchen domain ###
import json
deprel = pd.DataFrame()

with open(kitchen_neg) as f:
    kitchen_neg_data = json.load(f)
    for dict in kitchen_neg_data:
        sentences = dict['sentence']
        tokens = dict['tokens']
        tags = dict['tags']
        # get the syntax relations of each sentence
        dep = dict['predicted_dependencies']
        deprel = deprel.append(dep)

# print(len(kitchen_deprel)) #98422
print(deprel[0].value_counts())


with open(kitchen_pos) as f:
    kitchen_pos_data = json.load(f)
    for dict in kitchen_pos_data:
        sentences = dict['sentence']
        tokens = dict['tokens']
        tags = dict['tags']

        # get the syntax relations of each sentence
        dep = dict['predicted_dependencies']

        # get the syntax relation dataframe
        deprel = deprel.append(dep)

# print(len(kitchen_deprel)) #194643
print(deprel[0].value_counts())







