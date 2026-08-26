import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import pathlib
import scipy.stats as stats
import matplotlib.pyplot as plt
import nbformat
from matplotlib.ticker import MultipleLocator
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
                                              
CNST_STR_SALES_COMBINED_DATASET = "assets/csv/Data/VisualisationFiles/Sales_Combined_DataSet_Visualisation.csv"
CNST_STR_FEATURES_DATASET = "assets/csv/Data/VisualisationFiles/Features_DataSet_Visualisation.csv"
CNST_STR_SALES_DATASET = "assets/csv/Data/VisualisationFiles/Sales_DataSet_Visualisation.csv"
CNST_STR_STORES_DATASET = "assets/csv/Data/VisualisationFiles/Stores_DataSet_Visualisation.csv"

#sidebar radio button control
radRadioButtons = None
#containers 
conContainerMain = None
conMainFooter1 = None
conMainFooter2 = None

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

conSection1Title = None
conSection2Title = None
conSection3Title = None
conSection4Title = None

conSection1Tab = None
conSection2Tab = None
conSection3Tab = None
conSection4Tab = None

conSectionFooter1 = None
conSectionFooter2 = None
conSectionFooter3 = None
conSectionFooter4 = None
conSectionFooter5 = None
conSectionFooter6 = None
conSectionFooter7 = None
conSectionFooter8 = None
conSectionFooter9 = None
conSectionFooter10 = None
conSectionFooter11 = None
conSectionFooter12 = None
conSectionFooter13 = None
conSectionFooter14 = None
conSectionFooter15 = None
conSectionFooter16 = None
#tab 1
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

#sliders for user interaction
sldSliderFrom1 = None
sldSliderFrom2 = None

#DataFrames vars for csv files for ML
dfSales = pd.DataFrame()
dfFeatures = pd.DataFrame()
dfStores = pd.DataFrame()

#DataFrames vars
dfSales_Combined_DataSet = pd.DataFrame()
dfSales_Combined_DataSet_Work = pd.DataFrame()
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

#other vars
lstStoreRanges  = list()
lstMarkdownColumns = list()
lstFeatures = list()
lstTemp = list()

intYear = 0
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
import os
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

st.title("Sales Analysis")
st.subheader("What We See In The Data")

#create page controls container why will it not stretch to fill the page???
conContainerMain = st.container(border=True, width="stretch", key="conMain", height="stretch" ) #height=780

#create footer container
conMainFooter1 = st.container(border=True, width="stretch", key="conMainFooter1", height=40 )
conMainFooter1.write("Created by Roger Williams - 2026")
conMainFooter2 = st.container(border=True, width="stretch", key="conMainFooter2", height=50 )
conMainFooter2.write("Each Page With A Plot Has A Data Table and Description - Use Scroll Bar On Right (Or Mouse Wheel If It Is Not Visible)" +
                     "To Move Down and See All Contents If Only Plot Visible")

#create sidebar
st.sidebar.title("Analysis Options",width="content",anchor="left")

