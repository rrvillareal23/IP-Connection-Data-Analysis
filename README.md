# IP Connection Data Analysis

## Project Overview

This project focuses on analyzing and processing IP connection data to explore network traffic patterns. The provided code processes data from an IP observations CSV file, performs data cleaning, transformation, and sorting, and then outputs a cleaned and sorted dataset. It removes invalid or irrelevant data (e.g., IPv6 frames), converts categorical values into numeric values for easier analysis, and finally sorts the data based on the observed timestamp.

## Requirements

To run this project, you need to have the following Python libraries installed:

- `pandas`: A powerful data analysis library.

You can install the necessary dependencies using `pip`:

pip install pandas

## Script Overview

The script performs the following tasks:

1. **Library Imports**: 
   - Imports the `pandas` library, which is used to handle data manipulation tasks.

2. **Data Loading**: 
   - Loads the CSV file `ipObservations.csv` into a Pandas DataFrame.

3. **Data Cleaning**:
   - Filters out rows where the `FRAME-TYPE` is 'IPV6' to remove IPv6 data from the analysis.
   - Maps categorical values for `SRC-COUNTRY`, `DST-COUNTRY`, `FRAME-TYPE`, and `PROTOCOL` to numeric values to make the data easier to analyze.

4. **Data Transformation**:
   - Converts `SRC-PORT` and `DST-PORT` values to numeric values.
   - Maps 'EPH' (ephemeral) ports to `-1` for consistency.
   
5. **Sorting**:
   - Sorts the DataFrame by the `Observed` column in descending order to show the most recent observations first.

6. **Output**:
   - Saves the cleaned and sorted DataFrame into a new CSV file (`VillarealR-WK-2-Sorted.csv`).

## How to Run the Script

1. Make sure the required libraries are installed.
2. Download or clone the repository to your local machine.
3. Place the `ipObservations.csv` file in the same directory as the script.
4. Run the script in your Python environment.

5. The cleaned and sorted data will be saved in a file named `VillarealR-WK-2-Sorted.csv`.

## File Description

- `ipObservations.csv`: The original dataset containing IP connection data.
- `VillarealR-WK-2-Sorted.csv`: The cleaned and sorted dataset saved as a CSV file after processing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
