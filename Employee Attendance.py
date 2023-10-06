import sys
import mysql.connector

# Connect to the database
db = mysql.connector.connect(host='127.0.0.1', database='employee', user='root', password='%TGBnhy6')

# Get all employees from the database
# sql = 'SELECT * FROM employee list'
cursor = db.cursor()


n = 0
emp=[]
class Employee:
    def __init__(self):
        self.full_name = ""
        self.ID_NO = ""
        self.password = ""

def Admin():
    global n
    global connection
    date = input("Enter today's date: ")
    # with open("qwertyui.txt", "w") as outputfile:
    #     outputfile.write("\nAttendance of employee\n")
    #     outputfile.write("Name" + "{:<25}".format("ID NO") + "{:<20}".format("password") + "{:<20}".format(date) + "\n")
    for i in range(n):
            print("Enter employee {} Full name: ".format(i + 1), end="")
            emp[n].full_name = input()
            print("Enter employee {} password: ".format(i + 1), end="")
            emp[n].password = input()
            print("Enter  {} Date: ".format(i + 1), end="")
            emp[n].ID_NO = input()
            print("Enter employee {} ID NO: ".format(i + 1), end="")
            emp[n].ID_NO = input()

            
            result=connection.cursor()
            query = "INSERT INTO books (name, password, price) values (%s,%s)"
            VALUES =('$title', '$author', '$price')
            result.execute(query,VALUES)
            outputfile.write(emp[n].full_name + "{:<27}".format(emp[n].ID_NO) + "{:<25}".format(emp[n].password) + "\n")

            n += 1
            emp[n].empty()
            n += 1

def empty():
    for i in range(10):
        for j in range(10):
            pass

def Employee():
    name = input("Enter your full name: ")
    for b in range(n ):
        if emp[b].full_name == name:
            break
    ## else:
       ## print("Your name is not registered")
         ## return

    id_no = input("Enter your ID NO: ")
    for b in range(n):
        if emp[b].ID_NO == id_no:
            break
    ## else:
        ##print("Your ID NO is not registered")
        ##return

    password = input("Enter your password: ")
    for b in range(n):
        if emp[b].password == password:
            break
    ##else:
       ## print("Incorrect password")
        ##return

    present = input("\nEnter p for present: ")
   

def main():
    global n
    while True:
        print("\n   ************** Employee Attendance *************")
        print("{:<34}".format("1. Administration"))
        print("{:<30}".format("2. Employee"))
        print("{:<25}".format("3. Exit"))
        choice = int(input("Enter your choice: "))

        if choice == 1:
            Admin()
        elif choice == 2:
            Employee()
        elif choice == 3:
            quit()

if __name__ == "__main__":
   main()
   emp = [Employee() for _ in range(10)]
    