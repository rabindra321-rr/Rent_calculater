rent=int(input("Enter Rent your Room="))
food=int(input("Enter Food Amount="))
electric=int(input("Enter total of electricity spend="))
#charge=int(input("Enter the charge per unit="))
person=int(input("Enter the number of person="))
total=(rent+food+electric)/person
print("Each person will pay=",total)