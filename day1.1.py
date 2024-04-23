name=["nischal","rohan","sushil"]
print(name)
name.append("Niraj")
name.extend("dipan")
name.insert(0,"Hikmat")
# name.pop("rohan")

del name[0]
name.reverse()
subName=name.copy()
print(f"These are datas of name: {name}")
print()
print(F"These are the datas of subNames:{subName}")

