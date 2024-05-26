

# # def readFile(filename):
# with open('/readme.txt','r') as file:
#     content=file.read()
#     print(content)
#     # return content    
            


# # filename='readme.txt'
# # content=readFile(filename)
# # print(content)
def read_and_print_file(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        print(content)

# Example usage:
read_and_print_file('/readme.txt')
