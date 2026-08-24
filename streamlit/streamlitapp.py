
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import pathlib
import scipy.stats as stats
import matplotlib.pyplot as plt

#use custom module
# import modGlobal
# import modETL_Library as modETL
import nbformat
from matplotlib.ticker import MultipleLocator

#for experiment ML
# from sklearn.linear_model import LogisticRegression
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import (
#     accuracy_score, confusion_matrix, ConfusionMatrixDisplay,
#     precision_score, recall_score, f1_score,
#     roc_auc_score, roc_curve, classification_report,
# )
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# from sklearn.model_selection import train_test_split
# import statsmodels.formula.api as smf
import numpy as np

import joblib
#
#  Created 28/07/2026 By Roger Williams
#  
#  for temperature hypothesis
#  
#  uses global var dfTemperature for visualisations
#  
#

#VARS

#file paths
CNST_STR_LINEAR_PIPELINE_HYPOTHESIS12_TEST_STREAMLIT_PATH =  "assets/pipelines/linear_regression_hypothesis12_test_pipeline.pkl"
CNST_STR_FOREST_PIPELINE_HYPOTHESIS12_TEST_STREAMLIT_PATH = "assets/pipelines/randomforest_hypothesis12_test_pipeline.pkl"

CNST_STR_LINEAR_PIPELINE_HYPOTHESIS12_STREAMLIT_PATH =  "assets/pipelines/linear_regression_hypothesis12_pipeline.pkl"
CNST_STR_FOREST_PIPELINE_HYPOTHESIS12_STREAMLIT_PATH =  "assets/pipelines/randomforest_hypothesis12_pipeline.pkl"

CNST_STR_SALES_COMBINED_DATASET = "assets/csv/Data/Sales_Combined_DataSet_Visualisation.csv"
CNST_STR_FEATURES_DATASET = "assets/csv/Data/Features_DataSet_Visualisation.csv"
CNST_STR_SALES_DATASET = "assets/csv/Data/Sales_DataSet_Visualisation.csv"
CNST_STR_STORES_DATASET = "assets/csv/Data/Stores_DataSet_Visualisation.csv"


radRadioButtons = None

conContainerMain = None
conContainerTab1 = None
conContainerTab2 = None
conContainerTab3 = None
conContainerTab4 = None
conContainerTab5 = None
conContainerTab6 = None
conContainerTab7 = None
conContainerTab8 = None
conContainerTab9 = None
conContainerTab10 = None
conContainerTab11 = None
conContainerTab12 = None
conContainerTab13 = None

conContainerTab1_Sub = None
conContainerTab2_Sub = None
conContainerTab3_Sub = None
conContainerTab4_Sub = None
conContainerTab5_Sub = None
conContainerTab6_Sub = None
conContainerTab7_Sub = None
conContainerTab8_Sub = None
conContainerTab9_Sub = None
conContainerTab10_Sub = None
conContainerTab11_Sub = None
conContainerTab12_Sub = None
conContainerTab13_Sub = None

conSection1 = None
conSection2 = None
conSection3 = None
conSection4 = None
conSection5 = None
conSection6 = None

conSection1Title = None
conSection2Title = None
conSection3Title = None
conSection4Title = None
conSection5Title = None
conSection6Title = None

conSection1Tab = None
conSection2Tab = None
conSection3Tab = None
conSection4Tab = None
conSection5Tab = None
conSection6Tab = None
conSection7Tab = None
conSection8Tab = None


conOverview = None


expExpander1 = None
expExpander2 = None
expExpander3 = None
expExpander4 = None
expExpander5 = None
expExpander6 = None
expExpander7 = None
expExpander8 = None
expExpander9 = None
expExpander10 = None
expExpander11 = None
expExpander12 = None
expExpander13 = None
expExpander14 = None
expExpander15 = None
expExpander16 = None
expExpander17 = None
expExpander18 = None
expExpander19 = None
expExpander20 = None


col1Tab1 = None
col2Tab1 = None
col3Tab1 = None
col4Tab1 = None

col1Tab2 = None
col2Tab2 = None
col3Tab2 = None
col4Tab2 = None

col1Tab3 = None
col2Tab3 = None
col3Tab3 = None
col4Tab3 = None
col5Tab3 = None
col6Tab3 = None
col7Tab3 = None
col8Tab3 = None
col9Tab3 = None
col10Tab3 = None

col1Tab4 = None
col2Tab4 = None
col3Tab4 = None
col4Tab4 = None

col1Tab5 = None
col2Tab5 = None
col3Tab5 = None
col4Tab5 = None
col5Tab5 = None
col6Tab5 = None
col7Tab5 = None
col8Tab5 = None


tabTab1 = None
tabTab2 = None
tabTab3 = None
tabTab4 = None
tabTab5 = None
tabTab5 = None
tabTab6 = None
tabTab7 = None
tabTab8 = None
tabTab9 = None
tabTab10 = None
tabTab11 = None
tabTab12 = None
tabTab13 = None
tabTab14 = None
tabTab15 = None
tabTab16 = None

tabHypothesis = None

txtText = None
figPlot = None

dictDataFrames = dict()
dictWhat = dict()
dictTransform = dict()

dfSales = pd.DataFrame()
dfFeatures = pd.DataFrame()
dfStores = pd.DataFrame()
dfSales_Combined_DataSet = pd.DataFrame()
dfSales_Combined_DataSet_Work = pd.DataFrame()
dteStartDate = pd.DataFrame()
dfSales_Combined_DataSet_StoreType = pd.DataFrame()
dfSales_Combined_DataSet_SubSet = pd.DataFrame()
dfSales_Combined_DataSet_Final = pd.DataFrame()
dfSales_Combined_DataSet_Summary = pd.DataFrame()
dfSunburst_DataSet = pd.DataFrame()
dfSales_Combined_DataSet_Profit = pd.DataFrame()
dfSales_Combined_DataSet_HighestProfit = pd.DataFrame()
dfSalesDataML_Work = pd.DataFrame()
dfPrevious = pd.DataFrame()
dfPreviousSales = pd.DataFrame()
dfActualSales = pd.DataFrame()
dfPredictedSales = pd.DataFrame()
dfPlot = pd.DataFrame()
dfXTest = pd.DataFrame()



lstStoreRanges  = list()
lstMarkdownColumns = list()
lstFeatures = list()

fltSkew = 0.0
fltKurtosis = 0.0
intYear = 0
intStartYear = 0
intEndYear = 0
intNum = 0
dteStartDate = None
objPipeline = None
ax = None
fig = None

 
# Function to load custom CSS
def funcLoadCSS(fileName):
    with open(fileName) as fileCSS:
        st.markdown(f"<style>{fileCSS.read()}</style>", unsafe_allow_html=True)


#******** main code ********

#try and load csvs from assets folder
dfSales_Combined_DataSet = pd.read_csv(CNST_STR_SALES_COMBINED_DATASET)
dfFeatures = pd.read_csv(CNST_STR_FEATURES_DATASET)
dfSales = pd.read_csv(CNST_STR_SALES_DATASET)
dfStores = pd.read_csv(CNST_STR_STORES_DATASET)

#convert Date to datetime
dfSales_Combined_DataSet["Date"] = pd.to_datetime(dfSales_Combined_DataSet["Date"], format="%d/%m/%Y")

#get 12 months from last date in DataFrame
dteStartDate = dfSales_Combined_DataSet['Date'].max() - pd.DateOffset(months = 12)


#init streamlit dashboard 
# Load the CSS file
funcLoadCSS(pathlib.Path("assets/css/style.css") )

#configure streamlit page
st.set_page_config(
   page_title = "Sales Analysis",
   page_icon =":temperature:",
   layout = "wide",
   initial_sidebar_state = "expanded"
)
 
st.session_state.sidebar_state = 'expanded'
 
# if: @st.cache_data  - put before function means if run any results are reused i.e. on loading data

#key does NOT create a HTML id just a link to the current page session for reading current values e.g.
#st.session_state.<key name>
#useful if using mutiple widgets of the same type


st.title("Sales Analysis")
st.subheader("What We See In The Data")

#create page controls container
conContainerMain = st.container(border=True, width="stretch", key="conMain", height=900 ) #height=780

#create sidebar
st.sidebar.title("Analysis Options",width="content",anchor="left")

#add radio button group for options
radRadioButtons = st.sidebar.radio("Select:", ["Overview", "Hypothesis 1 -4", "Hypothesis 5 - 8", "Hypothesis 9 - 11", "ML Test"], index=0, key="radRadioButtons")

#populate container with page controls
match radRadioButtons:
   case "Overview":
        conOverview = conContainerMain.container(border=False, width="stretch", key="conSection1", height=860) 
        # conContainerMain.markdown("<div style='background-color:#222; color:#00FF00; padding:10px; border-radius:5px;'>"
        #  "This is green text on a dark background"
        #  "</div>",
        #  unsafe_allow_html=True)
        conOverview.info("Overview")
        conOverview.markdown("### Purpose of The Analysis")
        conOverview.write("This test came about after the Met office declared the first heatwave. Was it **really** a heatwave? The event lasted"
                             "for four days, then temperatures seemed to cool slightly (but not by much), then same happened again the next week.")
        conOverview.write("Hmmmm.. I thought is this a 'coincidence' that two heatwaves occur back-to-back or is it simply Summer?")
        conOverview.write(" ")
        conOverview.write("On the 'Hypothesis' page I dig deep into the data and attempt to answer this question!")
   case "Hypothesis 1 -4": 
 #******tab 1*******  
        #plotly visualisation for hypothesis 1 - are sales increased if weather is hotter or colder in the last 12 months? 
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conSection1 = conContainerMain.container(border=False, width="stretch", key="conSection1", height=860)
        conSection1Title = conSection1.container(border=False, width="stretch", key="conSection1Title", height=40)
         
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab1, tabTab2, tabTab3, tabTab4 = conSection1.tabs([
          "Hypothesis 1", "Hypothesis 2", "Hypothesis 3", "Hypothesis 4"
        ])
     
        conSection1Tab = tabTab1.container(border=True, width="stretch", height=780)
        conSection1Title.info("Are Sales Increased If Weather Is Hotter Or Colder In The Last 12 Months?")

        #load into DataFrame copy for working with   
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()


        #get year from last date in DataFrame
        intYear = dfSales_Combined_DataSet_Work['Date'].dt.year.max() -1

        #filter DataFrame for last 12 months
        dfSales_Combined_DataSet_Work= dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work['Date'] >= dteStartDate]

        #set plot size
        fig = px.scatter(dfSales_Combined_DataSet_Work , x="Temperature", y="Weekly_Sales",
                 title="Sales vs Temperature Over Last 12 Months", color="Temperature", opacity=0.5)

        #code copied from chatGPT
        fig.update_xaxes(
           ticks="outside",
           minor=dict(
              ticks="outside",
              ticklen=4,
              showgrid=False
           )
        )

        fig.update_yaxes(
           ticks="outside",
           minor=dict(
              ticks="outside",
              ticklen=4,
              showgrid=False
           )
        )
        
        fig.update_layout(
           xaxis_title="Temperature (°C)",
           yaxis_title="Weekly Sales (£)", 
        )
             
        #remove after testing
        fig.update_xaxes(dtick=10)        # every 10 degrees
        fig.update_yaxes(dtick=100000)    # every 100,000 sales
        #end code copied from chatGPT

        conSection1Tab.plotly_chart(fig, use_container_width=True, key="figTab1") 
         
 
 
 #******tab 2*******   
        #plotly visualisation for hypothesis 2 - Sales Differences Between holiday and Non Holiday Weeks per Store Over last 12 Months
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab2_Sub = tabTab2.container(border=True, width="stretch", key="conTab2Sub", height=780)
        conContainerTab2_Sub.info("Sales Differences Between Holiday and Non Holiday Weeks per Store Over last 12 Months")
        #load into DataFrame copy for working with   
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()

        #create plot
        fig = px.box(dfSales_Combined_DataSet_Work,
           x="Store",
           y="Weekly_Sales",
           color="IsHoliday",
           title="Sales Differences Between Holiday and Non-Holiday Weeks Per Store Last 12 Momths",
           labels={
              "IsHoliday": "Holiday Status",
              "Weekly_Sales": "Total Weekly Sales"
           },
           #set plot size
           height=600,
           width=1050
        )

        conContainerTab2_Sub.plotly_chart(fig, use_container_width=True, key="figTab2") 
         
  
  

 #******tab 3*******  
        #plotly visualisation for hypothesis 3 - What is most profitable store type over the last 12 months?
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab3_Sub = tabTab3.container(border=True, width="stretch", key="conTab3Sub", height=780)
        conContainerTab3_Sub.info("What is Most Profitable Store Type Over The Last 12 Months?")

        #load into DataFrame copy for working with   
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()
        
        #create plot#get year from last date in DataFrame
        intYear = dfSales_Combined_DataSet_Work['Date'].dt.year.max() -1

        #filter DataFrame for last 12 months
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work['Date'] >= dteStartDate]

        #filter data by doing simple grouby on store type and weekly sales
        #reset the index so that the store type is a column and not an index
        dfSales_Combined_DataSet_StoreType = dfSales_Combined_DataSet_Work.groupby("Store_Type")["Weekly_Sales"].sum().reset_index()

        #splot chart
        fig = px.bar(dfSales_Combined_DataSet_StoreType,
           x="Store_Type",
           y="Weekly_Sales",
           color="Weekly_Sales",
           title="Most Profitable Store By Type Over Last 12 Months",
           labels={
              "IsHoliday": "Holiday Status",
              "Weekly_Sales": "Total Weekly Sales"
           },
           #set plot size
           height=600,
           width=1050
        )

        #by default plotly will show 1B, 2B in the y axis so change it to something more understandable
        fig.update_yaxes(
           tickprefix="£",
           tickformat=","
        )
 
        conContainerTab3_Sub.plotly_chart(fig, use_container_width=True, key="figTab3") 
         
   
   
   

   
 #******tab 4*******    
        #SeaBorn visualisation for hypothesis 4 - Does store size affect profitability? If so, how much?
        #over the last 12 months?
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab4_Sub = tabTab4.container(border=True, width="stretch", key="conTab4Sub", height=780)
        conContainerTab4_Sub.info("Does Store Size Affect Profitability? If So, How Much Over The Last 12 Months?")

        #create the plot

        #define list of store numbers as a set of ranges
        #there is probably some clever way of doing this dynamically but I don't know it!
        #so went "old skool" and simply looked at the last store number in the csv file: stores data-set.csv
        #obviously if more stores are added this isn't a good solution!
        lstStoreRanges = [
           range(1, 10),
           range(10, 20),
           range(20, 30),
           range(30, 40),
           range(40, 46)
        ]
        
        #load into DataFrame copy for working with   
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()
        
        #get year from last date in DataFrame
        intYear = dfSales_Combined_DataSet_Work['Date'].dt.year.max() -1

        #filter DataFrame for last 12 months
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work['Date'] >= dteStartDate]

        #read through DataFrame see if store number is in range
        #Note: this is probably a mute step but is a a god way of validating the result BEFORE
        #      creating a plot
        intNum = 4
        
        for objStores in lstStoreRanges:
           #add row to new DataFrame
           dfSales_Combined_DataSet_SubSet = dfSales_Combined_DataSet_Work [
              dfSales_Combined_DataSet_Work["Store"].isin(objStores)
           ]

           fig, ax = plt.subplots(figsize=(20, 6))
         
           #set subplots defaults
           sns.barplot(data=dfSales_Combined_DataSet_SubSet, x="Store_Size", y="Weekly_Sales",
                        hue="Store_Size")

           #set tick params for x axis
           plt.tick_params(axis='x', which='minor', length=4, width=1.2)
           plt.tick_params(axis='x', which='major', length=8, width=0.8)

               
           #set title
           plt.title(f"Most Profitable Store By Size Over Last 12 Months - Stores: {min(objStores)}-{max(objStores)}",
                     fontsize=20)
           #need to use pyplot for seaborn plots
           conContainerTab4_Sub.pyplot(fig, use_container_width=True) 
           intNum += 1

         
   case "Hypothesis 5 - 8":                
  #******tab 5*******    
        #plotly visualisation for hypothesis 5 - Weekly Sales by Store Type, Store and Department For Last 12 Months
        conSection2 = conContainerMain.container(border=False, width="stretch", key="conSection2", height=860)
        conSection2Title = conSection2.container(border=False, width="stretch", key="conSection2Title", height=40)
         
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab5, tabTab6, tabTab7, tabTab8 = conSection2.tabs([
          "Hypothesis 5", "Hypothesis 6", "Hypothesis 7", "Hypothesis 8"
        ])
     
        conSection2Tab = tabTab5.container(border=True, width="stretch", height=780)
        conSection2Title.info("Weekly Sales by Store Type, Store and Department For Last 12 Months")


        #chatGPT generated code used as a base and heavily modified to suit my needs
        #added code comments
        #load into DataFrame copy for working with   
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()

        # Aggregate data
        dfSunburst_DataSet = (
           dfSales_Combined_DataSet_Work
           .groupby(["Store_Type", "Store", "Dept"], as_index=False)
           ["Weekly_Sales"]
           .sum()
        )

        # Remove negative and zero sales
        dfSunburst_DataSet = dfSunburst_DataSet[
           dfSunburst_DataSet["Weekly_Sales"] > 0
        ]

        # Convert hierarchy columns to strings
        dfSunburst_DataSet["Store_Type"] = dfSunburst_DataSet["Store_Type"].astype(str)
        dfSunburst_DataSet["Store"] = dfSunburst_DataSet["Store"].astype(str)
        dfSunburst_DataSet["Dept"] = dfSunburst_DataSet["Dept"].astype(str)

        #create sunburst plot
        fig = px.sunburst(
           dfSunburst_DataSet,
           path=["Store_Type", "Store", "Dept"],
           values="Weekly_Sales",
           custom_data=["Store_Type", "Store", "Dept"],
           title="Weekly Sales by Store Type, Store and Department Last 12 Months"
        )

        #update hover labels
        fig.update_traces(
           hovertemplate=
              "<b>Store Type:</b> %{customdata[0]}<br>" +
              "<b>Store Number:</b> %{customdata[1]}<br>" +
              "<b>Department:</b> %{customdata[2]}<br>" +
              "<b>Total Weekly Sales:</b> £%{value:,.0f}" +
              "<extra></extra>"
        )

        #set plot size
        fig.update_layout(
           width=1000,
           height=900
        )
 
        conSection2Tab.plotly_chart(fig, use_container_width=True, key="figTab5") 
         
   
 
 #******tab 6*******  
        #plotly visualisation for hypothesis 6 - Impact of markdowns on sales during holiday periods in the last 12 months by store
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab6_Sub = tabTab6.container(border=True, width="stretch", key="conTab6Sub", height=780)
        conContainerTab6_Sub.info("What is Most Profitable Store Type Over The Last 12 Months?")

        lstMarkdownColumns = ['MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5']

        #make copy of DataFrame
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()

        #filter for JUST holidays
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work['IsHoliday'] == True]

        #make sure date formatted correctly
        dfSales_Combined_DataSet_Work['Date'] = pd.to_datetime(
           dfSales_Combined_DataSet_Work['Date'],
           dayfirst=True,
           errors='coerce'
        )
    
        #get last date in DataFrame
        intYear = dfSales_Combined_DataSet_Work['Date'].max()
        #filter DataFrame for last 12 months from above value
        dfSales_Combined_DataSet_GroupBy = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work['Date'] >= intYear - pd.DateOffset(months=12)].copy()

        # Aggregate
        dfSales_Combined_DataSet_Summary = (
           dfSales_Combined_DataSet_GroupBy.groupby('Store')[['Weekly_Sales'] + lstMarkdownColumns]
           .sum()
           .reset_index()
        )

        # Convert markdown columns into rows
        dfSales_Combined_DataSet_Final = dfSales_Combined_DataSet_Summary.melt(
           id_vars=['Store', 'Weekly_Sales'],
           value_vars=lstMarkdownColumns,
           var_name='Markdown Type',
           value_name='Markdown Value'
        )

        fig = px.sunburst(
           dfSales_Combined_DataSet_Final,
           path=['Store', 'Markdown Type'],
           values='Markdown Value',
           color='Weekly_Sales',
           color_continuous_scale='Viridis',
           custom_data=['Weekly_Sales'],
           title="Impact Of Markdowns On Sales By Store During Holiday Periods In The Last 12 Months By Store"
        )

        #update hover labels
        fig.update_traces(
           hovertemplate=
              "<b>Store:</b> %{parent}<br>" +
              "<b>Markdown Type:</b> %{label}<br>" +
              "<b>Markdown Value:</b> $%{value:,.2f}<br>" +
              "<b>Weekly Sales:</b> $%{customdata[0]:,.2f}" +
              "<extra></extra>"
        )

        #set plot size
        fig.update_layout(
           width=1000,
           height=900
        )
 
        conContainerTab6_Sub.plotly_chart(fig, use_container_width=True, key="figTab6") 
         
     
 
 #******tab 7*******  
        #plotly visualisation for hypothesis 7 - What are the most profitable departments per store in the last 12 months?
        #Note: last year in data is: 2012
      
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab7_Sub = tabTab7.container(border=True, width="stretch", key="conTab7Sub", height=780)
        conContainerTab7_Sub.info("What Are The Most Profitable Departments Per Store In  The Last 12 Months?")
 
         #make copy of DataFrame
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()
        
        #first filter by year 2012
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work['Date'].dt.year == 2012]

        #code created by chatGPT modified by me to suit naming conventions etc
        dfSales_Combined_DataSet_Profit= (
           dfSales_Combined_DataSet_Work
           .groupby(["Store", "Dept"])["Weekly_Sales"]
           .sum()
           .reset_index()
        )

        dfSales_Combined_DataSet_HighestProfit = (
           dfSales_Combined_DataSet_Profit.loc[dfSales_Combined_DataSet_Profit.groupby("Store")["Weekly_Sales"].idxmax()]
           .sort_values("Store")
        )

        #sort by Store added by me
        dfSales_Combined_DataSet_HighestProfit.sort_values(by="Store", ascending=True, inplace=True)

        #show plot
        plt.figure(figsize=(12, 8))

        dfSales_Combined_DataSet_HighestProfit["Store_Dept"] = (
           "Store " + dfSales_Combined_DataSet_HighestProfit["Store"].astype(str) +
           " - Dept " + dfSales_Combined_DataSet_HighestProfit["Dept"].astype(str)
        )

        #changed chatGPT seaborn plot to the much better looking plotly express one
        fig =px.bar(
           dfSales_Combined_DataSet_HighestProfit,
           x="Weekly_Sales",
           y="Store_Dept",
           orientation="h",
           color="Weekly_Sales",
           color_continuous_scale="Blues",
           title="Highest Selling Department For Each Store For Last 12 Months",
           #set plot size
           height=1000,
           width=1050
        )

        fig.update_layout(
           xaxis_title="Total Sales (£)",
           yaxis_title="Store and Department",
           yaxis=dict(autorange="reversed"),  # Reverse the y-axis to have the highest sales at the top
           coloraxis_colorbar=dict(title="Total Sales (£)"),
           title_x=0.5,  # Center the title
           font=dict(size=12),  # Set font size for better readability
        )  

        conContainerTab7_Sub.plotly_chart(fig, use_container_width=True, key="figTab7") 
          
        
 #******tab 8*******  
        #plotly visualisation for hypothesis 8 - What are the top 10 stores in terms of profitability in the last 12 months?
        #Note: last year in data is: 2012
      
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab8_Sub = tabTab8.container(border=True, width="stretch", key="conTab8Sub", height=780)
        conContainerTab8_Sub.info("What Are the Top 10 Stores In Terms of Profitability In The Last 12 Months?")
 
         #make copy of DataFrame
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()
        
        #first filter by year 2012
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work['Date'].dt.year == 2012]

        #group by Store and get sum of Weekly_Sales
        dfSales_Combined_DataSet_Work = (
           dfSales_Combined_DataSet_Work
           .groupby("Store")["Weekly_Sales"]
           .sum()
           .sort_values(ascending=False)
           .head(10)
           .reset_index()
        )


        #need to handle plot differntly as matplotlib does not work in streamlit like ploty express
        ax = dfSales_Combined_DataSet_Work.plot(
           x="Store",
           y="Weekly_Sales",
           kind="barh",
           color="steelblue",
           figsize=(10, 3),
           legend=False
        )

        #sort dataset
        dfSales_Combined_DataSet_Work.sort_values("Weekly_Sales", ascending=False).head(10).plot(
           x="Store",
           y="Weekly_Sales",
           kind="barh",
           color="steelblue"   
        )

        #unique to matplotlib
        ax.set_title("Top 10 Stores By Sales For Last 12 Months")
        ax.set_xlabel("Total Sales (£)")
        ax.set_ylabel("Store")
        ax.set_facecolor("#1e1e1e")
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")
        #need to apply as close a colour as possible to plotly express plot colours
        fig = ax.get_figure()
        # Background of the entire figure
        fig.set_facecolor("#070707")
        
        plt.tight_layout()
        
        conContainerTab8_Sub.pyplot(fig, use_container_width=True) 
          
   

   case "Hypothesis 9 - 11":     

   
