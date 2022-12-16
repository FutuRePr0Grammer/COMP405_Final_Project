'''Module containing functions related to the user interface'''

def run_main_interface(user_wants_to_run):
    '''Cycles through required input prompts and saves answers'''
    while user_wants_to_run:
        #Print product choices until viable input is entered, then save input
        desired_product = product_number_prompt_loop(0)
        #Print star review prompt until viable input is entered
        desired_star_review = star_review_prompt_loop(-1)
        #Print equality operator prompt until viable input is entered
        desired_equality_operation_star = equality_operator_prompt_loop('')
        #Print review number prompt until viable input is entered
        desired_review_number = number_reviews_prompt_loop(-1)
        #Print equality operator prompt until viable input is entered
        desired_equality_operation_review_count = equality_operator_prompt_loop('')
        #Print desired price prompt until viable input is entered
        desired_product_price = price_prompt_loop(-1)
        #Print equality operator prompt until viable input is entered
        desired_equality_operation_price = equality_operator_prompt_loop('')
        #Print exit prompt until viable input entered
        exit_input_from_user = exit_prompt_loop('')
        if exit_input_from_user == 'yes':
            continue
        else:
            print('Exiting Program')
            user_wants_to_run = False

def exit_prompt_loop(exit_input_from_user):
    '''Loops optional exit message until viable input entered, then returns input'''
    while not is_viable_exit_input(exit_input_from_user):
        exit_input_from_user = input(print_final_message())
    return exit_input_from_user
def price_prompt_loop(desired_product_price):
    '''Loops desired price message until viable input entered, then returns input'''
    while not is_viable_price(desired_product_price):
        desired_product_price = input(print_target_price_prompt())
    return desired_product_price

def number_reviews_prompt_loop(desired_review_number):
    '''Loops number of reviews message until viable input entered, then returns input'''
    while not is_viable_review_number(desired_review_number):
        desired_review_number = input(print_target_number_reviews_prompt())
    return desired_review_number
def equality_operator_prompt_loop(desired_equality_operation_star):
    '''Loops equality operator message until viable input entered, then returns input'''
    while not is_viable_equality_operator(desired_equality_operation_star):
        desired_equality_operation_star = input(print_equality_operator_prompt())
    return desired_equality_operation_star
def star_review_prompt_loop(desired_star_review):
    '''Loops star review message until viable input entered, then returns input'''
    while not is_viable_star_num(desired_star_review):
        desired_star_review = input(print_star_review_prompt())
    return desired_star_review
def product_number_prompt_loop(desired_product):
    '''Loops product listing prompt until viable input is entered, then return input'''
    while not is_viable_product_num(desired_product):
        desired_product = input(print_product_choice_prompt())
    return desired_product
def is_viable_exit_input(exit_input):
    '''Checks if user typed 'yes' or 'no' '''
    if exit_input == 'yes':
        return True
    elif exit_input == 'no':
        return True
    else:
        print('Please enter valid input')
        return False

def is_viable_price(potential_num):
    '''Checks if user input is positive number'''
    #NEED TO CHECK FOR DECIMALS OVER 2 PLACES OR ROUND TO TWO PLACES
    if not is_number(potential_num):
        print('Please enter positive number')
        return False
    else:
        if float(potential_num) < 0:
            print('Please enter positive number')
            return False
        else:
            return True

def is_viable_equality_operator(potential_operator):
    '''Checks if input is valid equality operator'''
    if potential_operator == '>':
        return True
    elif potential_operator == '<':
        return True
    elif potential_operator == '>=':
        return True
    elif potential_operator == '<=':
        return True
    elif potential_operator == '=':
        return True
    else:
        return False

def is_viable_review_number(potential_num):
    '''Checks if user input is positive integer'''
    if not is_int(potential_num):
        print('Please enter positive integer')
        return False
    else:
        if int(potential_num) < 0:
            print('Please enter positive integer')
            return False
        else:
            return True


def is_viable_product_num(potential_num):
    '''Checks if input is viable product number'''
    if not is_int(potential_num):
        print('Please input valid product number')
        return False
    else:
        if int(potential_num) == 0:
            print('Please input valid product number')
            return False
        elif 1 <= int(potential_num) <= 6:
            return True
        else:
            print('Please input valid product number')
            return False

def is_viable_star_num(potential_num):
    '''Checks if input is viable star review number'''
    if not is_number(potential_num):
        print('Please input valid star review rating')
        return False
    else:
        if float(potential_num) == -1:
            print('Please input valid star review rating')
            return False
        elif 0.0 <= float(potential_num) <= 5.0:
            return True
        else:
            print('Please input valid star review rating')
            return False

def is_number(potential_num):
    '''Checks if potential number is actually number'''
    try:
        float(potential_num)
        return True
    except TypeError:
        return False
    except ValueError:
        return False

def is_int(potential_int):
    '''Checks if number is integer'''
    try:
        int(potential_int)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def print_product_choice_prompt():
    '''Returns product choice prompt'''
    return 'Choose a product category(Enter Number): \n        1. Over Ear Headhpones\n        2. USB Microphones\n      ' \
           '  3. 1080p WebCams\n        4. Capture Cards\n        5. 8-channel Audio Mixers\n        6. Gaming Laptops\n'

def print_star_review_prompt():
    '''Returns star rating prompt'''
    return 'Enter a target star review (ex. \'3.7\'): \n'

def print_equality_operator_prompt():
    '''Returns equality operator prompt'''
    return 'Choose an equality operator (>, <, >=, <=, =): '

def print_target_number_reviews_prompt():
    '''Returns target number of reviews prompt'''
    return 'Enter a target number of reveiws (ex. \'1000\'): '

def print_target_price_prompt():
    '''Returns target price prompt'''
    return 'Enter a target price (ex. \'59.99\'): '

def print_final_message():
    '''Prints final prompt message'''
    return 'Would you like to excecute another query (yes/no): '