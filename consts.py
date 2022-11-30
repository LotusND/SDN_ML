from tkinter.tix import COLUMN


DROP_COLUMN = ["Flow ID", "Src IP", "Src Port", "Dst IP", "Dst Port", "Timestamp", "Fwd PSH Flags", "Bwd PSH Flags",
               "Fwd URG Flags", "Bwd URG Flags", "FIN Flag Cnt", "SYN Flag Cnt", "RST Flag Cnt", "PSH Flag Cnt",
               "ACK Flag Cnt", "URG Flag Cnt", "CWE Flag Count", "CWE Flag Count", "Down/Up Ratio", "Fwd Seg Size Avg",
               "Bwd Seg Size Avg", "Subflow Fwd Pkts", "Subflow Fwd Byts", "Subflow Bwd Pkts", "Subflow Bwd Byts",
               "Init Fwd Win Byts", "Init Bwd Win Byts", "Fwd Act Data Pkts", "Fwd Seg Size Min", "ECE Flag Cnt",
               "Fwd Byts/b Avg", "Fwd Pkts/b Avg", "Fwd Blk Rate Avg", "Bwd Byts/b Avg", "Bwd Pkts/b Avg",
               "Bwd Blk Rate Avg", ]

# Xóa column có giá trị tùy vào môi trường mạng và có giá trị là hằng số
DROP_COLUMN_Redundant = ["Flow ID", "Src IP", "Src Port", "Dst IP", "Timestamp", 'Fwd PSH Flags',
                         'Fwd URG Flags', 'CWE Flag Count', 'ECE Flag Cnt',
                         'Fwd Byts/b Avg', 'Fwd Pkts/b Avg', 'Fwd Blk Rate Avg', 'Bwd Byts/b Avg',
                         'Bwd Pkts/b Avg', 'Bwd Blk Rate Avg', 'Init Fwd Win Byts', 'Fwd Seg Size Min']

COLUMN_30 = ["Protocol", "Init Bwd Win Byts", "Pkt Len Min", "FIN Flag Cnt", "Bwd Pkt Len Min", "Down/Up Ratio", "Pkt Size Avg",
             "Pkt Len Mean", "Bwd Pkt Len Mean", "Bwd Seg Size Avg", "Dst Port", "Pkt Len Std", "Fwd IAT Tot", "Bwd Pkt Len Std", "Fwd Pkt Len Min",
             "Fwd IAT Max", "SYN Flag Cnt", "Pkt Len Max", "Fwd Pkt Len Max", "Fwd IAT Std", "Fwd Pkt Len Mean", "Fwd Seg Size Avg",
             "Fwd IAT Mean", "Bwd Pkt Len Max", "ACK Flag Cnt", "Idle Min", "Bwd Pkts/s", "Flow Byts/s", "Idle Mean", "Flow IAT Std", "Label" ]

COLUMN_40 = ["Protocol", "Init Bwd Win Byts", "Pkt Len Min", "FIN Flag Cnt", "Bwd Pkt Len Min",
             "Down/Up Ratio", "Pkt Size Avg", "Pkt Len Mean", "Bwd Pkt Len Mean", "Bwd Seg Size Avg",
             "Dst Port", "Pkt Len Std", "Fwd IAT Tot", "Bwd Pkt Len Std", "Fwd Pkt Len Min",
             "Fwd IAT Max", "SYN Flag Cnt", "Pkt Len Max", "Fwd Pkt Len Max", "Fwd IAT Std",
             "Fwd Pkt Len Mean", "Fwd Seg Size Avg", "Fwd IAT Mean", "Bwd Pkt Len Max",
             "ACK Flag Cnt", "Idle Min", "Bwd Pkts/s", "Flow Byts/s", "Idle Mean", "Flow IAT Std","Fwd Pkt Len Std","Idle Max",
             "Bwd IAT Std","Bwd IAT Max","Flow IAT Max","Bwd PSH Flags","PSH Flag Cnt","Bwd URG Flags","URG Flag Cnt",
             "Idle Std", ]


