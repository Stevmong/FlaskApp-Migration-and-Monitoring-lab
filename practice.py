print("reverse string examples")

def reverse_string(s: str) -> str:
    return s[::-1]
print(reverse_string("Andela"))


log = "2026-08-10 22:39:01 ERROR123"
# Reverse the string
rev = log[::-1]

# Grab the first 7 characters (which are the error code backwards)
error_code = rev[:7][::-1]  # "ERROR123"
print(error_code)


log = "2026-08-10 22:39:01 ERROR123"

# Get the last word (error code)
error_code = log.split()[-1]
print(error_code)  # ERROR123

# Get the first word (date)
date = log.split()[0]
print(date)  # 2026-08-10

# Get the second word (time)
time = log.split()[1]
print(time)  # 22:39:01

print("---------------------------------")

print("word count example: useful to check ERROR frequency, Failed builds FAILURE vs SUCCESS, API call counts POST or GET Resource monitoring count timeout, connection reset")

def word_count(text: str) -> dict:
    counts = {}  # empty dictionary
    for word in text.split():  # loop through each word
        counts[word] = counts.get(word, 0) + 1
    return counts

print(word_count("devops devops devops devops azure azure"))

print("another example")

log_data = "ERROR ERROR WARNING INFO ERROR"
print(word_count(log_data))
# Output: {'ERROR': 3, 'WARNING': 1, 'INFO': 1}

print("---------------------------------")

print("Arrays and Lists example Sorting & Searching means finding a specific item, in this example sorting the numbers and checking if number 3 is found")

numbers = [3, 1, 2, 5, 4]

# Sort the list
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Search for a number
target = 3
if target in numbers:
    print(f"{target} found!")
else:
    print(f"{target} not found.")


print("---------------------------------")


print("Recursion, Stack depth example, Directory traversal Each nested folder increases stack depth, for Config parsing Each nested key increases depth, for Monitoring dependencies Each service call adds depth until you find the failing one")


import sys

def recursive_function(n, depth=0):
    print(f"Entering depth {depth}, n={n}")
    
    # base case
    if n == 0:
        print(f"Reached base case at depth {depth}")
        return
    
    # recursive call
    recursive_function(n-1, depth+1)
    
    print(f"Exiting depth {depth}, n={n}")

# --- Test 1: Normal recursion with small depth ---
print("=== Normal Recursion Test ===")
recursive_function(5)

# --- Test 2: Force stack overflow by lowering recursion limit ---
print("\n=== Stack Overflow Test ===")
sys.setrecursionlimit(50)   # artificially low limit
try:
    recursive_function(100) # will exceed the stack depth
except RecursionError as e:
    print("RecursionError caught:", e)


print("---------------------------------")

print(" What This Does, Normal Test Runs recursive function 5 it  shows how stack depth grows and shrinks safely, Overflow Test: Sets recursion limit to 50, then tries recursivefunction(100) exceeds the limit and throws a RecursionError, The try/except block catches the error so your program does not crash, and prints a friendly message")


print("---------------------------------")


print("Example with file handling, You read the file back into content, The script checks If ERROR is found prints Bad, If SUCCESS is found prints Good, If neither prints Unknown status")

# Write a status to the file
with open("log.txt", "w") as f:
    f.write("ERROR: Something failed\n")  # could also be "SUCCESS: Everything worked\n"

# Read the file and check content
with open("log.txt", "r") as f:
    content = f.read()

if "ERROR" in content:
    print("Bad: Something failed")
elif "SUCCESS" in content:
    print("Good: Everything worked")
else:
    print("Unknown status")



print("Very useful for log parsing, monitoring and others, grafana or azure application insights do this")


print("---------------------------------")

print("Automation Script Example useful to Parse a log file and count errors")

def count_errors(filename: str) -> int:
    count = 0
    with open(filename, "r") as f:
        for line in f:
            if "ERROR" in line:
                count += 1
    return count

print(count_errors("log.txt"))


print("---------------------------------")

print("Error Handling example, useful to catch problems so your script does not crash")

try:
    num = int("abc")  # invalid conversion
except ValueError as e:
    print("Error occurred:", e)

print("---------------------------------")