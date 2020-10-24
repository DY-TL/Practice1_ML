import numpy as np
import matplotlib.pyplot as plot
from sklearn.datasets import load_iris
dataset = load_iris()

print (u'%s\tlable' % (u'\t'.join(dataset.feature_names)))

for feature, lable in   zip(dataset.data, dataset.target):
    feature_line = u'\t'.join([str(f) for f in feature])
    lable_line = dataset.target_names[lable]
    print('%s\t%s' %(feature_line, lable_line))