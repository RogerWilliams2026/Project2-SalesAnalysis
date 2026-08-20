import os
import pathlib
import zipfile
import shutil
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import plotly.express as px
import nbformat as nbf
import modGlobal

# Modified 18/07/2026 By Roger Williams
#
# ETL library for extracting, transforming, and loading data from pandas supported file formats
#

#
#
# added:
#
# funcReadWorkingFilesReturnDictionary - reads csv file(s) from WorkingFiles and returns a dictionary of fils found
# funcReadCleanedFilesReturnDictionary - reads csv file(s) from CleanedFiles and returns a dictionary of fils found
#
# funcReadCleanedFilesReturnDictionary added but might not be needed.....
#
# Modified 20/07/2026 By Roger Williams
#
# renamed:
#
# funcReadFilesReturnDictionary 
#
# To:
#
# funcReadExtractedFilesReturnDictionary 
#
# Added:
#
# funcReadFileReturnDataFrame
#
# for use with csv file not in a ZIP file
#
# funcReadExistingFileReturnDataFrame
#
# for use with csv file from extractedfiles folder
#

#NOTE: NEED TO ADD CODE TO RESTORE FROM CLEANED FOLDER


# why not use?: """
# the comments in the above are parsed so warnings appear about invalid escape sequence
# for EVERTY \ in the comments so used the old way instead where everything after the #
# symbol is ignored!


# Folder Structure:
#
# Data 
#     \ExtractedFiles - extracted files from ZIP file
#     \OriginalFiles - original ZIP file
#     \CleanedFiles - ETL cleansed and prepared files copied into WorkingFiles
#     \WorkingFiles - csv files ready for use in analysis
#     \VisualisationFiles - user created files to visualisations
#
#
#
# Public Functions:
#
# funcCreateDirectories - creates the folder structure for the ETL library to use:
#                         Data 
#                             \ExtractedFiles - extracted files from ZIP file
#                             \OriginalFiles - original ZIP file
#                             \WorkingFiles
#                             \VisualisationFiles
#
# funcExtractZIPFile - extracts a ZIP file containing files use for analysis these are the accepted 
#                      formats:
#                      text, JSON, csv, Excel (xls, xlsx)
#                      also runs: funcCreateDirectories to make sure there are folders to use!
#
# funcReadExtractedFilesReturnDictionary - reads csv file(s) from ExtractedFiles and returns a dictionary of 
#                                 dataframes with the  KEY as the filename and the VALUE as the dataframe 
#
# funcReadFileReturnDataFrame - reads a specific csv file and returns a DataFrame of the data
#
# funcReadExtractedFileReturnDataFrame - reads a specific csv file from the ExtractedFiles folder and returns a DataFrame of the data
#
# funcGetStructure - displays the schema structure of passed DataFrame
#
# funcGetStatistics - displays basic statistics for the passed DataFrame
#
# funcGetUniqueValues - displays total unique values for each column in the passed DataFrame
#
# funcTransformValues - transform passed column(s) to another datatype returns transformed DataFrame
#
# funcFillMissingValues - fills missing values in passed column(s) with passed value(s) 
#                         returns modified DataFrame
#
# funcRemoveTimeFromDateString - removes 00:00 from the end fo date values (when stored as strings before transform)
#
# funcFindRelatedColumns - finds related columns in passed DataFrame and returns a list of related columns
#
# funcSaveDataFrameToCleanedFile - saves the passed cleaned DataFrame as csv in the cleaned folder
#
# funcSaveDataFrameToWorkingFile - saves the passed cleaned DataFrame as csv in the working folder
#
# funcSaveDataFrameToVisualisationFile - saves the passed cleaned DataFrame as csv in the visualisation folder
#
# funcReadVisualisationFilesReturnDictionary - reads csv file(s) from VisualisationFiles and returns a dictionary of 
#                                 dataframes with the  KEY as the filename and the VALUE as the dataframe 
#
# funcReadWorkingFilesReturnDictionary - reads csv file(s) from WorkingFiles and returns a dictionary of fils found
#
# funcGetCategoricalValueDistribution - Displays the value distribution for each categorical column in the passed DataFrame
#
#
#
# Private functions:
#
# funcGetSpaces - returns a string of spaces to make the column name length equal to the passed intLength
#
#
# Order of Precedence:
#
# if using a ZIP file:
#    funcExtractZIPFile - Extracts ZIP file into Data folder and keeps original in OriginalFiles Folder
#    funcReadExtractedFilesReturnDictionary - reads csv file(s) from ExtractedFiles and returns a dictionary of dataframes with the  KEY as the filename and the VALUE as the dataframe
# else
#    funcReadFileReturnDataFrame - reads a specific csv file and returns a DataFrame of the data
#
# funcSaveDataFrameToWorkingFile - saves the passed cleaned DataFrame as csv in the working folder
# funcReadWorkingFilesReturnDictionary - reads csv file(s) from WorkingFiles and returns a dictionary of fils found
#
# Statistics:
#
# funcGetStructure - Displays the schema structure of passed DataFrame
# funcGetStatistics - Displays basic statistics for the passed DataFrame
# funcGetUniqueValues - Displays total unique values for each column in the passed DataFrame
# funcGetCategoricalValueDistribution - Displays the value distribution for each categorical column in the passed DataFrame
# funcTransformValues - Transform passed column(s) to another datatype returns transformed DataFrame
# funcGetColumnSkew - Displays the skew for each data column in the passed DataFrame ONLY if not categorical data!
#
# Transform/Clean:
#
# funcFillMissingValues - Fills missing values in passed column(s) with passed value(s) returns modified DataFrame
#
# 
# funcSaveDataFrameToCleanedFile - saves the passed cleaned DataFrame as csv in the cleaned folder
# funcSaveDataFrameToVisualisationFile - saves the passed cleaned DataFrame as csv in the visualisation folder
# 
# for analysis:
#
# funcReadVisualisationFilesReturnDictionary - reads csv file(s) from VisualisationFiles and returns a dictionary of 
#                                 dataframes with the KEY as the filename and the VALUE as the dataframe 
# 




