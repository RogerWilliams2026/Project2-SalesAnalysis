# What Generative AI Was Used For

Throughout this project from time to time Generative AI was used to help in certain situations, where no amount of critical
thinking, pondering or the consumption of thinking biscuits could provide an answer.

This document highlights the areas where Generative AI was used and what it was used for, by providing a "before" and "after" showing what the issue was and what Genertive AI propsed, or the original code and the suggested replacement.

**Scenario One:**

Needed to create a new column (StoreType) in dfSales_Stores_DataSet_Work
So for science decided to see what Copilot could suggest.

Gave Copilot this instruction:

_Create column: StoreType as integer mapped from existing Type column_  
_i.e. have 1, 2, 3 values instead of Type columns values A, B, C_

Copilot responded with:

_type_mapping = {"A": 1, "B": 2, "C": 3}_
_dfSales_Stores_DataSet_Work["StoreType"] = dfSales_Stores_DataSet_Work["Type"].map(type_mapping).astype("int64")_

_dfSales_Stores_DataSet_Work.head()_

Viable as Type column only has A, B, C values. Why no proper naming conventions Copilot?

**Scenario Two:**

Needed to replace missing values for markdown columns with zero, dfSales_Features_DataSet_Work so for science asked Copilot for the answer and compared it with my own solution.

Copilot responded with:

markdown_cols = ["MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5"]

dfSales_Features_DataSet_Work[markdown_cols] = dfSales_Features_DataSet_Work[markdown_cols].fillna(0)
dfSales_Features_DataSet_Work[markdown_cols].isna().sum()

Works well, mine was a tad conveluted.

**Scenario Three:**

Noticed negative values in MarkDown columns for dfSales_Features_DataSet_Work

Not being entirely sure what "markdown" actually means typed this into chatGPT:

_In sales what is a markdown and how can it be negative?_

chatGPT responded with:

_In sales and retail, a markdown is a reduction in the selling price of a product, usually to encourage sales. For example:_

_Original price: £100_
_Markdown: £20_
_New selling price: £80_

_A markdown is different from a discount in some businesses. A discount is often a temporary promotional reduction at the point of sale, while a markdown is a permanent reduction in the item's listed price._

_How can a markdown be negative?_

_A negative markdown usually means the price has increased, not decreased. This can happen in retail \_reporting or sales systems where markdowns are stored as the difference between the original and current price._

_For example:_

_\*Original Price Current Price Markdown_
_\*£100 £80 +£20 (price reduced)_
_£100 £110 −£10 (price increased)_

_Reasons for a negative markdown include:_

_A pricing error was corrected and the price was raised._
_A temporary promotion ended and the item returned to a higher price._
_The business decided to increase the price due to demand or costs._
_A data or system adjustment reversed a previous markdown._
_In reporting_

_Some companies calculate markdown as:_

_Markdown = Original Price − Current Price_

_With this formula:_

_Positive result = price reduction._
_Negative result = price increase._

_Other companies use the opposite formula:_

_Price Change = Current Price − Original Price_

_In that case:_

_Positive result = price increase._
_Negative result = price reduction._

_So if you see a negative markdown on a report, it's worth checking how that specific system defines the \_metric. In many retail systems, it simply indicates that the current selling price is higher than the reference price._

That explains that nicely will help greatly with the analysis and interpretation of the data.

**Scenario Four:**

Discovered when saving the cleaned DataFrames to CSV, if it contained a date column even if it was formatted as datetime with string format of %d/%m/%Y, when saved to CSV it would be saved in American format of %m/%d/%Y!!

Typed this into chatGPT:

_in python pandas converted a str column to date and formatted using:
dfSales_DataSet_Work["Date"] = pd.to_datetime(dfSales_DataSet_Work["Date"], format="%d/%m/%Y")
However saving the dataframe to CSV it writes the Date column in format yyyy/mm/dd?_

chatGPT responded with:

_This is expected behavior. When you convert the column
you are not storing a formatted date string. You are converting the column to pandas' internal datetime64 type._
_Pandas stores dates internally without a display format. When you save to CSV, pandas uses its default representation_

