# Project 2 - Sales Analysis

Project s a data analysis project that sales data to answer business questions and validate hypotheses. The project involves data cleaning, transformation, and visualisation using Python and various libraries.

Uses Project 1 and enchances upon it with advanced EDA and machine learning

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content

Dataset package given by customer contains 3 related raw CSV files:

- Sales_Stores_DataSet.csv
- Sales_Features_DataSet.csv
- Sales_DataSet.csv

These shall be renamed so they follow a naming convention, then cleaned and transformed into   
3 cleaned CSV files, then combined into a single CSV file for visualisation.

**Project Folder Structure:**

- assets <- No files stored here is container folder for project notebooks etc

Subfolders:  
- css <- Contains file: style.css for streamlit
- csv <- Contains csv files during processing from raw to visualisation
  Subfolders:
  - CleanedFiles <- Contains cleaned data as csv files
  - ExtractedFiles <- Contains files extracted from ZIP files
  - OriginalFiles <- Contains the original data csv files
  - VisualisationFiles <- Contains a combined csv file for visualisation
- documents <- Contains files: 
  - What_AI_Used_For.md (terrible grammar)  
  - Project 2 Sales Analysis Dashboard Design.pdf 
- jupyter_notebooks <- Contains the Jupyter Notebooks used for ETL and Visualisation  
- Report <- Contains the report for the project
- Report/Images <- Contains images used in the report and all plot images
- streamlit <- contains files needed for Heroku to show streamlit dashboard

**Jupyter_Notebooks:**

There are separate notebooks for ETL on each csv file. THis was done so I can make sure each csv file is processed correctly which is easier to debug in one small notebook than a huge notebook with all the csv files in.

**Notebook Files:**

- Notebook_EDA_Sales_DataSet.ipynb <- EDA for Sales_Combined_Dataset_Visualization.csv
- Notebook_ETL_Sales_Stores_DataSet.ipynb <- ETL for Sales_Stores_DataSet.csv
- Notebook_ETL_Sales_DataSet.ipynb <- ETL for Sales_DataSet.csv
- Notebook_ETL_Sales_Features_DataSet.ipynb <- ETL for Sales_Features_DataSet.csv
- Notebook_ETL_Sales_Combined_DataSet.ipynb <- Combines the 3 cleaned csv files into one for visualisation
- Notebook_Visualisations1.ipynb <- Contains the visualisations for the hypotheses
- Notebook_Visualisations2.ipynb <- Contains the visualisations for the new hypotheses


**Report File**

- AnalysisConclusion.md <- Contains the reports for the visualisations this is the final report for the
  project and contains the analysis and conclusions for each hypothesis, _however_ the plots are represented as images in the report and are not interactive. The interactive plots can be found in the Notebook_Visualisations.ipynb notebook.
  This is report is two fold, is a great metric as to whether I can convey analysis in retrospect to the data story and test my ability to create an understandable report!

**Documents:**

What_AI_Used_For.md:

Describes in detail how I used AI to help with issues with the project.

### Using The Notebooks

In order to create the combined csv file and see the plots these notebooks need to be run in order from the Jupyter_notebooks folder:

- Notebook_ETL_Sales_DataSet.ipynb <- ETL for Sales_DataSet.csv
- Notebook_ETL_Sales_Stores_DataSet.ipynb <- ETL for Sales_Stores_DataSet.csv
- Notebook_ETL_Sales_Features_DataSet.ipynb <- ETL for Sales_Features_DataSet.csv
- Notebook_ETL_Sales_Combined_DataSet.ipynb <- Combines the 3 cleaned csv files into one for visualisation
- Notebook EDA_Sales_DataSet.ipynb <- Contains the EDA for the combined csv file
- Notebook_ML.ipynb <- Contains the machine learning model for experimentation has own visualisations
- Notebook_Visualisations1.ipynb <- Contains the visualisations for the old hypotheses
- Notebook_Visualisations2.ipynb <- Contains the visualisations for the new hopthesis and ML

To see the final report run the following notebook from the Report folder:

- Notebook_Reports.ipynb <- Contains the reports for the visualisations

## Business Requirements

The customer requires insights into the performance of the business in key areas, including sales trends, store performance, and the impact of various factors on sales. The business is particularly interested in understanding how weather, holidays, store types, and store sizes affect sales and profitability.

Additionally, the business wants to explore the impact of markdowns on sales during holiday periods.

It is a requirement that all analysis is done based on the last 12 months of data, and that the findings are presented in a clear and concise manner.

The business hopes this information will help it plan its store growth and marketing strategies to maximise profits in the areas that are shown to be profitable, but also focus on improvement for the stores that are not performing well.

## Hypothesis and How To Validate?