#******tab 9*******  
        #plotly visualisation for hypothesis 9 - What are the bottom 10 stores in terms of profitability in the last 12 months?
        #Note: last year in data is: 2012
        conSection3 = conContainerMain.container(border=False, width="stretch", key="conSection3", height=860)
        conSection3Title = conSection3.container(border=False, width="stretch", key="conSection3Title", height=40)
         
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab9, tabTab10, tabTab11 = conSection3.tabs([
          "Hypothesis 9", "Hypothesis 10", "Hypothesis 11"
        ])  

        conSection3Tab = tabTab9.container(border=True, width="stretch", height=780)
        conSection3Title.info("What Are The Bottom 10 Stores In Terms Of Profitability In The Last 12 Months?")

 
        #make copy of DataFrame
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()
         
        #first filter by year 2012
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work['Date'].dt.year == 2012]
 
        #group by Store and get sum of Weekly_Sales
        dfSales_Combined_DataSet_Work = (
            dfSales_Combined_DataSet_Work
            .groupby("Store")["Weekly_Sales"]
            .sum()
            .sort_values(ascending=False)
            .tail(10)
            .reset_index()
        )
 
 
        #need to handle plot differntly as matplotlib does not work in streamlit like ploty express
        ax = dfSales_Combined_DataSet_Work.plot(
           x="Store",
           y="Weekly_Sales",
           kind="barh",
           color="steelblue",
           figsize=(10, 3),
           legend=False
        )
 
        #sort dataset
        dfSales_Combined_DataSet_Work.sort_values("Weekly_Sales", ascending=False).head(10).plot(
           x="Store",
           y="Weekly_Sales",
           kind="barh",
           color="steelblue"   
        )
 
        #unique to matplotlib
        ax.set_title("Bottom 10 Stores By Sales For Last 12 Months")
        ax.set_xlabel("Total Sales (£)")
        ax.set_ylabel("Store")
        ax.set_facecolor("#1e1e1e")
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")
        #need to apply as close a colour as possible to plotly express plot colours
        fig = ax.get_figure()
        # Background of the entire figure
        fig.set_facecolor("#070707")
         
        plt.tight_layout()     
         
        conSection3Tab.pyplot(fig, use_container_width=True) 
          
   
 
 #******tab 10*******  
        #plotly visualisation for hypothesis 10 - What percentage of customers were unemployed per store by month for last year?
        #Note: last year in data is: 2012
      
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab10_Sub = tabTab10.container(border=True, width="stretch", key="conTab10Sub", height=780)
        conContainerTab10_Sub.info("What Percentage of Customers Were Unemployed Per Store By Month For Last Year")
 
         #make copy of DataFrame
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()

        #filter by last 3 years data
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work["Date"].dt.year ==2012] 
        dfSales_Combined_DataSet_Work["Month"] = (dfSales_Combined_DataSet_Work["Date"].dt.month)

        # Aggregate data
        dfSales_Combined_DataSet_Work = (
           dfSales_Combined_DataSet_Work
           .groupby(["Store", "Month"], as_index=False)
           ["Unemployment"]
           .sum()
        )

        #configure plot
        fig = px.line(
           dfSales_Combined_DataSet_Work,
           x="Month",
           y="Unemployment",
           color="Store",
           title="Percentage of Unemployed Customers Per Store By Month For Last Year",
           markers=True,
           height=600,
           width=1000
        )

        fig.update_layout(
           xaxis_title="Month",
           yaxis_title="Unemployment Rate (%)",
           title_x=0.5,  # Centre the title
           font=dict(size=12), 
        )

        fig.update_xaxes(
           dtick="M1",  # Set tick interval to 1 month
           tickformat="%Y-%m",  # Format ticks as Year-Month
           tickangle=45,  # Rotate ticks for better readability
        )

        fig.update_yaxes(
           tickformat=".1f",  
        )
         #show plot
        
        conContainerTab10_Sub.plotly_chart(fig, use_container_width=True) 
          
   
 
 #******tab 11*******  
        #plotly visualisation for hypothesis 11 - What percentage of customer were unemployed by store size last year?
        #Note: last year in data is: 2012
      
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab11_Sub = tabTab11.container(border=True, width="stretch", key="conTab11Sub", height=780)
        conContainerTab11_Sub.info("What Percentage of Customer Were Unemployed By Store Size Last Year?")

         #make copy of DataFrame
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()

        #filter by last 3 years data
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work["Date"].dt.year ==2012] 

        #sprinkle some feature engineering     
        dfSales_Combined_DataSet_Work["Year"] = dfSales_Combined_DataSet_Work["Date"].dt.year.astype(int)
        dfSales_Combined_DataSet_Work["month_label"] = dfSales_Combined_DataSet_Work["Date"].dt.strftime("%d") + " " + dfSales_Combined_DataSet_Work["Date"].dt.month_name() 

        # Aggregate data
        dfSales_Combined_DataSet_Work = (
           dfSales_Combined_DataSet_Work
           .groupby(["Store", "YearMonth","Store_Size"], as_index=False)
           ["Unemployment"]
           .sum()
        )

        #configure the plot
        fig = px.scatter_3d(
           dfSales_Combined_DataSet_Work,
           x="Unemployment",
           y="Store",
           z="Store_Size",
           color="Unemployment",
           # markers=True,
           height=700,
           title=f"Percentage of Unemployed Customers Per Store For Last Year by Store Size" 
        )

        fig.update_xaxes(type="category")
        #label axis
        fig.update_layout(scene = dict(
           xaxis_title="Unemployment %",
           yaxis_title="Store",
           zaxis_title="Store Size"
           ),
           title_x=0.2,  # Centre the title
           #zoom in slightly to better fill the whitespace
           scene_camera=dict(
              eye=dict(x=1.4, y=1.4, z=1.4)  # closer / more zoomed in
           )
        )       
      
        #show plot       
        conContainerTab11_Sub.plotly_chart(fig, use_container_width=True) 
          
   
   case "ML Test":
   
