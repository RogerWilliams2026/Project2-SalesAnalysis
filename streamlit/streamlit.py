
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import pathlib
import scipy.stats as stats
import matplotlib.pyplot as plt

#use custom module
import modGlobal
import modETL_Library as modETL
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

#
#  Created 28/07/2026 By Roger Williams
#  
#  for temperature hypothesis
#  
#  uses global var dfTemperature for visualisations
#  
#

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


fltSkew = 0.0
fltKurtosis = 0.0
intYear = 0
intStartYear = 0
intEndYear = 0
intNum = 0


# Function to load custom CSS
def funcLoadCSS(fileName):
    with open(fileName) as fileCSS:
        st.markdown(f"<style>{fileCSS.read()}</style>", unsafe_allow_html=True)


#******** main code ********

#try and load csv from visualisation folder
dictWhat = modETL.funcReadVisualisationFilesReturnDictionary()

if dictWhat is None:
   quit;

modGlobal.dfTemperature = dictWhat["birminghamtemperature_01012000_15082026" + modGlobal.CNST_STR_FILENAME_APPEND_VISUALISATION + ".csv"] 
#transform date column to date
dictTransform["date"] = "pandasdatetime"
#transform!
modGlobal.dfTemperature = modETL.funcTransformValues(modGlobal.dfTemperature,dictTransform)
#sprinkle a little feature engineering to make better plots
modGlobal.dfTemperature["Year"] = modGlobal.dfTemperature["date"].dt.year
modGlobal.dfTemperature["month_label"] = modGlobal.dfTemperature["date"].dt.strftime("%d") + " " + modGlobal.dfTemperature["date"].dt.month_name()  

#get year min/max values
intStartYear = modGlobal.dfTemperature["Year"].min()
intEndYear = modGlobal.dfTemperature["Year"].max()

#init streamlit dashboard 
# Load the CSS file
funcLoadCSS(pathlib.Path(modGlobal.CNST_STR_CSS_ROOTPATH))

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