def funcGetSpaces(intLength : int, strColumn : str):
    """
    Created 17/07/2026 By Roger Williams
    
    Returns a string of spaces to make the column name length equal to the passed intLength value


    VARS
    
    intLength - maxmimum size of string
    strColumn - column name to use to calculate if need extra space to get length to intLength


    RETURNS
    
    string of spaces to make the column name length equal to the passed intLength value.
    
    """
    
    #return string of spaces
    return (intLength - len(str(strColumn))) * " "  


def funcCreateDirectories():
    """
    Created 15/07/2026 By Roger Williams
    
    Creates the folder structure for the ETL library to use


    """
    
    #create Data folder if it does not exist
    if not os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_ROOTPATH):
        os.mkdir(os.getcwd() + modGlobal.CNST_STR_DATA_ROOTPATH)
    
    #create ExtractedFiles folder if it does not exist
    if not os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_EXTRACTEDPATH):
        os.mkdir(os.getcwd() + modGlobal.CNST_STR_DATA_EXTRACTEDPATH)
    
    #create OriginalFiles folder if it does not exist
    if not os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_ORIGINALPATH):
        os.mkdir(os.getcwd() + modGlobal.CNST_STR_DATA_ORIGINALPATH)

    #create WorkingFiles folder if it does not exist
    if not os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH):
        os.mkdir(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH)

    #create VisualisationFiles folder if it does not exist
    if not os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_VISUALISATIONPATH):
        os.mkdir(os.getcwd() + modGlobal.CNST_STR_DATA_VISUALISATIONPATH)

    if not os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_CLEANEDPATH):
        os.mkdir(os.getcwd() + modGlobal.CNST_STR_DATA_CLEANEDPATH)

    print("Folder Structure Created Successfully!")
    


def funcExtractZIPFile(strFile : str):
    """
    Created 15/07/2026 By Roger Williams
    
    Extracts a ZIP file to /Data/ExtractedFiles and keeps a copy of the original in /Data/OriginalFiles
    Deletes ZIP after use

    VARS
    
    strFile - path to the ZIP file to be extracted.


    """
    #store list of files in the ZIP
    lstFiles = []
    strFileName = ""
    
    #routine check see if necessary folders exist for data storage
    funcCreateDirectories()
    
    #check if file exists
    if not os.path.exists(strFile):
       #show error 
       raise FileNotFoundError(f"The ZIP File {strFile} Does Not Exist!")
    else:
       with zipfile.ZipFile(strFile, 'r') as zip_ref:
            #get list of files in zip
            lstFiles =zip_ref.filelist
            #unzip file
            zip_ref.extractall(os.getcwd() + modGlobal.CNST_STR_DATA_EXTRACTEDPATH)

       print( f"Extracted {len(lstFiles)} File(s) From {strFile} To {modGlobal.CNST_STR_DATA_EXTRACTEDPATH}\n")
       print( "Extracted:")
       #tell user file(s) extracted
       for strTemp in lstFiles:
           print(f"{strTemp.filename}")
           
       print("\n")
       #get JUST filename from strFile
       strFileName = os.path.basename(strFile)
       #make backup copy of file
       shutil.copyfile(strFile, os.getcwd() + modGlobal.CNST_STR_DATA_ORIGINALPATH + "/" + os.path.basename(strFile))
       print(f"Copied: {strFileName} To {modGlobal.CNST_STR_DATA_ORIGINALPATH} Folder")    
       
       
