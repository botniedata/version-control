# import packages pandas and numpy
import pandas as pd
import numpy as np

# function to extract excel file as dataframe
def extract(file_path, sheet, rows, ind_col):
    
    # read the file into memory
    data = pd.read_excel(file_path, sheet_name = sheet, nrows = rows, index_col = ind_col)

    # excel to df
    data = pd.DataFrame(data)
    
    # printing details about the file
    print(f"data store in [{file_path}]:")
    print(f"\nNumber of rows [{data.shape[0]}], and Number of columns [{data.shape[1]}] in dataframe")
    print(f"\nColumns in dataframe with it's data types: ")
    
    # print data types
    print(data.dtypes)
    
    print(f"\n Printing the count value of NULL per column\n")
    print(data.isna().sum())
    
    # print message before returning the dataframe
    print(f"\nTo view the dataframe extracted from {file_path}, display the value returned by this function!\n\n") 
    
    return data

# call the function
psgc = extract("PSGC-4Q-2023-Publication-Datafile.xlsx",
               sheet = 3,
               rows = None,
               ind_col = None )

# renaming and cleaning the columns/headers 
def transform(data):
    
    # changing columns/headers string to lowercase, replacing special characters to spaces
    clean_columns = data.columns.str.lower().str.replace('\W', '')
    
    # passing function as clean_columns to dataframe columns
    data.columns = clean_columns
    
    # return to function
    return data

def filter_cols(data, column_name, level):
    
    data = data[data[column_name] == level][['10digitpsgc', 'name', 'correspondencecode', 'geographiclevel',
       'oldnames', 'cityclass', 'incomeclassification',
       'urbanruralbasedon2020cph', '2015population',
       '2020population','status']]
    
    return data

psgc.columns

# Transformation
psgc = transform(psgc)

# Records per Regional
regional = filter_cols(psgc, 'geographiclevel', "Reg")

# Regional Output
regional

# Records per Regional
provincial = filter_cols(psgc, 'geographiclevel', "Prov")

# Provincial Output
provincial

# Records per Municipal
municipal = filter_cols(psgc, 'geographiclevel', "Mun")

# Municipal Output
municipal

# Records per City
city = filter_cols(psgc, 'geographiclevel', "City")

# City Output
city

def info_details(source):
    
    data = source
    print(f"There are {data.shape[0]} records\n")
    
    ur_count = data.groupby(['urbanruralbasedon2020cph'])['urbanruralbasedon2020cph'].count()
    print("Count of Urban/Rural based on 2020 CPH:")
    print(f"{ur_count.to_string(index=True, header=False)}\n")
    
    status_count = data.groupby(['status'])['status'].count()
    print("Count of Status:")
    print(f"{status_count.to_string(index=True, header=False)}\n")
    
    class_count = data.groupby(['incomeclassification'])['incomeclassification'].count()
    print("Count of Income Classification:")
    print(f"{class_count.to_string(index=True, header=False)}\n")     
    
    return data

# Urban Baranggay Based on 2020 CPH
urban = filter_cols(psgc, 'urbanruralbasedon2020cph', "U")

# Display rural dataframe
urban

# Rural Baranggay Based on 2020 CPH
rural = filter_cols(psgc, 'urbanruralbasedon2020cph', "R")

# Display rural dataframe
rural

# CC (Components Cities) based on City Class
cc = filter_cols(psgc, 'cityclass', 'CC')

# NCR Districts Output
cc

# ICC (Independent Components Cities) based on City Class
icc = filter_cols(psgc, 'cityclass', 'ICC')

# ICC
icc

# HUC (Highly Urbanized Cities) based on City Class
# Population: Minimum 200,000
# Annual Income: Php. 50M
huc = filter_cols(psgc, 'cityclass', 'HUC')

# HUC
huc

brgy_details = info_details(baranggay)

brgy_details