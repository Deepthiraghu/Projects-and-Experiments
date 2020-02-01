In this project, I have used the YouTube video statistics dataset and tried to predict a "Trending Score" for each video based on factors like views, comment count, likes and dislikes.

Steps to run the code:
1) First extract the dataset folder and place the three files mergeDatasets.py, trendingScoreCalculation.py and modelTrainer.py inside the youtube-new folder
2) Run the mergeDatasets.py file first. This should generate the dataset.csv file inside the youtube-new folder
3) Next, run the trendingScoreCalculation.py file. This should generate two files - binnedDataset.csv and WoEDataset.csv
4) Finally, run the modelTrainer.py file. This should generate the testScore.csv file and print the accuracy in the console. 

Note: Please ensure all the generated csv files are closed before running the code.