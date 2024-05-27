
# Methods to explore:
# 1. append()
# 2. insert()
# 3. extend()
# 4. remove()
# 5. pop()
# 6. count()
# 7. index()
# 8. sort()
# 9. reverse()
# 10. clear()




student=["Nischal","Ayush","Sushil","Rohan","Neeraz","Hikmat"]

student.append("Naruto")
print("\nAppened Student:\n",student)

# insert() methods:
student.insert(4,"Heeeyna")
print("\nNew Student is Inserted:\n",student)

# use of extend() method  making another list 
extendedData=["Nishant","Suprim"]
student.extend(extendedData)
print("Extended Students Data:",student)

list=[45,12,48,5,745,48,5,9]
list.sort()
print("Permanent way of Sorting:\n",list)
# print(list)

# temporary way of sorting through sorted() method:
anotherlist=[45,12,54,21,54,541,5,44,54,54,4]
sortNum=sorted(anotherlist)
print("Temporary way of Sorting:\n",sortNum)


