print("___Compound Interest Calculator___")


Principal=float(input("Enter principal value: "))
Rate=float(input("Enter rate:"))
Time=float(input("Enter interest:"))
Amount= Principal*(pow((1+Rate/100),Time))
ci = Amount - Principal
print("the compound interest is:", ci)