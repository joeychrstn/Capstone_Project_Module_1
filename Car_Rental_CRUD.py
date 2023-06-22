# DATA DUMMY
car_data_dict = {
        1:{'Car Name' : 'Avanza', 'Manufacturer' : 'Toyota', 'Capacity' : 7, 'Rent Price' : 300000, 'Car ID' : ''}, 
        2:{'Car Name' : 'Mobilio', 'Manufacturer' : 'Honda', 'Capacity' : 7, 'Rent Price' : 350000, 'Car ID' : ''}, 
        3:{'Car Name' : '330i','Manufacturer' : 'BMW', 'Capacity' : 5, 'Rent Price' : 500000, 'Car ID' : ''}
    }

car_id_list = []
all_car_id = []

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# PRINT FUNCTION

def print_confirmation():
    print('''
Press Y to proceed.
Press N to Return.
    ''')

def print_table_header():
    print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<16} | {:<14}".format('INDEX', 'ID MOBIL', 'CAR NAME','MANUFACTURER', 'CAPACITY', 'RENT PRICE'))
    print ('-----------+-----------------+-----------------+-----------------+------------------+---------------')

def print_no_cars_found():
    print('\nNo cars found. Please add car data.')

def print_input_not_numerical():
    print('Input is not a number. Please insert a number.')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# OTHER FUNCTIONS

# convert string into integer
def convert_str_to_int(input_string):
    if input_string.isnumeric():
        string_converted = int(input_string)
        return string_converted

    else:
        return input_string

def check_start_number_value(start_number):

    if start_number < 10:
        output = '00'

    elif start_number >= 10:
        output = '0'
    
    elif start_number >= 100:
        output = None

    return output

# insert car id to list
def append_car_id():

    car_id_list.clear()
    for key_number in car_data_dict.keys():

        starting_number = 1

        car_id = car_data_dict[key_number]['Car Name'][0:2:1] + car_data_dict[key_number]['Manufacturer'][0:2:1]
        car_id = car_id.upper()

        seperator = check_start_number_value(starting_number)

        car_id_complete = (f'{car_id}{seperator}{starting_number}')

        while True:
            if (car_id_complete in all_car_id) and (car_id_complete in car_id_list):
                starting_number = starting_number + 1

                car_id_complete = (f'{car_id}{seperator}{starting_number}')
                car_data_dict[key_number]['Car ID'] = car_id_complete
                continue

            else:
                car_data_dict[key_number]['Car ID'] = car_id_complete

                car_id_list.append(car_id_complete)
                all_car_id.append(car_id_complete)

                break

# finding car properties
def car_properties(car_index):
    car_name = car_data_dict[car_index]['Car Name']
    car_manufacturer = car_data_dict[car_index]['Manufacturer']
    car_capacity = car_data_dict[car_index]['Capacity']
    car_rent_price = car_data_dict[car_index]['Rent Price']
    car_id_for_print = car_data_dict[car_index]['Car ID']

    car_properties_list = [car_name, car_manufacturer, car_capacity, car_rent_price, car_id_for_print]

    return car_properties_list

