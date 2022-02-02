# This is the main Program that contains all of the main code.
# What this is gonna do:
#   - Build the Workout from the Config's json as a Collection of Exercise Objects
#   - Create a NoSQL Database to store the Data Persistently

# Process for the Program
# 	Get the Date that the Workout took place On
#	Take in what part of PPL you started on
#	Take in Weights for each exercise
import datetime as dt
import config as c

# Set the Starting Date:
def set_start_date():
    start_date = dt.date(c.starting_date_year, c.starting_date_month, c.starting_date_day)

def build_database():
    pass

def build_workouts(w):
    pass # TODO: build the workout Object using w(the json)
    for i in w:
        temp_name = i
        temp_num_exercises = len(w[i])
        temp_exercise_list = [None] * len(w[i])
        for x in range(len(w[i])):
            temp_e = w[i][str(x+1)] # This is the Exercise as a Dictionary
            print(temp_e)
            temp_add_to_list = c.Exercise(temp_e['name'], temp_e['sets'], temp_e['min_reps'], temp_e['max_reps'])
            print(temp_add_to_list)
            temp_exercise_list[x] = temp_add_to_list
    return


# Testing Class Stuff:

x = c.Exercise('lift', 3, 8, 10)
build_workouts(c.workouts)
