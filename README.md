# Project 2 - Sales Analysis

Project is a data analysis project that sales data to answer business questions and validate hypotheses. The project involves data cleaning, transformation, and visualisation using Python and various libraries.

Uses Project 1 and enhances upon it with advanced EDA and machine learning, new hypothesis are clearly noted

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Dataset Content

Dataset package given by customer contains 3 related raw CSV files:

- Sales_Stores_DataSet.csv
- Sales_Features_DataSet.csv
- Sales_DataSet.csv

These shall be renamed so they follow a naming convention, then cleaned and transformed into  
3 cleaned CSV files, then combined into a single CSV file for visualisation.

**Project Folder Structure:**

Subfolders:

assets:  
&nbsp;&nbsp;&nbsp;&nbsp;csv/Data <- Contains csv files during processing from raw to visualisation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CleanedFiles <- Contains cleaned data as csv files  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ExtractedFiles <- Contains files extracted from ZIP files  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OriginalFiles <- Contains the original data csv files  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VisualisationFiles <- Contains a combined csv file for visualisation  
&nbsp;&nbsp;&nbsp;&nbsp;pipelines - machine learning pipelines  
&nbsp;&nbsp;&nbsp;&nbsp;python_files  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains my custom modules  
documents <- Contains files:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What_AI_Used_For.md (terrible grammar)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Project 2 Sales Analysis Dashboard Design.pdf  
jupyter_notebooks <- Contains the Jupyter Notebooks used for ETL/EDA/ML and Visualisation  
reports<- Contains the report for the project  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Images <- Contains images used in the report  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains file: AnalysisConclusion.mdwhich is the project report  
streamlit <- contains files needed for Heroku to show streamlit dashboard  
&nbsp;&nbsp;&nbsp;&nbsp;assets:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;css <- Contains file: style.css for streamlit  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;csv/Data <- Contains csv files for visualisation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pipelines - machine learning pipelines (copy from main project folder)

**Jupyter_Notebooks:**

There are separate notebooks for ETL on each csv file. This was done so I can make sure each csv file is processed correctly which is easier to debug in one small notebook than a huge notebook with all the csv files in.

**Notebook Files:**

- Notebook_EDA_Sales_DataSet.ipynb <- EDA for Sales_Combined_Dataset_Visualization.csv
- Notebook_ETL_Sales_Stores_DataSet.ipynb <- ETL for Sales_Stores_DataSet.csv
- Notebook_ETL_Sales_DataSet.ipynb <- ETL for Sales_DataSet.csv
- Notebook_ETL_Sales_Features_DataSet.ipynb <- ETL for Sales_Features_DataSet.csv
- Notebook_ETL_Sales_Combined_DataSet.ipynb <- Combines the 3 cleaned csv files into one for visualisation
- Notebook_ML.ipynb <- Contains the machine learning model for experimentation has own visualisations
- Notebook_Visualisations1.ipynb <- Contains the visualisations for the hypotheses
- Notebook_Visualisations2.ipynb <- Contains the visualisations for the new hypotheses

**Report File**

- AnalysisConclusion.md <- Contains the report for the visualisations this is the final report for the
  project and contains the analysis and conclusions for each hypothesis, _however_ the plots are represented as images in the report and are not interactive. The interactive plots are in the dashboard
  This is report is two fold, is a great metric as to whether I can convey analysis in retrospect to the data story and test my ability to create an understandable report!

**Documents:**

- What_AI_Used_For.md:

Describes in detail how I used AI to help with issues with the project.

- Project 2 Sales Analysis Dashboard Design.pdf:

Outlines the dashboard design ethos.

**KANBAN**

In GitHub there is a KANBAN project, that was used for project management.

**Dashboard**

The dashboard is available via Heroku at this URL:

https://project2-salesanalysis-6a151d5ce7f3.herokuapp.com/

**GitHub**

Project GitHub URL is:

https://github.com/RogerWilliams2026/Project2-SalesAnalysis.gi

### Using The Notebooks

In order to create the combined csv file and see the plots these notebooks need to be run in order from the Jupyter_notebooks folder:

