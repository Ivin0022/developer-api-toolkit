a = [0, 1, 4, 9, 16, 25]


b = [ i**2 for i in range(10000) ]
c = [ i**2 for i in range(5) if i % 2 == 0]
d = [ (i**2 if i % 2 == 0 else i) for i in range(5)]

gb = (i**2 for i in range(10000))
gc = (i**2 for i in range(5) if i % 2 == 0)
gd = ((i**2 if i % 2 == 0 else i) for i in range(5))