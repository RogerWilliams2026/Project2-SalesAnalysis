
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import scipy.stats as stats
import matplotlib.pyplot as plt
import nbformat
from matplotlib.ticker import MultipleLocator

#for experiment ML
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

from pathlib import Path
#
#  Created 28/07/2026 By Roger Williams
#  
#  for temperature hypothesis
#  
#  uses global var dfTemperature for visualisations
#  
#

CNST_STR_BASE_DIR = Path(__file__).resolve().parent


#VARS
radRadioButtons = None

conContainerMain = None
conContainerMainSub1 = None
conContainerMainSub2 = None
conContainerMainSub3 = None
conContainerMainSub4 = None
conContainerMainSub5 = None
conContainerMainSub6 = None
conContainerMainSub7 = None
conContainerMainSub8 = None
conContainerMainSub9 = None
conContainerMainSub10 = None
conContainerMainSub11 = None
conContainerMainSub12 = None
conContainerMainSub13 = None
conContainerMainSub14 = None
conContainerMainSub15 = None
conContainerMainSub16 = None

expExpander1 = None
expExpander2 = None
expExpander3 = None
expExpander4 = None


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

tabHypothesis = None

txtText = None
figPlot = None

dictDataFrames = dict()
dictWhat = dict()
dictTransform = dict()


dfTemp = pd.DataFrame()
dfTemp2 = pd.DataFrame()
dfTemp3 = pd.DataFrame()
dfTemp4 = pd.DataFrame()

#used for ML plots
dfSales_Analysis = pd.DataFrame()
dfFeatures_DataSet_Visualisation = pd.DataFrame()
dfSales_DataSet_Visualisation = pd.DataFrame()
#used for all other plots
dfSales_Combined_DataSet_Visualisation = pd.DataFrame()

#other vars
intYear = 0
intStartYear = 0
intEndYear = 0
intNum = 0

#get correct path to csv file
strcsvFilePath = CNST_STR_BASE_DIR / "assets" / "csv" / "Data" / "Sales_Combined_DataSet_Visualisation.csv"
strcssFilePath = CNST_STR_BASE_DIR / "assets" / "css" / "style.css"
strPipelinePath_LinReg2013 = CNST_STR_BASE_DIR / "assets" / "csv" / "pipelines" / "linear_regression_2013_pipeline.pkl"
strPipelinePath_LinReg = CNST_STR_BASE_DIR / "assets" / "csv" / "pipelines" / "linear_regression_pipeline.pkl"
strPipelinePath_RandomForest2013 = CNST_STR_BASE_DIR / "assets" / "csv" / "pipelines" / "random_forest_2013_pipeline.pkl"
strPipelinePath_RandomForest = CNST_STR_BASE_DIR / "assets" / "csv" / "pipelines" / "random_forest_pipeline.pkl"

# Function to load custom CSS
def funcLoadCSS(fileName):
    with open(fileName) as fileCSS:
        st.markdown(f"<style>{fileCSS.read()}</style>", unsafe_allow_html=True)


#******** main code ********

#load csv from visualisation folder
dfSales_Combined_DataSet_Visualisation = pd.read_csv(strcsvFilePath)
#transform Date to datetime
dfSales_Combined_DataSet_Visualisation["Date"] = pd.to_datetime(dfSales_Combined_DataSet_Visualisation["Date"], format="%d/%m/%Y")
#sprinkle a little feature engineering to make better plots
dfSales_Combined_DataSet_Visualisation["Year"] = dfSales_Combined_DataSet_Visualisation["Date"].dt.year
dfSales_Combined_DataSet_Visualisation["month_label"] = dfSales_Combined_DataSet_Visualisation["Date"].dt.strftime("%d") + " " + dfSales_Combined_DataSet_Visualisation["Date"].dt.month_name()  

#get year min/max values
intStartYear = dfSales_Combined_DataSet_Visualisation["Year"].min()
intEndYear = dfSales_Combined_DataSet_Visualisation["Year"].max()

#init streamlit dashboard 

# Load the CSS file
funcLoadCSS(strcssFilePath)

#configure streamlit page
st.set_page_config(
   page_title = "Project 2 - Sales Analysis",
   page_icon =":temperature:",
   layout = "wide",
   initial_sidebar_state = "expanded"
)
 
st.session_state.sidebar_state = 'expanded'
 
# if: @st.cache_data  - put before function means if run any results are reused i.e. on loading data

#key does NOT create a HTML id just a link to the current page session for reading current values e.g.
#st.session_state.<key name>
#useful if using mutiple widgets of the same type


st.title("Project 2 - Sales Analysis")
st.subheader("Continuisation of Sales Analysis")

#create page controls container
conContainerMain = st.container(border=True, width="stretch", key="conMain", height="stretch" ) #height=780

#create sidebar
st.sidebar.title("Analysis Options",width="content",anchor="left")

#add radio button group for options
radRadioButtons = st.sidebar.radio("Select:", ["Overview", "Hypothesis"])

#populate container with page controls
if radRadioButtons == "Overview":
   conContainerMain.info("Overview")  
   # conContainerMain.markdown("<div style='background-color:#222; color:#00FF00; padding:10px; border-radius:5px;'>"
   #  "This is green text on a dark background"
   #  "</div>",
   #  unsafe_allow_html=True)
   conContainerMain.markdown("### What Validates This Test?")
   conContainerMain.write("This test came about after the Met office declared the first heatwave. Was it **really** a heatwave? The event lasted"
                          "for four days, then temperatures seemed to cool slightly (but not by much), then same happened again the next week.")
   conContainerMain.write("Hmmmm.. I thought is this a 'coincidence' that two heatwaves occur back-to-back or is it simply Summer?")
   conContainerMain.write(" ")
   conContainerMain.write("On the 'Hypothesis' page I dig deep into the data and attempt to answer this question!")
 
   
