################################################################################
# Workout Class: A Workout is a Collection Object of Exercises
################################################################################
class Workout:
	def __init__(self, name, num_exercises, exercise_list):
		self.name = name
		self.num_exercises = num_exercises # size of the sub-dict containing the workout
		self.exercise_list = exercise_list # Dictionary Storing the Exercise Object params
		self.build_workout()

	# Build the Workout Collection of Exercises
	def build_workout(self):
		pass

################################################################################


################################################################################
# Exercise Class Definition:
################################################################################
class Exercise:
	def __init__(self, name, num_sets, min_reps, max_reps):
		self.name = name
		self.num_sets = num_sets
		self.min_reps = min_reps
		self.max_reps = max_reps
		# vvv weight_arr is initialized here vvv
		#self.prompt_weight_per_set()
		# Don't want to init here, only when we log

	# Exercise-Specific Functions(getting weight amts, etc.; privated for now):
	def prompt_weight_per_set(self):
		self.weight_arr = [None] * self.num_sets
		print('What was the total weight for...')
		for i in range(self.num_sets):
			self.weight_arr[i] = input("Set " + str(i+1) + '?\t')


	# Setters(defaulted to private unless necessary):
	def __set_name(self, name):
		self.name = name

	def __set_num_sets(self, num_sets):
		self.num_sets = num_sets

	def __set_min_reps(self, min_sets):
		self.min_sets = min_sets

	def __set_max_reps(self, max_reps):
		self.max_reps = max_reps

	def __set_weight_arr(self, weight_arr):
		self.weight_arr = weight_arr

	# Getters(defaulted to private unless necessary):
	def __get_name(self):
		return self.name

	def __get_num_sets(self):
		return self.num_sets

	def __get_min_reps(self):
		return self.min_reps

	def __get_max_reps(self):
		return self.max_reps

	def __get_weight_arr(self):
		return self.weight_arr
################################################################################


################################################################################
# DATA: Starting Date of Workout Plan, Sample Workout JSON
################################################################################

starting_date_month = 1
starting_date_day = 25
starting_date_year = 2022

			########################################################