# print table for cars
def print_car_table():
    for key_number in car_data_dict.keys():
        car_properties_list = car_properties(key_number)

        print("{:<10} | {:<15} | {:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(key_number, car_properties_list[4], car_properties_list[0], car_properties_list[1], car_properties_list[2], '', car_properties_list[3]))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MAIN MENU

def main_menu():
    # print menu list
    print('''
CAR RENTAL ADMINISTRATOR PROGRAM
----------------------------------------------------------------------------------------------------
1. Show All Cars
2. Add Car Data
3. Edit Car Data
4. Delete Car Data
5. Exit Program
    ''')
    append_car_id()

    # input for main menu
    main_menu_input = input('Insert number from the menu to proceed: ').strip()

    # checking if input given is a numerical value or not
    if main_menu_input.isnumeric():
        # convert string input to integer
        main_menu_input = convert_str_to_int(main_menu_input)
        
        if main_menu_input == 1:
            show_all_cars_menu()

        elif main_menu_input == 2:
            add_car_menu()

        elif main_menu_input == 3:
            edit_car_menu()

        elif main_menu_input == 4:
            delete_car_menu()

        elif main_menu_input == 5:
            exit_menu()

        else:
            print('Input not in range. Please input numbers ranging from 1-5')
            main_menu()

    else:
        print_input_not_numerical()
        main_menu()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SHOW ALL CARS MENU

def show_all_cars_menu():
    print('''
SHOW ALL CARS MENU
----------------------------------------------------------------------------------------------------
1. Show All Data
2. Search Data by ID
3. Return to Main Menu
    ''')

    show_all_cars_input = input('Insert number from the menu to proceed: ').strip()

    if show_all_cars_input.isnumeric():
        # convert string input to integer
        show_all_cars_input = convert_str_to_int(show_all_cars_input)

        if show_all_cars_input == 1:
            show_all_data()

        elif show_all_cars_input == 2:
            search_data_by_id()

        elif show_all_cars_input == 3:
            main_menu()

        else:
            print('Input not in range. Please input numbers ranging from 1-5')
            show_all_cars_menu()
    
    else:
        print_input_not_numerical()
        # return to show all cars menu
        show_all_cars_menu()

# show all data menu (menu 1)
def show_all_data():
    print('''CARS AVAILABLE FOR RENTAL
----------------------------------------------------------------------------------------------------''')
    if len(car_data_dict) <= 0:
        print_no_cars_found()
        show_all_cars_menu()

    else:
        append_car_id()

        # print table
        print_table_header()
        print_car_table()

        # return to show all cars menu
        show_all_cars_menu()

# search data by ID (menu 2)
def search_data_by_id():
    car_id_search_input = input('Insert car ID: ').strip()
    car_id_search_input = car_id_search_input.upper()

    counter = 0
    for id in car_id_list:
        if len(car_data_dict) <= 0:
            print_no_cars_found()
            show_all_cars_menu()

        else:
            if car_id_search_input == id:
                index = car_id_list.index(car_id_search_input)
                index = index + 1

                print('Car data found.')
                print_table_header()

                search_result = car_properties(index)
                print("{:<10} | {:<15} | {:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(index, search_result[4], search_result[0], search_result[1], search_result[2], '', search_result[3]))

                show_all_cars_menu()

            else:
                print('Car ID not found. Please Insert Valid car ID.')
                search_data_by_id()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ADD CAR DATA MENU

def add_car_menu():
    print('''
ADD NEW CARS MENU
----------------------------------------------------------------------------------------------------
1. Insert New Car Data
2. Return to Main Menu
    ''')

    # input for add data menu
    add_car_menu_input = input('Insert number from the menu to proceed: ').strip()

    # checking if input given is a numerical value or not
    if add_car_menu_input.isnumeric():

        # convert string input to integer
        add_car_menu_input = convert_str_to_int(add_car_menu_input)
        
        if add_car_menu_input == 1:
            insert_new_car()

        elif add_car_menu_input == 2:
            main_menu()

        else:
            print('Input not in range. Please input numbers ranging from 1-2')
            add_car_menu()

    else:
        print_input_not_numerical()
        add_car_menu()

def insert_new_car():
    car_name = input('Insert new car name: ').strip()
    car_name = car_name.capitalize()

    car_manufacturer = input('Insert new car manufacturer: ').strip()
    car_manufacturer = car_manufacturer.capitalize()

    while True:
        car_capacity = input('Insert new car capacity: ').strip()

        if car_capacity.isnumeric():
            car_capacity = convert_str_to_int(car_capacity)

            if car_capacity <= 1 or car_capacity >= 8:
                print('The capacity does meets the requirement. Please insert a number ranging from 2-7.')
                continue

            else:
                break

        else:
            print_input_not_numerical()
            continue

    while True:
        rental_price = input('Input new car rent price: ').strip()
        if rental_price.isnumeric():
            rental_price = convert_str_to_int(rental_price)

            if rental_price <= 10000:
                print('Rental price to low. Please input rental price above 10000.')
                continue
            
            elif rental_price >= 100000000:
                print('Rental price to high. Please input rental price below 100000000.')
                continue

            else:
                break

        else:
            print_input_not_numerical()
            continue

    print()
    print('NEW CAR DATA')
    print("{:<15} | {:<15} | {:<16} | {:<14}".format('CAR NAME', 'MANUFACTURER', 'CAPACITY', 'RENT PRICE'))
    print ('----------------+-----------------+------------------+---------------')
    print("{:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(car_name, car_manufacturer, car_capacity, '', rental_price))

    print('\nIs the new data correct?')
    print_confirmation()

    index_list = list(car_data_dict.keys())

    while True:
        confirmation_input = input('Do you wish to proceed? ').strip()
        confirmation_input = confirmation_input.upper()

        if confirmation_input.isalpha():
            if confirmation_input == 'Y':
                temp_dict = {
                    max(index_list) + 1 :{'Car Name' : car_name, 'Manufacturer' : car_manufacturer, 'Capacity' : car_capacity, 'Rent Price' : rental_price, 'Car ID' : ''}
                }

                # inserting new car data to main dictionary
                car_data_dict.update(temp_dict)

                print('New car data added succesfully.')
                add_car_menu()

            elif confirmation_input == 'N':
                print('Failed to add new car data.')
                add_car_menu()

            else:
                print('Input not found. Please input Y/N.')
                continue

        else:
            print('Input is not a letter. Please insert a letter.')
            continue

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EDIT CAR DATA

def edit_car_menu():
    print('''
EDIT CAR DATA MENU
----------------------------------------------------------------------------------------------------
1. Edit Car Data
2. Return to Main Menu
    ''')
    append_car_id()

    edit_car_menu_input = input('Insert number from the menu to proceed: ').strip()

    # checking if input given is a numerical value or not
    if edit_car_menu_input.isnumeric():

        # convert string input to integer
        edit_car_menu_input = convert_str_to_int(edit_car_menu_input)
        
        if edit_car_menu_input == 1:
            edit_car()

        elif edit_car_menu_input == 2:
            main_menu()

        else:
            print('Input not in range. Please input numbers ranging from 1-2')
            edit_car_menu()

    else:
        print_input_not_numerical()
        edit_car_menu()

def edit_car():

    if len(car_data_dict) <= 0:
        print_no_cars_found()
        edit_car_menu()

    else:
        print_table_header()
        print_car_table()
        print()
        print('Which car data needs to be edited?')

        car_id_to_edit = input('Insert car ID to edit: ').strip()
        car_id_to_edit = car_id_to_edit.upper()
        counter = 0

        for car_id in car_id_list:
            if car_id_to_edit == car_id:

                car_index = car_id_list.index(car_id_to_edit)
                car_index = car_index + 1

                print_table_header()
                car_to_edit = car_properties(car_index)
                print("{:<10} | {:<15} | {:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(car_index, car_to_edit[4], car_to_edit[0], car_to_edit[1], car_to_edit[2], '', car_to_edit[3]))

                while True:
                    columns_to_edit_input = input("Column that needs to be edited: ").strip()
                    columns_to_edit_input = columns_to_edit_input.lower()

                    # check if columns_to_edit_input is numerical or not
                    if columns_to_edit_input.isnumeric():
                        print('Input is not alphabetical. Please insert alphabetical characters.')
                        continue

                    else:
                        if columns_to_edit_input == 'car name':
                            edited_car_name = input('Insert new car name: ').strip()
                            edited_car_name = edited_car_name.capitalize()

                            print()
                            print('Is the edited car name correct?')
                            print_confirmation()

                            while True:
                                confirmation_input = input('Do you wish to proceed? ').strip()
                                confirmation_input = confirmation_input.upper()

                                if confirmation_input.isalpha():

                                    if confirmation_input == 'Y': 
                                        car_data_dict[car_index]['Car Name'] = edited_car_name
                                        print(f'Car name for {car_id_to_edit} changed succesfully.')
                                        edit_car_menu()

                                    elif confirmation_input == 'N':
                                        print('Failed to edit car data.')
                                        edit_car_menu()

                                    else:
                                        print('Input not found. Please input Y/N.')
                                        continue

                                else:
                                    print('Input is not a letter. Please insert a letter.')
                                    continue

                        elif columns_to_edit_input == 'manufacturer':
                            edited_car_manufacturer = input('Insert new car manufacturer: ').strip()
                            edited_car_manufacturer = edited_car_manufacturer.capitalize()

                            print()
                            print('Is the edited car manufacturer correct?')
                            print_confirmation()

                            while True:

                                confirmation_input = input('Do you wish to proceed? ').strip()
                                confirmation_input = confirmation_input.upper()

                                if confirmation_input.isalpha():
                                    if confirmation_input == 'Y': 
                                        car_data_dict[car_index]['Manufacturer'] = edited_car_manufacturer
                                        print(f'Car manufacturer for {car_id_to_edit} changed succesfully.')
                                        edit_car_menu()

                                    elif confirmation_input == 'N':
                                        print('Failed to edit car data.')
                                        edit_car_menu()

                                    else:
                                        print('Input not found. Please input Y/N.')
                                        continue

                                else:
                                    print('Input is not a letter. Please insert a letter.')
                                    continue

                        elif columns_to_edit_input == 'capacity':
                            edited_car_capacity = input('Insert new car capacity: ').strip()
                            edited_car_capacity = edited_car_capacity.capitalize()

                            while True:
                                if edited_car_capacity.isnumeric():
                                    edited_car_capacity = convert_str_to_int(edited_car_capacity)

                                    if edited_car_capacity <= 1 or edited_car_capacity >= 8:
                                        print('The capacity does meets the requirement. Please insert a number ranging from 2-7.')
                                        continue

                                    else: 
                                        print()
                                        print('Is the edited car capacity correct?')
                                        print_confirmation()

                                        while True:

                                            confirmation_input = input('Do you wish to proceed? ').strip()
                                            confirmation_input = confirmation_input.upper()

                                            if confirmation_input.isalpha():

                                                if confirmation_input == 'Y': 
                                                    car_data_dict[car_index]['Capacity'] = edited_car_capacity
                                                    print(f'Car name for {car_id_to_edit} changed succesfully.')
                                                    edit_car_menu()

                                                elif confirmation_input == 'N':
                                                    print('Failed to edit car data.')
                                                    edit_car_menu()

                                                else:
                                                    print('Input not found. Please input Y/N.')
                                                    continue

                                            else:
                                                print('Input is not a letter. Please insert a letter.')
                                                continue
                                        
                                else:
                                    print_input_not_numerical()
                                    continue

                        elif columns_to_edit_input == 'rent price':
                            edited_car_price = input('Insert new car price: ').strip()
                            edited_car_price = edited_car_price.capitalize()

                            while True:
                                if edited_car_price.isnumeric():
                                    edited_car_price = convert_str_to_int(edited_car_price)

                                    if edited_car_price <= 10000:
                                        print('Rental price to low. Please input rental price above 10000.')
                                        continue

                                    elif edited_car_price >= 100000000:
                                        print('Rental price to high. Please input rental price below 100000000.')
                                        continue

                                    else: 
                                        print()
                                        print('Is the edited car price correct?')
                                        print_confirmation()

                                        while True:

                                            confirmation_input = input('Do you wish to proceed? ').strip()
                                            confirmation_input = confirmation_input.upper()

                                            if confirmation_input.isalpha():

                                                if confirmation_input == 'Y': 
                                                    car_data_dict[car_index]['Rent Price'] = edited_car_capacity
                                                    print(f'Rent price for {car_id_to_edit} changed succesfully.')
                                                    edit_car_menu()

                                                elif confirmation_input == 'N':
                                                    print('Failed to edit car data.')
                                                    edit_car_menu()

                                                else:
                                                    print('Input not found. Please input Y/N.')
                                                    continue

                                            else:
                                                print('Input is not a letter. Please insert a letter.')
                                                continue

                                else:
                                    print_input_not_numerical()
                                    continue
            counter = counter + 1

            if counter == len(car_data_dict):
                print('Car ID not found. Please insert a valid ID.')
                edit_car()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DELETE CAR DATA

def delete_car_menu():
    print('''
DELETE CAR DATA MENU
----------------------------------------------------------------------------------------------------
1. Delete Car Data
2. Return to Main Menu
    ''')

    delete_car_menu_input = input('Insert number from the menu to proceed: ').strip()

    # checking if input given is a numerical value or not
    if delete_car_menu_input.isnumeric():

        # convert string input to integer
        delete_car_menu_input = convert_str_to_int(delete_car_menu_input)
        
        if delete_car_menu_input == 1:
            delete_car()

        elif delete_car_menu_input == 2:
            main_menu()

        else:
            print('Input not in range. Please input numbers ranging from 1-2')
            delete_car_menu()

    else:
        print_input_not_numerical()
        delete_car_menu()

def delete_car():
    if len(car_data_dict) <= 0:
        print_no_cars_found()
        delete_car_menu()

    else:
        print_table_header()
        print_car_table()
        print()
        print('Which car data needs to be delted?')

        car_id_to_delete = input('Insert car ID to delete: ').strip()
        car_id_to_delete = car_id_to_delete.upper()
        counter = 0

        for car_index in car_data_dict.keys():

            car_index = car_index + 1
            car_id_remove = car_data_dict[car_index]['Car ID']

            if car_id_to_delete == car_id_remove:

                print_table_header()
                car_to_delete = car_properties(car_index)
                print("{:<10} | {:<15} | {:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(car_index, car_to_delete[4], car_to_delete[0], car_to_delete[1], car_to_delete[2], '', car_to_delete[3]))

                print(f'Car data with ID {car_id_to_delete} will be deleted.')

                print_confirmation()

                while True:
                    confirmation_input = input('Do you wish to proceed? ').strip()
                    confirmation_input = confirmation_input.upper()

                    if confirmation_input.isalpha():
                        if confirmation_input == 'Y':

                            # deleting data from dictionary
                            del car_data_dict[car_index]

                            print(f'Car data with ID {car_id_to_delete} has been deleted successfully.')
                            delete_car_menu()

                        elif confirmation_input == 'N':
                            print('Failed to delete car data.')
                            delete_car_menu()

                        else:
                            print('Input not found. Please input Y/N.')
                            continue

                    else:
                        print('Input is not a letter. Please insert a letter.')
                        continue

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EXIT PROGRAM

def exit_menu():

    print('Are you sure you want to exit the program?')
    print_confirmation()

    while True:
        confirmation_input = input('Do you wish to proceed? ').strip()
        confirmation_input = confirmation_input.upper()

        if confirmation_input.isalpha():
            if confirmation_input == 'Y':
                print('Goodbye')
                exit()

            elif confirmation_input == 'N':
                main_menu()
            else:
                print('Input not found. Please input Y/N.')
                continue

        else:
            print('Input is not a letter. Please insert a letter.')
            continue

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

main_menu()