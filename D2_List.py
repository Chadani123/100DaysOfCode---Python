new_guests = ['Sagar','Bhim','Sanju','Rejina','Riya']
print(new_guests[2])
print (new_guests)
new_guests.sort()
print (new_guests)

#Creating another list of special guests
special_guests = []
special_guests.append (new_guests[0])
special_guests.append (new_guests[1])
special_guests.append (new_guests[2])
print (special_guests)

#Removing one guest
special_guests.remove('Riya')
print (special_guests)

#Adding another guest
special_guests.append('Kanchan')
print (special_guests)
