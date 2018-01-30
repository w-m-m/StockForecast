from getProcessedData import getProcessedData
import argparse
from runModel import runModel
from showResult import showResult

if __name__ == '__main__':

    '''

        python run -f [filepath] -s [filepath] -c [stock code]

    output:
        stock error : implement by regression.score() 
        picture : implement by drawer

    '''
    parser = argparse.ArgumentParser()

    parser.add_argument("filepath", type=str, help="the directory of the .csv file")
    parser.add_argument("code", type=str, help="the stock code you want to predict")
    parser.add_argument("-r", "--ratio", type=float,
                        default=0.2, help="the validate data set ratio")
    parser.add_argument("-m", "--model", type=str, help="the model you choose",
                        default='MLPRegression')
    parser.add_argument("-p", "--preprocess", type=bool, help="preprocessing or not",
                        default=True)

    args = parser.parse_args()

    file_path = args.filepath

    # create pre processor
    # if args.p:
    processor = getProcessedData(file_path, args.code, args.ratio)
    train_feature, train_label, test_feature, test_label = processor.run()

    regression = runModel(args.model)
    regression.fit(train_feature, train_label)

    pred_result = regression.predict(test_feature)

    score = regression.score(test_feature, pred_result)
    print 'result'
    print pred_result
    print 'score'
    print score
    showResult = showResult(test_label,pred_result)
    showResult.run()