import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import *

class showResult(object):

    def __init__(self,test_lable,predict_lable):
        self.test_label=test_lable
        self.predict_label=predict_lable

    def DivergingPic(self,test_label,predict_lable):
        num = range(len(test_label))
        sns.set()
        plt.plot(num,test_label, label=u'test_lablel')
        plt.plot(num,predict_lable , label=u'predict_label')
        plt.legend()
        plt.show()

    def run(self):
        self.DivergingPic(self.test_label,self.predict_label)