st.title("Temperature Hypothesis Test")
st.subheader("Is It Summer Or A Heatwave?")

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
       f"Basic Plots {modGlobal.dfTemperature['Year'].max() - 4} To {modGlobal.dfTemperature['Year'].max()}", 
       f"Deeper Plots {modGlobal.dfTemperature['Year'].max() -4}/{modGlobal.dfTemperature['Year'].max()}", 
       f"Q-Q Plots {modGlobal.dfTemperature['Year'].max() -4} To {modGlobal.dfTemperature['Year'].max()}", 
       f"Tests {modGlobal.dfTemperature['Year'].max() -4} To {modGlobal.dfTemperature['Year'].max()}", 
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

   #conContainerMainSub2.error("Average Temperature Values June To August For 6 Years!")
    
   #configure column 1
   conContainerMainSub2.write("Average Temperature Values June To August For 6 Years!")
   #create plot
   dfTemp = modGlobal.dfTemperature.copy()
   intYear = 0
   intNum = 1

   #print first 3 dataframes in each column 
   for intYear in range(intEndYear-4,intEndYear +1):
       #show data tables for each year in the data
       dfTemp = modGlobal.dfTemperature.loc[ modGlobal.dfTemperature["date"].between(pd.Timestamp(f"{intYear}-06-01"), pd.Timestamp(f"{intYear} -08-31")) ,["date","tmin","tmax","tavg","Year"] ]            
       #filter for intYear
       dfTemp = dfTemp.loc[ dfTemp["date"].between(pd.Timestamp(f"{intYear}-06-01"), pd.Timestamp(f"{intYear}-08-31")) ,["date","tmin","tmax","tavg","Year"] ] 
      
       fig = px.area(
             dfTemp,
             x="date",
             y="tavg",
             markers=True,
             height=280,
             width=260,
             title=f"Average Temperature Values June To August For {intYear}"
          )      
 
       plt.style.use("dark_background")
       #set axis labels   
       fig.update_layout(xaxis_title="Date", yaxis_title="Average Temperature", template="plotly_dark")  
 
       #attempt to centre title    
       fig.update_layout(title_x = 0.13)  
       
       if intYear > intEndYear -2:
          col2Tab1.plotly_chart(fig, use_container_width=True)
          #create expander and populate with dataframe
          expExpander1 = col2Tab1.expander("Show Data Table",key=f"expTab1-{intNum}")
          expExpander1.dataframe(dfTemp[["date","tmin","tmax","tavg"] ])
       else:
          col1Tab1.plotly_chart(fig, use_container_width=True)
          #create expander and populate with dataframe
          expExpander1 = col1Tab1.expander("Show Data Table",key=f"expTab1-{intNum}")
          expExpander1.dataframe(dfTemp[["date","tmin","tmax","tavg"] ])          
          
       intNum += 1

   #configure column 2
   #col2Tab1.error("Average Temperature Values June To August  For 2025 and 2026")

   # #create combined plot for 2025 and 2026
 

   # fig = px.line(
   #    dfTemp2,
   #    x="month_label",
   #    y="tavg",
   #    color="Year",
   #    markers=True,
   #    height=280,
   #    title="Average Temperature Values June To August  For 2025 and 2026"
   # )

   # fig.update_xaxes(type="category")
   # fig.update_layout(xaxis_title="Day of Month", yaxis_title="Average Temperature")
   
   # col2Tab1.plotly_chart(fig, use_container_width=True)
  
  
   # #move down 2 lines so chart in line woth 2nd chart in col 1!
   # col2Tab1.write("  ")
   # col2Tab1.write("  ")
   # col2Tab1.write("  ")

 #******tab 2*******   
   #create sub container for plots for 2 col  tab 1
   conContainerMainSub4 = tabTab2.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT, key="conTab2")
  # conContainerMainSub2 = conContainerMainSub1.container(border=True,width="stretch",height=40, key="conTab1Title")
   conContainerMainSub5 = conContainerMainSub4.container(border=True,width="stretch",height=modGlobal.CNST_INT_INNER_CONTAINTER_HEIGHT)
   #create columns for charts
   col1Tab2, col2Tab2 = conContainerMainSub5.columns(2, gap="xsmall")   
  
  

   #print first 3 dataframes in each column 
   for intYear in range(intEndYear -4,intEndYear):  
       dfTemp = modGlobal.dfTemperature.loc[ modGlobal.dfTemperature["Year"] .isin([intYear, intEndYear]),
                                           ["date","tmin","tmax","tavg","Year","month_label"] ]            

       fig = px.line(
          dfTemp,
          x="month_label",
          y="tavg",
          color="Year",
          markers=True,
          height=280,
          title=f"Comparing Average Temperature Values June To August For {intEndYear} Against {intYear}"
       )

       plt.style.use("dark_background")
       fig.update_xaxes(type="category")
       fig.update_layout(xaxis_title="Day of Month", yaxis_title="Average Temperature", template="plotly_dark") 
      
       if intYear > intEndYear -3:
          col2Tab2.plotly_chart(fig, use_container_width=True)
       else:
          col1Tab2.plotly_chart(fig, use_container_width=True)

