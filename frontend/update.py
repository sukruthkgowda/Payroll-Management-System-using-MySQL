import pandas as pd
import streamlit as st



from database import view_Eids,get_emp,edit_employee_data
from database import view_deptids,get_Department,edit_Department_data

from database import view_table


def update():
    list_of_tables=['Employee','Department','Dept_Locations','Project','Works_On','Dependents','Pay_Grade','Pay_Roll']
    choice=st.selectbox("Select Table to UPDATE Data", list_of_tables)

    if choice == "Employee":
        result = view_table('Employee')
        df = pd.DataFrame(result, columns=['Emp_ID','First_Name','Middle_Name','Last_Name','Email','Phone_Number','Emp_DOB','Emp_DOJ','Gender','D_ID','Emp_Address'])
        with st.expander("Current Employee Table"):
            st.dataframe(df)
        E_ids = [i[0] for i in view_Eids()]
        selected_eid = st.selectbox("Select Employee ID", E_ids)
        selected_result = get_emp(selected_eid)
        if selected_result:
            E_id = selected_result[0][0]
            Firstname = selected_result[0][1]
            Middlename = selected_result[0][2]
            Lastname = selected_result[0][3]
            Email = selected_result[0][4]
            Phone = selected_result[0][5]
            DOB = selected_result[0][6]
            DOJ = selected_result[0][7]
            Gender = selected_result[0][8]
            D_id = selected_result[0][9]
            Address = selected_result[0][10]

        ecol1,ecol2,ecol3 = st.columns(3)
        with ecol1:
            new_FirstName = st.text_input("First Name",Firstname)
            new_MiddleName = st.text_input("Middle Name",Middlename)
            new_LastName = st.text_input("Last Name",Lastname)
            
        
        with ecol2:
            new_email = st.text_input("Email",Email)
            new_Phone = st.text_input("Phone Number",Phone)
            new_DOB = st.text_input("DOB",DOB)
            

        with ecol3:
            new_DOJ = st.text_input("DOJ",DOJ)
            new_Gender = st.text_input("Gender",Gender)
            new_D_id = st.text_input("Department ID",D_id)
            new_Address = st.text_input("Address",Address)
            
            
        
        if st.button("Update Employee"):
            edit_employee_data(new_FirstName,new_MiddleName,new_LastName,new_email,new_Phone,new_DOB,new_DOJ,new_Gender,new_D_id,new_Address,Firstname,Middlename,Lastname,Email,Phone,DOB,DOJ,Gender,D_id,Address)#new_c_id,c_id,
            st.success("Successfully Updated Employee with ID : {} ".format(E_id))

        result2 = view_table('Employee')
        df2 = pd.DataFrame(result2, columns=['Emp_ID','First_Name','Middle_Name','Last_Name','Email','Phone_Number','Emp_DOB','Emp_DOJ','Gender','D_ID','Emp_Address'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == "Department":
        result = view_table('Department')
        df = pd.DataFrame(result, columns=['Dept_ID','Dept_Name','Mgr_ID','Mgr_Start_Date','Base_Sal','Number_of_Emp'])
        with st.expander("Current Department Table"):
            st.dataframe(df)
        D_ids = [i[0] for i in view_deptids()]
        selected_did = st.selectbox("Select Department ID", D_ids)
        selected_result = get_Department(selected_did)
        if selected_result:
            Dept_id = selected_result[0][0]
            Dept_Name = selected_result[0][1]
            Mgr_ID = selected_result[0][2]
            Mgr_Start_Date = selected_result[0][3]
            Base_Sal = selected_result[0][4]
            Number_of_Emp = selected_result[0][5]


        ecol1,ecol2 = st.columns(2)
        with ecol1:
            new_dname = st.text_input("Department Name",Dept_Name)
            new_mgrid = st.text_input("Mgr ID",Mgr_ID)
        
        with ecol2:
            new_mgrdd = st.text_input("Mgr start Date",Mgr_Start_Date)
            new_base_sal = st.text_input("Base Salary",Base_Sal)
            new_no_emp = st.text_input("Number of Employee",Number_of_Emp)
        
        if st.button("Update Department"):
            edit_Department_data(new_dname,new_mgrid,new_mgrdd,new_base_sal,new_no_emp ,Dept_Name,Mgr_ID,Mgr_Start_Date,Base_Sal,Number_of_Emp)
            st.success("Successfully Updated Department ID : {} ".format(Dept_id))

        result2 = view_table('Department')
        df2 = pd.DataFrame(result2, columns=['Dept_ID','Dept_Name','Mgr_ID','Mgr_Start_Date','Base_Sal','Number_of_Emp'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    '''
    elif choice=="Project":
        result = view_table('Project')
        df = pd.DataFrame(result, columns=['Category Name','No of Persons','Cost Per Day','Delay Fee per Hour'])
        with st.expander("Car Category Table"):
            st.dataframe(df)
        category = [i[0] for i in view_Car_Category()]
        selected_category = st.selectbox("Select Location ID", category)
        selected_result = get_category(selected_category)
        if selected_result:
            category_name = selected_result[0][0]
            no_of_persons = selected_result[0][1]
            cost_per_day = selected_result[0][2]
            Delay_Fee_per_hour = selected_result[0][3]

            #new_category_name = st.text_input("Category Name",category_name)
            new_no_of_persons = st.text_input("No of Persons",no_of_persons)
            new_cost_per_day = st.text_input("Cost Per Day",cost_per_day)
            new_Delay_Fee_per_hour = st.text_input("Delay Fee Per Hour",Delay_Fee_per_hour)
        
        if st.button("Update Car Category"):
            edit_category_data(new_no_of_persons,new_cost_per_day,new_Delay_Fee_per_hour,no_of_persons,cost_per_day,Delay_Fee_per_hour)
            st.success("Successfully Updated Category with Name : {} ".format(category_name))

        result2 = view_table('car_category')
        df2 = pd.DataFrame(result2, columns=['Category Name','No of Persons','Cost Per Day','Delay Fee per Hour'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice=="car_detail":
        result = view_table('car_detail')
        df = pd.DataFrame(result, columns=['Registration No','Model','Make','Model_Year','Mileage','Availability','Category','Location'])
        with st.expander("Car Details Table"):
            st.dataframe(df)
        car = [i[0] for i in view_RegNo()]
        selected_car = st.selectbox("Select Car", car)
        selected_result = get_car(selected_car)
        if selected_result:
            Registration_No = selected_result[0][0]
            Model = selected_result[0][1]
            Make = selected_result[0][2]
            Model_Year = selected_result[0][3]
            Mileage = selected_result[0][4]
            Availability = selected_result[0][5]
            Category = selected_result[0][6]
            Location = selected_result[0][7]
            

        ecol1,ecol2 = st.columns(2)
        with ecol1:
            #new_Registration_No = st.text_input("Registration No",Registration_No)
            new_Model = st.text_input("Model",Model)
            new_Make = st.text_input("Model",Make)
            new_Model_Year = st.text_input("Model Year",Model_Year)

        with ecol2:
            new_Mileage = st.text_input("Mileage",Mileage)
            new_Availability = st.text_input("Availability",Availability)
            new_Category = st.text_input("Category",Category)
            new_Location = st.text_input("Location",Location)
        
        if st.button("Update Car Details"):
            edit_Car_data(new_Model,new_Make,new_Model_Year,new_Mileage,new_Availability,new_Category,new_Location,Model,Make,Model_Year,Mileage,Availability,Category,Location)
            st.success("Successfully Updated Car with Registration_No : {} ".format(Registration_No))

        result2 = view_table('car_detail')
        df2 = pd.DataFrame(result2, columns=['Registration No','Model','Make','Model_Year','Mileage','Availability','Category','Location'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice=="Car_Insurance":
        result = view_table('Car_Insurance')
        df = pd.DataFrame(result, columns=['Insurance ID','Insurance Name','Coverage Type','Insurance Cost Per Day'])
        with st.expander("Car Insurance Table"):
            st.dataframe(df)
        insurance = [i[0] for i in view_Iids()]
        selected_insurance = st.selectbox("Select Car Insurance", insurance)
        selected_result = get_Insurance(selected_insurance)
        if selected_result:
            Insurance_ID = selected_result[0][0]
            Insurance_Name = selected_result[0][1]
            Coverage_Type = selected_result[0][2]
            Insurance_Cost_Per_Day = selected_result[0][3]

            #new_Insurance_No = st.text_input("Insurance ID",Insurance_ID)
            new_Insurance_Name = st.text_input("Insurance_Name",Insurance_Name)
            new_Coverage_Type = st.text_input("Coverage_Type",Coverage_Type)
            new_Insurance_Cost = st.text_input("Insurance Cost Per Day",Insurance_Cost_Per_Day)

        
        if st.button("Update Car Insurance Details"):
            edit_Insurance_data(new_Insurance_Name,new_Coverage_Type,new_Insurance_Cost,Insurance_Name,Coverage_Type,Insurance_Cost_Per_Day)
            st.success("Successfully Updated Car Insurance with ID : {} ".format(Insurance_ID))

        result2 = view_table('Car_Insurance')
        df2 = pd.DataFrame(result2, columns=['Insurance ID','Insurance Name','Coverage Type','Insurance Cost Per Day'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Payment':
        result = view_table('Payment')
        df = pd.DataFrame(result, columns=['Payment ID','Total Amount','Payment Method','Payment Status'])
        with st.expander("Car Payment Table"):
            st.dataframe(df)
        Payment = [i[0] for i in view_Pids()]
        selected_payment = st.selectbox("Select Car Insurance", Payment)
        selected_result = get_Payment(selected_payment)
        if selected_result:
            Payment_ID = selected_result[0][0]
            Total_Amount = selected_result[0][1]
            Payment_Method = selected_result[0][2]
            Payment_status = selected_result[0][3]

            #new_Payment_ID = st.text_input("Payment ID",Payment_ID)
            new_Total_Amount = st.text_input("Total Amount",Total_Amount)
            new_Payment_Method = st.text_input("Payment Method",Payment_Method)
            new_Payment_status = st.text_input("Payment Status",Payment_status)

        
        if st.button("Update Car Payment Details"):
            edit_Payment_data(new_Total_Amount,new_Payment_Method,new_Payment_status,Total_Amount,Payment_Method,Payment_status)
            st.success("Successfully Updated Payment Details with ID : {} ".format(Payment_ID))

        result2 = view_table('Payment')
        df2 = pd.DataFrame(result2, columns=['Payment ID','Total Amount','Payment Method','Payment Status'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif choice == 'Booking_Details':
        result = view_table('Booking_Details')
        df = pd.DataFrame(result, columns=['Booking ID','Customer ID','From Date','Return Date','Amount','Actual Return Date','Pick Up Location','Drop Location','Insurance','Car Registration No','Payment ID'])
        with st.expander("Current Booking Details Table"):
            st.dataframe(df)
        Booking_ids = [i[0] for i in view_Bookingids()]
        selected_Bookingid = st.selectbox("Select Booking ID", Booking_ids)
        selected_result = get_Booking(selected_Bookingid)
        if selected_result:
            Booking_id = selected_result[0][0]
            Customer_id = selected_result[0][1]
            From_Date = selected_result[0][2]
            Return_Date = selected_result[0][3]
            Amount = selected_result[0][4]
            #Booking_Status = selected_result[0][5]
            Actual_Return_Date = selected_result[0][5]
            Pickup_Location = selected_result[0][6]
            Drop_Location = selected_result[0][7]
            Insurance = selected_result[0][8]
            Car_Reg_No = selected_result[0][9]
            Payment_Booking_ID = selected_result[0][10]

        ecol1,ecol2,ecol3 = st.columns(3)
        with ecol1:
            #new_Booking_id = st.text_input("Booking ID",Booking_id)
            new_Customer_id = st.text_input("Customer ID",Customer_id)
            new_From_Date = st.text_input("From Date",From_Date)
            new_Return_Date = st.text_input("Return Date",Return_Date)
        
        with ecol2:
            new_Amount = st.text_input("Amount",Amount)
            #new_Booking_Status = st.text_input("Booking Status",Booking_Status)
            new_Actual_Return_Date = st.text_input("Actual Return Date",Actual_Return_Date)
            new_Pickup_Location = st.text_input("Pick Up Location",Pickup_Location)

        with ecol3:
            new_Drop_Location = st.text_input("Drop Location",Drop_Location)
            new_Insurance = st.text_input("Insurance",Insurance)
            new_Car_Reg_No = st.text_input("Car Registration No",Car_Reg_No)
            new_Payment_Booking_ID = st.text_input("Payment ID",Payment_Booking_ID)
        
        if st.button("Update Booking Details"):
            edit_Booking_data(new_Customer_id,new_From_Date,new_Return_Date,new_Amount,new_Actual_Return_Date,new_Pickup_Location,new_Drop_Location,new_Insurance,new_Car_Reg_No,new_Payment_Booking_ID,Customer_id,From_Date,Return_Date,Amount,Actual_Return_Date,Pickup_Location,Drop_Location,Insurance,Car_Reg_No,Payment_Booking_ID)
            st.success("Successfully Updated Booking with ID : {} ".format(Booking_id))

        result2 = view_table('Booking_Details')
        df2 = pd.DataFrame(result2, columns=['Booking ID','Customer ID','From Date','Return Date','Amount','Actual Return Date','Pick Up Location','Drop Location','Insurance','Car Registration No','Payment ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)     
   
    else:
        st.subheader("Select Table")   
    '''




