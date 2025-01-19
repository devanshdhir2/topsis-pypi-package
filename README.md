TOPSIS-Devansh-102203449

Description:-

This package implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method for Multiple Criteria Decision Making (MCDM). TOPSIS is a method of compensatory aggregation that compares a set of alternatives based on their geometric distance from both the ideal best and ideal worst solutions.
Installation
Install the package using pip:
bashCopypip install TOPSIS-Devansh-102203449
Usage
Command Line Interface
bashCopypython -m topsis_yourname <InputDataFile> <Weights> <Impacts> <ResultFileName>
Arguments:

InputDataFile: CSV file containing the decision matrix

First column: Object/Variable names
2nd to last columns: Numeric values only


Weights: Comma-separated weights (e.g., "1,1,1,2")
Impacts: Comma-separated impacts, either + or - (e.g., "+,+,-,+")
ResultFileName: Output CSV file name

Example:
bashCopypython -m topsis_yourname input.csv "1,1,1,2" "+,+,-,+" output.csv
Python Package Usage
pythonCopyfrom topsis_yourname import topsis_score

# Read your data into a pandas DataFrame
import pandas as pd
df = pd.read_csv('input.csv')

# Define weights and impacts
weights = [1, 1, 1, 2]
impacts = ['+', '+', '-', '+']

# Calculate TOPSIS scores
result = topsis_score(df, weights, impacts)
result.to_csv('output.csv', index=False)
Input File Format

CSV file with 3 or more columns
First column: Object/Variable names
All other columns: Numeric values only

Example input.csv:
CopyModel,Price,Storage,Camera,Battery
M1,800,256,12,4000
M2,900,512,16,4500
M3,850,256,16,4200
Output Format
The output file will contain all columns from the input file plus two additional columns:

Topsis Score: The calculated TOPSIS score
Rank: The rank based on the TOPSIS score

Error Handling
The package handles the following errors:

Incorrect number of command-line parameters
File not found
Invalid file format
Non-numeric values in columns
Unequal number of weights, impacts, and columns
Invalid impact symbols (must be + or -)

License
This project is licensed under the MIT License - see the LICENSE file for details.
Author
[Devansh Dhir]
Support
For any questions or issues, please open an issue on the GitHub repository.
