

def binarySearch(list,element):
    middle=0
    start=0
    end=len(list)
    steps=0
    
    
    while (start<=end):
        print("Stop",steps, ":" ,str(list[start : end+1]))
        steps=steps+1
        middle =(start+end) // 2

         
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end=middle-1
        else:
            start=middle+1
    return -1
mylist={1,2,3,4,5,6,7,8,9,10,11,12}
target=2

binarySearch(mylist,target)
            