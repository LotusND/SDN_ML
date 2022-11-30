import pandas as pd
import consts
import pickle as pkl


#Data Preparation

# replace 'DDos ' to 'DDoS' save OVS_R.csv
def rep():
    ovs_rep = pd.read_csv("I:\Visual code\sdn-ml\dataset\OVS.csv")
    ovs_rep['Label'] = ovs_rep['Label'].replace({'DDoS ': 'DDoS'})
    ovs_rep.to_csv("I:\Visual code\sdn-ml\dataset\OVS.csv", index=False)

rep()

def concat_data(meta_path, normal_path, ovs_path):
    """
    Concat 3 csv data to 1 dataset
    :param meta_path: metasploitable-2.csv path
    :param normal_path: Normal_data.csv path
    :param ovs_path: OVS.csv path
    :return: 1 dataset
    """

    meta_df = drop_duplicate_data(pd.read_csv(meta_path))
    normal_df = drop_duplicate_data(pd.read_csv(normal_path))
    ovs_df = drop_duplicate_data(pd.read_csv(ovs_path))

    df = pd.concat([meta_df, normal_df, ovs_df], ignore_index=True) 

    df.to_csv(consts.DATASET_PATH_DROP, index=False)

# concat_data("dataset/metasploitable-2.csv", "dataset/Normal_data.csv", "dataset/OVS.csv")


def drop_duplicate_data(dataframe: pd.DataFrame):
    """
    Drop columns that do not use, and drop duplicate data
    :param dataframe: DataFrame of dataset
    :return: DataFrame has been preprocessed
    """
    dataframe = dataframe.drop(columns=consts.DROP_COLUMN_Redundant)
    dataframe = dataframe.drop_duplicates()
    return dataframe





def check():
    print('Reading dataset ...')

    df = pd.read_csv(consts.DATASET_PATH_SDN)

    # df=df.drop(columns=consts.DROP_COLUMN)
    # df.to_csv(consts.DATASET_TEST_DoS_DROP, index=False)
    # print(df.shape[1])
    print(df.head)
    # print(df.info)
    # print(df['Label'])
    print(df.query("Label=='Normal'"))
    # print(df.query("Label=='BFA'"))
    # print(df.query("Label=='BOTNET'"))
    # print(df.query("Label=='DDoS'"))
    # print(df.query("Label=='DoS'"))
    # print(df.query("Label=='Probe'"))
    # print(df.query("Label=='U2R'"))
    # print(df.query("Label=='Web-Attack'"))
    # print(df.shape)

    # df2 = df[df.duplicated()]
    # print(df2)
    # print('Reading dataset ...')
    # df = pd.read_csv(consts.DATASET_PATH)
    # X = df.drop(['Label'], axis=1)  # drop colum Label X
    # X = X.astype('float64')
    # Y = df['Label']  # Y col Label
    # print('Read data done!')
    # # print(Y.shape)
    # Y2 = numpy.array(Y).reshape((-1, 1))
    # print(Y2.shape)


check()



# remove DROP_COLUMN_Redundant
# df=pd.read_csv(consts.DATASET_PATH)
# sf=df.drop(columns=consts.DROP_COLUMN_Redundant)
# sf.to_csv(consts.DATASET_PATH_DROP, index=False)

# def remove_constant_value_features(df):
#     return [e for e in df.columns if df[e].nunique() == 1]

# drop_col=remove_constant_value_features(df)
# print(drop_col)
