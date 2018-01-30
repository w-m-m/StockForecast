from processor.cleanData import CleanData
from processor.getCorrCode import getCorrCode
from processor.dataGenerator_pchange import dataGenerator_pchange
from processor.dataGenerator import dataGenerator

class getProcessedData(object):

    def __init__(self,file_path,code,test_data_ratio):
        self.file_path = file_path
        self.code = code
        self.test_data_ratio=test_data_ratio

    def run(self):
        clean_data=CleanData(self.file_path)
        clean_data.run()

        data_generator_pchange= dataGenerator_pchange('..\data',self.code,self.test_data_ratio)
        train_feature, train_label, test_feature, test_label = data_generator_pchange.run()

        # data_generator = dataGenerator('..\data', self.code, self.test_data_ratio)
        # train_feature, train_label, test_feature, test_label = data_generator.run()

        return train_feature, train_label, test_feature, test_label