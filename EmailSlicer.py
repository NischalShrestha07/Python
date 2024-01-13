# Example:
'''
hello@codewithNischal@gmail.com

Output:
UserName: hello
domain: codewithNischal
extension: com

'''


def main():
    print("Welcome to Email Slicer")
    print("")

    email_input=input("Input Your Email Address:")
    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")


    print("UserName: ", username)
    print("Domain: ", domain)
    print("extension: ", extension)
while True:
  main()
    
     