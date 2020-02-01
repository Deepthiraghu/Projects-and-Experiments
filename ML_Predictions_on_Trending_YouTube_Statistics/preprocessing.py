import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
from collections import Counter
import datetime
import json

# Hiding warnings for cleaner display
warnings.filterwarnings('ignore')

df = pd.read_csv("USvideos.csv")
print (df.info())

# retrieves rows having null in the specified column
null_vals = df[df["description"].apply(lambda x: pd.isna(x))].head(3)
print (null_vals)

# replaces null values with NaN
df["description"] = df["description"].fillna(value="")
print (df.head())

null_vals = df[df["description"].apply(lambda x: pd.isna(x))].head(3)
print (null_vals)

year_count = df["trending_date"].apply(lambda x: '20' + x[:2]).value_counts(normalize=True)
print (year_count)


# correlation matrix
h_labels = [x.replace('_', ' ').title() for x in 
            list(df.select_dtypes(include=['number', 'bool']).columns.values)]

fig, ax = plt.subplots(figsize=(6,6))
_ = sns.heatmap(df.corr(), annot=True, xticklabels=h_labels, yticklabels=h_labels, cmap="PuBuGn", ax=ax)

plt.show()

# # channel vs no. of videos 
# cdf = df.groupby("channel_title").size().reset_index(name="video_count") \
#     .sort_values("video_count", ascending=False).head(20)

# fig, ax = plt.subplots(figsize=(8,8))
# _ = sns.barplot(x="video_count", y="channel_title", data=cdf,
#                 palette=sns.cubehelix_palette(n_colors=20, reverse=True), ax=ax)
# _ = ax.set(xlabel="No. of videos", ylabel="Channel")
# plt.show()
# # category vs no. of videos

# with open("US_category_id.json") as f:
#     categories = json.load(f)["items"]
# cat_dict = {}
# for cat in categories:
#     cat_dict[int(cat["id"])] = cat["snippet"]["title"]
# df['category_name'] = df['category_id'].map(cat_dict)

# cdf = df["category_name"].value_counts().to_frame().reset_index()
# cdf.rename(columns={"index": "category_name", "category_name": "No_of_videos"}, inplace=True)
# fig, ax = plt.subplots()
# _ = sns.barplot(x="category_name", y="No_of_videos", data=cdf, 
#                 palette=sns.cubehelix_palette(n_colors=16, reverse=True), ax=ax)
# _ = ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
# _ = ax.set(xlabel="Category", ylabel="No. of videos")
# plt.show()
# # publishing day vs no. of videos

# df["publishing_day"] = df["publish_time"].apply(
#     lambda x: datetime.datetime.strptime(x[:10], "%Y-%m-%d").date().strftime('%a'))
# df["publishing_hour"] = df["publish_time"].apply(lambda x: x[11:13])
# df.drop(labels='publish_time', axis=1, inplace=True)

# cdf = df["publishing_day"].value_counts()\
#         .to_frame().reset_index().rename(columns={"index": "publishing_day", "publishing_day": "No_of_videos"})
# fig, ax = plt.subplots()
# _ = sns.barplot(x="publishing_day", y="No_of_videos", data=cdf, 
#                 palette=sns.color_palette(['#003f5c', '#374c80', '#7a5195', 
#                                            '#bc5090', '#ef5675', '#ff764a', '#ffa600'], n_colors=7), ax=ax)
# _ = ax.set(xlabel="Publishing Day", ylabel="No. of videos")
# plt.show()
# # publishing hour vs no. of videos

# cdf = df["publishing_hour"].value_counts().to_frame().reset_index()\
#         .rename(columns={"index": "publishing_hour", "publishing_hour": "No_of_videos"})
# fig, ax = plt.subplots()
# _ = sns.barplot(x="publishing_hour", y="No_of_videos", data=cdf, 
#                 palette=sns.cubehelix_palette(n_colors=24), ax=ax)
# _ = ax.set(xlabel="Publishing Hour", ylabel="No. of videos")
# plt.show()






# # This Python 3 environment comes with many helpful analytics libraries installed
# # It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# # For example, here's several helpful packages to load in 

# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# # Input data files are available in the "../input/" directory.
# # For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

# import os

# # Any results you write to the current directory are saved as output.
# us_df = pd.read_csv('USvideos.csv', index_col='video_id')

# # print (us_df[['trending_date', 'publish_time']].head())

# us_df['trending_date'] = pd.to_datetime(us_df['trending_date'], format='%y.%d.%m')
# us_df['trending_date'].head()
# print (us_df['trending_date'])

# us_df['publish_time'] = pd.to_datetime(us_df['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
# us_df['publish_time'].head()

# us_df.insert(3, 'publish_date', us_df['publish_time'].dt.date)
# us_df['publish_time'] = us_df['publish_time'].dt.time
# # print (us_df[['publish_time', 'publish_date', 'trending_date']].head())

# import datetime

# us_df["publishing_day"] = us_df["publish_time"].apply(
#     lambda x: datetime.datetime.strptime(x[:10], "%Y-%m-%d").date().strftime('%a'))
# us_df["publishing_hour"] = us_df["publish_time"].apply(lambda x: x[11:13])
# us_df.drop(labels='publish_time', axis=1, inplace=True)
# print (us_df["publishing_day"])