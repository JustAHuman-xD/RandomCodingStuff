import json
import time
import random

states = {
    "A": ["F", "B", "G"],
    "B": ["B", "C", "E"],
    "C": ["C", "D", "E"],
    "D": ["E", "A"],
    "E": ["A"],
    "F": ["A"]
}

def get_int_input(prompt):
    string_input = input(prompt)
    while not string_input.isnumeric():
        print("Not a Valid Input!")
        string_input = input(prompt)
    return int(string_input)

def get_bool_input(prompt):
    string_input = input(prompt).upper()
    while not (string_input == "Y" or string_input == "YES" or string_input == "T" or string_input == "TRUE" or string_input == "1" or string_input == "N" or string_input == "NO" or string_input == "F" or string_input == "FALSE" or string_input == "0"):
        print("Not a Valid Input!")
        string_input = input(prompt).upper()
    return string_input == "Y" or string_input == "YES" or string_input == "T" or string_input == "TRUE" or string_input == "1"

def generate_case(case):
    global states
    last_state = case[-1]
    if last_state == "G":
        return case
    else:
        next_states = states[last_state]
        return generate_case(case + random.choice(next_states))

case_set_id = ""
case_set_name = ""

cases_to_create = 0
max_case_attempts = 0

cases_made = 0
case_attempts = 0

time_started = 0
time_ended = 0
time_delta = 0

allow_duplicates = None

json_file = None
cases = []

with open("test_cases.json", "r") as file:
    json_file = json.load(file)
    
case_set_id = input("Input Case Set Id: ").lower().replace(" ", "_")
case_set_name = input("Input Case Set Name: ")

cases_to_create = get_int_input("How many cases to create: ")
max_case_attempts = get_int_input("How many attempts to create a case: ")

allow_duplicates = get_bool_input("Allow duplicates: ")

time_started = time.time()

while cases_made < cases_to_create and case_attempts < max_case_attempts:
    case = generate_case("A")
    case_attempts += 1
    if not case in cases or allow_duplicates:
        cases.append(case)
        cases_made += 1

time_ended = time.time()
time_delta = round(time_ended - time_started, 3)

with open("test_cases.json", "w") as file:
    json_file[case_set_id] = {}
    json_file[case_set_id]["name"] = case_set_name
    json_file[case_set_id]["cases"] = cases
    file.write(json.dumps(json_file, indent=4))
    
print("")
print("Created Case Set:", case_set_name, "(", case_set_id, ")")
print("Cases Made:", cases_made)
print("Case Attempts:", case_attempts)
print("Took:", time_delta, "(s)")
print("")