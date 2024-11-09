# 3rd Party Library Imports
print("Please wait, importing libraries")
import pandas as pd        # import Pandas 3rd party library

if __name__ == '__main__':
    
    print("Assignment 2 - STARTER SCRIPT")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)   
    pd.set_option('display.width', 2000)

    # Create a Panda DataFrame from a CSV File
    testDF = pd.read_csv(r'ipObservations.csv')

    # Remove rows where FRAME-TYPE is "IPV6"
    testDF = testDF[testDF['FRAME-TYPE'] != 'IPV6']

    # MAPS strings and Bool to integer values  
    testDF['SRC-COUNTRY'] = testDF['SRC-COUNTRY'].map({'LOCAL': 1, 'United States': 2, 'MULTICAST': 3, 'Russian Federation': 4, 'Ireland': 5, 'United Kingdom': 6, 'Argentina': 7, 'France': 8, 'RESERVED': 9})  
    testDF['DST-COUNTRY'] = testDF['DST-COUNTRY'].map({'LOCAL': 1, 'United States': 2, 'MULTICAST': 3, 'Russian Federation': 4, 'Ireland': 5, 'United Kingdom': 6, 'Argentina': 7, 'France': 8, 'RESERVED': 9})  
    testDF['FRAME-TYPE']  = testDF['FRAME-TYPE'].map({'IPV4': 1, 'IPV6': 2}) #I know IPV6 will be taken out, just for clarity of understanding how to label
    testDF['PROTOCOL']    = testDF['PROTOCOL'].map({'TCP': 1, 'UDP': 2})  
    testDF['SRC-PORT']    = testDF['SRC-PORT'].map({'EPH': -1})         
    testDF['DST-PORT']    = testDF['DST-PORT'].map({'EPH': -1})  
    
    # Convert ports to numeric, if they are not already
    testDF['SRC-PORT'] = pd.to_numeric(testDF['SRC-PORT'], errors='coerce')
    testDF['DST-PORT'] = pd.to_numeric(testDF['DST-PORT'], errors='coerce')

    # Sort connections by observed
    df_sorted = testDF.sort_values(by='Observed', ascending=False)
    
    # Read in data
    df = pd.read_csv(r'ipObservations.csv')

    # Display the sorted DataFrame
    print(df_sorted.head(10))

    # Save the resulting DataFrame to a CSV file
    df_sorted.to_csv(r'VillarealR-WK-2-Sorted.csv', index=False)