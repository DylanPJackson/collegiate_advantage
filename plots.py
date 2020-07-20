"""
    filename : plots.py
    author : Dylan P. Jackson
    description : Perform some initial analysis on data using pyplot
"""

import matplotlib.pyplot as plt
import pandas as pd

def salary_by_college():
    data = pd.read_csv('data/sal_college.csv')
    data = data.head(30)
    sorted_data = data.sort_values(by=['Starting Median Salary'], ascending=False)
    #print(sorted_data.head(5))
    school_name = sorted_data['School Name']
    start_med_sal = sorted_data['Starting Median Salary']
    plt.xticks(rotation='vertical')
    plt.scatter(start_med_sal, school_name)
    plt.show()
    

def main():
    salary_by_college() 

main()