def funcReadExtractedFilesReturnDictionary():
    """
    Created 15/07/2026 By Roger Williams
    
    Reads csv file(s) from ExtractedFiles and returns a dictionary of dataframes with the
    KEY as the filename and the VALUE as the dataframe 

    RETURNS
    
    dictionary of dataframes with the KEY as the filename and the VALUE as the dataframe
    
    """
    lstFiles = []
    dfTemp = None
    
    #get list of files in ExtractedFiles folder
    lstFiles = os.listdir(os.getcwd() + modGlobal.CNST_STR_DATA_EXTRACTEDPATH)
    
    #create dictionary to hold dataframes
    dictDataFrames = {}
    
    #loop through files and read into dictionary
    for strFile in lstFiles:
        #if csv
        if strFile.endswith(".csv"):
            #read csv into dataframe
            dfTemp = pd.read_csv(os.getcwd() + modGlobal.CNST_STR_DATA_EXTRACTEDPATH + "/" + strFile)
            #name DataFrame
            dfTemp.attrs["name"] = strFile[: strFile.index(".")]
            
            #add DataFrame to dictionary setting KEY to filename (no path)
            dictDataFrames[strFile] = dfTemp
            
    print( f"{len(dictDataFrames)} csv Files Read Into DataFrames\n") 
    print("DataFrames Created:")
    
    #show user what DataFrames have been created
    for strKey in dictDataFrames.keys():
        print(f"{strKey}")
    
    print("\n")
    #passback dictionary of all DataFrame       
    return dictDataFrames


       
def funcReadWorkingFilesReturnDictionary():
    """
    Created 19/08/2026 By Roger Williams
    
    Reads csv file(s) from WorkingFiles and returns a dictionary of dataframes with the
    KEY as the filename and the VALUE as the dataframe 

    RETURNS
    
    dictionary of dataframes with the KEY as the filename and the VALUE as the dataframe
    
    """
    lstFiles = []
    dfTemp = None
    
    #get list of files in WorkingFiles folder
    lstFiles = os.listdir(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH)
    
    #create dictionary to hold dataframes
    dictDataFrames = {}
    
    #loop through files and read into dictionary
    for strFile in lstFiles:
        #if csv
        if strFile.endswith(".csv"):
            #read csv into dataframe
            dfTemp = pd.read_csv(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH  + "/" + strFile)
            #name DataFrame
            dfTemp.attrs["name"] = strFile[: strFile.index(".")]
            
            #add DataFrame to dictionary setting KEY to filename (no path)
            dictDataFrames[strFile] = dfTemp
            
    print( f"{len(dictDataFrames)} csv Files Read Into DataFrames\n") 
    print("DataFrames Created:")
    
    #show user what DataFrames have been created
    for strKey in dictDataFrames.keys():
        print(f"{strKey}")
    
    print("\n")
    #passback dictionary of all DataFrame       
    return dictDataFrames


       
def funcReadCleanedFilesReturnDictionary():
    """
    Created 19/08/2026 By Roger Williams
    
    Reads csv file(s) from CleanedFiles and returns a dictionary of dataframes with the
    KEY as the filename and the VALUE as the dataframe 

    RETURNS
    
    dictionary of dataframes with the KEY as the filename and the VALUE as the dataframe
    
    """
    lstFiles = []
    dfTemp = None
    
    #get list of files in CleanedFiles folder
    lstFiles = os.listdir(os.getcwd() + modGlobal.CNST_STR_DATA_CLEANEDPATH)
    
    #create dictionary to hold dataframes
    dictDataFrames = {}
    
    #loop through files and read into dictionary
    for strFile in lstFiles:
        #if csv
        if strFile.endswith(".csv"):
            #read csv into dataframe
            dfTemp = pd.read_csv(os.getcwd() + modGlobal.CNST_STR_DATA_CLEANEDPATH  + "/" + strFile)
            #name DataFrame
            dfTemp.attrs["name"] = strFile[: strFile.index(".")]
            
            #add DataFrame to dictionary setting KEY to filename (no path)
            dictDataFrames[strFile] = dfTemp
            
    print( f"{len(dictDataFrames)} csv Files Read Into DataFrames\n") 
    print("DataFrames Created:")
    
    #show user what DataFrames have been created
    for strKey in dictDataFrames.keys():
        print(f"{strKey}")
    
    print("\n")
    #passback dictionary of all DataFrame       
    return dictDataFrames



   
