

def count_total_actions(log_filename):
	"""
	Calculates the total number of actions in the given file.
	
	Args:
		log_filename: file of player logs
	
	Returns:
		int: total number of actions in log
	"""
	
	file = open(log_filename,"r")
	
	count = 0

	for line in file:
		count += 1
	
	file.close()

	return count

def count_player_actions(log_filename, player_name):
	"""
	Calculates the total number of actions in the given file performed by the given player.
	
	Args:
		log_filename: file of player logs
		player_name: player name
	
	Returns:
		int: total number of actions performed by player
	"""
	file = open(log_filename,'r')

	count = 0

	for line in file:
		if player_name in line:
			count += 1
	
	file.close()
	
	return count

def find_total_value(log_filename, action_type):	
	"""
	Calculates the total value of the given action type in the given file.
	
	Args:
		log_filename: file of player logs
		action_type: action type
	
	Returns:
		int: total value of the given action type
	"""
	file = open(log_filename,'r')

	total = 0

	for line in file:
		if action_type in line:
			total += int(line.strip()[-1])
	
	file.close()
	
	return total		 
                      
def is_player_present(log_filename, player_name):
    """
	Checks to see if the given player is present in the log file.
	
	Args:
		log_filename: file of player logs
		player_name: player name
	
	Returns:
		bool: presence of the given player
	"""
    return player_name in log_filename

def get_first_action(log_filename):
	"""
	Returns the first log line of the first action in the file.

	Args:
		log_filename: file of player logs

	Returns:
		str: data from first action in file
	"""
	
	return log_filename[0]