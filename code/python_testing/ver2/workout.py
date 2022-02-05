# workout.py - This is the Class Definition for a Workout Object

class Workout:
	def __init__(self, name, num_exercises, exercise_list):
		self.name = name
		self.num_exercises = num_exercises # size of the sub-dict containing the workout
		self.exercise_list = exercise_list # Dictionary Storing the Exercise Object params
		self.build_workout()

	# Build the Workout Collection of Exercises
	def build_workout(self):
		pass

    # ToString Method
    def to_string():
        ret_str = ''
        ret_str += 'Workout: ' + str(self.name) + '\n'
        for i in range(len(self.exercise_list)):
            temp_e = self.exercise_list[i]
            ret_str += '\t' + str(i+1) + '- ' + str(temp_e.get_name())
            ret_str += ': ' + str(temp_e.get_num_sets()) + 's x '
            ret_str += str(temp_e.get_min_reps()) + '-' + str(temp_e.get_max_reps())
            ret_str += '\n'

	# Setters:
	def __set_name(self, name):
		self.name = name
		return

	def __set_num_exercises(self, num_exercises):
		self.num_exercises = num_exercises
		return

	def __set_exercise_list(self, exercise_list):
		self.exercise_list = exercise_list
		return

	# Getters:
	def get_name(self):
		return self.name

	def __get_num_exercises(self):
		return self.num_exercises

	def __get_exercise_list(self):
		return self.exercise_list
