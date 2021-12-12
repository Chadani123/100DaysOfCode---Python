def func1():
     print("Hello Chadni!")
     print("You are beautiful.")

# func1()
# func1()
# func1()
# func1()
# func1()

def print_hello():
    print("hello")

#print_hello()
def addition(firstname,lastname):
    print(firstname + lastname)

fullname = addition('Chadni ', 'Acharya')


#parameters
def get_fullname(firstname, middlename, lastname):
    fullname = firstname+' '+middlename+' '+lastname
    print(fullname)

    firstname = 'Sagar'
    middlename = 'Kumar'
    lastname = 'Thapa'

#Calling function with arguments
get_fullname(firstname = "Sagar", middlename = "Kumar",lastname= "Thapa")

def fruit_counter(basket):
    for fruit in basket:
        print("We have {{fruit}} in the basket.".format(fruit))
    print('we have total {} in the basket'.format(len(basket)))

basket = ["Apple", "Orange", "Mango"]

fruit_counter(basket)