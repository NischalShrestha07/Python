

def fibbo(n):
    if n<=1:
        return n
    else:
        return (fibbo(n-1)+fibbo(n-2))

nterms=10

if nterms<=0:
    print("Positive number only")
else:
    for i in range(nterms):
     print(fibbo(i))