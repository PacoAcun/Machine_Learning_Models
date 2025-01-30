"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.10
"""
from pandas import DataFrame
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def process_data(df:DataFrame)->DataFrame:
    
    df.drop(df.columns[0], axis=1, inplace=True)

    df = df[['drive-wheels','horsepower','engine-size','length', 'width', 'height','curb-weight','city-mpg']]

    #encode categoriacal value
    lb_encoder = LabelBinarizer()
    dw_encoded = lb_encoder.fit_transform(df['drive-wheels'])
    df_w_encoded = pd.concat([df, pd.DataFrame(data=dw_encoded, columns=lb_encoder.classes_)],axis=1)
    df_w_encoded.drop('drive-wheels', axis=1, inplace=True)

    return df_w_encoded

def add_volume(df):
    df['volume'] = df['length']*df['width']*df['height']
    
    return df

def scale_features(df):
    y = df['city-mpg']
    df = df.drop('city-mpg',axis=1)

    scaler = MinMaxScaler()
    scaler.fit(df)
    df_scaled_values = scaler.transform(df)
    df_scaled = pd.DataFrame(data=df_scaled_values,columns=df.columns)
    df_scaled['city-mpg'] = y
    return pd.concat([df_scaled,y],axis=0)


