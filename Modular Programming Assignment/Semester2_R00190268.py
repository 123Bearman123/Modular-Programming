# DYLAN BEARMAN
# R00190268

from reading_from_user import read_nonempty_alphabetical_string
from reading_from_user import read_nonnegative_integer
from reading_from_user import read_between_and3
# I imported these for validation, the first one to make sure what they enter is a sting/letter. The second
# one is to read a positive number and the third is to read a positive number between 1 and 3


def login():
    print('Module Record System')
    print(22 * '-')
    name_input = read_nonempty_alphabetical_string('Name:')
    password_input = read_nonnegative_integer('Password:')
    confidential = open("login_details.txt", "r")
    lines = confidential.readlines()
    name_file = str(lines[0]).rstrip()
    password_file = int((lines[1]))
    confidential.close()
    if name_input == name_file and password_input == password_file:
        login_status = str('True')
    else:
        login_status = str('False')
    return login_status, name_input
# This functions compares the users name and password to that within the file and returns weather they are equal or not


def load_modules():
    module_code_list = []
    modules = open("modules.txt", "r")
    for module_info in modules:
        module_info = module_info.rstrip()
        line_info = module_info.split(',')
        module_code_list.append(line_info[0])
    modules.close()
    print('Module Record System - Choose a Module')
    print(50 * '-')
    x = 1
    for i in module_code_list:
        print(f'{x}.{i}')
        x += 1
    while True:
        choice = read_nonnegative_integer('>')
        if choice > x - 1:
            print(f'Please choose a number between 1 and {x - 1}')
        else:
            filename = module_code_list[choice - 1] + '.txt'
            m_code = module_code_list[choice - 1]
            return filename, m_code
# This function adds the module code to a list, prints this to a user and gets them to choose what module they want
# and returns this under filename and also returns the module code


def get_class_attendance(filename):
    name_list = []
    present_list = []
    absent_list = []
    excused_list = []
    m1_file = open(filename, 'r')
    for attendance_data in m1_file:
        attendance_data = attendance_data.rstrip()
        line_info = attendance_data.split(',')
        name_list.append(line_info[0])
        present_list.append(int((line_info[1])))
        absent_list.append(int((line_info[2])))
        excused_list.append(int((line_info[3])))
    m1_file.close()

    return name_list, present_list, absent_list, excused_list
# This receives the name of the file the user choose and opens this file and adds the content to four lists, name,
# present, absent, excused


def take_class_attendance(name_list, present_list, absent_list, excused_list, filename, m_code):
    print(f'Module Record System(Attendance) {m_code}')
    print(50 * '-')
    line_count = open(filename, 'r')
    all_line_in_the_file = line_count.readlines()
    all_number = len(all_line_in_the_file)
    print(f'There are {all_number} enrolled')
    line_count.close()

    x = 1
    for i in name_list:
        print(f'Student #{x}: {i}')
        print('1. Present')
        print('2. Absent')
        print('3. Excused')
        option3 = read_between_and3('>')
        if option3 == 1:
            present_list[x - 1] = int(present_list[x - 1]) + 1
            x += 1
        if option3 == 2:
            absent_list[x - 1] = int(absent_list[x - 1]) + 1
            x += 1
        if option3 == 3:
            excused_list[x - 1] = int(excused_list[x - 1]) + 1
            x += 1
    print(m_code, 'updated with the latest attendance records')
    print('')
    return name_list, present_list, absent_list, excused_list
# This function receives the four lists along with the filename and the module code and it asks the user what
# students are present absent and excused and returns the new lists


def update_class_data(name_list_updated, present_list_updated, absent_list_updated, excused_list_updated, filename):
    change = open(filename, 'w')
    for i in range(len(name_list_updated)):
        print(f'{name_list_updated[i]},{present_list_updated[i]},{absent_list_updated[i]},{excused_list_updated[i]}',
              file=change)
    change.close()
# This function receives the newly updated lists and rewrites this information to a file


