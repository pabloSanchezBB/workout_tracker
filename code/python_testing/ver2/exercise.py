# exercise.py - This file is the Class Definition of an Exercise Object
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

    def to_string():
        ret_str = ''
        ret_str += str(self.name) + ':\n'
        ret_str += '# of Sets: ' + str(self.num_sets) + 's\n'
        ret_str += 'Rep Range: ' + str(self.min_reps) + '-' str(max_reps) + 'r\n'
        if self.weight_arr[0] == None:
            continue
        else:
            for i in range(len(weight_arr)):
                ret_str += 'Set ' + str(i+1) + 'Weight: ' + str(self.weight_arr[i])
            # exit loop


	# Setters(defaulted to private unless necessary):
	def __set_name(self, name):
		self.name = name
		return

	def __set_num_sets(self, num_sets):
		self.num_sets = num_sets
		return

	def __set_min_reps(self, min_sets):
		self.min_sets = min_sets
		return

	def __set_max_reps(self, max_reps):
		self.max_reps = max_reps
		return

	def __set_weight_arr(self, weight_arr):
		self.weight_arr = weight_arr
		return

	# Getters(defaulted to private unless necessary):
	def get_name(self):
		return self.name

	def get_num_sets(self):
		return self.num_sets

	def get_min_reps(self):
		return self.min_reps

	def get_max_reps(self):
		return self.max_reps

	def get_weight_arr(self):
		return self.weight_arr