else:
   conContainerMain.info("Hypothesis")  
   
   #create tab control which houses containers for the tab data (split into columns!)
   
   tabTab1, tabTab2, tabTab3, tabTab4, tabTab5, tabTab6, tabTab7, tabTab8 = conContainerMain.tabs([
       f"Basic Plots {dfSales_Combined_DataSet_Visualisation['Year'].max() - 4} To {dfSales_Combined_DataSet_Visualisation['Year'].max()}", 
       f"Deeper Plots {dfSales_Combined_DataSet_Visualisation['Year'].max() -4}/{dfSales_Combined_DataSet_Visualisation['Year'].max()}", 
       f"Q-Q Plots {dfSales_Combined_DataSet_Visualisation['Year'].max() -4} To {dfSales_Combined_DataSet_Visualisation['Year'].max()}", 
       f"Tests {dfSales_Combined_DataSet_Visualisation['Year'].max() -4} To {dfSales_Combined_DataSet_Visualisation['Year'].max()}", 
       "6 Year Analysis Plot","6 Year Data Tables",
       "Grand Experiment",
       "Conclusion"    
   ])
          
      
   
#******tab 1*******  
   
   #create sub container for plots for 2 col  tab 1
   conContainerMainSub1 = tabTab1.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT, key="conTab1")
   conContainerMainSub2 = conContainerMainSub1.container(border=True,width="stretch",height=40, key="conTab1Title")
   conContainerMainSub3 = conContainerMainSub1.container(border=True,width="stretch",height=modGlobal.CNST_INT_INNER_CONTAINTER_HEIGHT)
   #create columns for charts
   col1Tab1, col2Tab1 = conContainerMainSub3.columns(2, gap="xsmall")   

   #configure column 1
   conContainerMainSub2.write("Average Temperature Values June To August For 6 Years!")
   #create plot
   dfTemp = dfSales_Combined_DataSet_Visualisation.copy()
   intYear = 0
   intNum = 1


  #show plot
  # conContainerMainSub12.plotly_chart(fig, use_container_width=True, width="stretch", height="stretch")



 #******tab 2*******   
   #create sub container for plots for 2 col  tab 1
   conContainerMainSub4 = tabTab2.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT, key="conTab2")
  # conContainerMainSub2 = conContainerMainSub1.container(border=True,width="stretch",height=40, key="conTab1Title")
   conContainerMainSub5 = conContainerMainSub4.container(border=True,width="stretch",height=modGlobal.CNST_INT_INNER_CONTAINTER_HEIGHT)
   #create columns for charts
   col1Tab2, col2Tab2 = conContainerMainSub5.columns(2, gap="xsmall")   
  
  
   #configure column 2
   conContainerMainSub4.write("Average Temperature Values June To August For 6 Years!")
   #create plot
   dfTemp = dfSales_Combined_DataSet_Visualisation.copy()


#******tab 3*******  

   #create sub container for plots for col 1 tab 2
   conContainerMainSub6 = tabTab3.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT, key="conTab3")
   conContainerMainSub7 = conContainerMainSub6.container(border=True,width="stretch", height=40, key="conTab2Title")
   conContainerMainSub8 = conContainerMainSub6.container(border=True,width="stretch",height=modGlobal.CNST_INT_INNER_CONTAINTER_HEIGHT)
   #create columns for charts
   col1Tab3, col2Tab3 = conContainerMainSub8.columns(2, gap="xsmall")  
       
   conContainerMainSub4.write(f"Q-Q Plots June To August For{intYear -4}/{modGlobal.dfTemperature['Year'].max()}") 
   
            
   
   
 #******tab 4*******    
            
   #create sub container in tab 4
   conContainerMainSub9 = tabTab4.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT, key="conTab4")
   conContainerMainSub10 = conContainerMainSub9.container(border=True,width="stretch", height=40, key="conTab3Title")
   conContainerMainSub11 = conContainerMainSub9.container(border=True,width="stretch",height=modGlobal.CNST_INT_INNER_CONTAINTER_HEIGHT)
   #create columns for charts
   col1Tab4, col2Tab4 = conContainerMainSub11.columns(2, gap="xsmall")  
 
   conContainerMainSub10.write(f"Average Temperature Values June To August For{modGlobal.dfTemperature['Year'].min()}/{modGlobal.dfTemperature['Year'].max()}") 
    
   #configure column 1

         
          
 #******tab 5*******  
 
   #create sub container for tab 4
   conContainerMainSub12 = tabTab5.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT)
   # #create columns for charts
  # col1Tab4, col2Tab4 = conContainerMainSub6.columns(2, gap="xsmall")  
  
   dfTemp = modGlobal.dfTemperature.copy()



  # conContainerMainSub12.plotly_chart(fig, use_container_width=True, width="stretch", height="stretch")
 
       
 #******tab 6*******   
 
   #create sub container for tab 6
   conContainerMainSub13 = tabTab6.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT)
    # #create columns for datatables
   col1Tab5, col2Tab5 = conContainerMainSub13.columns(2, gap="xsmall")  
   



 #******tab 7*******   
 
   #create sub container for tab 7
   conContainerMainSub14 = tabTab7.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT)
   
   #experiment ML test can it predict next years values?
   
 #linear regression
 
   #init test dataframe
   dfTemp = modGlobal.dfTemperature.copy()
 

      
#******tab 8*******   
 
   #create sub container for tab 8
   conContainerMainSub15 = tabTab8.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT)
   conContainerMainSub15.write("Conclusion")   
    