def calculate_attendance_rate(name_list, present_list, absent_list, excused_list):
    total_days = int(present_list[0]) + int(absent_list[0]) + int(excused_list[0])

    p = 0
    non_attender = []
    for i in present_list:
        p += 1
        if i == 0:
            non_attender.append(name_list[p - 1])
        else:
            continue

    low_attender = []
    z = 0
    for i in present_list:
        z += 1
        if ((int(i) / total_days) * 100) < 70:
            low_attender.append(name_list[z - 1])
        else:
            continue

    high_attender = []
    high_attender_amount = []
    top_attender = max(present_list)
    k = 0
    for i in present_list:
        k += 1
        if i == top_attender:
            high_attender.append(name_list[k - 1])
            high_attender_amount.append(i)
        else:
            continue

    present_list_int = len(present_list)
    x = 0
    for i in range(len(present_list)):
        x += int(present_list[i])
    average_attendance = x / present_list_int

    return low_attender, non_attender, high_attender, high_attender_amount, average_attendance, total_days
# This function calculates all the stats needed for option 2 in the menu


def display_stats(m_code, filename, total_days, average_attendance, low_attender, non_attender, high_attender,
                  high_attender_amount):
    from datetime import date
    today = date.today()
    stats_file = open(f'{m_code}_{today}.txt', 'w')

    print(f'Module:', m_code)
    print(f'Module:', m_code, file=stats_file)
    line_count = open(filename, 'r')
    all_line_in_the_file = line_count.readlines()
    all_number = len(all_line_in_the_file)
    print(f'Number of students:{all_number}')
    print(f'Number of students:{all_number}', file=stats_file)
    line_count.close()
    print(f'Number of Classes:{total_days}')
    print(f'Number of Classes:{total_days}', file=stats_file)
    print(f'Average Attendance: {average_attendance:.2f} days')
    print(f'Average Attendance: {average_attendance:.2f} days', file=stats_file)
    print('Low Attender(s): under 70.0%')
    print('Low Attender(s): under 70.0%', file=stats_file)
    if not low_attender:
        print((5 * ' '), "Everyones' attendance is above 70%, also includes non attenders")
        print((5 * ' '), "Everyones' attendance is above 70%, also includes non attenders", file=stats_file)
    else:
        for i in low_attender:
            print((5 * ' '), i)
            print((5 * ' '), i, file=stats_file)
    print('Non Attender(s):')
    print('Non Attender(s):', file=stats_file)
    if not non_attender:
        print((5 * ' '), 'Everyone has attended at least one class')
        print((5 * ' '), 'Everyone has attended at least one class', file=stats_file)
    else:
        for i in non_attender:
            print((5 * ' '), i)
            print((5 * ' '), i, file=stats_file)
    print('Best Attender(s):')
    print('Best Attender(s):', file=stats_file)
    if not high_attender:
        print((5 * ' '), 'Everyones attendance is below 70%')
        print((5 * ' '), 'Everyones attendance is below 70%', file=stats_file)
    else:
        for (i, x) in zip(high_attender, high_attender_amount):
            print((5 * ' '), i)
            print((5 * ' '), i, file=stats_file)
            print(f"{6 * ' '}Attended {x}/{total_days} days")
            print(f"{6 * ' '}Attended {x}/{total_days} days", file=stats_file)
    print('')
    stats_file.close()
# This function receives all the stats and displays it presentable to the screen and to a file


def main():
    login_status, name = login()
    if login_status == str('True'):
        print('')
        print(f'Welcome {name}')
        while True:
            print('Module Record System - Options')
            print(30 * '-')
            print('1.Record Attendance')
            print('2.General Statics')
            print('3.Exit')
            option7 = read_between_and3('>')
            print('')
            if option7 == 1:
                filename, m_code = load_modules()
                name_list, present_list, absent_list, excused_list = get_class_attendance(filename)
                name_list_updated, present_list_updated, absent_list_updated, excused_list_updated = \
                    take_class_attendance(name_list, present_list, absent_list, excused_list, filename, m_code)
                update_class_data(name_list_updated, present_list_updated, absent_list_updated, excused_list_updated,
                                  filename)

            if option7 == 2:
                filename, m_code = load_modules()
                name_list, present_list, absent_list, excused_list = get_class_attendance(filename)
                low_attender, non_attender, high_attender, high_attender_amount, average_attendance, total_days = \
                    calculate_attendance_rate(name_list, present_list, absent_list, excused_list)
                display_stats(m_code, filename, total_days, average_attendance, low_attender, non_attender,
                              high_attender, high_attender_amount)

            if option7 == 3:
                break

    else:
        print('')
        print('Module Record System: Login Failed')
        print('ONE MORE ATTEMPT')
        print('')
        login()
# this function puts all the functions together along with a main menu


main()
