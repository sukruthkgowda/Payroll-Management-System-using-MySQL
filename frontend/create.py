import streamlit as st
from database import add_Employee,add_Department,add_Dept_Locations,add_Project,add_Works_On,add_Dependents,add_payroll,add_paygrade


def create():
    list_of_tables=['Employee','Department','Dept_Locations','Project','Works_On','Dependents','Pay_Grade','Pay_Roll']
    choice=st.selectbox("Select Table to INSERT Data", list_of_tables)

    if choice == "Employee":
        st.text("Fill out the Employee Details")

        E_id = st.text_input("Emp_ID")
        E_fname = st.text_input("First Name")
        E_mname = st.text_input("Middle Name")
        E_lname = st.text_input("Last Name")
        E_mail = st.text_input("Email ID")
        E_phone = st.text_input("Phone Number")
        E_dob = st.text_input("Employee DOB(Format-- YYYY-MM-DD)")
        E_doj = st.text_input("Employee DOJ(Format-- YYYY-MM-DD)")
        E_gender = st.text_input("Gender")
        E_did = st.text_input("Department ID")
        E_address = st.text_input("Address")
        
        
        if st.button("Add Employee Details:"):
            add_Employee(E_id,E_fname,E_mname,E_lname,E_mail,E_phone,E_dob,E_doj,E_gender,E_did,E_address)
            st.success("Successfully added Employee : {}".format(E_fname))


    elif choice == "Department":
        st.text("Fill the Department Details:")

        D_id = st.text_input("Department ID")
        D_name = st.text_input("Department Name")
        Mgr_id = st.text_input("Manager ID")
        Mgr_str = st.text_input("Manager Start Date(Format-- YYYY-MM-DD)")
        Base_sal = st.text_input("Department Base Salary")
        no_emp = st.text_input("No. of Employees")
        

        if st.button("Add Department Details:"):
            add_Department(D_id,D_name,Mgr_id,Mgr_str,Base_sal,no_emp)
            st.success("Successfully added the Department Details for : {}".format(D_name))


    elif choice == "Dept_Locations":
        st.text("Fill the Department Locations Details:")

        De_id = st.text_input("Department ID")
        De_loc = st.text_input("Department Location")
        
        if st.button("Add Department Locations Details:"):
            add_Dept_Locations(De_id,De_loc)
            st.success("Successfully added the Department Locations Details for : {}".format(De_id))


    elif choice == "Project":
        st.text("Fill the Project Details:")

        P_id = st.text_input("Project ID")
        Dep_id = st.text_input("Department ID")
        P_name = st.text_input("Project Name")
        P_desc = st.text_input("Project Description")
        P_inc = st.text_input("Project Incremental Salary")
        
        if st.button("Add Project Details:"):
            add_Project(P_id,Dep_id,P_name,P_desc,P_inc)
            st.success("Successfully added the Project Details for : {}".format(P_name))



    elif choice == "Works_On":
        st.text("Fill the Works on Details:")

        Em_id = st.text_input("Employee ID")
        Pr_id = st.text_input("Project ID")
        W_hrs = st.text_input("Work Hours")
        
        if st.button("Add Works On Details:"):
            add_Works_On(Em_id,Pr_id,W_hrs)
            st.success("Successfully added the Works On Details for : {}".format(Em_id))

    elif choice == "Dependents":
        st.text("Fill the Dependents Details:")

        D_eid = st.text_input("Employee ID")
        De_name = st.text_input("Department  Name")
        D_gen= st.text_input("Dependent Gender")
        D_dob = st.text_input("Dependent DOB(Format-- YYYY-MM-DD)")
        D_rel = st.text_input("Dependent Relationship")
        
        if st.button("Add Dependents Details:"):
            add_Dependents(D_eid,De_name,D_gen,D_dob,D_rel)
            st.success("Successfully added Dependents Details: {}".format(De_name))


    elif choice == "Pay_Roll":
        st.text("Fill the PayRoll Details:")

        P_eid = st.text_input("Employee ID ")
        Sal_mon = st.text_input("Salary per Month ")
        Sal_ann = st.text_input("Salary per Annum ")
        T_id = st.text_input("Transaction ID ")

        if st.button("Add PayRoll Details:"):
            add_payroll(P_eid,Sal_mon,Sal_ann,T_id)
            st.success("Successfully added Payroll Details for Emp_ID : {}".format(P_eid))


    elif choice == "Pay_Grade":
        st.text("Fill the Pay Grade Details:")

        pg_id = st.text_input("Department ID")
        Bas_sal = st.text_input("Departments Base Salary")
        ta = st.text_input("Travel Allowance")
        da = st.text_input("Dearness Allowance")
        pf = st.text_input("Provident Fund")
        ma = st.text_input("Medical Allowance")

        if st.button("Add Pay Grade Details"):
            add_paygrade(pg_id,Bas_sal,ta,da,pf,ma)
            st.success("Successfully added Pay Grade Details for Department ID : {}".format(pg_id))

    else:
        st.subheader("Select Table")