#******tab 12*******
        #tab 12 hypothesis 12 - ML prediction
        #Note: last year in data is: 2012
        conSection4 = conContainerMain.container(border=False, width="stretch", key="conSection4", height=860)
        conSection4Title = conSection4.container(border=False, width="stretch", key="conSection4Title", height=40)
         
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab12, tabTab13, tabTab14, tabTab15 = conSection4.tabs([
          "Machine Learning Tests Linear Regression", "Machine Learning Tests Random Forest","Machine Learning Prediction - Linear Regression",
          "Machine Learning Prediction - Random Forest"
        ])  

        conSection4Title.info("Can Machine Learning Predict Sales Values That Match The Last 12 Months?")
        conSection4Tab = tabTab12.container(border=True, width="stretch", height=780)
  
        #now plot the results

        dfSalesDataML_Work = dfSales_Combined_DataSet.copy() 
        dfSalesDataML_Work = dfSalesDataML_Work.dropna(subset=["Date"])

        #sprinkle some feature engineering
        dfSalesDataML_Work["Year"] = dfSalesDataML_Work["Date"].dt.year
        dfSalesDataML_Work["Month"] = dfSalesDataML_Work["Date"].dt.month
        dfSalesDataML_Work["Day"] = dfSalesDataML_Work["Date"].dt.day
        dfSalesDataML_Work["DayOfWeek"] = dfSalesDataML_Work    ["Date"].dt.dayofweek
        dfSalesDataML_Work["WeekOfYear"] = dfSalesDataML_Work["Date"].dt.isocalendar().week.astype(int)
        dfSalesDataML_Work["Quarter"] = dfSalesDataML_Work["Date"].dt.quarter

        #Thanks to StackOverflow user chimpsarehungry for the solution
        dfSalesDataML_Work["MonthSin"] = np.sin(2 * np.pi * dfSalesDataML_Work["Month"] / 12)
        dfSalesDataML_Work["MonthCos"] = np.cos(2 * np.pi * dfSalesDataML_Work["Month"] / 12)

        dfSalesDataML_Work["IsHoliday"] = dfSalesDataML_Work["IsHoliday"].astype(int)

        #load linear regression pipeline
        objPipeline = joblib.load(CNST_STR_LINEAR_PIPELINE_HYPOTHESIS12_TEST_STREAMLIT_PATH)

        #set year range
        intYear= 2012
        intPreviousYear = intYear - 1

        dfTest = dfSalesDataML_Work.copy()
        dfTest = dfTest[dfTest["Year"] == intYear]

        dfPrevious = dfSalesDataML_Work.copy()
        dfPrevious = dfPrevious[dfPrevious["Year"] == intPreviousYear]

        #show year range
        print("Test year:", intYear)
        print("Previous year:", intPreviousYear)

        #show row data
        print("Test rows:", len(dfTest))
        print("Previous year rows:", len(dfPrevious))

        #configure features
        lstFeatures = [
           "Store",
           "Dept",
           "IsHoliday",
           "Year",
           "Month",
           "Day",
           "DayOfWeek",
           "WeekOfYear",
           "Quarter",
           "MonthSin",
           "MonthCos"
        ]

        #create model prediction
        dfXTest = dfTest[lstFeatures]
        dfTest["Predicted_Sales"] = objPipeline.predict(dfXTest)


        #get actual sales to compare
        dfActualSales = (
           dfTest
           .groupby(
              ["Date", "WeekOfYear"]
           )["Weekly_Sales"]
           .sum()
           .reset_index()
        )

        #make sure we don't get a clash fof names in the plot!
        dfActualSales = dfActualSales.rename(
           columns={
              "Weekly_Sales": "Actual_Sales"
           }
        )


        #get predicted sales to compare
        dfPredictedSales = (
           dfTest
           .groupby(
              ["Date", "WeekOfYear"]
           )["Predicted_Sales"]
           .sum()
           .reset_index()
        )


        #get previous sales by week to compare
        dfPreviousSales = (
           dfPrevious
           .groupby(
              "WeekOfYear"
           )["Weekly_Sales"]
           .sum()
           .reset_index()
        )

        #make sure we don't get a clash of names in the plot!
        dfPreviousSales = dfPreviousSales.rename(
           columns={
              "Weekly_Sales": "Previous_Year_Sales"
           }
        )


        #merge plots
        dfPlot = dfActualSales.merge(
           dfPredictedSales,
           on=["Date", "WeekOfYear"],
           how="left"
        )

        #merge previous year
        dfPlot = dfPlot.merge(
           dfPreviousSales,
           on="WeekOfYear",
           how="left"
        )

        #sort by Date
        dfPlot = dfPlot.sort_values("Date")

        #check for missing previous year values
        dfMissingPrevious = dfPlot["Previous_Year_Sales"].isna().sum()

        #create plot
        fig, ax = plt.subplots(figsize=(15, 7))

        # Set background colours
        fig.set_facecolor("#070707")
        ax.set_facecolor("#070707")         
        
        #plot actual sales
        ax.plot(
           dfPlot["Date"],
           dfPlot["Actual_Sales"],
           label="Actual Sales",
           color="white",
           linewidth=2
        )

        #plot predictions
        ax.plot(
           dfPlot["Date"],
           dfPlot["Predicted_Sales"],
           label="Linear Regression Prediction",
           color="red",
           linewidth=2
        )

        #plot previous year sales as comparison
        ax.plot(
           dfPlot["Date"],
           dfPlot["Previous_Year_Sales"],
           label="Previous Year Sales",
           color="blue",
           linestyle="--",
           linewidth=2
        )

        #configure plot
        ax.set_title(
           "Sales - Linear Regression vs Previous Year",
           fontsize=16,
           color="white"
        )

        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Weekly Sales", fontsize=12)

        ax.legend(loc="best")
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=45, color="white")
        plt.yticks(color="white")

        plt.tight_layout()

        #show plot in Streamlit
        conSection4Tab.pyplot(fig, use_container_width=True)

        expExpander1 = conSection4Tab.expander("Show Data Used For Plot", expanded=False, key="expExpander1")
        expExpander1.dataframe(dfPlot, use_container_width=True)
  
  
