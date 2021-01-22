import numpy as np
from numpy import *
import tensorflow as tf
import os
import re
import pickle
import nltk

def load_data(source_domain, target_domain, root_path):
    train_data = []
    val_data = []
    test_data = []
    source_unlabeled_data = []
    target_unlabeled_data = []
    src, tar = 1, 0

    print("source domian: ", source_domain, "target domain: ", target_domain)

    #load training data
    for (mode, label) in [("train", "positive"), ("train", "negative")]:
        fname = root_path + "%s/tokens_%s.%s" % (source_domain, mode, label)
        train_data.extend(get_review(fname, src, label))
    print("train_data_size: ", len(train_data))

    #load validation data
    for (mode, label) in [("test", "positive"), ("test", "negative")]:
        fname = root_path + "%s/tokens_%s.%s" % (source_domain, mode, label)
        val_data.extend(get_review(fname, src, label))
    print("validate_data_size: ", len(val_data))

    # load testing data// 
    # Test data contains all data? That's make no sense! And the result is certain improved!
    for (mode, label) in [("train", "positive"), ("train", "negative"), ("test", "positive"), ("test", "negative")]:
        fname = root_path+"%s/tokens_%s.%s" % (target_domain, mode, label)
        test_data.extend(get_review(fname, tar, label))
    print("test-size: ", len(test_data))

    # load unlabeled data
    for (mode, label) in [("train", "unlabeled")]:
        fname = root_path+"%s/tokens_%s.%s" % (source_domain, mode, label)
        source_unlabeled_data.extend(get_review(fname, src, label))
        fname = root_path+"%s/tokens_%s.%s" % (target_domain, mode, label)
        target_unlabeled_data.extend(get_review(fname, tar, label))
    print("unlabeled-size: ", len(source_unlabeled_data), len(target_unlabeled_data))

    vocab = getVocab(train_data + val_data + test_data + source_unlabeled_data + target_unlabeled_data)
    print("vocab-size: ", len(vocab))

    output_dir = "./work/logs/"

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    return train_data, val_data, test_data, source_unlabeled_data, target_unlabeled_data, vocab