def funcReadVisualisationFilesReturnDictionary():
    """
    Created 30/07/2026 By Roger Williams
    
    Reads csv file(s) from VisualisationFiles and returns a dictionary of dataframes with the
    KEY as the filename and the VALUE as the dataframe 

    RETURNS
    
    dictionary of dataframes with the KEY as the filename and the VALUE as the dataframe
    
    """
    lstFiles = []
    dfTemp = None
    
    #get list of files in ExtractedFiles folder
    lstFiles = os.listdir(os.getcwd() + modGlobal.CNST_STR_DATA_VISUALISATIONPATH)
    
    #create dictionary to hold dataframes
    dictDataFrames = {}
    
    #loop through files and read into dictionary
    for strFile in lstFiles:
        #if csv
        if strFile.endswith(".csv"):
            #read csv into dataframe
            dfTemp = pd.read_csv(os.getcwd() + modGlobal.CNST_STR_DATA_VISUALISATIONPATH + "/" + strFile)
            #name DataFrame
            dfTemp.attrs["name"] = strFile[: strFile.index(".")]
            
            #add DataFrame to dictionary setting KEY to filename (no path)
            dictDataFrames[strFile] = dfTemp
            
    print( f"{len(dictDataFrames)} csv Files Read Into DataFrames\n") 
    print("DataFrames Created:")
    
    #show user what DataFrames have been created
    for strKey in dictDataFrames.keys():
        print(f"{strKey}")
    
    print("\n")
    #passback dictionary of all DataFrame       
    return dictDataFrames




    
def funcReadFileReturnDataFrame(strFileName : str):
    """
    Created 20/07/2026 By Roger Williams
    
    Reads csv file passed then returns a DataFrame of the data
    Creates sub folders for project if missing
    Makes backup copy of the csv file
    Copies csv file into ExtractedFiles folder for future use

    VARS
    
    strFileName - name of the csv file to read 
    

    RETURNS
    
    DataFrame of the data
    
    """
    dfTemp = None
   
       
    #routine check see if necessary folders exist for data storage
    funcCreateDirectories()

    #check if file exists
    if not os.path.exists(strFileName):
       #show error 
       raise FileNotFoundError(f"The CSV File {strFileName} Does Not Exist In csv Folder!")
    else:
       #read csv into dataframe
       dfTemp = pd.read_csv(strFileName)
       #name DataFrame
       dfTemp.attrs["name"] = strFileName[: strFileName.index(".")]
       
       print( f"Read {strFileName} Into DataFrame\n")
       #check if file exists in extractedfiles folder
       if not os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_EXTRACTEDPATH + "/" + os.path.basename(strFileName)):
          #copy file into extractedfiles folder
          shutil.copyfile(strFileName, os.getcwd() + modGlobal.CNST_STR_DATA_EXTRACTEDPATH + "/" + os.path.basename(strFileName))
          print(f"Copied: {strFileName} To Assets/Data/ExtractedFiles Folder")   
          #make backup copy of file
          shutil.copyfile(strFileName, os.getcwd() + modGlobal.CNST_STR_DATA_ORIGINALPATH + "/" + os.path.basename(strFileName))
          print(f"Copied: {strFileName} To {modGlobal.CNST_STR_DATA_ORIGINALPATH} Folder")   
  

       #return DataFrame
       return dfTemp    



def funcReadExtractedFileReturnDataFrame(strFileName : str):
    """
    Created 20/07/2026 By Roger Williams
    
    Reads csv file passed from ExtractedFiles folder then returns a DataFrame of the data

    VARS
    
    strFileName - name of the csv file to read 
    

    RETURNS
    
    DataFrame of the data
    
    """
    dfTemp = None

    #check if file exists
    if not os.path.exists("./" + modGlobal.CNST_STR_DATA_EXTRACTEDPATH + "/" + strFileName):
       #show error 
       raise FileNotFoundError(f"The CSV File {strFileName} Does Not Exist In csv Folder!")
    else:
       #read csv into dataframe
       dfTemp = pd.read_csv("./" + modGlobal.CNST_STR_DATA_EXTRACTEDPATH + "/" + strFileName)
       #name DataFrame
       dfTemp.attrs["name"] = strFileName[: strFileName.index(".")]
       print( f"Read {strFileName} Into DataFrame\n")
       #return DataFrame
       return dfTemp    


  
def funcSaveDataFrameToWorkingFile(dfWhat : pd.DataFrame):
    """
    Created 28/07/2026 By Roger Williams
    
    saves the passed cleaned DataFrame as csv in the working folder

    
    VARS
    
    dfWhat      - DataFrame to save as csv

   
    """
  
    #delete if already exists
    if os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH + "/" + dfWhat.attrs["name"] + modGlobal.CNST_STR_FILENAME_APPEND_WORKING + ".csv"):
       os.remove(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH + "/" + dfWhat.attrs["name"] + modGlobal.CNST_STR_FILENAME_APPEND_WORKING + ".csv")
        
    dfWhat.to_csv(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH + "/" + dfWhat.attrs["name"] + modGlobal.CNST_STR_FILENAME_APPEND_WORKING + ".csv", date_format="%d/%m/%Y")
    print(f"Saved: {dfWhat.attrs["name"]} To Working Folder") 
  
  
  
