"""
 #Created 28/07/2026 By Roger Wiliams
 
 globals vars
 
 conceit with: dfTemperature so modETl and main py could use same DataFrame! 

"""

#VARS

#folder paths
CNST_STR_DATA_ROOTPATH = "/assets/csv/Data"
CNST_STR_DATA_EXTRACTEDPATH = CNST_STR_DATA_ROOTPATH +"/ExtractedFiles"
CNST_STR_DATA_ORIGINALPATH = CNST_STR_DATA_ROOTPATH +"/OriginalFiles"
CNST_STR_DATA_WORKINGPATH = CNST_STR_DATA_ROOTPATH +"/WorkingFiles"
CNST_STR_DATA_CLEANEDPATH = CNST_STR_DATA_ROOTPATH +"/CleanedFiles"
CNST_STR_DATA_VISUALISATIONPATH = CNST_STR_DATA_ROOTPATH +"/VisualisationFiles"

#file name appenders
CNST_STR_FILENAME_APPEND_CLEANED = "_Cleaned"
CNST_STR_FILENAME_APPEND_WORKING = "_Working"
CNST_STR_FILENAME_APPEND_VISUALISATION = "_Visualisation"

#default container size for tabs
CNST_INT_CONTAINTER_HEIGHT = 800
CNST_INT_INNER_CONTAINTER_HEIGHT = 780

dfTemperature = None