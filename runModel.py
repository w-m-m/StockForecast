from sklearn.neural_network import MLPRegressor
import getProcessedData

class runModel(object):

    def __init__(self,method='MLPRegression'):
        self.method=method

    def fit(self,train_feature,train_label):
        if self.method=='MLPRegression':
            self.regression = MLPRegressor()
        self.regression.fit(train_feature, train_label)

    def predict(self,test_feature):
        self.predict_label = self.regression.predict(test_feature)
        return self.predict_label

    def getMSE(self,test_label):
        lable_size = len(test_label)
        mse = 0
        for index in range(lable_size):
            mse += (test_label[index] - self.predict_lable[index]) ** 2
        mse = float(mse / lable_size)
        return mse

    def score(self, test_feature, predict_label):
        score = self.regression.score(test_feature,predict_label)
        return score