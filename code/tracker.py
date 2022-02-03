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

################################################################################
# Workout Plan Start Date Setter -- ONLY FOR INITIALIZATION USE
################################################################################
def set_start_date():
    start_date = dt.date(c.starting_date_year, c.starting_date_month, c.starting_date_day)

################################################################################


################################################################################
# Current Date Setter -- USED WITH LOGGING
################################################################################
def set_date_for_workout():
    today = dt.date.today()
    return today

################################################################################


################################################################################
# Builds Database of Persistent Storage
################################################################################
def build_database():
    pass
    # Persistent Storage Needs...
    #   - A Workout Object with the key of a Datetime object for the day of the workout
    #   - The Index of the Workout in the split, so the next day the program knows what the next Workout is
    # Use...
    #   - A Text Document?
    #   - Excel/CSV?
    #   - NoSQL Database?

################################################################################


################################################################################
# Workout Plan Builder -- ONLY FOR INITIALIZATION USE
################################################################################
def build_workouts(w):
    # Create an Empty List of Workout Objects
    workout_list = [None] * len(w)

    # Loop Through the Workouts
    for i in w:
        # Parameters for the Workout Object
        temp_name = i # Name of the Workout
        temp_num_exercises = len(w[i]) # Number of Exercises
        temp_exercise_list = [None] * len(w[i]) # The Exercise List that will be filled below

        # Loop Through The Exercises in the Workout
        for x in range(len(w[i])):
            # Create a Temp Variable of the Dictionary Version of the Exercise
            temp_e = w[i][str(x+1)]

            # Create the Exercise;
            temp_add_to_list = c.Exercise(temp_e['name'], temp_e['sets'], temp_e['min_reps'], temp_e['max_reps'])

            # Add the Exercise Object to the List:
            temp_exercise_list[x] = temp_add_to_list

        # Exit Inner For Loop, go to next workout or exit

        # Create the Workout Object
        temp_workout = c.Workout(temp_name, temp_num_exercises, temp_exercise_list)
        # Add the Workout to the List of Workouts
        workout_list[i] = temp_workout]
    # Exit Outer For Loop

    return workout_list

################################################################################


################################################################################
# MAIN CODE:
################################################################################

# Check to ensure the user wants to reset their workout plan
is_init_happening = input('This is the Initialization Mode. Restart your Workout? y/n:')

# Check User Input:
if is_init_happening == 'y' or is_init_happening == 'Y' or is_init_happening == 'yes' or is_init_happening == 'YES' or is_init_happening == 'Yes':
    continue
else:
    exit()



################################################################################
