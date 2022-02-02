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

## TODO: Make the workout logger auto-cycle through the ppl cycle


# Set the Starting Date:
def set_start_date():
    start_date = dt.date(c.starting_date_year, c.starting_date_month, c.starting_date_day)

def build_database():
    pass

def build_workouts(w):
# TODO: build the workout Object using w(the json)
    workout_list = [None] * len(w)
    for i in w: # For all the workouts:
        temp_name = i
        temp_num_exercises = len(w[i])
        temp_exercise_list = [None] * len(w[i])
        for x in range(len(w[i])):
            # Create a Temp Variable of the Dictionary Version of the Exercise
            temp_e = w[i][str(x+1)]
            # Create the Exercise;
            temp_add_to_list = c.Exercise(temp_e['name'], temp_e['sets'], temp_e['min_reps'], temp_e['max_reps'])
            # Add the Exercise Object to the List:
            temp_exercise_list[x] = temp_add_to_list

        # Now Build the Workout Object
        temp_workout = c.Workout(temp_name, temp_num_exercises, temp_exercise_list)
        workout_list[i] = temp_workout
    return workout_list

# Main Code:


# Testing Class Stuff:

x = c.Exercise('lift', 3, 8, 10)
build_workouts(c.workouts)