def funcSaveDataFrameToVisualisationFile(dfWhat : pd.DataFrame):
    """
    Created 28/07/2026 By Roger Williams
    
    saves the passed cleaned DataFrame as csv in the visualisationfolder

    
    VARS
    
    dfWhat      - DataFrame to save as csv
    strFileName - what to call saved file

   
    """
    if os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH + "/" + dfWhat.attrs["name"] + modGlobal.CNST_STR_FILENAME_APPEND_VISUALISATION + ".csv"):
       os.remove(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH + "/" + dfWhat.attrs["name"] + modGlobal.CNST_STR_FILENAME_APPEND_VISUALISATION + ".csv")
  
    dfWhat.to_csv(os.getcwd() + modGlobal.CNST_STR_DATA_VISUALISATIONPATH + "/" + dfWhat.attrs["name"] + modGlobal.CNST_STR_FILENAME_APPEND_VISUALISATION +".csv", date_format="%d/%m/%Y")
    print(f"Saved: {dfWhat.attrs["name"]} To Visualisation Folder") 
    
  
  
def funcSaveDataFrameToCleanedFile(dfWhat : pd.DataFrame):
    """
    Created 28/07/2026 By Roger Williams
    
    saves the passed cleaned DataFrame as csv in the cleaned folder
    makes a copy in the visualisations folder 
    
    if name has _working in it remove
    
    VARS
    
    dfWhat      - DataFrame to save as csv

   
    """
    if dfWhat.attrs["name"].endswith(modGlobal.CNST_STR_FILENAME_APPEND_WORKING):
       dfWhat.attrs["name"] = dfWhat.attrs["name"][:dfWhat.attrs["name"].index(modGlobal.CNST_STR_FILENAME_APPEND_WORKING)]
    
    if os.path.exists(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH + "/" + dfWhat.attrs["name"] + modGlobal.CNST_STR_FILENAME_APPEND_CLEANED + ".csv"):
       os.remove(os.getcwd() + modGlobal.CNST_STR_DATA_WORKINGPATH + "/" + dfWhat.attrs["name"] + modGlobal.CNST_STR_FILENAME_APPEND_CLEANED + ".csv")
   
    dfWhat.to_csv(os.getcwd() + modGlobal.CNST_STR_DATA_CLEANEDPATH + "/" + dfWhat.attrs["name"] + modGlobal.CNST_STR_FILENAME_APPEND_CLEANED + ".csv", date_format="%d/%m/%Y")
    funcSaveDataFrameToVisualisationFile(dfWhat)
   
  
  
  
  
#******schema routines****   
              
def funcGetStructure(dfWhat : pd.DataFrame):
    """
    Created 15/07/2026 By Roger Williams
    
    Displays the schema structure of passed DataFrame:
    
    - .info
    
    
    VARS
    
    dfWhat - DataFrame to display structure of


    """
    dfNumbers = pd.DataFrame()
    dfStrings = pd.DataFrame()
    dfDateTime = pd.DataFrame()
    
    #print heard
    print("DataFrame Structure:")
    print("=" * 19)
    #get info
    print(dfWhat.info())
    print("\n")
    print("Summary of DataFrame Structure:")
    print("=" * 31)
    #see if any numeric columns    
    dfNumbers = dfWhat.select_dtypes(include=['number'])
    
    if not dfNumbers.empty:
        print("Numeric Columns:\n")
        #get details
        print(dfNumbers.describe())
        print("\n")
    else:
        print("No Numeric Columns Found!\n")    
    
    #see if any string columns
    dfStrings = dfWhat.select_dtypes(include=["str","category","object"])    
    
    if not dfStrings.empty:
        print("String Columns:\n")
        #get details
        print(dfStrings.describe())
        print("\n")
    else:
        print("No String Columns Found!\n")
    
     #see if any datetime columns
    dfDateTime = dfWhat.select_dtypes(include=["datetime", "datetime64"])    
        
    if not dfDateTime.empty:
        print("DateTime Columns:\n")
        #get details
        print(dfDateTime.describe())
        print("\n")
    else:
        print("No DateTime   Columns Found!\n")

    print()
    

    
def funcGetCategoricalValueDistribution(dfWhat : pd.DataFrame):
    """
    Created 18/08/2026 By Roger Williams
    
    Displays the value distribution for each categorical column in the passed DataFrame:
    
    VARS
    
    dfWhat - DataFrame to display value distribution of


    """
    
    #print header
    print("DataFrame Categorical Value Distribution:")
    print("=" * 40)
    
    for colColumn in dfWhat.select_dtypes(include=["str","category","object"]).columns:
        print( f"[{colColumn}] Value Distribution:")
        print( dfWhat[colColumn].value_counts())  
        print("\n")    
       
      
