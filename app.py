from flask import Flask, request, jsonify, json
import logging as logger
logger.basicConfig(level="DEBUG")

# from sklearn.svm import SVR
# from warfit_learn import datasets, preprocessing
# from warfit_learn.metrics import score_pw20
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# from sklearn.externals import joblib
import pickle

# import numpy as np

app = Flask(__name__)

# if __name__ == '__main__':
#     logger.debug("starting the application")
#     from api import *
#     app.run(host="127.0.0.1", port=5000, debug=True, load_dotenv=True)

@app.route("/", methods=["POST"])
def hello():

    # raw_iwpc = datasets.load_iwpc()
    # data = preprocessing.prepare_iwpc(raw_iwpc)
    # train_set, test_set = train_test_split(data, test_size=0.2)
    #
    # svr_model = SVR(kernel='linear', degree=3, gamma='scale', coef0=0.0, tol=0.001, C=1.0, epsilon=0.1, shrinking=True,
    #                 cache_size=1000, verbose=False, max_iter=-1)
    #
    # Y_train = train_set['Therapeutic Dose of Warfarin']
    # X_train = train_set.drop(['Therapeutic Dose of Warfarin'], axis=1)
    #
    # svr_model.fit(X_train, Y_train)
    #
    # pickle_out = open("file1.pickle", "wb")
    # pickle.dump(svr_model, pickle_out)
    # pickle_out.close()
    # joblib.dump(svr_model, 'file.pkl')
    #
    # Y_test = np.array(test_set['Therapeutic Dose of Warfarin'])
    # X_test = test_set.drop(['Therapeutic Dose of Warfarin'], axis=1)
    # print("\nInput features:\n\n", X_test.iloc[0])
    # X_pred = X_test.iloc[0].values.reshape(1, -1)
    # print("\nInput features as passed to predict function: \n", X_pred)

    # Height = request.form.get('Height')
    # Weight = request.form.get('Weight')
    # Amiodarone = request.form.get('Amiodarone')
    # Carbamazepine = request.form.get('Carbamazepine')
    # Phenytoin = request.form.get('Phenytoin')
    #
    # Rifampin = request.form.get('Rifampin')
    # Smoker = request.form.get('Smoker')
    # _Asian = request.form.get('_Asian')
    # _Black = request.form.get('_Black')
    # _Unknown = request.form.get('_Unknown')
    #
    # _White = request.form.get('_White')
    # Age_10 = request.form.get('Age_10')
    # Age_20 = request.form.get('Age_20')
    # Age_30 = request.form.get('Age_30')
    # Age_40 = request.form.get('Age_40')
    #
    # Age_50 = request.form.get('Age_50')
    # Age_60 = request.form.get('Age_60')
    # Age_70 = request.form.get('Age_70')
    # Age_80 = request.form.get('Age_80')
    # Age_90 = request.form.get('Age_90')
    #
    # consensus_11 = request.form.get('consensus_11')
    # consensus_12 = request.form.get('consensus_12')
    # consensus_13 = request.form.get('consensus_13')
    # consensus_22 = request.form.get('consensus_22')
    # consensus_23 = request.form.get('consensus_23')
    # consensus_33 = request.form.get('consensus_33')
    # consensus_Unknown = request.form.get('consensus_Unknown')
    #
    # VKORC1_AA = request.form.get('VKORC1_AA')
    # VKORC1_AG = request.form.get('VKORC1_AG')
    # VKORC1_GG = request.form.get('VKORC1_GG')
    # VKORC1_Unknown = request.form.get('VKORC1_Unknown')

    Height = request.json['Height']
    Weight = request.json['Weight']
    Amiodarone = request.json['Amiodarone']
    Carbamazepine = request.json['Carbamazepine']
    Phenytoin = request.json['Phenytoin']

    Rifampin = request.json['Rifampin']
    Smoker = request.json['Smoker']
    _Asian = request.json['_Asian']
    _Black = request.json['_Black']
    _Unknown = request.json['_Unknown']

    _White = request.json['_White']
    Age_10 = request.json['Age_10']
    Age_20 = request.json['Age_20']
    Age_30 = request.json['Age_30']
    Age_40 = request.json['Age_40']

    Age_50 = request.json['Age_50']
    Age_60 = request.json['Age_60']
    Age_70 = request.json['Age_70']
    Age_80 = request.json['Age_80']
    Age_90 = request.json['Age_90']

    consensus_11 = request.json['consensus_11']
    consensus_12 = request.json['consensus_12']
    consensus_13 = request.json['consensus_13']
    consensus_22 = request.json['consensus_22']
    consensus_23 = request.json['consensus_23']
    consensus_33 = request.json['consensus_33']
    consensus_Unknown = request.json['consensus_Unknown']

    VKORC1_AA = request.json['VKORC1_AA']
    VKORC1_AG = request.json['VKORC1_AG']
    VKORC1_GG = request.json['VKORC1_GG']
    VKORC1_Unknown = request.json['VKORC1_Unknown']

    X_predi = [[Height, Weight, Amiodarone, Carbamazepine, Phenytoin, Rifampin, Smoker, _Asian, _Black, _Unknown,
                _White, Age_10, Age_20, Age_30, Age_40, Age_50, Age_60, Age_70, Age_80, Age_90,
                consensus_11, consensus_12, consensus_13, consensus_22, consensus_23, consensus_33, consensus_Unknown, VKORC1_AA, VKORC1_AG, VKORC1_GG,
                VKORC1_Unknown]]

    X_predi1 = [[170.99, 61, 1, 0, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0]]

    print("\nInput features as passed to predict function: \n", X_predi)
    # svr_model_jolib = joblib.load('file.pkl')

    pickle_in = open("file1.pickle", "rb")
    svr_model_jolib = pickle.load(pickle_in)
    Y_pred = svr_model_jolib.predict(X_predi)

    print("\nPredicted dosage: ", Y_pred[0], "mg/week")
    return "Predicted dosage: " + repr(Y_pred[0]) + " mg/week";


@app.route('/login/', methods=["POST"])
def login_page():

        if request.method == "POST":
            data = request.json['key']
            print(data)
            # attempted_password = request.form['password']
            return "Hello " + data

        if request.method == "GET":
            key = request.json['key']
            # attempted_password = request.form['password']
            return {"message" : "inside post method " + key}


app.run(host='0.0.0.0')
