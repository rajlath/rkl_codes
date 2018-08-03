def calculate_pay():
    '''
    calculate pay due to an employee
    ins : hourly wage, total regular hours, and total overtime hours
    out : pay due to employee
    '''
    hourly_wage = int(input("Enter hourly wage :"))
    total_hours = int(input("Enter total regular hours done by employee :"))
    total_overtime = int(input("Enter total overtime hours done by employee :"))

    regular_pay  = hourly_wage * total_hours
    overtime_pay = total_overtime * 1.5 * hourly_wage
    pay = regular_pay + overtime_pay

    print("Regular pay :{}".format(regular_pay))
    print("Overtime pay : {}".format(overtime_pay))
    print("Total pay due to employee : {}".format(pay))




if __name__ == "__main__"    :
    calculate_pay()