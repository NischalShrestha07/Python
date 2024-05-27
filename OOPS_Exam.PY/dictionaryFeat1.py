
# Methods to explore:
# 1. keys()
# 2. values()
# 3. items()
# 4. get()
# 5. pop()
# 6. popitem()
# 7. update()
# 8. clear()

from email.utils import getaddresses
from turtle import st


student={
    "name":"Nischal",
    "age":21,
    "address":"NEPAL",
    'grade':{
        'Math':91,
        'Science':85,
        'Nepali':53
    }
}
# only prints keys 
print(student.keys())

print(student.values())
print("")

# prints every items present on the student.
print("All Items:",student.items())

# use of get() method 
print("Age is:",student.get('age'))

# printing single value from dictionary
name=student.pop("name")
print("You Popped: ",name)

# below is to access the single value from the dictionary.
mathGrade=student.pop('grade')["Math"]
print("Math Grade:",mathGrade)

# use of popitem() which pops the last keys and values.
getAddress=student.popitem()
print("Last Item is:",getAddress)

# use of update() method
student.update({
    "Name":"Pri N ka",
    "qualification":"Bachelor",
    "Faculty":"Computer engineering"
})
print("Updated Student Details:\n",student)