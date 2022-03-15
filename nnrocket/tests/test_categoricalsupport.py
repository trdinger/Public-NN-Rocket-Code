# IBM Time Series Classification version 1.0.0
# IBM Confidential
# Copyright IBM Corp., 2021

import pathlib
import ray
import sys
import pickle
import torch
import random
import numpy as np
from nnrocket.core.NNRocketRay import *
from nnrocket.core.apihub import *
from utils.limits import *

# --time_column Time --time_format "%Y-%m-%d %H:%M:%S" --target_columns '["Value1","Value2","Value3","Value4","Value5","Value6"]' --label_column Label --categorical_columns '["Category1","Category2","Category3"]' --snapshot_column Snapshot --train_test_split 0.7 --result_type accuracy

def test_categoricalsupport():

    current_dir=str(pathlib.Path().resolve())
    if "nnrocket" in current_dir:
        csvfile = ('../data/UEA-BasicMotions-Cat.csv')
    else:
        csvfile = (str(pathlib.Path().resolve())+'/nnrocket/data/UEA-BasicMotions-Cat.csv')

    args = {}
    args['time_column'] = "Time"
    args['time_format'] = "%Y-%m-%d %H:%M:%S"
    args['target_columns'] = '["Value1","Value2","Value3","Value4","Value5","Value6"]'
    args['label_column'] = "Label"
    args['snapshot_column'] = "Snapshot"
    args['train_test_split'] = 0.2
    args['result_type'] = "accuracy"
    args['categorical_columns'] = '["Category1","Category2","Category3"]'

    (report) = apihub(csvfile ,args['time_column'],args['time_format'],args['target_columns'],args['label_column'],\
        args['snapshot_column'],args['train_test_split'],args['result_type'],args['categorical_columns'])

    assert len(str(report)) > 10

if __name__ == '__main__':
    test_categoricalsupport()
