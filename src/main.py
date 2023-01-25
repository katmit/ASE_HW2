import sys
import os
import random
import traceback
import data

# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.sys.path.insert(0,parentdir) 

# set to their default values
random_instance = random.Random()
seed = 937162211 
dump = False

## run_test counts the number of arguments that have been passed and failed and it also,
## it displays the names tests passed and failed.
def run_tests():
    print("Executing tests...\n")
    
    passCount = 0
    failCount = 0
    test_suite = [test_num_generation_rand, test_syms, test_nums, test_show_dump]

    for test in test_suite:
        if(test()):
            passCount = passCount + 1
        else:
            failCount = failCount + 1
    
    print("Passing: " + str(passCount) + "\nFailing: " + str(failCount))

# uses the value of the dump parameter and passed exception to determine what message to display to the user
def get_crashing_behavior_message(e: Exception):
    crash_message = str(e)
    if(dump):
        crash_message = crash_message + '\n'
        stack = traceback.extract_stack().format()
        for item in stack:
            crash_message = crash_message + item
            
    return crash_message

# api-side function to get the current seed value
def get_seed() -> int:
    return seed

# api-side function to get the current dump boolean status
def should_dump() -> bool:
    return dump

## find_arg_values gets the value of a command line argument
# first it gets set of args 
# second it get option A (-h or -d or -s or -f )
# third is get option B (--help or --dump or --seed or --file)
def find_arg_value(args: list[str], optionA: str, optionB: str) -> str:
    index = args.index(optionA) if optionA in args else args.index(optionB)
    if (index + 1) < len(args):
        return args[index + 1]
    return None

help_string = """script.py : an example script with help text and a test suite.\n
based on the original script (script.lua) by Tim Menzies <timm@ieee.org>\n
USAGE:   script.lua  [OPTIONS] [-g ACTION]
OPTIONS:
  -d  --dump  on crash, dump stack = false
  -f  --file  name of file         = /// file path ///
  -g  --go    start-up action      = data
  -h  --help  show help            = false
  -s  --seed  random number seed   = 937162211
]]"""

if __name__ == "__main__":
    args = sys.argv
    print(args[2])
    try:
        if '-h' in args or '--help' in args:
            print(help_string)

        if '-d' in args or '--dump' in args:
            dump = True

        if '-f' in args or '--file' in args:
            data.data(args[2])

        if '-s' in args or '--seed' in args:
            seed_value = find_arg_value(args, '-s', '--seed')
            if seed_value is not None:
                try:
                    seed = int(seed_value)
                except ValueError:
                    raise ValueError("Seed value must be an integer!")
            else:
                print("USAGE: Provide an integer value following an -s or --seed argument to set the seed value.\n Example: (-s 3030, --seed 3030)")
        
        # NOTE: the seed will be set in main, the rest of the application need not set it
        random_instance.seed(seed)    
        if '-g' in args or '--go' in args:
            run_tests()
    except Exception as e:
        print(get_crashing_behavior_message(e))