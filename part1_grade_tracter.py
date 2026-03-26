
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"}
]
cleaned_students = []
for student in raw_students:
    # clean name 
    name = student["name"].strip().title()
    # convert roll
    roll = int(student["roll"])
    #convert marks string to list
    marks = list(map(int,
student["marks_str"].split(",")))
    # check valid name 
    valid = all(word.isalpha() for word in name.split())

     # store cleaned data
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "valid": valid
     })
#print results
for s in cleaned_students:
    print(f"student: {s['name']}")
    print(f"roll no: {s['roll']}")
    print(f"marks: {s['marks']}")
    print("valid name" if s["valid"] 
else "invalid name")

# extra requirement
for s in cleaned_students:
    if s["roll"] == 101:
        print("\nall caps:",
s["name"].upper())
    if s["roll"] == 103:
        print("lowercase:",
s["name"].lower())        
    
      



















