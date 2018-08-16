#Name: Chris Demundo
#Umich ID: cdemundo

# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

db_name = './Northwind_small.sqlite'

def main():

	correct_use = "Correct usage: part2.py customers OR part2py employees OR part2.py orders cust=CustID OR part2.py orders emp=EmpID"
	
	conn = MakeConnection()
	c = conn.cursor()

	if len(sys.argv) < 2:
		print(correct_use)
	else:
		if(sys.argv[1] == 'customers'):
			rows = GetCustomers(c)
			print("ID       Customer Name")
			for row in rows:
				print("{ID}     {CustName}".format(ID=row[0], CustName=row[1]))
		elif(sys.argv[1] == 'employees'):
			rows = GetEmployees(c)
			print("ID    Employee Name")
			for row in rows:
				print('{ID}     {FirstName} {LastName}'.format(ID=row[0], FirstName = row[1], LastName = row[2]))
		elif(sys.argv[1] == 'orders'):
			if len(sys.argv) > 2:
				if "cust" in sys.argv[2]:
					rows = GetOrderDatesByCust(c, sys.argv[2].split("=")[1])
					print("Order dates")
					for row in rows:
						print(row[0])
				elif "emp" in sys.argv[2]:
					rows = GetOrderDatesByEmp(c, sys.argv[2].split("=")[1])
					print("Order Dates")
					for row in rows: 
						print(row[0])
				else:
					print(correct_use)
			else:
				print(correct_use)
		else:
			print(correct_use)


def MakeConnection():
	try:
		conn = sqlite3.connect(db_name)
		return conn
	except:
		print("DB Connection not working")

	return none

def GetCustomers(c):
	c.execute("SELECT ID, CompanyName FROM Customer")
	return c.fetchall()

def GetEmployees(c):
	c.execute("SELECT ID, FirstName, Lastname FROM Employee")
	return c.fetchall()

def GetOrderDatesByCust(c, customerID):
	c.execute("SELECT OrderDate FROM `Order` WHERE CustomerID = '{cid}'".format(cid=customerID))
	return c.fetchall()

def GetOrderDatesByEmp(c, empLastName):
	select_statement = "SELECT OrderDate FROM `Order` INNER JOIN Employee on Employee.Id = `Order`.EmployeeId WHERE Employee.LastName = '{eLN}'".format(eLN=empLastName)

	c.execute(select_statement)
	return c.fetchall()


if __name__ == "__main__":
	main()