#******tab 13*******
        #tab 13 hypothesis 13 - ML prediction
        #Note: last year in data is: 2012  
        conContainerTab13_Sub = tabTab13.container(border=True, width="stretch", key="conTab13Sub", height=780)
   
        #now plot the results
        dfSalesDataML_Work = dfSales_Combined_DataSet.copy() 
        #random forest plot test compare last years sales with predicted values for same year

        dfSalesDataML_Work = dfSalesDataML_Work.dropna(subset=["Date"])

        #sprinkle some feature engineering
        dfSalesDataML_Work["Year"] = dfSalesDataML_Work["Date"].dt.year
        dfSalesDataML_Work["Month"] = dfSalesDataML_Work["Date"].dt.month
        dfSalesDataML_Work["Day"] = dfSalesDataML_Work["Date"].dt.day
        dfSalesDataML_Work["DayOfWeek"] = dfSalesDataML_Work["Date"].dt.dayofweek
        dfSalesDataML_Work["WeekOfYear"] = dfSalesDataML_Work["Date"].dt.isocalendar().week.astype(int)
        dfSalesDataML_Work["Quarter"] = dfSalesDataML_Work["Date"].dt.quarter

        #cyclical month features thanks to StackOverflow user chimpsarehungry for the solution
        dfSalesDataML_Work["MonthSin"] = np.sin(2 * np.pi * dfSalesDataML_Work["Month"] / 12)
        dfSalesDataML_Work["MonthCos"] = np.cos(2 * np.pi * dfSalesDataML_Work["Month"] / 12)

        dfSalesDataML_Work["IsHoliday"] = dfSalesDataML_Work["IsHoliday"].astype(int)



        #load pipeline for random forest
        objPipeline = joblib.load(CNST_STR_FOREST_PIPELINE_HYPOTHESIS12_TEST_STREAMLIT_PATH)

        #set year range
        intYear= 2012
        intPreviousYear = intYear - 1
        dfTest = dfSalesDataML_Work.copy()
        dfTest = dfTest[dfTest["Year"] == intYear]
        dfPrevious = dfSalesDataML_Work.copy()
        dfPrevious = dfPrevious[dfPrevious["Year"] == intPreviousYear].copy()

        #configure features
        lstFeatures = [
           "Store",
           "Dept",
           "IsHoliday",
           "Year",
           "Month",
           "Day",
           "DayOfWeek",
           "WeekOfYear",
           "Quarter",
           "MonthSin",
           "MonthCos"
        ]

        #get predictions
        dfXTest = dfTest[lstFeatures]
        dfTest["Predicted_Sales"] = objPipeline.predict(dfXTest)

        #get actual sales
        dfActualSales = (
           dfTest
           .groupby(
              ["Date", "WeekOfYear"]
           )["Weekly_Sales"]
           .sum()
           .reset_index()
        )

        #make sure no name clashes in the plot!
        dfActualSales = dfActualSales.rename(
           columns={
              "Weekly_Sales": "Actual_Sales"
           }
        )

        #get predicted sales
        dfPredictedSales = (
           dfTest
           .groupby(
              ["Date", "WeekOfYear"]
           )["Predicted_Sales"]
           .sum()
           .reset_index()
        )

        #get previous year sales
        dfPreviousSales = (
           dfPrevious
           .groupby(
              "WeekOfYear"
           )["Weekly_Sales"]
           .sum()
           .reset_index()
        )

        #make sure no name clashes in the plot!
        dfPreviousSales = dfPreviousSales.rename(
           columns={
              "Weekly_Sales": "Previous_Year_Sales"
           }
        )

        #merge DataFrames
        dfPlot = dfActualSales.merge(
           dfPredictedSales,
           on=["Date", "WeekOfYear"],
           how="left"
        )

        #merge DataFrames
        dfPlot = dfPlot.merge(
           dfPreviousSales,
           on="WeekOfYear",
           how="left"
        )

        #Sort by date
        dfPlot = dfPlot.sort_values("Date")

        #check missing previous-year values
        dfMissingPrevious = (
           dfPlot["Previous_Year_Sales"]
           .isna()
           .sum()
        )

        #create plot
        fig, ax = plt.subplots(figsize=(15, 7))
        # Set background colours
        fig.set_facecolor("#070707")
        ax.set_facecolor("#070707")        

        #create actual sales plot
        plt.plot(
           dfPlot["Date"],
           dfPlot["Actual_Sales"],
           label="Actual Sales",
           color="white",
           linewidth=2
        )

        #plot predictions
        plt.plot(
           dfPlot["Date"],
           dfPlot["Predicted_Sales"],
           label="Random Forest Prediction",
           color="red",
           linewidth=2
        )

        #plot previous years sales
        plt.plot(   
           dfPlot["Date"],
           dfPlot["Previous_Year_Sales"],
           label="Previous Year Sales",
           color="blue",
           linestyle="--",
           linewidth=2
        )

        #format plot
        plt.title("Sales - Random Forest vs Previous Year", fontsize=16)
        plt.xlabel("Date", fontsize=12)
        plt.ylabel("Weekly Sales", fontsize=12)
        #prefer best fit
        plt.legend(loc="best")
        plt.grid(True, alpha=0.3)
        #make sure ticks are readable
        plt.xticks(rotation=45, color="white")
        plt.tight_layout()
        plt.yticks(color="white")

        ax.set_title(
           "Sales - Random Forest vs Previous Year",
           fontsize=16,
           color="white"
        )

        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Weekly Sales", fontsize=12)
        plt.xticks(rotation=45, color="white")
        ax.legend(loc="best")
        ax.grid(True, alpha=0.3)

        # Show plot in Streamlit
        conContainerTab13_Sub.pyplot(fig, use_container_width=True)

        expExpander2 = conContainerTab13_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander2")
        expExpander2.dataframe(dfPlot, use_container_width=True)
  
   
    