- Are sales increased if weather is hotter or colder in the last 12 months?
  Validation: Test with a suitable plot to show temperature and sales correlation.
- Sales differences between holiday and non-holiday weeks per store in the last 12 months
  Validation: Compare sales using statistical analysis and visualisation techniques.
- What is most profitable store type in the last 12 months?
  Validation: Compare store types with weekly sales.
- Does store size affect profitability? If so, how much in the last 12 months?
  Validation: Compare store size with weekly sales
- What are the Weekly Sales by Store, Store Type and Department Last 12 Months?
  Validation: Compare weekly sales by store and department using appropriate plot
- What is the impact of markdowns on sales during holiday periods in the last 12 months by store?
  Validation: Accumulate and visualise markdown data per store during holiday periods

**New Hypothesis:**

- What are the most profitable departments per store in the last 12 months?
- What are the top 10 stores in terms of profitability in the last 12 months?
- What are the bottom 10 stores in terms of profitability in the last 12 months?
- What are the predicted sales for store type A for next year?
- What are the predicted sales for stores in areas of high unemployment for next year?

## Project Plan

- Acquire raw data as csv files from the customer
- Clean and transform the raw data into cleaned csv file
- Combine the cleaned csv files into a single csv file for visualisation
- Visualise the data to validate the hypotheses and answer the business questions
  using multiple visualisation libraries to find best fit for the customer requirements
  as well as the best looking visualisations for clear insights into the data and choosing
  the most appropriate visualisation for the hypothesis being validated
- Create a report to present the findings to the customer

## The Rationale Used To Map The Business Requirements To The Data Visualisations

_Hypothesis 1: Are sales increased if weather is hotter or colder in the last 12 months?_
Chose scatter plot to show the correlation between temperature and sales. Due to the large amount of data, a scatter plot is the best way to visualise the data and show the correlation.

_Hypothesis 2: Sales differences between holiday and non-holiday weeks per store in the last 12 months_
Chose boxplot to show the sales differences between holiday and non-holiday weeks per store as it seems the best way to visualise the data and show the differences between the two groups.

_Hypothesis 3: What is most profitable store type in the last 12 months?_
Chose bar plot to show the sales differences between store types. As provides a simple easy to read visualisation of the data.

_Hypothesis 4: Does store size affect profitability? If so, how much in the last 12 months?_
Chose scatter plot to show the correlation between store size and sales. Due to the large amount of data, a scatter plot is the best way to visualise the data and show the correlation without causing the plot render engine to crash!

_Hypothesis 5: Weekly Sales by Store, Store Type and Department Last 12 Months_
Chose sunburst plot to allow the viewer to drill down into the data and see the individual departments weekly sales per store. Other types produced large confusing visualisations or cramped plots due to sheer amount of data.
Felt an interactive approach lends itself better to this type of analysis, and adds a "hands on" approach to data visualisation.

_Hypothesis 6: Impact of markdowns on sales during holiday periods in the last 12 months by store_
Chose sunburst plot to show the sales and indiviudal markdowns per store during holiday periods as other types produced large confusing visualisations or cramped plots due to sheer amount of data.
Again felt an interactive approach lends itself better to this type of analysis.



## Analysis techniques used

From the 3 csv files 4 more are created 3 via ETL and 1 via merging the 3 cleaned csv files all with
an applied naming convention:

- Sales_Stores_DataSet_Cleaned.csv
- Sales_Features_DataSet_Cleaned.csv
- Sales_DataSet_Cleaned.csv
- Sales_Combined.csv

**Methods Used:**

Generative AI tools were mostly used to solve code issues and occasionaly for plotting ideas due to my lack of exerience with visualisation libraries particularly the first sunburst plot as I was unsure if my approach was the correct one.

Data was a limiting factor, not in terms of detail but sheer volume and breadth. I was stumped with some hypothesis by the fact I was trying to analyse sales data with 45 stores each with 97 departments and was lacking experience to know what plots and strategies are best to use to visualise this type data.

Adapted with a "best guess Mr Sulu" approach to visualising large data, running plot tests to see what the libraries can handle and go beyond, bar, histogram and scatter plots which worked well, as I could
now use more effective plot types but ran out of time to reimagine the plots.

Analysed plots compared to hypothesis, by checking expected values against queries with the raw data. If the dataset to use is corrupt or incorrect the plot will be useless.

For example the features data set.csv file has 7 months of date values not in sales data-set.csv, so that needed to be filtered before creating the combined csv file.

## Libraries Used

import os
import numpy
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import pathlib
import scipy.stats as stats
import matplotlib.pyplot as plt
import nbformat
from matplotlib.ticker import MultipleLocator
import seaborn as sns

