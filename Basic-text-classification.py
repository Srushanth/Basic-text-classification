import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf

print(tf.__version__)

url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
dataset = tf.keras.utils.get_file(
    'aclImdb_v1',
    url,
    untar=True,
    catche_dir='.',
    cache_subdir=''
)
dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')

os.listdir(dataset_dir)
