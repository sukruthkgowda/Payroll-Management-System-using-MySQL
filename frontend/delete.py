import pandas as pd
import streamlit as st

from database import view_table
from database import view_Eids,delete_Employee_data
from database import view_deptids,delete_Department
from database import view_Project,delete_Project
from database import view_Dependents,delete_Dependents
from database import view_payroll,delete_payroll
from database import view_paygrade,delete_PayGrade
from database import view_deptloc,delete_Dept_Locations
from database import view_Works_On,delete_Works_On





def delete():
    list_of_tables=['Employee','Department','Works_Ons','Project','Works_On','Dependents','Works_On','Pay_Roll']
    choice=st.selectbox("Select Table to DELETE Data", list_of_tables)

    if choice == "Employee":
        result = view_table('Employee')
        df = pd.DataFrame(result, columns=['Emp_ID','First_Name','Middle_Name','Last_Name','Email','Phone_Number','Emp_DOB','Emp_DOJ','Gender','D_ID','Emp_Address'])
        with st.expander("Current data in Employee Table"):
            st.dataframe(df)
        
        E_ids = [i[0] for i in view_Eids()]
        selected_Eid = st.selectbox("Select Employee ID", E_ids)
        st.warning("Do you want to Delete Employee ID:: {} ".format(selected_Eid))
        if st.button("Delete Employee"):
            delete_Employee_data(selected_Eid)            
            st.success("Employee has been deleted successfully")
        
        new_result = view_table('Employee')
        df2 = pd.DataFrame(new_result, columns=['Emp_ID','First_Name','Middle_Name','Last_Name','Email','Phone_Number','Emp_DOB','Emp_DOJ','Gender','D_ID','Emp_Address'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "Department":
        result = view_table('Department')
        df = pd.DataFrame(result, columns=['Dept_ID','Dept_Name','Mgr_ID','Mgr_Start_Date','Base_Sal','Number_of_Emp'])
        with st.expander("Current data in Department Table"):
            st.dataframe(df)
        
        dept_ids = [i[0] for i in view_deptids()]
        selected_deptid = st.selectbox("Select Department ID", dept_ids)
        st.warning("Do you want to Delete Department ID:: {} ".format(selected_deptid))
        if st.button("Delete Department"):
            delete_Department(selected_deptid)            
            st.success("Department has been deleted successfully")
        
        new_result = view_table('Department')
        df2 = pd.DataFrame(new_result, columns=['Dept_ID','Dept_Name','Mgr_ID','Mgr_Start_Date','Base_Sal','Number_of_Emp'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Project':
        result = view_table('Project')
        df = pd.DataFrame(result, columns=['P_ID','D_ID','P_Name','P_Desc','P_Incremental_Sal'])
        with st.expander("Current data in Project Table"):
            st.dataframe(df)
        
        p_ids = [i[0] for i in view_Project()]
        selected_Project = st.selectbox("Select Project ID", p_ids)
        st.warning("Do you want to Delete Project:: {} ".format(selected_Project))
        if st.button("Delete Project"):
            delete_Project(selected_Project)            
            st.success("Project Details has been deleted successfully")
        
        new_result = view_table('Project')
        df2 = pd.DataFrame(new_result, columns=['P_ID','D_ID','P_Name','P_Desc','P_Incremental_Sal'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Dependents':
        result = view_table('Dependents')
        df = pd.DataFrame(result, columns=['Emp_ID','Dependent_Name','Gender','Bdate','Relationship'])
        with st.expander("Current data in Dependents Table"):
            st.dataframe(df)
        
        e_ids = [i[0] for i in view_Dependents()]
        selected_eid = st.selectbox("Select Dependents",e_ids)
        st.warning("Do you want to Delete Dependents employee ID: {} ".format(selected_eid))
        if st.button("Delete Dependents"):
            delete_Dependents(selected_eid)            
            st.success("Dependents has been deleted successfully")
        
        new_result = view_table('Dependents')
        df2 = pd.DataFrame(new_result, columns=['Emp_ID','Dependent_Name','Gender','Bdate','Relationship'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Pay_Roll':
        result = view_table('Pay_Roll')
        df = pd.DataFrame(result, columns=['Emp_ID','Sal_Per_Month','Sal_Per_Annum','Transaction_ID'])
        with st.expander("Current data in Pay_Roll Table"):
            st.dataframe(df)
        
        payroll = [i[0] for i in view_payroll()]
        selected_payroll = st.selectbox("Select Pay_Roll", payroll)
        st.warning("Do you want to Delete Pay_Roll: {} ".format(selected_payroll))
        if st.button("Delete Pay_Roll"):
            delete_payroll(selected_payroll)            
            st.success("Pay_Roll has been deleted successfully")
        
        new_result = view_table('Pay_Roll')
        df2 = pd.DataFrame(new_result, columns=['Emp_ID','Sal_Per_Month','Sal_Per_Annum','Transaction_ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Works_On':
        result = view_table('Works_On')
        df = pd.DataFrame(result, columns=['Emp_ID','P_ID','Work_Hours'])
        with st.expander("Current data in Works_On Table"):
            st.dataframe(df)
        
        Works_On = [i[0] for i in view_Works_On()]
        selected_Works_On = st.selectbox("Select Works_On", Works_On)
        st.warning("Do you want to Delete Works_On: {} ".format(selected_Works_On))
        if st.button("Delete Works_On"):
            delete_Works_On(selected_Works_On)            
            st.success("Works_On has been deleted successfully")
        
        new_result = view_table('Works_On')
        df2 = pd.DataFrame(new_result, columns=['Emp_ID','P_ID','Work_Hours'])
        with st.expander("Updated data"):
            st.dataframe(df2)


    elif choice == 'Pay_Grade':
        result = view_table('Pay_Grade')
        df = pd.DataFrame(result, columns=['Dept_ID','Base_Sal','Grade_TA','Grade_DA','Grade_PF','Grade_MA'])
        with st.expander("Current data in Pay_Grade Table"):
            st.dataframe(df)
        
        PayGrade = [i[0] for i in view_paygrade()]
        selected_paygrade = st.selectbox("Select Pay_Grade", PayGrade)
        st.warning("Do you want to Delete Pay_Grade of Department: {} ".format(selected_paygrade))
        if st.button("Delete Pay_Grade"):
            delete_PayGrade(selected_paygrade)            
            st.success("Pay_Grade has been deleted successfully")
        
        new_result = view_table('Works_On')
        df2 = pd.DataFrame(new_result, columns=['Dept_ID','Base_Sal','Grade_TA','Grade_DA','Grade_PF','Grade_MA'])
        with st.expander("Updated data"):
            st.dataframe(df2)


    elif choice == 'Dept_Locations':
        result = view_table('Dept_Locations')
        df = pd.DataFrame(result, columns=['Dept_ID','Dept_Location'])
        with st.expander("Current data in Dept_Locations Table"):
            st.dataframe(df)
        
        dept_loc = [i[0] for i in view_deptloc()]
        selected_dept_loc = st.selectbox("Select Dept_Location", dept_loc)
        st.warning("Do you want to Delete Dept_Locations of Department : {} ".format(selected_dept_loc))
        if st.button("Delete Dept_Locations"):
            delete_Dept_Locations(selected_dept_loc)            
            st.success("Dept_Locations has been deleted successfully")
        
        new_result = view_table('Dept_Locations')
        df2 = pd.DataFrame(new_result, columns=['Dept_ID','Dept_Location'])
        with st.expander("Updated data"):
            st.dataframe(df2)




