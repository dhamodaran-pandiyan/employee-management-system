while True:

  choice = input("\nEnter:\n1: Enter Details\n2: Display Details\n3: Exit\n")

  if choice == '1':
    f = open('./employee.txt','a')

    name = input("Enter employee name:")
    name = name.replace(" ", "_")
    while True:
        if name.isdigit():
         name = input("Enter employee name with string format:")
        else:
         f.write(name +' ')
         break
     
    designation= input("Enter employee designation:")
    designation = designation.replace(" ","_")
    while True:
        if designation.isdigit():
         designation= input("Enter employee designation with string format:")
        else:
         f.write(designation+' ')
         break

    hours_worked = input("Enter the number of hours employee worked in a week:")
    while True:
        if hours_worked.isdigit():
            f.write(hours_worked + ' ')
            break
        else:
            hours_worked = input("Enter the number of hours employee worked in a week in proper format(int):")

    pay_rate= input("Enter employee hourly pay rate:")
    while True:
        if pay_rate.isdigit():
            f.write(pay_rate + ' ')
            break
        else:
            pay_rate = input("Enter employee hourly pay rate in proper format(int):")

    f.write("\n")
    f.close()

  elif choice == '2':
    f = open('employee.txt')
    
    ip = input("\nChoose:\n1: Choose employee by Name\n2: All employees\n")

    if ip == '1':
      entered_name = input("\nEnter the Name of the employee: ")
      entered_name = entered_name.replace(" ","_")
      flag = 1
      for line in f:
        li = line.split()
        if li[0].lower()==entered_name.lower():
          flag = 0
          print("--------------------------------")
          print("Payroll Statement\n\n")
          print("Employee Name:{}\nEmployee Designation:{}\nTotal hours worked:{}\nPay Rate:{}\n".format(li[0].replace("_"," "),li[1].replace("_"," "),li[2],li[3]))
          print("--------------------------------")
      if flag == 1:
        print("No Match! Enter correct name or add employee details")  
    elif ip =='2':
      print("--------------------------------")
      print("Payroll Statement\n\n")
      for line in f:
        li = line.split()
        print("Employee Name:{}\nEmployee Designation:{}\nTotal hours worked:{}\nPay Rate:{}\n".format(li[0].replace("_"," "),li[1].replace("_"," "),li[2],li[3]))
      print("--------------------------------")
    f.close()
    
  elif choice == '3':
    print("Application exited sucessfully...")
    break

  else:
    print("Invalid Choice\n")