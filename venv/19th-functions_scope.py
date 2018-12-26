#########global var 'name'###############

name = "Tom"


def say_hi1():
    print("Hello", name)


def say_bye1():
    print("Good bye", name)


say_hi1()
say_bye1()

print('\n')

##############local var 'name'############

def say_hi2():
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)


def say_bye2():
    name = "Tom"
    print("Good bye", name)


say_hi2()
say_bye2()

print('\n')

###################local and global vars 'name'#################

name = "Tom"


def say_hi3():
    print("Hello", name)


def say_bye3():
    name = "Bob"
    print("Good bye", name)


say_hi3()  # Hello Tom
say_bye3()  # Good bye Bob

print('\n')

###############use global var when you have a local#########

name4 = 'Edgar'


def say_bye4():
    global name4
    name4 = "Bob"
    print("Good bye", name4)


say_bye4() # Tom