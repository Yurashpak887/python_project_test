from .system_helpers import save_list_to_file, get_file_data, save_file
from .decorators_helpers import is_number_valid, is_email_valid

@is_number_valid
def save(email, first_name, last_name, phone):
    new_employee = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    }
    save_file(new_employee)


def get_all_employers():
    employees = get_file_data()
    for employee in employees:
        print(employee["email"])
        print(employee["first_name"])
        print(employee["last_name"])
        print(employee["phone"])


def get_employee_by_email(email):
    employees = get_file_data()
    for employee in employees:
        if employee["email"] == email:
            print(employee["email"])
            print(employee["first_name"])
            print(employee["last_name"])
            print(employee["phone"])

def delete_employee(username):
    employees = get_file_data()
    for i in range(len(employees)):
        if username == employees[i]["last_name"]:
            del employees[i]
            save_list_to_file(employees, "database/employees.json")
            email = input("Employee email: ")
            first_name = input("Employee first name: ")
            last_name = input("Employee last name: ")
            phone = input("Employee phone number. Must contain 9 digits, starting with 0: ")
            save(email, first_name,last_name,phone)
            break

