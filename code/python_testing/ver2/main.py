# main.py - this file will init the workout as a csv file

import datetime as dt
import csv

import workout as w
import exercise as e
import config as cf

print('Workout Tracker by pabloSanchezBB')
print('This is the Initialization step of the Tracker')
print('WARNING: THIS WILL OVERWRITE EXISTING DATA')
is_init = input('Do you wish to proceed? y/n: ')

if is_init == 'y' or is_init == 'Y' or is_init == 'YES' or is_init == 'Yes' or is_init == 'yes':
    # Run the program as usual

    # Create the CSV File
    filename = 'workout_data.csv'
    with open(filename, 'w', newline = '') as file
    writer = csv.writer(file) # Create the Writer Object
    # Use writer.writerow(data) for adding rows to the document

else:
    # Exit, the User doesn't want to Initialize the csv
    print('If you meant to view your workouts, try \'./view.sh\'')
    print('If you meant to log a workout, try \'./log.sh\'')
    print('\nExiting...')
    exit()