def funcGetStatistics(dfWhat : pd.DataFrame):
    """
    Created 15/07/2026 By Roger Williams
    
    Displays basic statistics for the passed DataFrame:
    
    - .describe
    - .shape
    - show missing values per column
    - show duplicate count and percent per column
    
    
    VARS
    
    dfWhat - DataFrame to display statistics for


    """
    
    intMissing = 0
    intPercent = 0
    strTemp = ""
    
    #print header
    print("DataFrame Statistics:")
    print("=" * 22)
    #print describe
    print(dfWhat.describe())    
    print("\n")
    #print schema shape header
    print("DataFrame Shape:")
    print("=" * 20)
    #print schema shape    
    print( f"Rows: {dfWhat.shape[0]}, Columns: {dfWhat.shape[1]}\n" )     
    
    #print missing values header
    print("\nMissing Values Per Column:")
    print("=" * 30)
    
    for colColumn in dfWhat.columns:
        #get total number of missing values per column
        intMissing = dfWhat[colColumn].isnull().sum()
        #get percentage of missing values per column
        intPercent = (intMissing / dfWhat.shape[0]) * 100
        #print percent missing IF not zero
        if intMissing > 0:
           #create padded string
           strTemp = funcGetSpaces(20, colColumn) 
           print( f"{colColumn}{strTemp} - {intMissing}: Missing Values, {intPercent:.2f}% Percent Missing Values" )
           
    print()       
    #print duplicate values header
    print("\nDuplicate Value Count Per Column:")
    print("=" * 30)
    
    for colColumn in dfWhat.columns:
        #get total number of duplicate values per column
        intMissing = dfWhat[colColumn].duplicated().sum()
        #get percentage of duplicate values per column
        intPercent = (intMissing / dfWhat.shape[0]) * 100
        #print percent duplicate IF not zero
        if intMissing > 0:
           #create padded string
           strTemp = funcGetSpaces(20, colColumn) 
           print( f"{colColumn}{strTemp} Total Values: {dfWhat[colColumn].count()}  Duplicate Values: {intMissing}, {intPercent:.2f}% Percent Duplicate Values" )
           
    print() 
  
  
  
   
    
def funcGetUniqueValuesCount(dfWhat : pd.DataFrame):
    """
    Created 17/07/2026 By Roger Williams
    
    Displays total unique values for each column in the passed DataFrame:
    Spaces each column by 20 charcters before displaying total e.g.:
    
    column1             - 10: Unique Values
    date                - 12: Unique Values 
    
    
    VARS
    
    dfWhat - DataFrame to display unique values for


    """
    
    strTemp = ""
    #print header
    print("DataFrame Unique Values Per Column:")
    #underline
    print("=" * 35)

    for colColumn in dfWhat.columns:
        #put number of spaces to make column name 20 characters long
        strTemp = funcGetSpaces(20, colColumn)
        #print column data
        print(f"{colColumn}{strTemp} - {dfWhat[colColumn].nunique()}: Unique Values Out Of {dfWhat[colColumn].count()} Total Values")   
     
    print() 


                 
def funcTransformValues(dfSource : pd.DataFrame, dictWhat : dict):
    """
    Created 17/07/2026 By Roger Williams
    
    Transform passed column(s) to another datatype returns transformed DataFrame 
    
    
    VARS
    
    dfWhat - DataFrame to transform column(s) for
    dictWhat - dictionary of columns to transform and their new data types

    if dictWhat value = "pandasdatetime" will convert to pandas datetime format using 
    pd.to_datetime() with UK date format


    RETURNS
    
    transformed DataFrame
    
    """
    
    colColumn = ""
    strType = ""
    dfWhat = dfSource.copy() 
     
    #loop through columns and transform
    for colColumn, strType in dictWhat.items():
        if strType == "pandasdatetime":
              #if in format that needs to be converted  
              dfWhat[colColumn] = pd.to_datetime(dfWhat[colColumn], format="%d/%m/%Y") #, errors="coerce")
        else: 
           dfWhat[colColumn] = dfWhat[colColumn].astype(strType)
        
    #print new schema
    print(dfWhat.info())    
    #return transformed DataFrame
    return dfWhat



