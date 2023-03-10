from helpers import save_file, get_all_employers, get_employee_by_email, delete_employee, save


while True:
    print("1.Add new Employee\n2.Get all Employees\n3.Get employee by email\n4. Update")
    flag = input("Choose menu item: ")
    if flag == "1":
        email = input("Employee email: ")
        first_name = input("Employee first name: ")
        last_name = input("Employee last name: ")
        phone = input("Employee phone number. Must contain 9 digits, starting with 0: ")
        save(email, first_name, last_name, phone)
    elif flag == "2":
        get_all_employers()
    elif flag == "3":
        email_to_find = input("Type email of employee which you want to find: ")
        get_employee_by_email(email_to_find)

    elif flag == "4":
        username = input("Type surname who want to update")
        delete_employee(username)
