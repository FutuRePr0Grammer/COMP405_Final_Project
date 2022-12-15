'''Module containing functions related to user interface'''

def run_main_interface():
    '''Cycles through required input prompts and saves answers'''
    user_wants_to_run = True
    while user_wants_to_run:
        #Reset all values at begining of input cycle
        desired_product = 0
        desired_star_review = 0
        desired_review_number = -1
        desired_product_price = -1
        desired_equality_operation_star = ''
        desired_equality_operation_review_count = ''
        desired_equality_operation_price = ''
        exit_input_from_user = ''
        #Print product listing prompt until viable input is entered
        while not is_viable_product_num(desired_product):
            desired_product = input(print_product_choice_prompt())
        #Print star review prompt until viable input is entered
        while not is_viable_star_num(desired_star_review):
            desired_star_review = input(print_star_review_prompt())
        #Print equality operator prompt until viable input is entered
        while not is_viable_equality_operator(desired_equality_operation_star):
            desired_equality_operation_star = input(print_equality_operator_prompt())
        #Print review number prompt until viable input is entered
        while not is_viable_review_number(desired_review_number):
            desired_review_number = input(print_target_number_reviews_prompt())
        #Print equality operator prompt until viable input is entered
        while not is_viable_equality_operator(desired_equality_operation_review_count):
            desired_equality_operation_review_count = input(print_equality_operator_prompt())
        #Print desired price prompt until viable input is entered
        while not is_viable_price(desired_product_price):
            desired_product_price = input(print_target_price_prompt())
        while not is_viable_equality_operator(desired_equality_operation_price):
            desired_equality_operation_price = input(print_equality_operator_prompt())
        while not is_viable_exit_input(exit_input_from_user):
            exit_input_from_user = input(print_final_message())
        if exit_input_from_user == 'yes':
            continue
        else:
            print('Exiting Program')
            user_wants_to_run = False


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
        if float(potential_num) == 0:
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