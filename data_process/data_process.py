'''
Biaffine Dependency parser from AllenNLP
'''
import argparse
import json
import os
import re
import sys
import pandas as np

from allennlp.predictors.predictor import Predictor
from lxml import etree
from nltk.tokenize import TreebankWordTokenizer
from tqdm import tqdm

pt_models_dir = '/data/kkzhang/Cross_GAT/AllenNLP'
model_path = os.path.join(pt_models_dir, "biaffine-dependency-parser-ptb-2020.04.06.tar.gz")


def parse_args():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument('--model_path', type=str, default=model_path,
                        help='Path of biaffine dependency parser.')
    parser.add_argument('--data_path', type=str, default='/data/kkzhang/Cross_GAT/dataset/raw_data',
                        help='Directory of where original data held.')
    return parser.parse_args()


def text2docs(file_path, predictor):
    '''
    Annotate the sentences from extracted txt file using AllenNLP's predictor.
    '''
    with open(file_path, 'r') as f:
        sentences = f.readlines()
    docs = []
    print('Predicting dependency information...')
    for i in tqdm(range(len(sentences))):
        docs.append(predictor.predict(sentence=sentences[i]))

    return docs


def dependencies2format(doc):  # doc.sentences[i]
    '''
    Format annotation: sentence of keys
                                - tokens
                                - tags
                                - predicted_dependencies
                                - predicted_heads
                                - dependencies
    '''
    sentence = {}
    sentence['tokens'] = doc['words']
    sentence['tags'] = doc['pos']
    # sentence['energy'] = doc['energy']
    predicted_dependencies = doc['predicted_dependencies']
    predicted_heads = doc['predicted_heads']
    sentence['predicted_dependencies'] = doc['predicted_dependencies']
    sentence['predicted_heads'] = doc['predicted_heads']
    sentence['dependencies'] = []
    for idx, item in enumerate(predicted_dependencies):
        dep_tag = item
        frm = predicted_heads[idx]
        to = idx + 1
        sentence['dependencies'].append([dep_tag, frm, to])

    return sentence


def get_dependencies(file_path, predictor):
    docs = text2docs(file_path, predictor)
    sentences = [dependencies2format(doc) for doc in docs]
    return sentences


def syntax2json(sentences, origin_file):
    json_data = []
    tk = TreebankWordTokenizer()
    mismatch_counter = 0
    idx = 0
    with open(origin_file, 'r') as fopen:
        raw = fopen.readlines()
        for sentence in raw:
            example = dict()
            example["sentence"] = sentence
            example['tokens'] = sentences[idx]['tokens'] 
            example['tags'] = sentences[idx]['tags']
            example['predicted_dependencies'] = sentences[idx]['predicted_dependencies']
            example['predicted_heads'] = sentences[idx]['predicted_heads']
            example['dependencies'] = sentences[idx]['dependencies']            

            json_data.append(example)
            idx+=1

    # extended_filename = origin_file.replace('.txt', '_biaffine_depparsed.json')
    extended_filename = origin_file.replace('.txt', '_depparse.json')

    with open(extended_filename, 'w') as f:
        json.dump(json_data, f)

    print('done,json_data length:', len(json_data))
    print('idx_length:', idx) # DataItem Number


def main():
    args = parse_args()
    print("-------------", args.model_path)
    predictor = Predictor.from_path(args.model_path)

    # data = [('books/review_negative.txt', 'books/review_positive.txt', 'books/review_unlabeled'),
    #         ('dvd/review_negative.txt', 'dvd/review_positive.txt', 'dvd/review_unlabeled.txt'),
    #         ('electronics/review_negative.txt', 'electronics/review_positive.txt', 'electronics/review_unlabeled.txt'),
    #         ('kitchen/review_negative.txt', 'kitchen/review_positive.txt', 'kitchen/review_unlabeled.txt'),
    #         ('video/review_negative.txt', 'video/review_positive.txt', 'video/review_unlabeled.txt')
    #         ]

    # for neg_file, pos_file, unlabel_file in data:
    
    #     neg_sentences = get_dependencies(os.path.join(args.data_path, neg_file), predictor)
    #     pos_sentences = get_dependencies(os.path.join(args.data_path, pos_file), predictor)
    #     unlabel_sentences = get_dependencies(os.path.join(args.data_path, unlabel_file), predictor)

    #     print(len(neg_sentences), len(pos_sentences), len(unlabel_sentences))

    #     syntax2json(neg_sentences, os.path.join(args.data_path, neg_file))
    #     syntax2json(pos_sentences, os.path.join(args.data_path, pos_file))
    #     syntax2json(unlabel_sentences, os.path.join(args.data_path, unlabel_file))
        
    data = [('books/review_negative.txt', 'books/review_positive.txt'),
            ('dvd/review_negative.txt', 'dvd/review_positive.txt'),
            ('electronics/review_negative.txt', 'electronics/review_positive.txt'),
            ('kitchen/review_negative.txt', 'kitchen/review_positive.txt'),
            ('video/review_negative.txt', 'video/review_positive.txt')
            ]

    for neg_file, pos_file in data:
    
        neg_sentences = get_dependencies(os.path.join(args.data_path, neg_file), predictor)
        pos_sentences = get_dependencies(os.path.join(args.data_path, pos_file), predictor)

        print(len(neg_sentences), len(pos_sentences))

        syntax2json(neg_sentences, os.path.join(args.data_path, neg_file))
        syntax2json(pos_sentences, os.path.join(args.data_path, pos_file))

if __name__ == "__main__":
    main()
