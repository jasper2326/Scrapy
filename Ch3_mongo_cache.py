# author = Jasper_Jiao@ele.me
# -*- coding: cp936 -*-
# coding: cp936

try:
    import cPickle as pickle
except ImportError:
    import pickle
import zlib
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.binary import Binary

class MongoCache:
    def __init__(self):