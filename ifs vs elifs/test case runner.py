import json
import time
import math

states = ["A", "B", "C", "D", "E", "F"]

elif_checks = []
elif_checks_total = 0
elif_count = 0
elif_average = 0

if_checks = []
if_checks_total = 0
if_count = 0
if_average = 0

time_started = 0
time_ended = 0
time_delta = 0

def average(x):
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    n = len(x)
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

def testSequenceElseIfs(case):
    global elif_checks_total, elif_count
    
    checks = 0
    for i in range(len(case)):
        current_state = case[i]
        checks += 1
        if current_state == "G":
            break
        if current_state == "A":
            checks += 1
            continue
        elif current_state == "B":
            checks += 2
            continue
        elif current_state == "C":
            checks += 3
            continue
        elif current_state == "D":
            checks += 4
            continue
        elif current_state == "E":
            checks += 5
            continue
        elif current_state == "F":
            checks += 6
            continue
    
    elif_checks.append(checks)
    elif_checks_total += checks
    elif_count += 1
        
def testSequenceIfs(case):
    global states, if_checks_total, if_count
    
    i = 0
    checks = 0
    while i < len(case):
        checks += 1
        current_state = case[i]
        if current_state == "G":
            break
        
        while i < len(case):
            next_state = case[i + 1]
            if next_state in states and states.index(current_state) < states.index(next_state):
                current_state = next_state
                i +=1
            else:
                break
        
        i += 1
        checks += 6
    
    if_checks.append(checks)
    if_checks_total += checks
    if_count += 1
    
def test_case_set(json_file, case_set_id):
    global time_started, time_ended, time_delta, elif_average, elif_checks_total, elif_count, if_average, if_checks_total, if_count, elif_checks, if_checks
    
    time_started = time.time()
    
    for case in json_file[case_set_id]["cases"]:
        testSequenceElseIfs(case)
        testSequenceIfs(case)
        
    time_ended = time.time()
    time_delta = round(time_ended - time_started, 3)
            
    elif_average = elif_checks_total / elif_count
    if_average = if_checks_total / if_count

    print("CaseSet(\"" + json_file[case_set_id]["name"] + "\") {")
    print("\tCases Run: ", elif_count)
    print("\tTook: ", time_delta, "(s)")
    print("")
    print("\tTotal Checks Elifs: ", elif_checks_total)
    print("\tAverage Checks Elifs: ", elif_average)
    print("")
    print("\tTotal Checks Ifs: ", if_checks_total)
    print("\tAverage Checks Ifs: ", if_average)
    print("")
    print("\tChange Percent: ", if_average / elif_average)
    print("\tr: ", pearson_def(elif_checks, if_checks))
    print("}")
    
def reset_variables():
    global time_started, time_ended, time_delta, elif_average, elif_checks_total, elif_count, if_average, if_checks_total, if_count, elif_checks, if_checks
    
    elif_checks = []
    elif_checks_total = 0
    elif_count = 0
    elif_average = 0

    if_checks = []
    if_checks_total = 0
    if_count = 0
    if_average = 0

    time_started = 0
    time_ended = 0
    time_delta = 0

with open("test_cases.json", "r") as file:
    print("")
    json_file = json.load(file)
    for id in json_file:
        test_case_set(json_file, id)
        reset_variables()
        print("")
    print("")