Amended my code to so it had index and date_format in the CSV save command e.g:  
dfCleaned.to_csv(strCurrentDir + CNST_STR_CLEANFILEPATH,index=False, date_format="%d/%m/%Y"

**Scenario Five:**

First visualisation. Was not happy with the x axis as there is no indicator BETWEEN the x axis values
to show the reader (analyst) what the values are between the x axis values. So asked chatGPT for a solution with this mighty question:

in python matplotlib when a scatter plot is created the x axis markers for values could be 0, 20, 40, 60, 80 is there anyway to get some visual mark on the x axis the values BETWEEN the numbers i.e. a marker for every 2 values a crude ASCII based example:  
0-------20  
| | | | | | | | |

chatGPT responded with:

_Yes. In Matplotlib, what you want is called minor ticks. You can add smaller tick marks between the major ticks (0, 20, 40, …) using MultipleLocator._

_import matplotlib.pyplot as plt_
_from matplotlib.ticker import MultipleLocator_

_x = [0, 10, 25, 40, 60, 80]_
_y = [5, 12, 7, 20, 15, 25]_

_fig, ax = plt.subplots()_

_ax.scatter(x, y)_

_# Major ticks every 20 units_
_ax.xaxis.set_major_locator(MultipleLocator(20))_

_# Minor ticks every 2 units_
_ax.xaxis.set_minor_locator(MultipleLocator(2))_

_# Make minor tick marks visible_
_ax.tick_params(axis='x', which='minor', length=4)_
_ax.tick_params(axis='x', which='major', length=8)_

_plt.show()_

Heavily modfiied the code idea to fit the project.

**Scenario Six:**

When trying to visualise plots with plotly.express could not find a way to get imtermediate ticks between the x axis values. So asked chatGPT for a solution with this question:

_python plotly.express create plot with this code_
_px.scatter(dfSales_Combined_DataSet, x="Temperature", y="Weekly_Sales",
title="Sales vs Temperature", color="Temperature", opacity=0.5)_
_how can I get ticks across both axes?_

chatGPT responded with:

_I think I understand. You're looking for minor ticks between the major tick marks (e.g. if the x-axis labels are 0, 20, 40, you'd like small tick marks at 10, 30, etc.)._

_Unfortunately, Plotly Express doesn't display minor ticks by default, and dtick only changes the major tick spacing—it doesn't add intermediate ticks._

_If you're using Plotly 5.8+, you can enable minor ticks:_

_fig.update_xaxes(_
_ ticks="outside",_
_ minor=dict(_
_ ticks="outside",_
_ ticklen=4,_
_ showgrid=False_
_ )_
_)_

_fig.update_yaxes(_
_ ticks="outside",_
_ minor=dict(_
_ ticks="outside",_
_ ticklen=4,_
_ showgrid=False_
_ )_
_)_

Copied it and used it!

**Scenario Seven:**

Attempting to create a sunburst plot to drill down and show stores and allow user to drill down into the departments and see their weekly sales. After many attempts could not get it to work. So asked chatGPT for a solution, decided not to include my malfunctioning code in case it skewed the result i.e. I was going in the wrong direction and chatGPT makes a poor solution work!

_So asked chatGPT this question:_

_I am doing a python pandas plotly based project which consists of 3 csv files:_

_stores data-set.csv_
_sales data-set.csv_
_features data set.csv_

_first csv file columns_
_Store,Type,Size_
_Second csv file columns_
_Store,Dept,Date,Weekly_Sales,IsHoliday_

_Third csv file columns_
_Store,Date,Temperature,Fuel_Price,MarkDown1,MarkDown2,MarkDown3,MarkDown4,MarkDown5,CPI,Unemployment,IsHoliday_

_I am attempting to create an interactive plotly plot with some sort of "drilldown" but i do not know how to do it, any suggestions?_

It replied with a lot of code examples but the most important part was this:

_With your three CSV files, you have a classic hierarchical retail analytics dataset, which is a good fit for a Plotly "drilldown" style dashboard. Plotly itself does not have a native drilldown chart like some BI tools (Power BI/Tableau), but you can create the same experience using interactive filters, dropdowns, click events, and linked charts._

I asked:

_How can I visualise the data as a sunburst plot?_

It replied with a lot of code these were the most relevant sections:

_import pandas as pd_
_import plotly.express as px_

_# Load data_
_stores = pd.read_csv("stores data-set.csv")_
_sales = pd.read_csv("sales data-set.csv")_

_# Merge store information_
_df = sales.merge(_
_ stores,_
_ on="Store",_
_ how="left"_
_)_

_# Aggregate sales by Store and Department_
_sunburst_data = (_
_ df.groupby(["Store", "Dept"], as_index=False)_
_ ["WeeklySales"]_
_ .sum()_
_)_

_sunburst_data.head()_

_sunburst_data = (_
_ df.groupby(_
_ ["Type", "Store", "Dept"],_
_ as_index=False_
_ )_
_ ["WeeklySales"]_
_ .sum()_
_)_

_fig = px.sunburst(_
_ sunburst_data,_
_ path=["Type", "Store", "Dept"],_
_ values="WeeklySales",_
_ title="Store Type → Store → Department Sales"_
_)_

_fig.show()_

This code was heavily modified to fit naming conventions and how I needed the plot to look.