#******tab 3*******  

   #create sub container for plots for col 1 tab 2
   conContainerMainSub6 = tabTab3.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT, key="conTab3")
   conContainerMainSub7 = conContainerMainSub6.container(border=True,width="stretch", height=40, key="conTab2Title")
   conContainerMainSub8 = conContainerMainSub6.container(border=True,width="stretch",height=modGlobal.CNST_INT_INNER_CONTAINTER_HEIGHT)
   #create columns for charts
   col1Tab3, col2Tab3 = conContainerMainSub8.columns(2, gap="xsmall")  
       
   conContainerMainSub4.write(f"Q-Q Plots June To August For{intYear -4}/{modGlobal.dfTemperature['Year'].max()}") 
   
   
   #print first 3 dataframes in each column 
   for intYear in range(intEndYear -4,intEndYear +1):   
       dfTemp = modGlobal.dfTemperature[ modGlobal.dfTemperature["Year"] == intYear ]
       #create Q-Q plot
       fig, axis = plt.subplots(figsize=(14,11))
       plt.style.use("dark_background")

       stats.probplot(dfTemp["tavg"], dist="norm", plot=axis)
       #set title and font size
       axis.set_title(f"Q-Q Plot For Average Temperature June To August For {intYear}")
       axis.title.set_fontsize(20)
       axis.set_xlabel(f"Q-Q Plot For Average Temperature {intYear}")
       axis.set_ylabel("Theoretical Quantiles")
       #set axis ticks seems to be a fixed fraction of maximum value e.g. trial and error!
       axis.yaxis.set_minor_locator(MultipleLocator(0.5))
       axis.tick_params(axis='y', which='minor', length=4, width=1.2)
       
       if intYear > intEndYear -2:
          #show plot
          col2Tab3.pyplot(fig, use_container_width=True)
          #create shapiro wilk test
          shapiro_stat, shapiro_probability = stats.shapiro(dfTemp["tavg"])
          col2Tab3.write(f"Shapiro Wilk Test Probability: {shapiro_probability:.2f}")
          col2Tab3.write("If < 0.05 (alpha) Hypothesis Zero NOT met")
          col2Tab3.write("If > 0.05 (alpha) Hypothesis Zero MET") 
       else:
          #show plot
          col1Tab3.pyplot(fig, use_container_width=True)
          #create shapiro wilk test
          shapiro_stat, shapiro_probability = stats.shapiro(dfTemp["tavg"])
          col1Tab3.write(f"Shapiro Wilk Test Probability: {shapiro_probability:.2f}")
          col1Tab3.write("If < 0.05 (alpha) Hypothesis Zero NOT met")
          col1Tab3.write("If > 0.05 (alpha) Hypothesis Zero MET")             
   
   
 #******tab 4*******    
            
   #create sub container in tab 4
   conContainerMainSub9 = tabTab4.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT, key="conTab4")
   conContainerMainSub10 = conContainerMainSub9.container(border=True,width="stretch", height=40, key="conTab3Title")
   conContainerMainSub11 = conContainerMainSub9.container(border=True,width="stretch",height=modGlobal.CNST_INT_INNER_CONTAINTER_HEIGHT)
   #create columns for charts
   col1Tab4, col2Tab4 = conContainerMainSub11.columns(2, gap="xsmall")  
 
   conContainerMainSub10.write(f"Average Temperature Values June To August For{modGlobal.dfTemperature['Year'].min()}/{modGlobal.dfTemperature['Year'].max()}") 
    
   #configure column 1

   #print first 3 dataframes in each column 
   for intYear in range(intEndYear -4,intEndYear +1):  
       #compare inyear data with current year data
       dfTemp = modGlobal.dfTemperature.loc[ modGlobal.dfTemperature["date"].between(pd.Timestamp(f"{intYear}-06-01"), pd.Timestamp(f"{intYear}-08-31")) ,["tavg"] ] 
       dfTemp2 = modGlobal.dfTemperature.loc[ modGlobal.dfTemperature["date"].between(pd.Timestamp(f"{intEndYear}-06-01"), pd.Timestamp(f"{intEndYear}-08-31")) ,["tavg"] ] 
      
       statUValue, statPValue = stats.ttest_ind(dfTemp, dfTemp2, equal_var=False)  

       if intYear > intEndYear -2:  
          col2Tab4.write("  ")
          col2Tab4.markdown(f"### Parametric T-Test For June To August For {intYear}:")
          col2Tab4.write(f"Parametric Test P Value: {statPValue[0]:.2f}")
          col2Tab4.write(f"Parametric Test U P Value: {statUValue[0]:.2f}")
          
          col2Tab4.markdown(f"### Non Parametric T-Test For June To August For {intYear}:")
          statUValue, statPValue = stats.mannwhitneyu(dfTemp, dfTemp2, alternative="two-sided")
          col2Tab4.write(f"Non Parametric Test P Value: {statPValue[0]:.2f}")
          col2Tab4.write(f"Non Parametric Test U Value: {statUValue[0]:.2f}")

          #get skew
          fltSkew = dfTemp["tavg"].skew()
          #get kurtosis
          fltKurtosis = dfTemp["tavg"].kurtosis()
         
          col2Tab4.markdown("### Skew and Kurtosis:")
          
          if fltSkew > 1:
                col2Tab4.write(f"Skew: {fltSkew:.2f} - Highly Positively Skewed Kurtosis: {fltKurtosis:.2f}")
          elif fltSkew < 0:    
                col2Tab4.write(f"Skew: {fltSkew:.2f} - Highly Negatively Skewed Kurtosis: {fltKurtosis:.2f}")
          else:
                col2Tab4.write(f"Skew: {fltSkew:.2f} - Approximately Symmetrical Kurtosis: {fltKurtosis:.2f}")             
       else:
           col1Tab4.write("  ")
           col1Tab4.markdown(f"### Parametric T-Test For June To August For {intYear}:")
           col1Tab4.write(f"Parametric Test P Value: {statPValue[0]:.2f}")
           col1Tab4.write(f"Parametric Test U P Value: {statUValue[0]:.2f}")
           
           col1Tab4.markdown(f"### Non Parametric T-Test For June To August For {intYear}:")
    
           statUValue, statPValue = stats.mannwhitneyu(dfTemp, dfTemp2, alternative="two-sided")
           col1Tab4.write(f"Non Parametric Test P Value: {statPValue[0]:.2f}")
           col1Tab4.write(f"Non Parametric Test U Value: {statUValue[0]:.2f}")
        
           #get skew
           fltSkew = dfTemp["tavg"].skew()
           #get kurtosis
           fltKurtosis = dfTemp["tavg"].kurtosis()
           col1Tab4.markdown("### Skew and Kurtosis:")
         
           if fltSkew > 1:
                 col1Tab4.write(f"Skew: {fltSkew:.2f} - Highly Positively Skewed Kurtosis: {fltKurtosis:.2f}")
           elif fltSkew < 0:    
                 col1Tab4.write(f"Skew: {fltSkew:.2f} - Highly Negatively Skewed Kurtosis: {fltKurtosis:.2f}")
           else:
                 col1Tab4.write(f"Skew: {fltSkew:.2f} - Approximately Symmetrical Kurtosis: {fltKurtosis:.2f}")           
          
 #******tab 5*******  
 
   #create sub container for tab 4
   conContainerMainSub12 = tabTab5.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT)
   # #create columns for charts
  # col1Tab4, col2Tab4 = conContainerMainSub6.columns(2, gap="xsmall")  
  
   dfTemp = modGlobal.dfTemperature.copy()
   #dfTemp2 = modGlobal.dfTemperature.copy()
       
   #sprinkle some feature engineering     
   dfTemp["Year"] = dfTemp["date"].dt.year.astype(int)
   dfTemp["month_label"] = dfTemp["date"].dt.strftime("%d") + " " + dfTemp["date"].dt.month_name() 

   #select columns for plot
   dfTemp = dfTemp[ ["tavg","month_label","Year","date"] ]
    
   #create slider so user can set year range manually
   sldSelectedYear = conContainerMainSub12.slider(
      f"Select Year Range (From {intEndYear -4} To {dfTemp['Year'].max()})",
      min_value=dfTemp["Year"].min(),
      max_value=dfTemp["Year"].max(),
      value=dfTemp["Year"].max(),
      step=1
   )

   # Filter data based on slider
   dfTemp_FilteredByYear = dfTemp[ dfTemp["Year"].between(dfTemp["Year"].max() - 4, sldSelectedYear) ]
 
   fig = px.scatter_3d(
      dfTemp_FilteredByYear,
      x="Year",
      y="tavg",
      z="month_label",
      color="Year",
     # markers=True,
      height=580,
      title=f"Average Temperature Values June and July For 2022 To {sldSelectedYear}" 
   )

   fig.update_xaxes(type="category")
   #label axis
   fig.update_layout(scene = dict(
        xaxis_title="Year",
        yaxis_title="Average Temperature",
        zaxis_title="Day of Month"
    ))
  
   plt.style.use("dark_background")

   conContainerMainSub12.plotly_chart(fig, use_container_width=True, width="stretch", height="stretch")
 
       
 #******tab 6*******   
 
   #create sub container for tab 6
   conContainerMainSub13 = tabTab6.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT)
    # #create columns for datatables
   col1Tab5, col2Tab5 = conContainerMainSub13.columns(2, gap="xsmall")  
   
   #print first 3 dataframes in each column 
   for intYear in range(intEndYear -4,dfTemp["Year"].max() + 1):
       #show data tables for each year in the data
       dfTemp2 = modGlobal.dfTemperature.loc[ modGlobal.dfTemperature["date"].between(pd.Timestamp(f"{intYear}-06-01"), pd.Timestamp(f"{intYear} -08-31")) ,["date","tmin","tmax","tavg"] ] 
       
       if intYear in range(intEndYear -1, dfTemp["Year"].max() +1):
          col2Tab5.write(f"Data Tables For June To August For {intYear}")
          col2Tab5.dataframe(dfTemp2,height=300)
       else:
          col1Tab5.write(f"Data Tables For June To August For {intYear}")
          col1Tab5.dataframe(dfTemp2,height=300)
       #column 2


 #******tab 7*******   
 
   #create sub container for tab 7
   conContainerMainSub14 = tabTab7.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT)
   
   #experiment ML test can it predict next years values?
   
 #linear regression
 
   #init test dataframe
   dfTemp = modGlobal.dfTemperature.copy()
   
   #regression does not handle dates so need to split the date into day and month as new features
   dfTemp["day"] = dfTemp["date"].dt.day
   dfTemp["month"] = dfTemp["date"].dt.month

   #init validation dataframe
   dfTemp2 = dfTemp.copy()
   
   #filter the dataframe to use only june to august
   ##dfTemp = dfTemp[dfTemp["month"].between(6,8)]
   #filter validation dataframe
   dfTemp2 = dfTemp2[dfTemp2["month"].between(6,8)]
   dfTemp2 = dfTemp2[dfTemp2["Year"] > 2024]

  
   features = ['tmin', 'tmax','day','month','Year']

   train = dfTemp[dfTemp["Year"] <= 2024] # & dfTemp["month"].between(6,8)]
   test = dfTemp[dfTemp ["Year"].between(2024,2025)] # & dfTemp["month"].between(6,8)]

   X_train = train[features]
   y_train = train["tavg"]

   X_test = test[features]
   y_test = test["tavg"] # y_test = test["tavg"]

   model = LinearRegression()
   model.fit(X_train, y_train)

   predictions = model.predict(X_test)


   #show mae and rmse values
   mae = mean_absolute_error(y_test, predictions)
   rmse = np.sqrt(mean_squared_error(y_test, predictions))

   conContainerMainSub14.write(f"RMSE: {rmse}")
   conContainerMainSub14.write(f"MAE: {mae}")
   
   matches = (dfTemp["month"] == 6) & (dfTemp["Year"] > 2024 ) 
   
   #predictions["month"] = 
   conContainerMainSub14.write(predictions)
   conContainerMainSub14.write(matches)     
      
   
   
   # #show predicated june-august 2026 temperatures
   # conContainerMainSub14.write(predictions)
   # #show actual june-august 2026 temperatures
   # conContainerMainSub14.write(dfTemp2["tavg"].values)   


   
   #show values in a plot
   # plt.figure(figsize=(24, 12))

   # plt.plot(
   #    dfTemp["date"],
   #    dfTemp["tavg"],
   # )

   # plt.xlabel("Date")
   # plt.ylabel("Predicted Average Temperature")
   # plt.title(f"Predicted Average Temperature for 2026")
   # plt.style.use("dark_background")

   # conContainerMainSub14.pyplot(plt) #

   #ordinary least sqaures regression
   #filter the dataframe to use only june to august

   #ols regression
   ols_model = smf.ols(
      formula="tavg ~ day + month + Year",
      data=dfTemp
   ).fit()

   #use ols summary html as looks better than the as_text option!
   conContainerMainSub14.html( 
      ols_model.summary().as_html(),
   )

   X = dfTemp[features]
   y = dfTemp["tavg"]


   #add stratify=y ONLY if dealing with a class/category as this is a continuous variable which can have
   #duplicates don't add!
   X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.2, random_state=42
   )

   conContainerMainSub14.write(f"Training Rows: {len(X_train)}")    
   conContainerMainSub14.write(f"Test Rows: {len(X_test)}")    
   
   dfTemp3 = predictions.copy()

   
   conContainerMainSub14.write("Predictions DataFrame")
   conContainerMainSub14.dataframe(dfTemp3)
   conContainerMainSub14.write("Validation DataFrame")
   conContainerMainSub14.dataframe(dfTemp2)
   # fig = px.line(
   # predictions,
   # x="month_label",
   # y="tavg",
   # color="Year",
   # markers=True,
   # height=280,
   # title=f"Predicted Average Temperature Values June To August For {intEndYear} Against {intYear}"
   # )

   # plt.style.use("dark_background")
   # fig.update_xaxes(type="category")
   # fig.update_layout(xaxis_title="Day of Month", yaxis_title="Average Temperature", template="plotly_dark") 

   # if intYear > intEndYear -3:
   #    conContainerMainSub14.plotly_chart(fig, use_container_width=True)
      
