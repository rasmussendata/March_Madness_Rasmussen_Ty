# March_Madness_Rasmussen_Ty
## Data Analytics Capstone Project, includes data for 22 years of march madness data, scripts in Python, SQL and more. 


# Data Cleaning & ETL steps

## Data extraction/original source

Kaggle provided me with two valuable databases, one of them has data between 2002 to 2025 and the other from 2008 to 2025. The first one with more years has mostly all KenPom data, which is rankings such as offense and defense throughout the year and the other one has many more statistical data such as shooting splits. I will be using both datasets by merging them on the keys of team name and season. 
(Link: https://www.kaggle.com/datasets/jonathanpilafas/2024-march-madness-statistical-analysis?select=REF+_+Post-Season+Tournament+Teams.csv)




My initial problem that I am trying to solve with the data is what factors or rankings have the biggest effect on basketball teams and their success in the tournament. This will be done with feature analysis and supervised machine learning to find correlated columns with winning the tournament. 
I might also derive new columns that show success other than just winning the tournament or not. 


The first dataset that contains data from 2002 contains 13 tables and 357 total columns. The one that’s from 2008 contains 34 tables and 1,054 total columns. There appears to be very little missing data and good quality data to begin with which is great for our analysis. Most of the data is numeric with a few text columns which is great for the modeling as there will not need to be a ton of one-hot encoding. 


I think that this data provides enough features required for future steps and also enough simple overview statistics for exploratory data analysis. The numeric data fields can be used as features and the ‘won championship’ field can be used as the response variable with one-hot encoding. Overall, the data seems well suited for the main purpose of this project. 

## Initial Cleaning

For this project, data cleaning took longer than expected but it is crucial that the time is spent so the analysis will only include quality data and relevant data. Revisions were made first, to keep only relevant data after all of the merges. For instance, there were duplicated columns that ended in _y or _x. One side of the columns must be dropped as they do not add any value. Some of the columns had many missing rows, however these were values such as ‘Tournament winner’ which makes sense, as only one team can win the tournament each year. Certain data such as seed do not bring value to the main goal of predicting playoff success so they can be removed. These also include miscellaneous data like ‘SFpts’ that do not provide data. 
For any of the statistical variables that do add value they will not be left missing. Instead, since most of them have 855 missing rows out of 16,205, the missing values will be imputed with the median value for the given column. There was a second dataset that had similar data but a wider range of years. However, after reviewing the dataset, there was a high proportion of missing data, redundant and irrelevant data so I decided to not use this one anymore and move forward with the first reviewed dataset. 




## Main ETL Steps & Procedures

The main transformations conducted in the ETL step exist within multiple Python files. The order of the scripts in the project are; merge tables, data cleaning, validation, EDA and SQL prep. All of these steps are clearly labeled and repeatable, although some of the steps might bleed into other scripts when they become necessary. This showed me how iterable the data cleaning process is, and certain parts of it may need to be revised throughout. Before cleaning could be conducted, I knew that all of the data needed to be put in one dataframe to avoid having tens of tables all with similar data. To merge or join the tables, I used primary keys of team name and season. This time was also when I decided that some of the supplementary data was redundant and irrelevant so I decided to drop these files before analysis. The initial cleaning looked at what columns can be removed and decided what to do with missing values. Columns with a majority of missing data were removed, and numerical columns still remaining were imputed with the median value. Data validation included the majority of further analysis into data integrity issues. I found that multiple seasons had multiple tournament winners, which ignited the search to find out what is happening. It turns out there were two conference columns for a single team and season, one of which included many inaccurate values. The up-to-date conference field was kept, and the other was removed, which resolved the original data integrity issues. The last duplicate that needed to be addressed was there were two rows for the same team and season, one of which had the wrong tournament listed once. The number of duplicate values (using team name and year) were zero after this. 

To improve consistency for future steps and analyses, all of the columns were changed to a consistent format of underscores instead of spaces, and all lowercase characters. Also, for values such as ‘made final four’ and ‘tournament winner’, nulls are in place for false values (teams that did not meet the criteria). All null values were replaced with a simple “No” value and can be easily changed for any one-hot encoding in machine learning analysis. 


The biggest limitation noticed is data surrounding the 2024-25 season. There are statistics listed for every team in the 2025 March season, however there are no winners or final four teams listed. It is unsure if these statistics include the entirety of the season so they will not be used for any testing of the model. 



## Relational Database (SQL Server)


I decided to create a SQL database within SQL server 2019, to then transfer the data from the Python dataframe into the SQL database. The main transformations already took place in Python, due to the advanced features and automations that it offers. SQL is being used to host the data in a relational database to then be used for querying from Power BI and Tableau. 

A GitHub repository was created that includes all scripts for creating tables and importing the data from Python. 


For importing the cleaned data into SQL server, I used the import flat file feature in SQL, under the correct database. Then I selected the location of the csv file that I downloaded after the transformations and wrangling steps in Python. After checking the preview of the data (which formatted the table correctly) there were some errors. This was mostly due to incorrect data types for certain columns and columns that were not selected to allow null values that should be null. Once this was corrected, all of the data was imported into the staging database in one single table. The current data in the database has the granularity of one team per season per row. I also created a view in the database that selects a common question needed by stakeholders. 