- Notebook_ETL_Sales_DataSet.ipynb <- ETL for Sales_DataSet.csv
- Notebook_ETL_Sales_Stores_DataSet.ipynb <- ETL for Sales_Stores_DataSet.csv
- Notebook_ETL_Sales_Features_DataSet.ipynb <- ETL for Sales_Features_DataSet.csv
- Notebook_ETL_Sales_Combined_DataSet.ipynb <- Combines the 3 cleaned csv files into one for visualisation
- Notebook_EDA_Sales_DataSet.ipynb <- Contains the EDA for the combined csv file
- Notebook_ML.ipynb <- Contains the machine learning model for experimentation has own visualisations
- Notebook_Visualisations1.ipynb <- Contains the visualisations for the old hypotheses
- Notebook_Visualisations2.ipynb <- Contains the visualisations for the new hopthesis and ML

## Business Requirements

The customer requires insights into the performance of the business in key areas, including sales trends, store performance, and the impact of various factors on sales. The business is particularly interested in understanding how weather, holidays, store types, unemployement rates in
the store locations and store sizes affect sales and profitability.

Additionally, the business wants to explore the impact of markdowns on sales during holiday periods and a global sales trend prediction for 2013.

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
  Validation: Test with suitable plot comparing store departments to show correlation
- What are the top 10 stores in terms of profitability in the last 12 months?
  Validation: Test with suitable plot filtered by top 10 records sorted in sales value descending
- What are the bottom 10 stores in terms of profitability in the last 12 months?
  Validation: Test with suitable plot filtered by top 10 records sorted in sales value ascending
- What was the unemployment percentage per store by month for last year?
  Validation: Test with suitable plot filtered by top 10 records sorted in sales value
- What Was The Unemployment Percentage Per Store By Store Size Last Year?  
  Validation: Test with plot which can be viewed interactively to make data easier to grasp

Machine Learning Predictions:

- What are the predicted sales for stores by month for next year?
  Validation: Test with linear regression and random forest to determine best model for hypothesis

## Project Plan

- Acquire raw data as csv files from the customer
- Clean and transform the raw data into cleaned csv file
- Combine the cleaned csv files into a single csv file for visualisation
- Perform EDA to see if there are any correlations between the data and the hypotheses
- Visualise the data to validate the hypotheses and answer the business questions
  using multiple visualisation libraries to find best fit for the customer requirements
  as well as the best looking visualisations for clear insights into the data and choosing
  the most appropriate visualisation for the hypothesis being validated
- Use machine learning to predict sales for the next year and visualise the results
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
Chose sunburst plot to show the sales and individual markdowns per store during holiday periods as other types produced large confusing visualisations or cramped plots due to sheer amount of data.
Again felt an interactive approach lends itself better to this type of analysis.

**New Hypothesis:**

_Hypothesis 7: What are the most profitable departments per store in the last 12 months?_
Chose bar chart plot to show best selling department for each store. Due to the complexity of the request a
number of dataframes where needed to group the stores with departments then group by highest sales. The reason I
chose a bar chart was the ease of reading, a scatter would look complicated and a histogram with KDE might have
been confusing.

_Hypothesis 8: What are the top 10 stores in terms of profitability in the last 12 months?_
Chose a bar chart again because it is the easiest method to see differences between values in the data.

_Hypothesis 9: What are the bottom 10 stores in terms of profitability in the last 12 months_
Chose a bar chart again because it is the easiest method to see differences between values in the data.

_Hypothesis 10: What was the unemployment percentage per store by month for last year?_
Chose a line plot for this one. Easiest way to show the comparison between the values, used different colours
for each store which is tricky as there are 45!

_Hypothesis 11: What Was The Unemployment Percentage Per Store By Store Size Last Year?_  
Had a lot thinking to do with this one, a line might be jumbled, a bar plot out of the question for the fact that
need to see three different types of data, so chose a 3D scatter plot. Mainly because it clearly shows all three
data columns **and** it can be moved around by the user aided to understanding and creates insights a fixed 2D
plot cannot.