#******tab 14*******
        #tab 14 hypothesis 13 - ML prediction
        #Note: last year in data is: 2012  
        conContainerTab14_Sub = tabTab14.container(border=True, width="stretch", key="conTab14Sub", height=780)

        #load csv files
        dfFeatures = pd.read_csv(CNST_STR_FEATURES_DATASET)
        dfSales = pd.read_csv(CNST_STR_SALES_DATASET)
        dfStores = pd.read_csv(CNST_STR_STORES_DATASET)
   
        #convert Date to datetime
        dfFeatures["Date"] = pd.to_datetime(
           dfFeatures["Date"],
           errors="coerce"
        )

        dfSales["Date"] = pd.to_datetime(
           dfSales["Date"],
           errors="coerce"
        )


        #remove invalid dates
        dfFeatures = dfFeatures.dropna(
           subset=["Date"]
        )

        dfSales = dfSales.dropna(
           subset=["Date"]
        )

        #merge features and stores
        dfFeaturesStores = dfFeatures.merge(
           dfStores,
           on="Store",
           how="left"
        )


        #merge sales with features
        dfTrain = dfSales.merge(
           dfFeaturesStores,
           on=[
              "Store",
              "Date",
              "IsHoliday"
           ],
           how="left"
        )

        #create forecast datas
        dfForecast = dfFeaturesStores.copy()
        dfFeatures = dfFeatures[
           dfFeatures["Date"] >
           dfSales["Date"].max()
        ]

        #we need predictions for every Store/Department!
        #get rid of duplicates
        dfDepts = dfSales[ ["Store", "Dept"] ].drop_duplicates()

        #merge forecast with departments 
        dfForecast = dfForecast.merge(
           dfDepts,
           on="Store",
           how="inner"
        )

        #sprinkle some feature engineering
        #date features
        dfTrain["Year"] = ( dfTrain["Date"].dt.year)
        dfTrain["Month"] = ( dfTrain["Date"].dt.month)
        dfTrain["Day"] = (dfTrain["Date"].dt.day)
        dfTrain["DayOfWeek"] = (dfTrain["Date"].dt.dayofweek)
        dfTrain["WeekOfYear"] = (dfTrain["Date"]
           .dt.isocalendar()
            .week
            .astype(int)
         )
        dfTrain["Quarter"] = ( dfTrain["Date"].dt.quarter)
        #cyclical features thanks to StackOverflow user chimpsarehungry for the solution
        dfTrain["MonthSin"] = np.sin(2 * np.pi * dfTrain["Month"] / 12)
        dfTrain["MonthCos"] = np.cos(2 * np.pi * dfTrain["Month"] / 12)
        dfTrain["WeekSin"] = np.sin(2 * np.pi * dfTrain["WeekOfYear"] / 52)
        dfTrain["WeekCos"] = np.cos(2 * np.pi * dfTrain["WeekOfYear"] / 52)

        #holiday
        dfTrain["IsHoliday"] = (dfTrain["IsHoliday"].astype(int))        
        
        
        dfForecast["Year"] = ( dfForecast["Date"].dt.year)
        dfForecast["Month"] = ( dfForecast["Date"].dt.month)
        dfForecast["Day"] = (dfForecast["Date"].dt.day)
        dfForecast["DayOfWeek"] = (dfForecast["Date"].dt.dayofweek)
        dfForecast["WeekOfYear"] = (dfForecast["Date"]
           .dt.isocalendar()
            .week
            .astype(int)
         )
        dfForecast["Quarter"] = ( dfForecast["Date"].dt.quarter)
        #cyclical features thanks to StackOverflow user chimpsarehungry for the solution
        dfForecast["MonthSin"] = np.sin(2 * np.pi * dfForecast["Month"] / 12)
        dfForecast["MonthCos"] = np.cos(2 * np.pi * dfForecast["Month"] / 12)
        dfForecast["WeekSin"] = np.sin(2 * np.pi * dfForecast["WeekOfYear"] / 52)
        dfForecast["WeekCos"] = np.cos(2 * np.pi * dfForecast["WeekOfYear"] / 52)

        #holiday
        dfForecast["IsHoliday"] = (dfForecast["IsHoliday"].astype(int))    
        
        #define markdown columns
        lstMarkdown = [
           "MarkDown1",
           "MarkDown2",
           "MarkDown3",
           "MarkDown4",
           "MarkDown5"
        ]


        for column in lstMarkdown:
           if column in dfTrain.columns:
              dfTrain[column] = (
                    dfTrain[column]
                    .fillna(0)
              )

           if column in dfForecast.columns:
              dfForecast[column] = (
                    dfForecast[column]
                    .fillna(0)
              )


        #define features
        lstFeatures = [
            # Store information
            "Store",
            "Dept",
            "Store_Type",
            "Size",

            # Date information
            "Year",
            "Month",
            "Day",
            "DayOfWeek",
            "WeekOfYear",
            "Quarter",

            # Cyclical features
            "MonthSin",
            "MonthCos",
            "WeekSin",
            "WeekCos",

            # Holiday
            "IsHoliday",

            # Walmart economic features
            "Temperature",
            "Unemployment",

            # Markdown
            "MarkDown1",
            "MarkDown2",
            "MarkDown3",
            "MarkDown4",
            "MarkDown5"
        ]

        #load pipeline for random forest
        objPipeline = joblib.load(CNST_STR_LINEAR_PIPELINE_HYPOTHESIS12_STREAMLIT_PATH)
    #    dfXTest = dfTest[lstFeatures]
    #    dfTest["Predicted_Sales"] = objPipeline.predict(dfXTest)
        #check columns
      #   objMissingColumns = [
      #      column
      #      for column in lstFeatures
      #      if column not in dfTrain.columns
      #   ]

        #missing columns?
      #   if objMissingColumns:
      #      raise ValueError(
      #         f"Missing columns: {objMissingColumns}"
      #      )


        #setup X and y for training and forecasting
      #   dfXTrain = dfTrain[lstFeatures]
      #   dfyTrain = dfTrain[strTarget]
      #   dfXForecast = dfForecast[lstFeatures]

      #   #define numeric features
      #   lstNumericFeatures = [
      #      "Size",
      #      "Year",
      #      "Month",
      #      "Day",
      #      "DayOfWeek",
      #      "WeekOfYear",
      #      "Quarter",
      #      "MonthSin",
      #      "MonthCos",
      #      "WeekSin",
      #      "WeekCos",
      #      "IsHoliday",
      #      "Temperature",
      #      "Unemployment",
      #      "MarkDown1",
      #      "MarkDown2",
      #      "MarkDown3",
      #      "MarkDown4",
      #      "MarkDown5"
      #   ]

      #   #define categorical features
      #   lstCategoricalFeatures = [
      #      "Store",
      #      "Dept",
      #      "Store_Type"
      #   ]

      #   #configure numeric transformer
      #   objNumericTransformer = Pipeline(
      #      steps=[
      #         (
      #               "imputer",
      #               SimpleImputer(
      #                  strategy="median"
      #               )
      #         ),
      #         (
      #               "scaler",
      #               StandardScaler()
      #         )
      #      ]
      #   )

      #   #configure categorical transformer
      #   objCategoricalTransformer = Pipeline(
      #      steps=[
      #         (
      #               "imputer",
      #               SimpleImputer(
      #                  strategy="most_frequent"
      #               )
      #         ),

      #         (
      #               "onehot",
      #               OneHotEncoder(
      #                  handle_unknown="ignore"
      #               )
      #         )
      #      ]
      #   )

      #    #configure column transformer
      #   objPreProcessor = ColumnTransformer(
      #      transformers=[
      #          (
      #                "numeric",
      #                objNumericTransformer,
      #                lstNumericFeatures
      #          ),

      #          (
      #                "categorical",
      #                objCategoricalTransformer,
      #                lstCategoricalFeatures
      #          )
      #       ]
      #   )

         #create linear regression model
 #       objModel = LinearRegression()

        #configure pipeline
      #   objPipeline = Pipeline(
      #       steps=[
      #          (
      #                "preprocessor",
      #                objPreProcessor
      #          ),
      #          (
      #                "model",
      #                objModel
      #          )
      #       ]
      #   )


        #train model
      #   objPipeline.fit(dfXTrain, dfyTrain)

      #   #save pipeline to main folder
      #   joblib.dump(
      #      objPipeline,
      #      CNST_STR_LINEAR_PIPELINE_HYPOTHESIS12_PATH
      #   )

      #   #save to sreamlit folder
      #   joblib.dump(
      #      objPipeline,
      #      CNST_STR_LINEAR_PIPELINE_HYPOTHESIS12_STREAMLIT_PATH
      #   )

        dfXForecast = dfForecast[lstFeatures]
        dfForecast["Predicted_Sales"] = (
           objPipeline.predict(
              dfXForecast
           )
        )

        #select 2013 predictions"
        dfTest = dfForecast.copy()
        dfTest = dfTest[ dfTest["Date"].dt.year == 2013]

        #aggregate prediction values
        dfForecast = (
           dfTest
           .groupby(
              ["Date", "WeekOfYear"]
           )["Predicted_Sales"]
           .sum()
           .reset_index()
        )


        #get actual sales for 2012 to compare with 2013 predictions
        dfActualSales = dfTrain[
           dfTrain["Year"] == 2012
        ].copy()

        #aggregate actual sales for 2012
        dfPrevious = (
           dfActualSales
           .groupby(
              "WeekOfYear"
           )["Weekly_Sales"]
           .sum()
           .reset_index()
        )

        #make sure we don't get a clash of names in the plot!
        dfPrevious = dfPrevious.rename(
           columns={
              "Weekly_Sales":
              "Previous_Year_Sales"
           }
        )


        #merge forecast with previous year sales for comparison
        dfPlot= dfForecast.merge(
           dfPrevious,
           on="WeekOfYear",
           how="left"
        )

        #sort by Date
        dfPlot = dfPlot.sort_values("Date")

        #create plot
        fig, ax = plt.subplots(figsize=(15, 7))
        # Set background colours
        fig.set_facecolor("#070707")
        ax.set_facecolor("#070707") 

        plt.plot(
           dfPlot["Date"],
           dfPlot["Predicted_Sales"],
           color="red",
           linewidth=2,
           label="2013 Predicted Sales"
        )

        plt.title(
           "Linear Regression - 2013 Sales Forecast",
           fontsize=16
        )
        
        ax.set_title(
           "Linear Regression - 2013 Sales Forecast",
           fontsize=16,
           color="white"
        )

        ax.set_xlabel("Date", fontsize=12, color="white")
        ax.set_ylabel("Weekly Sales", fontsize=12, color="white")

        ax.legend(loc="best")
        ax.grid(True, alpha=0.3)
        plt.xlabel("Date")
        plt.ylabel("Weekly Sales")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.xticks(rotation=45, color="white")
        plt.yticks(color="white")
        plt.tight_layout()
      
  
        # Show plot in Streamlit
        conContainerTab14_Sub.pyplot(fig, use_container_width=True)

        expExpander3 = conContainerTab14_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander3")
        expExpander3.dataframe(dfPlot, use_container_width=True)
  


