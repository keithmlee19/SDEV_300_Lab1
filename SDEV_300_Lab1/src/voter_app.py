'''Program to simulate a voter eligibility/registration application'''
import sys

# function to handle invalid inputs
def handlefun(i):
    pass

# function to ask user if they want to keep going with registration
def continue_reg():
    while True:
        try:
            user_input = input("Do you want to continue with voter registration?\n")
            if user_input.lower() == "yes":
                handlefun(user_input)
                break
            else:
                print("You've indicated that you want to stop. Thanks and goodbye")
        except:
            pass
        
        print("Invalid input, please enter yes or no")
    
print("Welcome to the Python voter registration application.")
continue_reg()
fname = input("What is your first name?\n")
lname = input("What is your last name?\n")
continue_reg()

while True: # validate age
    try:
        age = int(input("What is your age?\n"))
        if age < 120:
            handlefun(age)
            break
    except:
        pass
    
    print("Invalid age input, please try again")
    continue_reg()

continue_reg()
while True:
    try:
        citizen = input("Are you a U.S. citizen?\n")
        if citizen.lower() == "yes" or citizen.lower() == "no":
            handlefun(citizen)
            break
    except:
        pass
    print("Invalid input, please enter yes or no")
    continue_reg()

if age >= 18 and citizen.lower() == "yes":
    while True: # validate state/US territory
        try:
            state = input("What state/territory do you live in? Enter 2-letter abbreviation\n")
            state_arr = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC',
            'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
            'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE',
            'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK',
            'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT',
            'VI', 'VA', 'WA', 'WV', 'WI', 'WY']
            if state in state_arr:
                handlefun(state)
                break
        except:
            pass
        
        print("Sorry, that was not a valid abbreviation. Please try again.")
        continue_reg()
else:
    print("Sorry, you are not eligible to register to vote. Thanks and goodbye.\n")
    sys.exit(0)

while True: # validate zip code, lowest zip code is 00501 and highest is 99950
    try:
        zipcode = input("What is your zipcode?\n")
        if int(zipcode) in range(501,99951) and len(zipcode) == 5:
            handlefun(zipcode)
            break
    except:
        pass
    
    print("Invalid zip code, please try again")
    continue_reg()

print("Thanks for registering to vote. Here is the information we received:")
print("Name (first last): " + fname + " " + lname)
print("Age: " + str(age))
print("U.S. Citizen: Yes")
print("State: " + state)
print("Zipcode: " + zipcode)
print("Thanks for using the Voter Registration Application. Your voter registration card should be shipped within 3 weeks.")
