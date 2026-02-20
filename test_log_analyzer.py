import os, importlib

def test_count_total_actions(module):
    # check empty file
    if module.count_total_actions("test_data/empty_file.txt") == 0:
        print("Passed: empty file case " + str(module).split()[1])
    else:
        print("Failed: empty file case " + str(module).split()[1])
    
    # check file with one line
    if module.count_total_actions("test_data/one_line.txt") == 1:
        print("Passed: one line file case " + str(module).split()[1])
    else:
        print("Failed: one line file case " + str(module).split()[1])
    
    # check file with multiple lines
    if module.count_total_actions("test_data/multi_line.txt") == 4:
        print("Passed: multi line file case " + str(module).split()[1])
    else:
        print("Failed: multi line file case " + str(module).split()[1])

def test_count_player_actions(module):
	print("Is not yet implemented")

def test_find_total_value(module):	
	print("Is not yet implemented")		 
                      
def test_is_player_present(module):
    print("Is not yet implemented")

def test_get_first_action(module):
	print("Is not yet implemented")


def main():
    files = os.listdir(".")
    files = [f for f in files if os.path.isfile(f) and "log_analyzer" in f and 'test' not in f]

    test_list = [test_count_total_actions,test_count_player_actions,test_find_total_value,test_is_player_present,test_get_first_action]
	
    for item in test_list:
        print(f"Starting {str(item).split()[1]}")
        for file in files:
            module = importlib.import_module(file[:-3])
            item(module)
            print()
        print(f"Finished {str(item).split()[1]}\n\n\n")

if __name__ == "__main__":
    main()