import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from feature_engine import categorical_encoders as ce

# Load dataset
def load_titanic():
        data = pd.read_csv('https://www.openml.org/data/get_csv/16826755/phpMYEkMl')
        data = data.replace('?', np.nan)
        data['cabin'] = data['cabin'].astype(str).str[0]
        data['pclass'] = data['pclass'].astype('O')
        data['embarked'].fillna('C', inplace=True)
        return data

data = pd.read_csv(r'youtube-new/WoEdataset.csv', index_col=None, header=0)
data['likes_bin'] = data['likes_bin'].astype('str')
data['dislikes_bin'] = data['dislikes_bin'].astype('str')
data['views_bin'] = data['views_bin'].astype('str')
data['comment_count_bin'] = data['comment_count_bin'].astype('str')
data['performance'] = data['performance'].astype('bool')
x_col = ['likes_bin', 'dislikes_bin', 'views_bin','comment_count_bin']
x = data[x_col]
y = data["performance"]
# Separate into train and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
X_train = x
y_train = y
# set up a rare label encoder
rare_encoder = ce.RareLabelCategoricalEncoder(tol=0.03, n_categories=5,variables=['likes_bin', 'dislikes_bin', 'views_bin','comment_count_bin'])
# fit and transform data
train_t = rare_encoder.fit_transform(X_train)
test_t = rare_encoder.transform(X_train)

# set up a weight of evidence encoder
encoder = ce.WoERatioCategoricalEncoder(
encoding_method='woe', variables=['likes_bin', 'dislikes_bin', 'views_bin','comment_count_bin'])

# fit the encoder
encoder.fit(train_t, y_train)

# transform
train_t = rare_encoder.transform(train_t)
test_t = rare_encoder.transform(test_t)

woe_dict = (encoder.encoder_dict_)
likes_dict = (woe_dict['likes_bin'])
dislikes_dict = (woe_dict['dislikes_bin'])
views_dict = (woe_dict['views_bin'])
comment_count_dict = (woe_dict['comment_count_bin'])

def createDataset(dictionary,feature):
    keyList = []
    valueList = []
    for key,value in dictionary.items():
        keyList.append(key)
        valueList.append(value)
    woe_dataframe[feature+'_bin'] = keyList
    woe_dataframe[feature+'_WoE'] = valueList

woe_dataframe = pd.DataFrame()
createDataset(likes_dict,'likes')
createDataset(dislikes_dict,'dislikes')
createDataset(views_dict,'views')
createDataset(comment_count_dict,'comment_count')


print (woe_dataframe)
woe_dataframe.to_csv(path_or_buf=r'youtube-new/SKBinnedDataset.csv',index = None, header=True)