COLUMN_50= ["Protocol", "Init Bwd Win Byts", "Pkt Len Min", "FIN Flag Cnt", "Bwd Pkt Len Min",
             "Down/Up Ratio", "Pkt Size Avg", "Pkt Len Mean", "Bwd Pkt Len Mean", "Bwd Seg Size Avg",
             "Dst Port", "Pkt Len Std", "Fwd IAT Tot", "Bwd Pkt Len Std", "Fwd Pkt Len Min",
             "Fwd IAT Max", "SYN Flag Cnt", "Pkt Len Max", "Fwd Pkt Len Max", "Fwd IAT Std",
             "Fwd Pkt Len Mean", "Fwd Seg Size Avg", "Fwd IAT Mean", "Bwd Pkt Len Max",
             "ACK Flag Cnt", "Idle Min", "Bwd Pkts/s", "Flow Byts/s", "Idle Mean", "Flow IAT Std",
             "Fwd Pkt Len Std", "Idle Max", "Bwd IAT Std", "Bwd IAT Max", "Flow IAT Max", "Bwd PSH Flags",
             "PSH Flag Cnt", "Bwd URG Flags", "URG Flag Cnt", "Idle Std", "Flow IAT Mean", "Flow Duration",
             "Bwd IAT Tot", "Active Max", "Flow Pkts/s", "Active Mean", "Active Min", "Bwd IAT Mean", 
             "Active Std", "Pkt Len Var","Label", ]

COLUMN_60= ["Protocol", "Init Bwd Win Byts", "Pkt Len Min", "FIN Flag Cnt", "Bwd Pkt Len Min",
             "Down/Up Ratio", "Pkt Size Avg", "Pkt Len Mean", "Bwd Pkt Len Mean", "Bwd Seg Size Avg",
             "Dst Port", "Pkt Len Std", "Fwd IAT Tot", "Bwd Pkt Len Std", "Fwd Pkt Len Min",
             "Fwd IAT Max", "SYN Flag Cnt", "Pkt Len Max", "Fwd Pkt Len Max", "Fwd IAT Std",
             "Fwd Pkt Len Mean", "Fwd Seg Size Avg", "Fwd IAT Mean", "Bwd Pkt Len Max",
             "ACK Flag Cnt", "Idle Min", "Bwd Pkts/s", "Flow Byts/s", "Idle Mean", "Flow IAT Std",
             "Fwd Pkt Len Std", "Idle Max", "Bwd IAT Std", "Bwd IAT Max", "Flow IAT Max", "Bwd PSH Flags",
             "PSH Flag Cnt", "Bwd URG Flags", "URG Flag Cnt", "Idle Std", "Flow IAT Mean", "Flow Duration",
             "Bwd IAT Tot", "Active Max", "Flow Pkts/s", "Active Mean", "Active Min", "Bwd IAT Mean", 
             "Active Std", "Pkt Len Var", "Fwd Pkts/s", "Fwd Header Len", "Tot Bwd Pkts", 
             "Subflow Bwd Pkts", "TotLen Bwd Pkts", "Subflow Bwd Byts", "Fwd IAT Min", "Bwd Header Len", 
             "Fwd Act Data Pkts", "Bwd IAT Min","Label", ]



DATASET_PATH_DROP = "dataset/dataset_drop.csv" #all 66 feature
DATASET_PATH = "dataset/dataset.csv" # all 83 feature
Y_LABEL_ENCODER_MODEL = "model/y_encoder.pkl"
X_STANDARD_SCALE_MODEL = "model/standard_scaler.pkl"

# save model
RANDOM_FOREST_MODEL = "model/random_forest.pkl"
SVM_MODEL = "model/svm.pkl"
NAVIE_BAYES_MODEL = "model/navie_bayes.pkl"
DECISION_TREE_MODEL = "model/decision_tree.pkl"
KNN_MODEL = "model/knn.pkl"



DATASET_PATH_30 = "dataset/dataset30.csv" #Dataset Trainning model with Random Forest
DATASET_PATH_40 = "dataset/dataset40.csv"
# DATASET_PATH_49 = "dataset/dataset49.csv"
DATASET_PATH_50 = "dataset/dataset50.csv"
DATASET_PATH_60 = "dataset/dataset60.csv"


DATASET_TEST_ScanPort = "dataset/ScanPortFlow.csv"
DATASET_TEST_ScanPort_DROP = "dataset/ScanPortDrop.csv"


DATASET_TEST_DoS = "dataset/DoSFlow.csv"
DATASET_TEST_DoS_Drop = "dataset/DoSFlowDrop.csv"

DATASET_TEST_NMAP_Drop = "dataset/NmapFlowDrop.csv"

DATASET_TEST_NMAP_DoS_Drop = "dataset/Nmap_DoS.csv"


DATASET_TEST_SQLI = "dataset/SQLIFlow.csv"
DATASET_TEST_SQLI_DROP = "dataset/SQLI.csv"