#******tab 8*******   
 
   #create sub container for tab 8
   conContainerMainSub15 = tabTab8.container(border=False,width="stretch",height=modGlobal.CNST_INT_CONTAINTER_HEIGHT)
   conContainerMainSub15.write("Conclusion")   
    
   


   # conContainerMainSub15.dataframe(dfTemp[["date","tmin","tmax","tavg"]],height=300)
   #conContainerMainSub15.write("Test temperatures:", len(y))
   #conContainerMainSub15.write("  intercept:", model.intercept_)
   #conContainerMainSub15.write("  coefficients:", model.coef_)
   #conContainerMainSub15.write("  actually survived:", int(y.sum()))
   #conContainerMainSub15.write("  actually died:    ", int((y == 0).sum()))
   #conContainerMainSub15.write()
   #conContainerMainSub15.write("Accuracy: {:.4f}".format(accuracy_score(y, predictions)))
    
   
   
   
   # model.fit(X_train, y_train)
   # model.score(X_train, y_train)

   # predictions = model.predict(X_test)
   # probabilities = model.predict_proba(X_test)[:, 1]


   # conContainerMainSub15.write("Test temperatures:", len(y_test))
   # conContainerMainSub15.write("  intercept:", model.intercept_)
   # conContainerMainSub15.write("  coefficients:", model.coef_)
   # conContainerMainSub15.write("  actually survived:", int(y_test.sum()))
   # conContainerMainSub15.write("  actually died:    ", int((y_test == 0).sum()))
   # conContainerMainSub15.write()
   # conContainerMainSub15.write("Accuracy: {:.4f}".format(accuracy_score(y_test, predictions)))
   
    
    #plot confusion matrix

   # cm = confusion_matrix(y_test, predictions)
   # tn, fp, fn, tp = cm.ravel()

   # fig, ax = plt.subplots(figsize=(5.5, 4.5))
   # ConfusionMatrixDisplay(cm, display_labels=['died', 'survived']).plot(ax=ax, cmap='Blues')
   # plt.title('Confusion matrix')
   # plt.show()

   # print(f"True Negatives  (correctly said 'died')     : {tn}")
   # print(f"False Positives (said survived, actually died): {fp}")
   # print(f"False Negatives (said died, actually survived): {fn}")
   # print(f"True Positives  (correctly said 'survived') : {tp}")