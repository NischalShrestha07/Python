from turtle import st


student={
    "name":"Nischal Shrestha",
    "age":20,
    "address":"Nepal"

}
extraDict={
    "Year":2024,
    "GPA":3.64

}
student.update(extraDict)
print(student)

for key,value in student.items():
    key=key.capitalize()
    print(f"{key}:{value}")
    
    

# if "address" in student:
#     print("The name is present")
# else:
#     print("The name is not present")

        