def funcGetColumnSkew(dfWhat : pd.DataFrame):
    """
    Created 27/07/2026 By Roger Williams
    
    Displays the skew for each data column in the passed DataFrame ONLY if not categorical data!
    also shows kurtosis and Q-Q plot for each column
    
    VARS
    
    dfWhat - DataFrame to display unique values for


    """
    
    strTemp = ""
    objValue = None
    fltSkew = 0.0
    dictSkew = dict()
    dfTemp = pd.DataFrame()
    fltKurtosis = 0.0
    fig = None
    axis = None
    colColumn = None
    lstSkew = list()
    lstCol = list()
    
    
    #print header
    print("DataFrame Skew Values Per Column:")
    #underline
    print("=" * 33)
    
    for colColumn, objValue in dfWhat.items():
        #ignore categorical values
        if not objValue.dtype.name == "str":
           #put number of spaces to make column name 20 characters long
           strTemp = funcGetSpaces(20, colColumn)
           #print column data
           
           fltSkew = dfWhat[colColumn].skew()
           fltKurtosis = dfWhat[colColumn].kurtosis()
           #store skew for later use in histogram
           dictSkew[colColumn] = fltSkew
                      
           lstSkew.append(fltSkew)
           lstCol.append(colColumn)           
           
           if fltSkew > 1:
               print(f"{colColumn}{strTemp} Skew: {fltSkew:.2f} - Highly Positively Skewed Kurtosis: {fltKurtosis:.2f}")
           elif fltSkew < 0:    
               print(f"{colColumn}{strTemp} Skew: {fltSkew:.2f} - Highly Negatively Skewed Kurtosis: {fltKurtosis:.2f}")
           else:
               print(f"{colColumn}{strTemp} Skew: {fltSkew:.2f} - Approximately Symmetrical Kurtosis: {fltKurtosis:.2f}")   
      
    print()
    
      
    #show Q-Q plot for each column
    for colColumn, objValue in dfWhat.items():           
        #ignore categorical values
        if not objValue.dtype.name == "str":
           #configure plot
           fig, axis = plt.subplots(figsize=(12, 6))
           #put number of spaces to make column name 20 characters long
           strTemp = funcGetSpaces(20, colColumn)
           #print column data
           print(f"Q-Q Plot For Column: {colColumn}")
           print("=" * 30)
           stats.probplot(dfWhat[colColumn], dist="norm", plot=plt)
           plt.title(f"Q-Q Plot For Column: {colColumn}", fontweight="bold")
           axis.set_xlabel(f"Q-Q Plot For Column: {colColumn}")
           axis.set_ylabel("Theoretical Quantiles")

           plt.tight_layout()
           plt.show()
           print("\n")  
           
    print()

    #experimental - show skew amounts for all numeric columns in a histogram!
    dfTemp = pd.DataFrame( {"Column" : lstCol, "Skew" : lstSkew})       
    fig = px.bar(dfTemp, x="Column", y="Skew") # (x=lstCol, y=lstSkew)
    fig.update_xaxes(title_text="Columns")
    fig.update_yaxes(title_text="Skew Values")
    fig.update_layout(title_text="Distribution of Skew Values Across ALL Numeric Columns", title_x=0.5)
    fig.show()
    
    

def funcFillMissingValues(dfWhat : pd.DataFrame, dictWhat : dict):
    """
    Created 17/07/2026 By Roger Williams
    
    Fills missing values in passed column(s) with passed value(s) returns modified DataFrame 
    
    Reason:
    
    Some columns user might want to be certain default values e.g. True for boolean values
    or 1 for numeric values or "unknown" for string values
    
    
    VARS
    
    dfWhat - DataFrame to fill missing values for
    dictWhat - dictionary of columns missing values and their new values


    RETURNS
    
    modified DataFrame
    
    """
    colColumn = ""
    strValue = ""   
    
    
    #loop through columns and fill missing values
    for colColumn, strValue in dictWhat.items():
        
        dfWhat[colColumn] = dfWhat[colColumn].fillna(strValue)
        
    #return modified DataFrame
    return dfWhat



def funcRemoveTimeFromDateString(dfWhat : pd.DataFrame, strColumnName : str):
    """
    Created 29/07/2026 By Roger Williams
    
    Removes time from date string column in passed DataFrame 

    
    VARS
    
    dfWhat           - DataFrame to fill missing values for
    strColumnName    - column to process   


    RETURNS
    
    modified DataFrame
    
    """
    strColumn = ""
    strValue = ""   
    strTemp = ""
    intIndex = 0
    objRow = None
    
    #loop through columns values and remove 00:00
    for intIndex, objRow in dfWhat.iterrows():
        strTemp = objRow[strColumnName]
        
        if " " in strTemp:
           #remove 00:00
           strTemp = strTemp[:strTemp.index(" ")]
           #update column
           dfWhat.iloc[intIndex,0] = strTemp       

    #return modified DataFrame
    return dfWhat





#this is a bit of guess work as need to populate missing string values
#from rows with a RELATED field
#e.g. product category has a missing/null value
#so need to find a row WITH product category values with the SAME product name value
#as not willing to guess what the product category should be!