#add radio button group for options
radRadioButtons = st.sidebar.radio("Select:", ["Overview", "Hypothesis 1 -4", "Hypothesis 5 - 8", "Hypothesis 9 - 11", "ML Test"], 
                                   index=0, key="radRadioButtons")

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
        conOverview.write("Provides insights into the performance of the business in key areas such as: " +
                          "sales trends and the impact of various externalfactors on sales.")
        conOverview.write("All analysis is done as requested based on the last 12 months of data")
        conOverview.write()
        conOverview.write("Analysis Produced:")
        conOverview.write("- Are sales increased if weather is hotter or colder in the last 12 months?")
        conOverview.write("- Sales differences between holiday and non-holiday weeks per store in the last 12 months")
        conOverview.write("- What is most profitable store type in the last 12 months?")
        conOverview.write("- Does store size affect profitability? If so, how much in the last 12 months?")
        conOverview.write("- What are the Weekly Sales by Store, Store Type and Department Last 12 Months?")
        conOverview.write("- What is the impact of markdowns on sales during holiday periods in the last 12 months by store?")
        conOverview.write("- What are the most profitable departments per store in the last 12 months?")
        conOverview.write("- What are the top 10 stores in terms of profitability in the last 12 months?")
        conOverview.write("- What are the bottom 10 stores in terms of profitability in the last 12 months?")
        conOverview.write("- What percentage of customers were unemployed per store by month for last year?")
        conOverview.write("- What percentage of customer were unemployed by store size last year?")  
        conOverview.write("- What are the predicted sales for stores by month for next year?")
   
        
   case "Hypothesis 1 -4": 
 #******tab 1*******  
        #plotly visualisation for hypothesis 1 - are sales increased if weather is hotter or colder in the last 12 months? 
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conSection1 = conContainerMain.container(border=False, width="stretch", key="conSection1", height=860)

        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab1, tabTab2, tabTab3, tabTab4 = conSection1.tabs([
          "Hypothesis 1", "Hypothesis 2", "Hypothesis 3", "Hypothesis 4"
        ])   
   
        conSection1Tab = tabTab1.container(border=True, width="stretch", height=780)
        conSection1Title = conSection1Tab.container(border=False, width="stretch", key="conSection1Title", height=40)
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
           xaxis_title="Temperature (Farenheit)",
           yaxis_title="Weekly Sales (£)", 
           title_x = 0.3, 
           plot_bgcolor="#070707", 
           paper_bgcolor ="#070707"
        )
                
        #remove after testing
        fig.update_xaxes(dtick=10)        # every 10 degrees
        fig.update_yaxes(dtick=100000)    # every 100,000 sales
        #end code copied from chatGPT

        conSection1Tab.plotly_chart(fig, use_container_width=True, key="figTab1") 
        expExpander5 =  conSection1Tab.expander("Show Data Used For Plot", expanded=False, key="expExpander5")
        expExpander5.dataframe(dfSales_Combined_DataSet_Work, use_container_width=True)
        conSection1Tab.write("Note: in order for the 'ticks' to show on the axes Plotly needs to be version 5.8 or higher") 
   
        conSectionFooter1 = conSection1Tab.container(border=False, width="stretch", key="conSectionFooter1", height=400)
        conSectionFooter1.write("As we can see from the above visualisation, there is a correlation between sales and weather.")
        conSectionFooter1.write("There is a clear variance at extreme parts of the temperature range and during the centre range of " + 
                                "temperature approximately 42-58 Fahrenheit. So clearly temperature is an effective factor in sales, " + 
                                "_but_ other factors could be at play such as the environmental conditions a particular store is in.")
        conSectionFooter1.write("Deeper analysis preferably by stores in a sales region would offer a better visualisation of the question. ")
         
 
 #******tab 2*******   
        #plotly visualisation for hypothesis 2 - Sales Differences Between holiday and Non Holiday Weeks per Store Over last 12 Months
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab2_Sub = tabTab2.container(border=True, width="stretch", key="conTab2Sub", height=780)
        conContainerTab2_Sub.info("Sales Differences Between Holiday and Non Holiday Weeks Per Store Over last 12 Months")
        #load into DataFrame copy for working with   
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()

        #create plot
        fig = px.box(dfSales_Combined_DataSet_Work,
           x="Store",
           y="Weekly_Sales",
           color="IsHoliday",
           title="Sales Differences Between Holiday and Non-Holiday Weeks Per Store Last 12 Months",
           labels={
              "IsHoliday": "Holiday Status",
              "Weekly_Sales": "Total Weekly Sales"
           },
           #set plot size
           height=500,
           width=1050
        )

        fig.update_layout(title_x = 0.15, 
                          xaxis_color="white",
                          yaxis_color="white", 
                          plot_bgcolor="#070707", 
                          paper_bgcolor ="#070707")        
        conContainerTab2_Sub.plotly_chart(fig, use_container_width=True, key="figTab2") 
        expExpander6 =  conContainerTab2_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander6")
        expExpander6.dataframe(dfSales_Combined_DataSet_Work, use_container_width=True)         
  
        conSectionFooter2 = conContainerTab2_Sub.container(border=False, width="stretch", key="conSectionFooter2", height=400)
        conSectionFooter2.write("Due to the large amount of data I chose a boxplot style visualisation to show the distribution of sales" +
                                "by store type. Also it allows us to see the outliers in the data and the variance of sales by store, which" +
                                "gives us a quick visual depiction of how holiday weeks affects sales directly.")
        conSectionFooter2.write("We can deduce that holiday weeks have a positive effect on sales, and that the variance of sales is greater" +
                                "during holiday weeks than non holiday weeks. Clearly store size also pays a relationship between holiday and" +
                                "non holiday sales volumes, but we can see simply and clearly the effect a holiday week has on footfall and sales.")

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
           height=400,
           width=800
        )

        #by default plotly will show 1B, 2B in the y axis so change it to something more understandable
        fig.update_yaxes(
           tickprefix="£",
           tickformat=","
        )      
 
        fig.update_layout(title_x = 0.3, 
                          xaxis_color="white",
                          yaxis_color="white", 
                          plot_bgcolor="#070707", 
                          paper_bgcolor ="#070707")          
        conContainerTab3_Sub.plotly_chart(fig, use_container_width=True, key="figTab3") 
        expExpander7 =  conContainerTab3_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander7")
        expExpander7.dataframe(dfSales_Combined_DataSet_StoreType, use_container_width=True)         
        conSectionFooter3 = conContainerTab3_Sub.container(border=False, width="stretch", key="conSectionFooter3", height=400)   
        conSectionFooter3.write("This simple yet direct visualisation show the direct difference between the store _types_ and sales.") 
        conSectionFooter3.write("It is clear that the type 1 store is the most profitable store type in the last 12 months, and that the" +
                                "type 3 store is the least profitable store type in the last 12 months, but being a different type may by " +
                                "nature have a smaller customer based, but does not imply that it is not a profitable one in comparision to" +
                                "its market and customer base.")

   
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
        #create plots
        intNum = 8
        
        for objStores in lstStoreRanges:
           #add row to new DataFrame
           dfSales_Combined_DataSet_SubSet = dfSales_Combined_DataSet_Work [
              dfSales_Combined_DataSet_Work["Store"].isin(objStores)
           ]

           fig, ax = plt.subplots(figsize=(20, 6))
           #set colours
           fig.set_facecolor("#070707")
           ax.set_facecolor("#070707") 
           ax.xaxis.label.set_color("white")
           ax.yaxis.label.set_color("white")
           ax.title.set_color("white")
           ax.tick_params(axis='x', colors='white')
           ax.tick_params(axis='y', colors='white')
                    
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
           expExpander8 =  conContainerTab4_Sub.expander("Show Data Used For Plot", expanded=False, key=f"expExpander{intNum}")
           expExpander8.dataframe(dfSales_Combined_DataSet_SubSet, use_container_width=True)         
           intNum += 1
       
        conSectionFooter4 = conContainerTab4_Sub.container(border=False, width="stretch", key="conSectionFooter4", height=400)
        conSectionFooter4.write("An interesting visualisation that shows the correlation between store size and sales. It is clear that there" +
                                "is a positive correlation between store size and sales, ")
        conSectionFooter4.write("but it is not a linear correlation, as we can see from the plot, and remember a smaller stores is not necessarily" +
                                "a less profitable store, as it may have a ")
        conSectionFooter4.write("smaller customer base, but is still profitable in its own right _but_ suggest additional analysis regarding " +
                                "store _type_ in correlation to size and sales would be a logical next step.")
        conSectionFooter4.write("In stores: 9, 19, 26, 37 all have high sales but store 26 is the highest. Further analysis of theses stores by" +
                                "_type_ could yield some fascinating insights.")  

         
   case "Hypothesis 5 - 8":                
  #******tab 5*******    
        #plotly visualisation for hypothesis 5 - Weekly Sales by Store Type, Store and Department For Last 12 Months
        conSection2 = conContainerMain.container(border=False, width="stretch", key="conSection2", height=860)
         
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab5, tabTab6, tabTab7, tabTab8 = conSection2.tabs([
          "Hypothesis 5", "Hypothesis 6", "Hypothesis 7", "Hypothesis 8"
        ])
     
        conSection2Tab = tabTab5.container(border=True, width="stretch", height=780)
        conSection2Title = conSection2Tab.container(border=False, width="stretch", key="conSection2Title", height=40)
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
           width=800,
           height=600,
           title_x = 0.3,
           xaxis_color="white",
           yaxis_color="white", 
           plot_bgcolor="#070707", 
           paper_bgcolor ="#070707")                       
 
        conSection2Tab.plotly_chart(fig, use_container_width=True, key="figTab5") 
        expExpander9 =  conSection2Tab.expander("Show Data Used For Plot", expanded=False, key="expExpander9")
        expExpander9.dataframe(dfSunburst_DataSet, use_container_width=True)         
        conSectionFooter5 = conSection2Tab.container(border=False, width="stretch", key="conSectionFooter5", height=400)
        conSectionFooter5.write("As you are aware this is more than a visualisation it is an interactive tools, whereby you can" +
                                "\"drill down\" into the details and experience the data in a more dynamic way.")
        conSectionFooter5.write("As we can see the visualisation is presented as a circular dial with the outer ring representing the" +
                                "weekly sales, next ring inwards is the store number then finally the centre ring is the store type.")
        conSectionFooter5.write("Hovering the mouse over any section exposes brief details")          
        conSectionFooter5.write("Now we can see each departments sales performance within that store, and as we can see when we hover the mouse" +
                                "over a department the information for that exact department.")
        conSectionFooter5.write("Also take note in the previous image the centre ring clearly shows that store type 1 has the most profitable" +
                                "stores, and that store type 3 has the least profitable stores, but as we have seen previously this does not" +
                                "mean that they are not profitable in their own right. ") 
 
 #******tab 6*******  
        #plotly visualisation for hypothesis 6 - Impact of markdowns on sales during holiday periods in the last 12 months by store
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab6_Sub = tabTab6.container(border=True, width="stretch", key="conTab6Sub", height=800)
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
           width=800,
           height=600,
           xaxis_color="white",
           yaxis_color="white", 
           plot_bgcolor="#070707", 
           paper_bgcolor ="#070707")                       
 
        conContainerTab6_Sub.plotly_chart(fig, use_container_width=True, key="figTab6") 
        expExpander10 = conContainerTab6_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander10")
        expExpander10.dataframe(dfSales_Combined_DataSet_Final, use_container_width=True)         
        conSectionFooter6 = conContainerTab6_Sub.container(border=False, width="stretch", key="conSectionFooter6", height=400)
        conSectionFooter6.write("This is a nice detailed yet not too complex visualisation that just as you have discovered is the same methodology")
        conSectionFooter6.write("as the previous visualisation in that it is interactive, so we can \"drill down\" into finer detail.")
        conSectionFooter6.write("As we can see when we hover the mouse over a markdown section we can see the store number, the markdown amount" +
                                "and the sales for that store during the holiday period.")
        conSectionFooter6.write("When we double click on a store number we can see detailed markdown information for the store:")
        conSectionFooter6.write("Interactive insights are great when dealing (as we are) with a lot of data e,g. number of stores and their" +
                                "departments, and act as a great presentation tool for internal Q&A session regarding store performance and" +
                                "profitability.")   
     
 
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
           title_x=0.3,  # Center the title
           font=dict(size=12),  # Set font size for better readability
           xaxis_color="white",
           yaxis_color="white", 
           plot_bgcolor="#070707", 
           paper_bgcolor ="#070707")                       


        conContainerTab7_Sub.plotly_chart(fig, use_container_width=True, key="figTab7") 
        expExpander11 = conContainerTab7_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander11")
        expExpander11.dataframe(dfSales_Combined_DataSet_HighestProfit, use_container_width=True)         
        conSectionFooter7 = conContainerTab7_Sub.container(border=False, width="stretch", key="conSectionFooter7", height=400)
        conSectionFooter7.write("The plot shows the departments with the highest total sales for store during last 12 months")
        conSectionFooter7.write("We can see that stores 13, 14 and 19 have the highest earning departments  ")
        conSectionFooter7.write("Would be interesting to ask the question as to how big those stores are, is there a correlation?")
              
        
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

        #add slider so user can play with the report
        sdlSliderFrom = conContainerTab8_Sub.slider("Select Amount of Stores", min_value=10, 
                                                    max_value=dfSales_Combined_DataSet_Work["Store"].nunique(), value=10, step=1, 
                                                    key="sdlSliderFrom1")

        #group by Store and get sum of Weekly_Sales
        dfSales_Combined_DataSet_Work = (
           dfSales_Combined_DataSet_Work
           .groupby("Store")["Weekly_Sales"]
           .sum()
           .sort_values(ascending=False)
           .head(sdlSliderFrom)
           .reset_index()
        )


        #need to handle plot differntly as matplotlib does not work in streamlit like ploty express
        ax = dfSales_Combined_DataSet_Work.plot(
           x="Store",
           y="Weekly_Sales",
           kind="barh",
           color="steelblue",
           figsize=(18, 6),
           legend=False
        )

        #sort dataset
        dfSales_Combined_DataSet_Work.sort_values("Weekly_Sales", ascending=False).head(sdlSliderFrom).plot(
           x="Store",
           y="Weekly_Sales",
           kind="barh",
           color="steelblue"   
        )

        #unique to matplotlib
        ax.set_title(f"Top {sdlSliderFrom} Stores By Sales For Last 12 Months")
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
        expExpander12 = conContainerTab8_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander12")
        expExpander12.dataframe(dfSales_Combined_DataSet_Work, use_container_width=True)         
     
        #get top 3 stores to show in footer
        lstTemp = dfSales_Combined_DataSet_Work.head(sdlSliderFrom)["Store"]

        conSectionFooter8 = conContainerTab8_Sub.container(border=False, width="stretch", key="conSectionFooter8", height=400)
        conSectionFooter8.write(f"The plot shows the top {sdlSliderFrom} stores by total sales for the last 12 months")   
        conSectionFooter8.write(f"We can see stores {lstTemp[0]}, {lstTemp[1]} and {lstTemp[2]} are the highest earners in this context ")  
        conSectionFooter8.write("This is simple plot can cause a number of analytical questins to be asked:")  
        conSectionFooter8.write("- What size are the stores?")  
        conSectionFooter8.write("- Does store size pay a factor in sales?")  
        conSectionFooter8.write("- What effect does the employent rate have on these stores?")  
      

       

   case "Hypothesis 9 - 11":     

   
