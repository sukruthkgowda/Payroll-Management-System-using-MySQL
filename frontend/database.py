import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sukruth_payroll_management_system"
)
c = mydb.cursor()



def view_all_data(table):
    c.execute('SELECT * FROM {}'.format(table))
    data = c.fetchall()
    # print(data)
    return data

def getcolumns(table):
    c.execute('desc {}'.format(table))
    data = c.fetchall()
    return data

# view tables
def view_table(table):
    c.execute('SELECT * FROM {}'.format(table))
    data = c.fetchall()
    return data


#--------------------------------------------------------------------------------------


# add  data

def add_Employee(E_id,E_fname,E_mname,E_lname,E_mail,E_phone,E_dob,E_doj,E_gender,E_did,E_address):
    c.execute('INSERT into Employee(Emp_ID,First_Name,Middle_Name,Last_Name,Email,Phone_Number,Emp_DOB,Emp_DOJ,Gender,D_ID,Emp_Address) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    (E_id,E_fname,E_mname,E_lname,E_mail,E_phone,E_dob,E_doj,E_gender,E_did,E_address))
    mydb.commit()

def add_Department(D_id,D_name,Mgr_id,Mgr_str,Base_sal,no_emp):
    c.execute('insert into Department(Dept_ID,Dept_Name,Mgr_ID,Mgr_Start_Date,Base_Sal,Number_of_Emp) values (%s,%s,%s,%s,%s,%s)',
    (D_id,D_name,Mgr_id,Mgr_str,Base_sal,no_emp))
    mydb.commit()

def add_Dept_Locations(De_id,De_loc):
    c.execute('insert into Dept_Locations(Dept_ID,Dept_Location) values (%s,%s)',
    (De_id,De_loc))
    mydb.commit()

def add_Project(P_id,Dep_id,P_name,P_desc,P_inc):
    c.execute('insert into Project(P_ID,D_ID,P_Name,P_Desc,P_Incremental_Sal) values (%s,%s,%s,%s,%s)',
    (P_id,Dep_id,P_name,P_desc,P_inc))
    mydb.commit()


def add_Works_On(Em_id,Pr_id,W_hrs):
    c.execute('insert into Works_On(Emp_ID,P_ID,Work_Hours) values (%s,%s)',
    (Em_id,Pr_id,W_hrs))
    mydb.commit()

def add_Dependents(D_eid,De_name,D_gen,D_dob,D_rel):
    c.execute('insert into Dependents(Emp_ID,Dependent_Name,Gender,Bdate,Relationship) values (%s,%s,%s,%s,%s)',
    (D_eid,De_name,D_gen,D_dob,D_rel))
    mydb.commit()

def add_payroll(P_eid,Sal_mon,Sal_ann,T_id):
    c.execute('insert into Pay_Roll(Emp_ID,Sal_Per_Month,Sal_Per_Annum,Transaction_ID) values (%s,%s,%s,%s)',
    (P_eid,Sal_mon,Sal_ann,T_id))
    mydb.commit()

def add_paygrade(pg_id,Bas_sal,ta,da,pf,ma):
    c.execute('insert into Pay_Grade(Dept_ID,Base_Sal,Grade_TA,Grade_DA,Grade_PF,Grade_MA) values (%s,%s,%s,%s,%s,%s)',
    (pg_id,Bas_sal,ta,da,pf,ma))
    mydb.commit()




#---------------------------------------------------------------------------------------







#---------------------------------------------------------------------------------------
#To Delete Tables

#view only Emp_ID
def view_Eids():
    c.execute('SELECT Emp_ID from Employee')
    data = c.fetchall()
    return data

#Delete Employee
def delete_Employee_data(pid):
    c.execute('DELETE FROM Employee WHERE Emp_ID="{}"'.format(pid))
    mydb.commit()

#View Only Department ID
def view_deptids():
    c.execute('SELECT Dept_ID from Department')
    data = c.fetchall()
    return data

#Delete Department
def delete_Department(deptid):
    c.execute('DELETE FROM Department WHERE Dept_ID ="{}"'.format(deptid))
    mydb.commit()

#View Only Project
def view_Project():
    c.execute('SELECT P_ID from Project')
    data = c.fetchall()
    return data

#Delete Project
def delete_Project(pid):
    c.execute('DELETE FROM Project WHERE P_ID="{}"'.format(pid))
    mydb.commit()
    

#View Only Dependents
def view_Dependents():
    c.execute('SELECT Emp_ID from Employee')
    data = c.fetchall()
    return data

#Delete Dependents
def delete_Dependents(e_ids):
    c.execute('DELETE FROM Dependents WHERE Emp_ID="{}"'.format(e_ids))
    mydb.commit()

#View Ony Pay_Roll  
def view_payroll():
    c.execute('SELECT Emp_ID from Pay_Roll')
    data = c.fetchall()
    return data

#Delete All Pay_Roll
def delete_payroll(payroll):
    c.execute('DELETE FROM Pay_Roll WHERE Emp_ID="{}"'.format(payroll))
    mydb.commit()
    
#View Pay_Grade
def view_paygrade():
    c.execute('SELECT Dept_ID from PAy_Grade')
    data = c.fetchall()
    return data

#Delete Pay_Grade
def delete_PayGrade(PayGrade):
    c.execute('DELETE FROM matches WHERE match_id="{}"'.format(PayGrade))
    mydb.commit()

#View Dept_Locations
def view_deptloc():
    c.execute('SELECT Dept_ID from Dept_Locations')
    data = c.fetchall()
    return data

#Delete Dept_Locations
def delete_Dept_Locations(dept_loc):
    c.execute('DELETE FROM Dept_Locations WHERE Dept_ID="{}"'.format(dept_loc))
    mydb.commit()

#View Works_on
def view_Works_On():
    c.execute('SELECT Emp_ID from Works_On')
    data = c.fetchall()
    return data

#Delete Works_on
def delete_Works_On(workson):
    c.execute('DELETE FROM Works_On WHERE Emp_ID="{}"'.format(workson))
    mydb.commit()


#--------------------------------------------------------------------------------------------------------------------
#Update Details :

#View Employee Details : 
def get_emp(eid):
    c.execute('SELECT * FROM Employee WHERE Emp_ID="{}"'.format(eid))
    data = c.fetchall()
    return data

# update Employee Details:
def edit_employee_data(new_FirstName, new_MiddleName, new_LastName, new_email, new_Phone, new_DOB, new_DOJ, new_Gender, new_D_id,new_Address, Firstname, Middlename, Lastname, Email,Phone, DOB, DOJ,Gender,D_id,Address):  #new_Customer_ID,Customer_ID,
    c.execute("UPDATE Employee SET First_Name=%s, Middle_Name=%s, Last_Name=%s, Email=%s, Phone_Number=%s, Emp_DOB=%s, Emp_DOJ=%s, Gender=%s, D_id=%s,Emp_Address=%s WHERE First_Name=%s and Middle_Name=%s and Last_Name=%s and Email=%s and Phone_Number=%s and Emp_DOB=%s and Emp_DOJ=%s and Gender=%s and D_id=%s and Emp_Address=%s", (new_FirstName, new_MiddleName, new_LastName, new_email, new_Phone, new_DOB, new_DOJ, new_Gender, new_D_id,new_Address, Firstname, Middlename, Lastname, Email, Phone, DOB,DOJ,Gender,D_id, Address))# Customer_ID=%s, Customer_ID=%s and ,new_Customer_ID,Customer_ID,
    mydb.commit()
    
#View Department Details : 
def get_Department(Did):
    c.execute('SELECT * FROM Department WHERE Dept_ID="{}"'.format(Did))
    data = c.fetchall()
    return data

# update Department Details:
def edit_Department_data(new_dname,new_mgrid,new_mgrdd,new_base_sal,new_no_emp ,Dept_Name,Mgr_ID,Mgr_Start_Date,Base_Sal,Number_of_Emp):
    c.execute("UPDATE Department SET Dept_Name=%s, Mgr_ID=%s, Mgr_Start_Date=%s,Base_Sal=%s, Number_of_Emp=%s,  WHERE Dept_Name=%s and Mgr_ID=%s and Mgr_Start_Date=%s and Base_Sal=%s and Number_of_Emp=%s", ( new_dname,new_mgrid,new_mgrdd,new_base_sal,new_no_emp ,Dept_Name,Mgr_ID,Mgr_Start_Date,Base_Sal,Number_of_Emp))
    mydb.commit()



#Command Prompt
def execute_query(query):
    str(query).replace(";", '')
    if "select" in str(query).lower():
        c.execute(query)
        res = c.fetchall()
        return res,c.description

    elif "insert" in str(query).lower():
        c.execute(query)
        mydb.commit()

    elif "update" in str(query).lower():
        c.execute(query)
        mydb.commit()

    elif "delete" in str(query).lower():
        c.execute(query)
        mydb.commit()
