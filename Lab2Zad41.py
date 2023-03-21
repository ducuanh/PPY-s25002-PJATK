#DUC ANH DINH S25002
a = int(input("podaj 1 liczbe; "))
b = int(input("podaj 2 liczbe; "))
c = int(input("podaj 3 liczbe; "))

delta = b**2 - 4*a*c

if delta > 0:
  print("Delta jest większa od 0")
else:
  print("Delta jest mniejsza od 0")
