"""main.py - program logic and helper functions for Python Data Analysis App"""

import pandas as pd

import matplotlib.pyplot as plt

# -------------------- Helper Functions -------------------------


def get_column_data(data_frame, column_name):
    """prints statistics and generates a histogram for a given column"""
    data_frame = data_frame[column_name]
    print("Count = ", data_frame.count(),
          "\nMean = ", data_frame.mean(),
          "\nStandard Deviation = ", data_frame.std(),
          "\nMin = ", data_frame.min(),
          "\nMax = ", data_frame.max())
    plt.hist(data_frame)
    plt.show()
    print('The Histogram of this column is now displayed.')


# -------------------- Program Logic -------------------------

if __name__ == '__main__':

    # prompt indicated load every column into memory even if they cannot be accessed
    population_df = pd.read_csv('PopChange.csv')
    housing_df = pd.read_csv('Housing.csv')

    print('***************** Welcome to the Python Data Analysis App**********')
    while True:
        print('\n Select the file you want to analyze:')
        print(' 1. Population Data \n 2. Housing Data \n 3. Exit the Program \n')
        selection = input()
        while selection not in ('1', '2', '3'):
            selection = input('Invalid Selection \n')

        if selection == '1':
            print('You have entered Population Data.\n')
            print('Select the Column you want to analyze:')
            print(' a. Pop Apr 1 \n b. Pop Jul 1 \n c. Change Pop \n d. Exit Column Menu \n')
            selection = input()
            while True:
                while selection not in ('a', 'b', 'c', 'd'):
                    selection = input('Invalid Selection \n')
                if selection == 'a':
                    print('You selected Pop Apr 1')
                    get_column_data(population_df, 'Pop Apr 1')
                    break
                if selection == 'b':
                    print('You selected Pop Jul 1')
                    get_column_data(population_df, 'Pop Jul 1')
                    break
                if selection == 'c':
                    print('You selected Change Pop')
                    get_column_data(population_df, 'Change Pop')
                    break
                if selection == 'd':
                    print('You selected to exit the column menu')
                    break

        elif selection == '2':
            print('You have entered Housing Data. \n')
            print('Select the Column you would like to analyze:')
            print(' a. Age \n b. Bedrooms \n c. Built \n d. Rooms'
                  ' \n e. Utility \n f. Exit Column \n')
            selection = input()
            while True:
                while selection not in ('a', 'b', 'c', 'd', 'e', 'f'):
                    selection = input('Invalid Selection \n')
                if selection == 'a':
                    print('You selected Age')
                    get_column_data(housing_df, 'AGE')
                    break
                if selection == 'b':
                    print('You selected Bedrooms')
                    get_column_data(housing_df, 'BEDRMS')
                    break
                if selection == 'c':
                    print('You selected Built')
                    get_column_data(housing_df, 'BUILT')
                    break
                if selection == 'd':
                    print('You selected Rooms')
                    get_column_data(housing_df, 'ROOMS')
                    break
                if selection == 'e':
                    print('You selected Utility')
                    get_column_data(housing_df, 'UTILITY')
                    break
                if selection == 'f':
                    print('You selected to exit the column menu')
                    break

        elif selection == '3':
            print('*************** Thanks for using the Data Analysis App**********')
            break