def funcUpdateRelatedRecords(dfToProcess : pd.DataFrame, strRelatedColumn : str, strColumnToUpdate : str):
    #updates the values in strColumnToUpdate where is missing/null values from another row
    #where pstrRelatedColumn is the same and strColumnToUpdate is NOT Nmissing/null
    #easy to do in SQL but in pandas as a beginner....
    #
    #so broke open my mad scientist cookbook and cobbled together this wild stab in the dark
    #if all else fails fall back on your programming experience with database systems! 
    #
    #originally just handled product category but thought might be more useful if it was
    #a \generic\ function
    #
    #VARS
    #
    #dfToProcess             - dataframe (to update)
    #strRelatedColumn        - column to use as a pivot for the missing values    
    #strColumnToUpdate       - column with missing values to update   
    #
    #RETURNS
    #
    #dataframe with corrections
    #
    #
    #Future improvements
    #===================
    #
    #possibly use mean() to find most ranked strRelatedColumn values  
    #just in case there are strColumnToUpdate data anomylies 
    # 
    #e.g. product name tablet has product category of stationary when it should be electronics
    #could explode in my face but this is only an idea
    #
    #learn the pandas method of doing it correctly!
    #
    global pd
    
    #encapsulate dfToProcess and from the dfToProcess dataframe get rows excluding where product category = missing/null
    #and filter by product category and its related column
    dfFilterNotNaN = dfToProcess[ dfToProcess[strColumnToUpdate].notna()].filter([strRelatedColumn, strColumnToUpdate]) 
        
    #now look for those naughty missing values and populate them!
    for strName, strCategory in zip(dfToProcess[strRelatedColumn ], dfToProcess[strColumnToUpdate]):
        #is strCategory missing a value?
        if pd.isna(strCategory):
            #get list of all products with same name from dataframe with no missing product categories
            dfTemp = dfFilterNotNaN.query(f"{strRelatedColumn} == '{strName}'").filter([strColumnToUpdate]) 
            #get the value
            strTemp =dfTemp[strColumnToUpdate].iloc[0]
            #update dataframe dfToProcess
            dfToProcess[strColumnToUpdate] = dfToProcess[strColumnToUpdate].replace(to_replace=strCategory, value=strTemp) 
            #return changed dataframe
            return dfToProcess
    #Note: maybe the for loop is a crass solution but it was the best I could find....for now! 

# #create copy of df work dataframe
# dfWorkTemp = dfWork.copy()
# #get corrected dataframe
# dfWorkTemp = funcUpdateRelatedRecords(df, "Product Name", "Product Category") 
# #show the results (fingers crossed!)
# dfWorkTemp



# def funcFindRelatedColumns(dfWhat : pd.DataFrame):
#     """
#     Created 17/07/2026 By Roger Williams
    
#     Finds related columns in passed DataFrame and returns a list of related columns 
    
#     Reason:
    
#     Some columns may a have related column data e.g. product name could have related data in another 
#     column say product category, this function returns a dictionary of those columns with the KEY
#     as the first column and the VALUE as the related column
    
#     How it works:
    
#     Loops through each column in the DataFrame using one column as an anchor and getting the other
#     columns count of unique values for records with first column value. If number of unique records
#     is ZERO adds to a nested list of related columns which contains:
    
#     column name acting as anchor, its current value, comumn being checked, its value  
    
#     In theory if the total number of list items for the anchor column = the total number of rows
#     in the DataFrame then we have a related column!
    
    
#     VARS
    
#     dfWhat - DataFrame to find related columns for
#     strColumn - column to find related columns for


#     RETURNS
    
#     list of related columns
    
#     """
    
#     #create dictionary to hold related columns
#     dictRelatedColumns = {}
#     dfTemp = pd.DataFrame()
   
#     intUnique = 0
#     intNum = 0
#     intColumn = 0
    
#     strCurrentColumn = ""
#     strNextColumn = ""
#     objCurrentColumnValue = None
#     objNextColumnValue = None
#     lstNested = []
   
   
#     #go through each column in the DataFrame
#     for strCurrentColumn, strValue in dfWhat.items():
#         intNum = 0    
        
#         #iterate through rest of columns to compare current column with others
#         for intColumn in range(intNum + 1, len(dfWhat.columns)):      
#             #if not last column
#             if intNum != len(dfWhat.columns) - 1:
#                #get filtered DataFrame for current column value
#                dfTemp = dfWhat [ dfWhat[strCurrentColumn] == strValue[0] ]
#                #get next column name
#                strNextColumn = dfWhat.columns[intNum +1]
#                #get next columns value
#                objNextColumnValue = dfWhat[strNextColumn]
#                #get number of unique values in the next column
#                intUnique = dfWhat[strNextColumn].nunique()
            
#                #if ZERO we have a potential related column!
#                if intUnique == 0:
#                   #created nested list of:
#                   #current column and value
#                   #next column and value
#                   #
#                   #if total nuber of values = nummber of DataFrame rows we have a winner!
#                   #
#                   lstNested.append( [ strCurrentColumn, strValue[0], strNextColumn, objNextColumnValue[0] ] )   
#             #increment counter for next column tp check              
#             intNum +1
        
#         intColumn +1    
        
           
#     #now check if nested list size = DataFrame rows!       
#     lstNested
    
            
#     #return list of related columns
#     return dictRelatedColumns    





#******end schema routines****