_Hypothesis 12: What are the predicted sales for stores by month for next year?_
This comprises of the same plot type: line but used four times. Why? Well first ran linear regression and random forest on the
data for the previous year in the data (data only has combined records for 2012, but the features csv has till July 2013(?).
Then plotted two charts from the results for comparison, then repeated the procedure but this time to predict all of 2013 values.
Found the line plot made comparison simpler, with a bit more experience I might be able to find a better chart type.

## Analysis techniques used

From the 3 csv files 4 more are created 3 via ETL and 1 via merging the 3 cleaned csv files all with
an applied naming convention:

- Sales_Stores_DataSet_Cleaned.csv
- Sales_Features_DataSet_Cleaned.csv
- Sales_DataSet_Cleaned.csv
- Sales_Combined.csv

For machine learning 4 pipelines are created:

- forest_regression_hypothesis12_pipeline.pkl
- forest_regression_hypothesis12_test_pipeline.pkl
- linear_regression_hypothesis12_pipeline.pkl
- linear_regression_hypothesis12_test_pipeline.pkl

Files with _test_ in the name are used to run test "prediction" by getting machine learning processes
to "predict" values for an existing year. This is used to compare with the previous year via a plot

The other files are used in machine learning to predict the next years values, again shown in a plot

**Methods Used:**

Generative AI tools were mostly used to solve code issues and occasionally for plotting ideas due to my lack of experience with visualisation libraries particularly the first sunburst plot as I was unsure if my approach was the correct one.

Data was a limiting factor, not in terms of detail but sheer volume and breadth. I was stumped with some hypothesis by the fact I was trying to analyse sales data with 45 stores each with 97 departments and was lacking experience to know what plots and strategies are best to use to visualise this type data.

Adapted with a "best guess Mr Sulu" approach to visualising large data, running plot tests to see what the libraries can handle and go beyond, bar, histogram and scatter plots which worked well, as I could now use more effective plot types but ran out of time to reimagine the plots.

Analysed plots compared to hypothesis, by checking expected values against queries with the raw data. If the dataset to use is corrupt or incorrect the plot will be useless.

Discovered the features data set.csv file has 7 months of date values not in the other csv files, so that needed to be filtered before creating the combined csv file, easily achieved via a left join.

Decided to use both linear regression and random forest for the machine learning experiments, nice broad range of models that can be used with the data.

## Libraries Used

The requirements.txt has the full list, but here is a list taken from the Jupyter notebooks:

joblib  
matplotlib.pyplot  
matplotlib.ticker.
nbformat  
numpy  
os  
pandas  
pathlib  
plotly.express  
scipy.stats  
seaborn  
sklearn.compose  
sklearn.ensemble  
sklearn.impute  
sklearn.linear_model  
sklearn.metrics  
sklearn.model_selection  
sklearn.pipeline  
sklearn.preprocessing  
sklearn.tree  
statsmodels.api  
statsmodels.formula.api  
sys

Also included my own libraries:

modGlobal  
modETL_Library

The streamlit application uses these:

joblib  
matplotlib.pyplot  
matplotlib.ticker  
nbformat  
numpy  
pandas  
pathlib  
plotly.express  
scipy.stats  
seaborn  
streamlit

## Development Roadmap

### Basic Strategy:

- Get data into DataFrames and perform ETL using my custom library where possible
- Create cleaned csv files for each of the 3 raw csv files
- Merge the 3 cleaned csv files into a single csv file for visualisation
- Perform exploratory EDA to see if there are any correlations between the data and the hypotheses
- Visualise the data using all of the available plot libraries (where possible) to see which provide the
  best plot for the hypothesis I am testing. Then if have the time try and expand and develop them further
- Get data into a machine learning model for at least one hypothesis, choose example that could not achieved _without_ machine learning
- Choose best plots for each hypothesis (where there is a choice) to use in findings report
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
- Had a strange issue with streamlit not accepting / at the start of a path, then discovered the ML routines
  for saving pipelines and plots did not either but python did!(??)
- One major challenge was VS Code. When run with Jupyter notebooks **and** a virtual environment it quickly
  became as stable as a jelly on a JCB! Frequent kernel locks where it would say it was starting the kernel
  but never did, which meant having to close and re-open VS Code which usually meant the kernel would lock
  again, so **another** restart was required, then it would not respond to run command so **another** restart was
  required then it would run. Things quickly became exacerbated if _any_ change was made to a module as
  the Jupyter notebook would run _the old code_ which meant - yep restart the kernel...
  Usually I was restarting VS Code 12-20 times a development day. if virtual environments are not used it
  works fine!
- Machine learning was made a lot harder by the fact that the data worth using for it was continuous data!
  In particular date ranges, which had not been covered in the course in the way a lot of business requests would require
  such as sales per quarter. Would be cool if course had an example of machine learning using financial year data
  as I suspect this could be another common request. So I went to StackOverflow to get some basic code structure
  to get the data, which I faffed and fettled into what it is now, but I feel there is much room for improvement
- Markdown markup langauge is irritating in that need to but two spaces at the end of line just to get it to keeps lines seperate and most annoying of all it has no capactity for indenting!

## New Skills and Tools

- Generative AI tools (Copilot and chatGPT) helped hugely with strange library issues and code snippets
  and the generation of the first sunburst plot
- Learned about project management, and effective timeboxing for project sections e.g. documentation as
  well as the composite
- Discovered I preferred plotly as a visualisation tool due to its better appearence and options
- Some nice EDA skills and better ways to "know the data" than merely .shape/.describe etc. such as:
  Q-Q plots and the great eye opener the Parametric tests
- More plot skills, such as using sunbursts for drill-downs and finally found a use for my favourite plot
  the 3D scatter! In the LMS examples it was largely cosmetic and difficult to read but I found a hypothesis
  I had was the perfect fit, and it shows how can be more than a gimmick plot and actually show data in a
  way that would take many, many words to achieve
- Also got confident it applying lots of differing EDA styles to analyse columns and potential correlations
- Got quite handy with streamlit. Being familiar with HTML helped a lot for example I think of containers
  as HTML DIVs, and KEY as HTML ID
- Finally tamed MarkDown so I could add images using relative addressing, before it pretended to do it, then
  when MarkDown was previewed would _copy_ the image to the _root_ folder with a generic name and use that!
- Better understanding of how to look at raw data and see patterns and formulate hypothesis from them
- More confidence with plot type choice, now happy to experiment with newer chart types like sunbursts

## Who Won The Generative AI Battle?

chatGPT won hands down, I found Copilot in VS Code largely irritating and invasive, and it was not very good at solving code issues a bit of a mixed bag. chatGPT on the other hand was very good at solving code issues and providing code snippets that worked first time. When I went of the rails and without knowing it and was using the wrong approach to visualising one hypothesis. Copilot's suggested plot was cramped, difficult to read and (as I discovered) the wrong plot type for the data.

Posted the code into chatGPT and over an hour it honed and rehoned the code to a 92% working solution with a better type of plot. Due to the massive size of the data it caused many rendering issues such as a huge gap between the plot title and the first actual plot and missing x axis labels.

Which of course after a good nights sleep I realised _I_ was using the wrong plot _and_ data visualisation concept and looking at the data visualisation backwards!

Did notice as time has gone by CoPilot in VS Code is making a lot more mistakes, might be better off if Microsoft concentrated on making
an expert system version instead...

## Things To Learn Next

- Proper use of KANBAN for project management (there s a rumour it supports sprints..)
- Better understanding of the plotly.express library and its options for visualisation
- Better understanding interactive plots and how determine which is best for the data being visualised
- More practice with machine learning, particularly with categorical data and dates

## Unfixed Bugs and Things To Improve

- Had strange issue with first plot in hypothesis 3, where it puts: 1e9 in the top left corner of the
  pyplot plot. No idea why. Will have a look if there is a solution if I have time does not affect plot data.
- Uniformity regardling currency symbols in plots!
- streamlit likes making sure containers cannot fill entire height of the screen, there is a good inch left
  it will not let me use with a single container so put two others in to fill the gap!
- streamlit likes having narrow scrollbars which can make scrolling difficult
- 3D scatter chart is too big in streamlit but if I adjust the size it cuts off some X axis values and does not show a scroll bar
- Would like to see if I can get the ML feature engineering into the pipeline, getting the ML to work took such a long time I didn't
  get the chance to try it!
- Need more date data, for some reason while the csv files contain thousands of records, the date range for the first two ends at
  26/10/2012 (!) and the 3rd in July 2013 (?). Discovered this too late to hunt around for another dataset..

## Credits

- chatGPT really good for solving issues so far everything suggested worked!
- StackOverlfow what a machine did not know these people did!

## Acknowledgements (optional)

- Thank the people who supported this project and didn't laugh too loud at the speeling mistooks
