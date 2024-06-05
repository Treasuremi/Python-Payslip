class Staff:
    def __init__(self, name, salary, deductions):
        self.name = name
        self.salary = salary
        self.deductions = deductions

    def calculate_net_salary(self):
        return self.salary - self.deductions

# Define a function to generate payslip
def generate_payslip(staff):
    print("Payslip for:", staff.name)
    print("Salary:", staff.salary)
    print("Deductions:", staff.deductions)
    print("Net Salary:", staff.calculate_net_salary())

# Define a function to generate payroll
def generate_payroll(staffs):
    with open("payroll.txt", "a") as file:
        for staff in staffs:
            filename = staff.name
            f = open('payslip/'+filename+'.txt', 'w')
            file.write("Payslip for: " + staff.name + "\n")
            file.write("Salary: " + str(staff.salary) + "\n")
            file.write("Deductions: " + str(staff.deductions) + "\n")
            file.write("Net Salary: " + str(staff.calculate_net_salary()) + "\n\n")
            f.write("Payslip for: " + staff.name + "\n")
            f.write("Salary: " + str(staff.salary) + "\n")
            f.write("Deductions: " + str(staff.deductions) + "\n")
            f.write("Net Salary: " + str(staff.calculate_net_salary()) + "\n\n")


def dpayslip():
    with open("payroll.txt", "r") as file:
        out = file.read()
        print(out)

def dpayment(name):
    with open("payslip/"+name+".txt", "r") as file:
        out = file.read()
        print(out)



# Accept staff details from users
def accept_staff_details():
    staffs = []
    num_staff = int(input("Enter number of staff: "))
    for i in range(num_staff):
        name = input("Enter name: ")
        salary = float(input("Enter salary: "))
        deductions = float(input("Enter deductions: "))
        staff = Staff(name, salary, deductions)
        staffs.append(staff)
    return staffs

# Main program
def main():
    while True:
        print("Payroll System")
        print("1 = Add Staff\n2 = Display Staff Payslip\n3 = Display All Payroll\n4 = Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            staffs = accept_staff_details()
            generate_payroll(staffs)
            print("Payroll successfully generated!")
        elif choice == "2":
            print()
            dpayslip()
        elif choice == "3":
            name = input("Enter Staff's Name: ")
            dpayment(name)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")



if __name__ == "__main__":
    main()