#added by me for visualisation fine tuning
from matplotlib.ticker import MultipleLocator

#added by me for plotly.express visualisation issue
import nbformat
#for ML experiments
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
accuracy_score, confusion_matrix, ConfusionMatrixDisplay,
precision_score, recall_score, f1_score,
roc_auc_score, roc_curve, classification_report,
)
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as smf
import numpy as np
import joblib

#import user created modules
#below solution provided by chatGPT
from assets.python_files.modGlobal import modGlobal
from assets.python_files.modETL_Library import modETL

## Development Roadmap

### Basic Strategy:

- Get data into DataFrames and perform ETL
- Create cleaned csv files for each of the 3 raw csv files
- Merge the 3 cleaned csv files into a single csv file for visualisation
- Visualise the data using all of the available plot libraries (where possible) to see which provide the
  best plot for the hypothesis I am testing. Then if have the time try and expand and develop them further. Would be sweet to get some 3D plots in..
- Choose best plots for each hypothesis to use in findings report
- Populate findings report with plots and analysis for each hypothesis and submit to customer

### Challenges and Strategies

- installing dependencies from requirements.txt file produced error:  
  ModuleNotFoundError: No module named 'pkg_resources'  
  So had to install dependencies manually using pip install <package_name>.
  THEN after checking with course fascilitator needed to remove ppscore from the requirements.txt file
  This produced another error which I tracked down to being ydata-profiling so removed that as well
  Re-installed dependancies from the requirements.txt file - works fine.
- The project tempplate has Python code to change the working directory. On my machine it stayed in the
  notebook sub folder, so after some insightful help from StackOverFlow I crafted a working solution
- VS Code repeatedly has a kernel hang randomly during development requiring restarting VS Code  
  as kernel restart rarely fixes the issue.
- First hypothesis raised an unexpected issue as some plot types would not render due to the data size!
  bar plots particularly fell at the first fence. Pity as that would have looked cool...
  Developer ignorance perhaps??
- Trying to visualise plots with plotly.express produced an error stating nbformat was not installed.  
  Used pip install nbformat and added to dependencies in Notebook_Visualisations.ipynb to fix the issue
- Decided to use an ETL library I had created but could not get python to import it so had to resort to chatGPT  
  to get the methodology to use it! 


## New Skills and Tools

- Generative AI tools (Copilot and chatGPT) helped hugely with strange library issues and code snippets
  and the generation of the first sunburst plot
- Learned about project management, and effective timeboxing for project sections e.g. documentation
- Discovered I preferred plotly as a visualisation tool due to its better appearence and options

## Who Won The Generative AI Battle?

chatGPT won hands down, I found Copilot in VS Code largely irritating and invasive, and it was not very good at solving code issues a bit of a mixed bag. chatGPT on the other hand was very good at solving code issues and providing code snippets that worked first time. When I went of the rails and without knowing it and was using the wrong approach to visualising one hypothesis. Copilot's suggested plot was cramped, difficult to read and (as I discovered) the wrong plot type for the data.

Posted the code into chatGPT and over an hour it honed and rehoned the code to a 92% working solution with a better type of plot. Due to the massive size of the data it caused many rendering issues such as a huge gap between the plot title and the first actual plot and missing x axis labels.

Which of course after a good nights sleep I realised _I_ was using the wrong plot _and_ data visualisationconcept and looking at the data visualisation backwards!

## Things To Learn Next

- Proper use of KANBAN for project management
- How to dynamically create ranges for subplots e.g. stores 1 to 9
- Better understanding of the plotly.express library and its options for visualisation
- Better understanding interactive plots and how determine which is best for the data being visualised
- Better understanding of how look at a raw csv file and know how to determine what hypothesis can be
  achieved with it.

## Main Data Analysis Libraries (Mandatory For Project Use Of Visualisation)

- numpy
- pandas
- plotly.express
- seaborn
- matplotlib.pyplot

### Others Added By Me

- from matplotlib.ticker import MultipleLocator <- for "ticks" between axis values
- import nbformat <- added by me for plotly.express visualisation issue
- os <- for directory routines

## Unfixed Bugs and Things To Improve

- Had strange issue with first plot in hypothesis 3, where it puts: 1e9 in the top left corner of the
  pyplot plot. No idea why. Will have a look if there is a solution if I have time does not affect plot data.
- Uniformity regardling currency symbols in plots!
- When adding images into the report markdown file VS Code creates a copy and puts it into the same
  folder Must discover if it is possible to use relative paths to stop it duplicating images and putting them into the wrong folder!

## Credits

- chatGPT really good for solving issues so far everything suggested worked!

## Acknowledgements (optional)

- Thank the people who supported this project.
