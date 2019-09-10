# PrecogRITask


# Reddit-Flair-Detector

This project was created in order to complete the coding task provided by Precog, a research group from IIIT Delhi which focuses on studying and analyzing different social groups or networks, be it online or offline. Their work can be found on http://precog.iiitd.edu.in/


# End Goal

To scrape data from r/india (A subreddit on https://reddit.com/) and classify posts into their respective flairs/ categories by testing it with differnt Machine learning models, and further run data analysis on the scrapped data based on suitable queries.


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

..To be completed.


# Objective 2 (Pending)

Deploying ML model with maximum accuracy in form a Web-App using Heroku. 

..To be completed


# Objective 3 (Ongoing)

Data Analysis on collected data. 

1. Highest score gathered by each flair. 
2. Top 10 highest users gathering most score based on their posts. 
3. 


# External resources used. 
1. Took help from two *Open-Sourced* projects with similar objectives.
    a. https://github.com/chandan21gupta/Reddit-Flair-Detector
    b. https://github.com/radonys/Reddit-Flair-Detector
  
2. Articles on how to use PRAW to scrape data. 
    a. https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
    b. https://towardsdatascience.com/scraping-reddit-with-praw-76efc1d1e1d9
    c. http://www.storybench.org/how-to-scrape-reddit-with-python/
    d. Official PRAW documentation linked above.
  
3. 
