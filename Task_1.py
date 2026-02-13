# 1. User Login Check
correct_username = "admin"
correct_password = "1234"

username = "admin"
password = "1234"

if username == correct_username and password == correct_password:
    print("1. Login Successful")
else:
    print("1. Invalid Credentials")


# 2. Pass / Fail Analyzer
marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("\n2. Pass / Fail Analyzer")
print("Total Students:", len(marks))
print("Pass Students:", pass_count)
print("Fail Students:", fail_count)


# 3. Simple Data Cleaner
names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    cleaned_names.append(name.strip().lower())

print("\n3. Cleaned Names:", cleaned_names)


# 4. Message Length Analyzer
messages = ["Hi", "Welcome to the platform", "OK"]

print("\n4. Message Length Analyzer")
for message in messages:
    length = len(message)
    print(f"Message: '{message}' | Length: {length}")
    if length > 10:
        print("This message is longer than 10 characters")


# 5. Error Message Detector
logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = logs.count("ERROR")

print("\n5. Total ERROR messages:", error_count)
