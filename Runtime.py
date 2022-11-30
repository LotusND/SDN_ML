import pickle
import consts
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Module ML use model Random Forest

def predict(input_data):
    """
    Predict data in runtime
    :param input_data: a data like 1 row in dataset
    :return: kind of attack, or normal
    """
    standard_scale_model = pickle.load(open(consts.X_STANDARD_SCALE_MODEL, 'rb'))
    label_encoder_model = pickle.load(open(consts.Y_LABEL_ENCODER_MODEL, 'rb'))
    rfc_model = pickle.load(open(consts.RANDOM_FOREST_MODEL, 'rb'))


    data_header = standard_scale_model.transform(input_data)

    file_type = rfc_model.predict(data_header)
    kind_of_attack = label_encoder_model.inverse_transform(file_type)

    return kind_of_attack


data_test = pd.read_csv(consts.DATASET_TEST_NMAP_Drop)
# data_test = pd.read_csv(consts.DATASET_TEST_DoS_Drop)
# data_test = pd.read_csv(consts.DATASET_TEST_SQLI_DROP)



# print(data_test.shape)
# test predcit with 20 collumn
data_20 = data_test[:20]

data_20 = data_20.to_numpy()
# data_20 = data_test.to_numpy()

print(predict(data_20))


