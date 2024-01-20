# PayRoll Management System using MySQL
No organization can take risk when it comes to financial, accounting, bookkeeping
and payroll issues. Any errors in monetary records may lead to legal consequences as
well as financial loss. So here Payroll management system becomes instrumental.
Payroll management system is computer-operated system designed to record monitor
and manage employee's pay- roll matters in any Organization. With an increase in the
number of Employees and organizations, the financial management of the
organization is becoming a complex issue. Also, there is a great deal of strain on top
management in the Organization.

Other advantages of Payroll management system are as follows.
• Easy payroll record-keeping of Employees
• Help management employee related decisions
• Minimize financial loss due to errors
• Data consistency and Back-up
• Overcome the old procedures
• Easy information refreshing

Payroll management system will work and update the Employee's payroll records,
salary records, wages records, tax expenses, job duration records, attendance record,
experience record, duty hour's record, and other accounting details related to payrolls.
It deals with the recording and processing Employee's payroll data so that the
executives can easily manage the organizational operations.

# Requirements
- Xampp
- Streamlit(pip install streamlit) for ***Front End***
- Python 3.8 or higher
# Execution Steps:
- Clone or download the repository to your web server directory
- connect to the MariaDB database from the Xampp control panel
- Create a new MySQL database and import the ***Database Structure.sql*** file to create the necessary tables
- import the ***Data.sql*** file to insert the initial data
- Import ***Queries.sql*** to perform a set of different queries that can be executed on the database
   - This file contains Join Operations,Aggregate Functions,SET Operations.
- Import ***Function_Procedure_Trigger.sql*** to perform a Function,View,Procedure,Trigger Operations on the database.

### Front End
- Open the terminal and navigate to the ***Front End*** directory
- Run the following command to start the streamlit server
```bash
streamlit run app.py
```
- On the front End you can perform ***CRED*** Operations on the database. You will also be provided with a Command Prompt to perform SQL Queries on the database.