# Key:
# 	- A Negative Number of Reps Denotes the Exercise is Taken to Failure
workouts = { 'Push Day 1' :
				{
					'1' 	:	{'name' : 'Flat Bench','sets' : 3,'min_reps' : 6,'max_reps' : 8},
					'2' 	:	{'name' : 'Incline Bench','sets' : 3,'min_reps' : 6,'max_reps' : 8},
					'3' 	:	{'name' : 'Decline Bench','sets' : 3,'min_reps' : 6,'max_reps' : 8},
					'4' 	:	{'name' : 'Standing Arnold Press','sets' : 3,'min_reps' : 10,'max_reps' : 12},
					'5' 	:	{'name' : 'Dips','sets' : 3,'min_reps' : 12,'max_reps' : 15},
					'6' 	:	{'name' : 'Skull-Crusher','sets' : 3,'min_reps' : 8,'max_reps' : 10},
					'7' 	:	{'name' : 'Egyptian Lateral Raise','sets' : 3,'min_reps' : 10,'max_reps' : 12},
					'8' 	:	{'name' : 'Cable Tricep Kickback','sets' : 3,'min_reps' : 20,'max_reps' : 30},
				},

			 'Pull Day 1' :
			 	{
					'1' 	:	{'name' : 'Pull-Ups','sets' : 3,'min_reps' : 6,'max_reps' : 10},
					'2' 	:	{'name' : 'Seated Cable Row','sets' : 3,'min_reps' : 15,'max_reps' : 20},
					'3' 	:	{'name' : 'Kneeling Cable Pullover','sets' : 3,'min_reps' : 15,'max_reps' : 20},
					'4' 	:	{'name' : 'Hammer Cheat Curl','sets' : 3,'min_reps' : 8,'max_reps' : 10},
					'5' 	:	{'name' : 'Seated Incline Curls','sets' : 3,'min_reps' : 12,'max_reps' : 15},
					'6' 	:	{'name' : 'Hang Cleans','sets' : 3,'min_reps' : 8,'max_reps' : 10},
					'7' 	:	{'name' : 'Preacher Barbell Curls','sets' : 3,'min_reps' : 10,'max_reps' : 12}
			 	},

			 'Legs Day 1' :
			 	{
					'1'		:	{'name' : 'Squat Pyramid Warmup Set 1','sets' : 1,'min_reps' : 10,'max_reps' : 12},
					'2'		:	{'name' : 'Squat Pyramid Warmup Set 2','sets' : 1,'min_reps' : 8,'max_reps' : 10},
					'3'		:	{'name' : 'Squat Pyramid Warmup Set 3','sets' : 1,'min_reps' : 6,'max_reps' : 8},
					'4'		:	{'name' : 'Squat Pyramid Warmup Set 4','sets' : 1,'min_reps' : 3,'max_reps' : 4},
					'5'		:	{'name' : 'Squat Pyramid Warmup Set 5','sets' : 1,'min_reps' : 1,'max_reps' : 2},
					'6'		:	{'name' : 'Low Bar Squat','sets' : 4,'min_reps' : 4,'max_reps' : 6},
					'7'		:	{'name' : 'Romanian Deadlift','sets' : 3,'min_reps' : 10,'max_reps' : 12},
					'8'		:	{'name' : 'Bulgarian Split Squat','sets' : 3,'min_reps' : 12,'max_reps' : 15},
					'9'		:	{'name' : 'Leg Extension Machine','sets' : 3,'min_reps' : 10,'max_reps' : 12},
					'10'	:	{'name' : 'Seated Hamstring Curl','sets' : 3,'min_reps' : 10,'max_reps' : 12},
					'11'	:	{'name' : 'Calf Raise','sets' : 3,'min_reps' : 15,'max_reps' : 20},
					'12'	:	{'name' : 'Decline Crunches','sets' : 3,'min_reps' : 12,'max_reps' : 15},
					'13'	:	{'name' : 'Tibialis Raises','sets' : 3,'min_reps' : 15,'max_reps' : 20},
					'14'	:	{'name' : 'ATG Lunges','sets' : 3,'min_reps' : 10,'max_reps' : 12},
				},

			 'Push Day 2' :
			 	{
					'1'		:	{'name' : 'Overhead Press','sets' : 4,'min_reps' : 3,'max_reps' : 4},
					'2'		:	{'name' : 'Close Grip Flat Bench','sets' : 3,'min_reps' : 6,'max_reps' : 8},
					'3'		:	{'name' : 'Close Grip Incline Bench Press','sets' : 3,'min_reps' : 6,'max_reps' : 8},
					'4'		:	{'name' : 'Close Grip Decline Bench Press','sets' : 3,'min_reps' : 6,'max_reps' : 8},
					'5'		:	{'name' : 'Cable Crossover','sets' : 3,'min_reps' : 10,'max_reps' : 12},
					'6'		:	{'name' : 'Overhead Tricep Extension','sets' : 3,'min_reps':10,'max_reps' : 12},
					'7'		:	{'name' : 'Dumbell Lateral Raises','sets' : 3,'min_reps':21,'max_reps' : 21},
					'8'		:	{'name' : 'Neck Flexion','sets' : 3,'min_reps' : 10,'max_reps' : 12},
					'9'		:	{'name' : 'Neck Extension','sets' : 3,'min_reps' : 10,'max_reps' : 12}
			 	},

			 'Pull Day 2' :
			 	{
					'1'		:	{'name':'Lat Pulldown','sets': 3,'min_reps': 10,'max_reps':12},
					'2'		:	{'name':'Chest-Supported Row','sets': 3,'min_reps': 10,'max_reps':12},
					'3'		:	{'name':'Rope Face Pull','sets': 3,'min_reps': 10,'max_reps':15},
					'4'		:	{'name':'Incline Dumbell Shrug','sets': 3,'min_reps': 10,'max_reps':12},
					'5'		:	{'name':'Chest Fly Machine','sets': 2,'min_reps': 10,'max_reps':15},
					'6'		:	{'name':'Reverse Barbell Curl','sets': 3,'min_reps': 8,'max_reps':10},
					'7'		:	{'name':'Standard Barbell Curl','sets': 3,'min_reps': 8,'max_reps':10},
					'8'		:	{'name':'Hang Clean','sets': 3,'min_reps': 6,'max_reps':8}
			 	},

 			 'Legs Day 2' :
 			 	{
					'1'		:	{'name':'Deadlift Warmup Set 1','sets':1,'min_reps':10,'max_reps':12},
					'2'		:	{'name':'Deadlift Warmup Set 2','sets':1,'min_reps':8,'max_reps':10},
					'3'		:	{'name':'Deadlift Warmup Set 3','sets':1,'min_reps':5,'max_reps':8},
					'4'		:	{'name':'Deadlift Warmup Set 4','sets':1,'min_reps':3,'max_reps':4},
					'5'		:	{'name':'Deadlift Warmup Set 5','sets':1,'min_reps':1,'max_reps':2},
					'6'		:	{'name':'Deadlifts','sets':3,'min_reps':3,'max_reps':4},
					'7'		:	{'name':'Hack Squat','sets':3,'min_reps':10,'max_reps':12},
					'8'		:	{'name':'Reverse Hack Squat','sets':3,'min_reps':10,'max_reps':12},
					'9'		:	{'name':'Leg Press','sets':3,'min_reps':10,'max_reps':12},
					'10'	:	{'name':'Single Leg Hip Thrust','sets':2,'min_reps':12,'max_reps':15},
					'11'	:	{'name':'Hip Thrust','sets':3,'min_reps':6,'max_reps':8},
					'12'	:	{'name':'Nordic Hamstring Curl','sets':2,'min_reps':8,'max_reps':10},
					'13' 	:	{'name':'Prisoner Back Extension','sets':2,'min_reps':8,'max_reps':10},
					'14' 	:	{'name':'Single Leg Calf Raise','sets':3,'min_reps':15,'max_reps':20},
					'15' 	:	{'name':'Weighted L-Sit Hold(to Failure)','sets':3,'min_reps':-1,'max_reps':-1},
					'16' 	:	{'name':'ATG Lunges','sets':3,'min_reps':10,'max_reps':12},
				}
			}
################################################################################