#******tab 15*******
        #tab 15 hypothesis 12 - ML prediction
        #Note: last year in data is: 2012  
        #random forest predict next years sales
        conContainerTab15_Sub = tabTab15.container(border=True, width="stretch", key="conTab15Sub", height=780)

        #load csv files
        dfFeatures = pd.read_csv(CNST_STR_FEATURES_DATASET)
        dfSales = pd.read_csv(CNST_STR_SALES_DATASET)
        dfStores = pd.read_csv(CNST_STR_STORES_DATASET)


        #convert Date to datetime
        dfFeatures["Date"] = pd.to_datetime(
           dfFeatures["Date"],
           errors="coerce"
        )

        dfSales["Date"] = pd.to_datetime(
           dfSales["Date"],
           errors="coerce"
        )

        #delete rows with invalid dates
        dfFeatures = dfFeatures.dropna(
           subset=["Date"]
        )

        dfSales = dfSales.dropna(
           subset=["Date"]
        )


        #merge features and stores
        dfFeaturesStores = dfFeatures.merge(
           dfStores,
           on="Store",
           how="left"
        )

        #merge sales and featuresstores
        dfTraining = dfSales.merge(
           dfFeaturesStores,
           on=[
              "Store",
              "Date",
              "IsHoliday"
           ],
           how="left"
        )


        #get forecast data
        dfForecast = dfFeaturesStores[
           dfFeaturesStores["Date"] >
           dfSales["Date"].max()
        ].copy()


        store_depts = dfSales[
           ["Store", "Dept"]
        ].drop_duplicates()


        dfForecast = dfForecast.merge(
           store_depts,
           on="Store",
           how="inner"
        )

        #sprinkle some feature engineering
        #date features
        dfTrain["Year"] = ( dfTrain["Date"].dt.year)
        dfTrain["Month"] = ( dfTrain["Date"].dt.month)
        dfTrain["Day"] = (dfTrain["Date"].dt.day)
        dfTrain["DayOfWeek"] = (dfTrain["Date"].dt.dayofweek)
        dfTrain["WeekOfYear"] = (dfTrain["Date"]
           .dt.isocalendar()
            .week
            .astype(int)
         )
        dfTrain["Quarter"] = ( dfTrain["Date"].dt.quarter)
        #cyclical features thanks to StackOverflow user chimpsarehungry for the solution
        dfTrain["MonthSin"] = np.sin(2 * np.pi * dfTrain["Month"] / 12)
        dfTrain["MonthCos"] = np.cos(2 * np.pi * dfTrain["Month"] / 12)
        dfTrain["WeekSin"] = np.sin(2 * np.pi * dfTrain["WeekOfYear"] / 52)
        dfTrain["WeekCos"] = np.cos(2 * np.pi * dfTrain["WeekOfYear"] / 52)

        #holiday
        dfTrain["IsHoliday"] = (dfTrain["IsHoliday"].astype(int))        
        
        
        dfForecast["Year"] = ( dfForecast["Date"].dt.year)
        dfForecast["Month"] = ( dfForecast["Date"].dt.month)
        dfForecast["Day"] = (dfForecast["Date"].dt.day)
        dfForecast["DayOfWeek"] = (dfForecast["Date"].dt.dayofweek)
        dfForecast["WeekOfYear"] = (dfForecast["Date"]
           .dt.isocalendar()
            .week
            .astype(int)
         )
        dfForecast["Quarter"] = ( dfForecast["Date"].dt.quarter)
        #cyclical features thanks to StackOverflow user chimpsarehungry for the solution
        dfForecast["MonthSin"] = np.sin(2 * np.pi * dfForecast["Month"] / 12)
        dfForecast["MonthCos"] = np.cos(2 * np.pi * dfForecast["Month"] / 12)
        dfForecast["WeekSin"] = np.sin(2 * np.pi * dfForecast["WeekOfYear"] / 52)
        dfForecast["WeekCos"] = np.cos(2 * np.pi * dfForecast["WeekOfYear"] / 52)

        #holiday
        dfForecast["IsHoliday"] = (dfForecast["IsHoliday"].astype(int))    


       #define markdown columns
        markdown_columns = [
           "MarkDown1",
           "MarkDown2",
           "MarkDown3",
           "MarkDown4",
           "MarkDown5"
        ]


        for column in markdown_columns:
           if column in dfTraining.columns:
              dfTraining[column] = (
                    dfTraining[column]
                     .fillna(0)
              )

           if column in dfForecast.columns:
              dfForecast[column] = (
                    dfForecast[column]
                    .fillna(0)
              )

        #define features
        lstFeatures = [
            "Store",
            "Dept",
            "Store_Type",
            "Size",

            "Year",
            "Month",
            "Day",
            "DayOfWeek",
            "WeekOfYear",
            "Quarter",

            "MonthSin",
            "MonthCos",
            "WeekSin",
            "WeekCos",

            "IsHoliday",

            "Temperature",
            "Unemployment",

            "MarkDown1",
            "MarkDown2",
            "MarkDown3",
            "MarkDown4",
            "MarkDown5"
         ]


        dfXtrain = dfTrain[
           lstFeatures
        ]

        dfyTrain = dfTrain[
           "Weekly_Sales"
        ]

        dfXForecast = dfForecast[
           lstFeatures
        ]

       
 
         # lstNumericFeatures = [

         #    "Size",

         #    "Year",
         #    "Month",
         #    "Day",
         #    "DayOfWeek",
         #    "WeekOfYear",
         #    "Quarter",

         #    "MonthSin",
         #    "MonthCos",
         #    "WeekSin",
         #    "WeekCos",

         #    "IsHoliday",

         #    "Temperature",
         #    "Unemployment",

         #    "MarkDown1",
         #    "MarkDown2",
         #    "MarkDown3",
         #    "MarkDown4",
         #    "MarkDown5"
         # ]


         # lstCategoricalFeatures = [
         #    "Store",
         #    "Dept",
         #    "Store_Type"
         # ]


         # objNumericTransformer = Pipeline(
         #    steps=[
         #       (
         #             "imputer",
         #             SimpleImputer(
         #                strategy="median"
         #             )
         #       )
         #    ]
         # )


         # objCategoricalTransformer = Pipeline(
         #    steps=[
         #       (
         #             "imputer",
         #             SimpleImputer(
         #                strategy="most_frequent"
         #             )
         #       ),
         #       (
         #             "onehot",
         #             OneHotEncoder(
         #                handle_unknown="ignore"
         #             )
         #       )
         #    ]
         # )


         # objPreProcessor = ColumnTransformer(
         #    transformers=[

         #       (
         #             "numeric",
         #             objNumericTransformer,
         #             lstNumericFeatures
         #       ),

         #       (
         #             "categorical",
         #             objCategoricalTransformer,
         #             lstCategoricalFeatures
         #       )
         #    ]
         # )

        #load pipeline
      #   objModel = RandomForestRegressor(
      #       n_estimators=20,  #50
      #       max_depth=20,
      #       min_samples_split=5,
      #       min_samples_leaf=2,
      #       random_state=42,
      #       n_jobs=-1
      #    )


         # objPipeline = Pipeline(
         #    steps=[

         #       (
         #             "preprocessor",
         #             objPreProcessor
         #       ),

         #       (
         #             "model",
         #             objModel
         #       )
         #    ]
         # )


         # # ============================================================
         # # TRAIN
         # # ============================================================

         # print(
         #    "\nTraining Random Forest..."
         # )

         # objPipeline.fit(
         #    dfXtrain,
         #    dfyTrain
         # )

         # print(
         #    "Training complete."
         # )


         # ============================================================
         # SAVE PIPELINE
         # ============================================================

         # #save
         # joblib.dump(
         #    objPipeline,
         #    CNST_STR_FOREST_PIPELINE_HYPOTHESIS12_PATH
         # )

         # #save to streamlit folder
         # joblib.dump(
         #    objPipeline,
         #    CNST_STR_FOREST_PIPELINE_HYPOTHESIS12_STREAMLIT_PATH
         # )

         # print(
         #    "\nPipeline saved:"
         # )

         # print(CNST_STR_FOREST_PIPELINE_HYPOTHESIS12_PATH)
         # print(CNST_STR_FOREST_PIPELINE_HYPOTHESIS12_STREAMLIT_PATH)

        objPipeline = joblib.load(CNST_STR_FOREST_PIPELINE_HYPOTHESIS12_STREAMLIT_PATH)
        #predict sales for 2013
        dfForecast["Predicted_Sales"] = (
            objPipeline.predict(
               dfXForecast
            )
        )


        dfPredictedSales = dfForecast[
           dfForecast["Date"].dt.year == 2013
        ].copy()

        #aggregate
        dfForecastSales = (
           dfPredictedSales
            .groupby(
               ["Date", "WeekOfYear"]
            )["Predicted_Sales"]
            .sum()
            .reset_index()
        )


        #actual sales 2012
        dfActualSales = dfTrain.copy() 
        
        dfActualSales = dfActualSales[
            dfActualSales["Year"] == 2012
        ]


        dfPreviousSales = (
            dfActualSales
            .groupby(
               "WeekOfYear"
            )["Weekly_Sales"]
            .sum()
            .reset_index()
        )


        dfPreviousSales = dfPreviousSales.rename(
            columns={
               "Weekly_Sales":
               "Previous_Year_Sales"
            }
        )


        #merge forecastsales and previoussales
        dfPlot = dfForecastSales.merge(
            dfPreviousSales,
            on="WeekOfYear",
            how="left"
        )

        #sort by date
        dfPlot = dfPlot.sort_values("Date")

        #create plot
        fig, ax = plt.subplots(figsize=(15, 7))
        # Set background colours
        fig.set_facecolor("#070707")
        ax.set_facecolor("#070707") 

        plt.plot(
           dfPlot["Date"],
           dfPlot["Predicted_Sales"],
           color="red",
           linewidth=2,
           label="2013 Predicted Sales"
        )

        plt.title(
           "Random Forest - 2013 Sales Forecast",
           fontsize=16
        )
        
        ax.set_title(
           "Random Forest - 2013 Sales Forecast",
           fontsize=16,
           color="white"
        )

        ax.set_xlabel("Date", fontsize=12, color="white")
        ax.set_ylabel("Weekly Sales", fontsize=12, color="white")

        ax.legend(loc="best")
        ax.grid(True, alpha=0.3)
        plt.xlabel("Date")
        plt.ylabel("Weekly Sales")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.xticks(rotation=45, color="white")
        plt.yticks(color="white")
        plt.tight_layout()
        plt.figure(
            figsize=(15, 7)
        )

        plt.tight_layout()

       # Show plot in Streamlit
        conContainerTab15_Sub.pyplot(fig, use_container_width=True)

        expExpander4 = conContainerTab15_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander4")
        expExpander4.dataframe(dfPlot, use_container_width=True)