#******tab 9*******  
        #plotly visualisation for hypothesis 9 - What are the bottom 10 stores in terms of profitability in the last 12 months?
        #Note: last year in data is: 2012
        conSection3 = conContainerMain.container(border=False, width="stretch", key="conSection3", height=860)
         
        #create tab control which houses containers for the tab data (split into columns!)        
        tabTab9, tabTab10, tabTab11 = conSection3.tabs([
          "Hypothesis 9", "Hypothesis 10", "Hypothesis 11"
        ])  

        conSection3Tab = tabTab9.container(border=True, width="stretch", height=780)
        conSection3Title = conSection3Tab.container(border=False, width="stretch", key="conSection3Title", height=40)      
        conSection3Title.info("What Are The Bottom 10 Stores In Terms Of Profitability In The Last 12 Months?")
  
 
        #make copy of DataFrame
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()
         
        #first filter by year 2012
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work['Date'].dt.year == 2012]
 
        #add slider so user can play with the report
        sdlSliderFrom = conSection3Tab.slider("Select Amount of Stores", min_value=10, max_value=dfSales_Combined_DataSet_Work["Store"].nunique(), 
                                              value=10, step=1, key="sdlSliderFrom2")

 
        #group by Store and get sum of Weekly_Sales
        dfSales_Combined_DataSet_Work = (
            dfSales_Combined_DataSet_Work
            .groupby("Store")["Weekly_Sales"]
            .sum()
            .sort_values(ascending=False)
            .tail(sdlSliderFrom)
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
        dfSales_Combined_DataSet_Work.sort_values("Weekly_Sales", ascending=False).head(sdlSliderFrom).plot(
           x="Store",
           y="Weekly_Sales",
           kind="barh",
           color="steelblue"   
        )
 
        #unique to matplotlib
        ax.set_title(f"Bottom {sdlSliderFrom} Stores By Sales For Last 12 Months")
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
        expExpander13 = conSection3Tab.expander("Show Data Used For Plot", expanded=False, key="expExpander13")
        expExpander13.dataframe(dfSales_Combined_DataSet_Work, use_container_width=True)      
        
        #get top 3 stores to show in footer
        lstTemp = dfSales_Combined_DataSet_Work.head(sdlSliderFrom)["Store"]
      
        conSectionFooter9 = conSection3Tab.container(border=False, width="stretch", key="conSectionFooter9", height=400) 
        conSectionFooter9.write(f"The plot shows the bottom {sdlSliderFrom} stores by total sales for the last 12 months")   
        conSectionFooter9.write(f"We can see stores {lstTemp[len(lstTemp)-1]}, {lstTemp[len(lstTemp)-2]} and {lstTemp[len(lstTemp)-3]} are the lowest earners in this context ")  
        conSectionFooter9.write("This is simple plot can cause a number of analytical questins to be asked:")  
        conSectionFooter9.write("- What size are the stores?")  
        conSectionFooter9.write("- Does store size pay a factor in sales?")  
        conSectionFooter9.write("- What effect does the employent rate have on these stores?")             
   
 
 #******tab 10*******  
        #plotly visualisation for hypothesis 10 - What was the unemployment percentage per store by month for last year?
        #Note: last year in data is: 2012
      
        #Note: in order for the "ticks" to show on the axes Plotly needs to be version 5.8 or higher
        conContainerTab10_Sub = tabTab10.container(border=True, width="stretch", key="conTab10Sub", height=780)
        conContainerTab10_Sub.info("What Was The Unemployment Percentage Per Store By Month For Last Year")
 
         #make copy of DataFrame
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet.copy()

        #filter by last 3 years data
        dfSales_Combined_DataSet_Work = dfSales_Combined_DataSet_Work[dfSales_Combined_DataSet_Work["Date"].dt.year ==2012] 
        dfSales_Combined_DataSet_Work["Month"] = (dfSales_Combined_DataSet_Work["Date"].dt.month)

        #use mean for the aggreagtion as sum will produce wierd results!
        dfSales_Combined_DataSet_Work = (
           dfSales_Combined_DataSet_Work
           .groupby(["Store", "Month"], as_index=False)
           ["Unemployment"]
           .mean()
        )

        #configure plot
        fig = px.line(
           dfSales_Combined_DataSet_Work,
           x="Month",
           y="Unemployment",
           color="Store",
           title="Percentage of Unemployed Customers Per Store By Month For Last Year",
           markers=True,
           height=500,
           width=800
        )

        fig.update_layout(
           xaxis_title="Month",
           yaxis_title="Unemployment Rate (%)",
           title_x=0.3,  # Centre the title
                          xaxis_color="white",
                          yaxis_color="white", 
                          plot_bgcolor="#070707", 
                          paper_bgcolor ="#070707")                       

        fig.update_xaxes(
           dtick="M1",  # Set tick interval to 1 month
           tickformat="%Y-%m",  # Format ticks as Year-Month
        )

        fig.update_yaxes(
           tickformat=".1f",  
        )
         #show plot
        
        conContainerTab10_Sub.plotly_chart(fig, use_container_width=True) 
        expExpander14 = conContainerTab10_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander14")
        expExpander14.dataframe(dfSales_Combined_DataSet_Work, use_container_width=True)           
        conSectionFooter10 = conContainerTab10_Sub.container(border=False, width="stretch", key="conSectionFooter10", height=400)
        conSectionFooter10.write("Show an interesting trend that months 3, 6 and 8 (March, June and August) have a peak in unemployment rates")  
        conSectionFooter10.write("This is an interesting insight as it shows that there is a correlation between the months and the unemployment" +
                                 "rates, across ALL stores. ")
        
 
 #******tab 11*******  
        #plotly visualisation for hypothesis 11 - What Was The Unemployment Percentage Per Store By Store Size Last Year?
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

        #use mean rather than sum as the figures are not reliable if used!
        dfSales_Combined_DataSet_Work = (
           dfSales_Combined_DataSet_Work
           .groupby(["Store", "YearMonth","Store_Size"], as_index=False)
           ["Unemployment"]
           .mean()
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
           title="What Was The Unemployment Percentage Per Store By Store Size Last Year?" 
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
           ),
           xaxis_color="white",
           yaxis_color="white", 
           plot_bgcolor="#070707", 
           paper_bgcolor ="#070707")                       
      
        #show plot       
        conContainerTab11_Sub.plotly_chart(fig, use_container_width=True) 
        expExpander15 = conContainerTab11_Sub.expander("Show Data Used For Plot", expanded=False, key="expExpander15")
        expExpander15.dataframe(dfSales_Combined_DataSet_Work, use_container_width=True)           
        conSectionFooter11 = conContainerTab11_Sub.container(border=False, width="stretch", key="conSectionFooter11", height=400)
        conSectionFooter11.write("Shows an interesting trend that store size is not a factor in the amount of unemployed customers per store")
        conSectionFooter11.write("What makes this plot so cool, is you move it around and articulate the data points yourself exposing insights" + 
                                 "that words could miss")
   
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
        fig, ax = plt.subplots(figsize=(18, 7))

        # Set background colours
        fig.set_facecolor("#070707")
        ax.set_facecolor("#070707")         
        
        #plot actual sales

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
        conSectionFooter12 = conSection4Tab.container(border=False, width="stretch", key="conSectionFooter12", height=400)
        conSectionFooter12.write("This a machine learning prediction, where using linear regression it attempts to predict last years sales")
        conSectionFooter12.write("As we can see its does follow the mean after a fashion and the nature of the model is evens out the values")
        conSectionFooter12.write("Hence no sudden spikes")
  
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
        fig, ax = plt.subplots(figsize=(18, 7))
        # Set background colours
        fig.set_facecolor("#070707")
        ax.set_facecolor("#070707")        

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
        conSectionFooter14 = conContainerTab13_Sub.container(border=False, width="stretch", key="conSectionFooter14", height=400)
        conSectionFooter14.write("This a machine learning prediction, where using random forest it attempts to predict last years sales")
        conSectionFooter14.write("As we can see it follows the trend more closely then the linear regression model, but still smooths the values")
        conSectionFooter14.write("It follows the evenly which is important when making decisions based on machine learning models.")
        
        
   
    
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
        fig, ax = plt.subplots(figsize=(18, 7))
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
        conSectionFooter15 = conContainerTab14_Sub.container(border=False, width="stretch", key="conSectionFooter15", height=400)
        conSectionFooter15.write("This a machine learning prediction, where using linear regression it attempts to predict sales for 2013")
        conSectionFooter15.write("As we can see it has some of spikes and troughs as the main data but seems a little erratic, which suggest" +
                                 "this might not be the best model for this application!")
        


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
        fig, ax = plt.subplots(figsize=(18, 7))
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
        conSectionFooter16 = conContainerTab15_Sub.container(border=False, width="stretch", key="conSectionFooter16", height=400)
        conSectionFooter16.write("This a machine learning prediction, where using random forest it attempts to predict sales for 2013")
        conSectionFooter16.write("As we can see unlike the linear regression model this one better fits the existing data patterns.")
        conSectionFooter16.write("This is the model I present as the prediction for 2013 sales")
