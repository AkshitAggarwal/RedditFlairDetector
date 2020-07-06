# PrecogRITask


# Reddit-Flair-Detector: End Goal

To scrape data from r/india (A subreddit on https://reddit.com/) and classify posts into their respective flairs/ categories by testing it with different Machine learning models, and further run data analysis on the scrapped data based on suitable queries.


# Objective 0 (Completed)

To scrape data from r/india, this was made possible with the help of PRAW (Python reddit API wrapper) library which lets to scrape any public data with the help of Reddit's official API, you require an OAuth key in order to use PRAW and Reddit API.[1]
After completion of this step, I was able to gather data for 12 different flairs, 100 posts(rows of data) for each flair. 
These 8 categories of data was analyized: 1. Title, 2. ID, 3. Flair, 4. Author/Creator of post, 5. URL, 6. No. of Comments, 7. Score(Total score after all Upvotes/ Downvotes on the post), 8. Timestamp(Date and Time in UTC). 

Official documentation for PRAW can be found at: https://praw.readthedocs.io/en/latest/

1. The data was scrapped from r/india with respect to each flair.
2. The data was sorted and stored into 'Data.csv'
3. Data was cleaned with the help of re(A python library) to clean Bad symbols and stopwords from the Title and finally saved as 'Final_formatted_data.csv' 
    To learn how work with re : https://docs.python.org/3/library/re.html
    
4.(Pending) Stored the .csv data file into MongoDB instance (.csv -> .bson)


# Objective 1 (Completed)

Training different models with the help of Scikit-learn python library. https://scikit-learn.org/stable/index.html#
(12 * 100)Rows of data trained using the following four models from the the Scikit-learn library.

**Text based classification models**
1. Naive Bayse Classifier
2. Linear Logistic Regression
3. Linear SVM
4. Random Forest

**This data was trained using**

***Independent Variable***
Flair

***Dependent Variables***
1. Title
2. URL
3. Grouped Features: Title + URL

***Best Model:*** **53.33%** Accuracy using Linear SVM taking Title + URL as feature.

*Observation :* This accuracy can be improved if more data such as Body of post and Top comments are also combined to train for classification. 

# Objective 2 (Pending)

Deploying ML model with maximum accuracy in form a Web-App using Heroku. 

..To be completed


# Objective 3 (Completed - Can be improved)

Data Analysis on collected data. 

1. Out of all posts, how many were created by unique users. 
2. Scatter plot to visualize scores gathered by each flair's posts.
3. Scatter plot to visualize number of comments gathered by each flair's posts.


# External resources used. 

- [1]Articles on how to use PRAW to scrape data:
  - https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
  - https://towardsdatascience.com/scraping-reddit-with-praw-76efc1d1e1d9
  - http://www.storybench.org/how-to-scrape-reddit-with-python/
  - Official PRAW documentation linked above.
  
- Guides on using Scikit Learn for text based classification:
  - Scikit-learn official documentation
  - https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
  
- Data Analysis:
  - https://seaborn.pydata.org/tutorial/categorical.html#categorical-tutorial
  - https://towardsdatascience.com/a-guide-to-pandas-and-matplotlib-for-data-exploration-56fad95f951c
