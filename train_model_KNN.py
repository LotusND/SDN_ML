import pandas as pd
import consts
from sklearn.model_selection import train_test_split
from pickle import dump
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,f1_score


def train_model():
    print('Reading dataset ...')
    df = pd.read_csv(consts.DATASET_PATH_40)
    X = df.drop(['Label'], axis=1)  # drop colum Label X
    X = X.astype('float64')
    Y = df['Label']  # Y col Label
    print('Read data done!')

    print('Normalizing dataset ...')
    lb = LabelEncoder()
    Y = lb.fit_transform(Y)
    dump(lb, open(consts.Y_LABEL_ENCODER_MODEL, 'wb'))

    lb_name_mapping = dict(zip(lb.classes_, lb.transform(lb.classes_)))
    print(lb_name_mapping)

    scl = StandardScaler()
    X = scl.fit_transform(X)
    dump(scl, open(consts.X_STANDARD_SCALE_MODEL, 'wb'))
    print('Normalize data done!')

    print('Training model ...')
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0, shuffle=True)

    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    dump(knn, open(consts.KNN_MODEL, 'wb'))
    print('Train model done!')

    print('Predicting model ...')
    Y_pred = knn.predict(X_test)
    print('Predict model done!')

    print(classification_report(Y_test, Y_pred, zero_division=1))
    print(f1_score(Y_test, Y_pred, average='macro'))
    # print(confusion_matrix(Y_test, Y_pred))




train_model()
