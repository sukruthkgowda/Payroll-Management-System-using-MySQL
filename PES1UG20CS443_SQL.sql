--Creating Tables
CREATE TABLE EMPLOYEE
(	Emp_ID INT NOT NULL,    
    First_Name VARCHAR(255) NOT NULL,
	Middle_Name VARCHAR(255) NULL, 
	Last_Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Phone_Number VARCHAR(10) NOT NULL,
	Emp_DOB DATE NOT NULL,
    Emp_DOJ DATE NOT NULL,
	Gender CHAR NOT NULL,
	D_ID INT NOT NULL,
    Emp_Address VARCHAR(255) NOT NULL,
	PRIMARY KEY (Emp_ID));

	
CREATE TABLE DEPARTMENT
(	Dept_ID INT NOT NULL,
    Dept_Name VARCHAR(255) NOT NULL,
	Mgr_ID INT NOT NULL,
	Mgr_Start_Date DATE NOT NULL,
    Base_Sal DECIMAL(10, 3) NOT NULL,
    Number_of_Emp INT NOT NULL ,
	PRIMARY KEY (Dept_ID),
	UNIQUE (Dept_Name),
	FOREIGN KEY (Mgr_ID) REFERENCES  EMPLOYEE(Emp_ID) );
	

CREATE TABLE DEPT_LOCATIONS
(	Dept_ID INT NOT NULL, 
	Dept_Location VARCHAR(255) NOT NULL,
	PRIMARY KEY (Dept_ID),
	FOREIGN KEY (Dept_ID) REFERENCES  DEPARTMENT(Dept_ID) ON UPDATE CASCADE ON DELETE CASCADE);


CREATE TABLE PROJECT
(	P_ID INT NOT NULL,
    Dept_ID INT NOT NULL,
    P_Name VARCHAR(255) NOT NULL,
    P_Desc VARCHAR(255),
    P_Incremental_Sal DECIMAL(10, 2) NOT NULL,
	PRIMARY KEY (P_ID),
	UNIQUE(P_Name),
	FOREIGN KEY (Dept_ID) REFERENCES DEPARTMENT(Dept_ID) ON UPDATE CASCADE ON DELETE CASCADE);


CREATE TABLE WORKS_ON
(	Emp_ID INT NOT NULL,
	P_ID INT NOT NULL, 
	Work_Hours DECIMAL(6,2) NOT NULL,
	PRIMARY KEY (Emp_ID, P_ID),
	FOREIGN KEY (Emp_ID) REFERENCES EMPLOYEE(Emp_ID) ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY(P_ID) REFERENCES PROJECT(P_ID) ON UPDATE CASCADE ON DELETE CASCADE);

CREATE TABLE DEPENDENTS
(	Emp_ID INT NOT NULL,
	Dependent_Name VARCHAR(255) NOT NULL,
	Gender CHAR,
	Bdate DATE,
	Relationship VARCHAR(8),
	PRIMARY KEY (Emp_ID, Dependent_Name),
	FOREIGN KEY (Emp_ID) REFERENCES EMPLOYEE(Emp_ID) ON UPDATE CASCADE ON DELETE CASCADE);

CREATE TABLE PAY_ROLL
(	Emp_ID INT NOT NULL,
    Sal_Per_Month DECIMAL(10, 2) NOT NULL,
	Sal_Per_Annum DECIMAL(10, 2) NOT NULL,
	Transaction_ID VARCHAR(10) NOT NULL,
	PRIMARY KEY (Emp_ID),
	FOREIGN KEY (Emp_ID) REFERENCES EMPLOYEE(Emp_ID) ON UPDATE CASCADE ON DELETE CASCADE);

CREATE TABLE PAY_GRADE
(	Dept_ID INT NOT NULL,
	Base_Sal DECIMAL(10, 2) NOT NULL,
	Grade_TA DECIMAL(10, 2),
	Grade_DA DECIMAL(10, 2),
	Grade_PF DECIMAL(10, 2),
    Grade_MA DECIMAL(10, 2),
	PRIMARY KEY (Dept_ID),
	FOREIGN KEY (Dept_ID) REFERENCES DEPARTMENT(Dept_ID) ON UPDATE CASCADE ON DELETE CASCADE);


--Insering values

INSERT INTO EMPLOYEE VALUES(1,'Monin','h','Virk','uma@hotmail.com','9781322868','1994-09-23','2020-08-12','M',1,'225Godavari,Jekegram');
INSERT INTO EMPLOYEE VALUES(2,'Aarif','k','Kapadia','kapadia@gmail.com','9176386378','1984-05-30','2015-09-18','M',2,'Houston,tx stone450');
INSERT INTO EMPLOYEE VALUES(3,'Julie','Sharaf','u','sharf@gmail.com','9398856983','1980-06-14','2012-09-25','F',3,'65, Neerendra Heights, Neela Chowk');
INSERT INTO EMPLOYEE VALUES(4,'Prabhat','s','Sani','sani@gmail.com','6317927970','1988-03-12','2005-10-19','M',4,'34, Deccan Gymkhana, Pondicherry');
INSERT INTO EMPLOYEE VALUES(5,'Hema','A','Kapur','kapur@gmail.com','6199025439','1985-11-15','2006-05-16','F',5,'14, Deepesh Society, Samir Chowk');
INSERT INTO EMPLOYEE VALUES(6,'Meghana',NULL,'Persad','persad@gmail.com','6389474908','2001-04-23','2021-12-11','F',6,'49, Ishat Nagar, Pilani');
INSERT INTO EMPLOYEE VALUES(7,'Naval','l','Soman','soman@gmail.com','9453757869','1991-11-14','2016-11-09','M',1,'93, Sharad Society,JuhiPur');
INSERT INTO EMPLOYEE VALUES(8,'Jiya',NULL,'Sampath','sampath@gmail.com','9836732876','1992-12-15','2019-09-10','F',2,'97, Dadar,Mumbai');
INSERT INTO EMPLOYEE VALUES(9,'Mohanlal','v','Srinivas','srinij@gmail.com','7925782582','1999-02-19','2021-02-05','M',3,'71, BinoyaGarh,Kolkata');
INSERT INTO EMPLOYEE VALUES(10,'Bahadur','p','Raval','raval@gmail.com','9732586399','1986-09-15','2018-09-17','M',4,'23, Yeshwanthpur,bengaluru');
INSERT INTO EMPLOYEE VALUES(11,'Jasmin',NULL,'Bhat','bhat@gmail.com','6364758879','1979-07-06','2008-10-15','F',5,'36, CharandeepGarh,Kolkata');
INSERT INTO EMPLOYEE VALUES(12,'Qabeel','l','Mathew','meth@gmail.com','9764321987','1986-03-13','2009-05-19','M',6,'89, KiranSociety,VirarAhmedabad');
INSERT INTO EMPLOYEE VALUES(13,'John','a','cena','heisjohncena@gmail.com','9998899988','1988-08-08','2010-01-01','M',1,'450 Stone, Houston,TX');
INSERT INTO EMPLOYEE VALUES(14,'James','E','Borg','jamesborg@gmail.com','888665555','1981-01-01','2009-02-01','M',2,'731 Fondren,Houston,TX');
INSERT INTO EMPLOYEE VALUES(15,'John','','Smith','johnsmith@gmail.com','9997799977','1982-02-02','2008-03-01','M',3,'638 voss,Houston,TX');
INSERT INTO EMPLOYEE VALUES(16,'Franklin','T','Wong','franwong@gmail.com','333445555','1983-12-08','2011-04-02','M',4,'3321 Castle,Spring,Tx');
INSERT INTO EMPLOYEE VALUES(17,'Alicia','J','Zelaya','aliciazels@gmail.com','999887777','1983-01-19','2011-03-02','F',4,'3321 Castle,Spring,Tx');
INSERT INTO EMPLOYEE VALUES(18,'Jennifer','M','Wallace','jenniferwallace@gmail.com','987654321','1984-06-20','2010-03-15','F',5,'291 Berry, Bellaire,Tx');
INSERT INTO EMPLOYEE VALUES(19,'Ramesh','K','Narayan','rameshnarayan@gmail.com','666884444','1980-09-15','2009-03-04','M',6,'975 Fire Oak, Humble, TX');
INSERT INTO EMPLOYEE VALUES(20,'Ahmed','V','Jabbar','ahmedjabbar@gmail.com','987987987','1979-03-29','2008-05-28','M',3,'980 Dallas, Houston,TX');

INSERT INTO DEPARTMENT VALUES(1, 'Marketing Department',3,'2015-10-17', 32561.000, 2);
INSERT INTO DEPARTMENT VALUES(2, 'Operations Department',9,'2009-12-01', 36321.000, 2);
INSERT INTO DEPARTMENT VALUES(3, 'Finance Department',2,'2008-10-15', 27168.000, 2);
INSERT INTO DEPARTMENT VALUES(4, 'Sales Department',1,'2016-09-13', 23747.000, 2);
INSERT INTO DEPARTMENT VALUES(5, 'Human Resource Department',5,'2005-10-19', 23533.000, 2);
INSERT INTO DEPARTMENT VALUES(6, 'Purchase Department',7,'2015-09-18', 34356.000, 2);

INSERT INTO DEPT_LOCATIONS VALUES(1, 'bengaluru');
INSERT INTO DEPT_LOCATIONS VALUES(2,'houston');
INSERT INTO DEPT_LOCATIONS VALUES(3,'rajkot');
INSERT INTO DEPT_LOCATIONS VALUES(4,'nasik');
INSERT INTO DEPT_LOCATIONS VALUES(5,'stafford');
INSERT INTO DEPT_LOCATIONS VALUES(6,'mumbai');

INSERT INTO PROJECT VALUES(1,1,'Obscure Steamy','The Prometheus monitoring system and time series',25000.00);
INSERT INTO PROJECT VALUES(2,1,'Blue Steamy','The time series',35000.00);
INSERT INTO PROJECT VALUES(3,2,'Blue Moose','The plugin-driven server agent for collecting & reporting metrics',30000.00);
INSERT INTO PROJECT VALUES(4,2,'Green Moose','The driver agent for collecting & reporting metrics',20000.00);
INSERT INTO PROJECT VALUES(5,3,'Project X','Daemon to ban hosts that cause multiple authentication errors',35000.00);
INSERT INTO PROJECT VALUES(6,3,'Project Y','Doraemon to ban hosts that cause multiple',39000.00);
INSERT INTO PROJECT VALUES(7,4,'Epsilon Hollow','Monitoring, visualisation & management for Docker & Kubernetes',39000.00);
INSERT INTO PROJECT VALUES(8,5,'Olive Moon','Continuous Profiling Platform! Debug performance issues down to a single line of code',45000.00);
INSERT INTO PROJECT VALUES(9,6,'Everyday Street','Puppeteer example scripts for running Headless Chrome from Node',29000.00);

INSERT INTO WORKS_ON VALUES(1, 1, 32.5);
INSERT INTO WORKS_ON VALUES(2, 2, 18.6);
INSERT INTO WORKS_ON VALUES(3, 3, 22.5);
INSERT INTO WORKS_ON VALUES(4, 4, 19.8);
INSERT INTO WORKS_ON VALUES(5, 5, 9.8);
INSERT INTO WORKS_ON VALUES(1, 2, 12.9);
INSERT INTO WORKS_ON VALUES(6, 3, 12.5);
INSERT INTO WORKS_ON VALUES(7, 1, 15.8);
INSERT INTO WORKS_ON VALUES(8, 3, 11.4);
INSERT INTO WORKS_ON VALUES(9, 5, 16.2);
INSERT INTO WORKS_ON VALUES(10, 7, 16.9);
INSERT INTO WORKS_ON VALUES(11, 8, 14.4);
INSERT INTO WORKS_ON VALUES(12, 6, 13.9);
INSERT INTO WORKS_ON VALUES(11, 2, 19.4);
INSERT INTO WORKS_ON VALUES(13, 8, 12.7);
INSERT INTO WORKS_ON VALUES(14, 1, 15.1);
INSERT INTO WORKS_ON VALUES(15, 7, 13.8);
INSERT INTO WORKS_ON VALUES(16, 2, 11.3);
INSERT INTO WORKS_ON VALUES(17, 3, 12.9);
INSERT INTO WORKS_ON VALUES(18, 4, 15.2);
INSERT INTO WORKS_ON VALUES(19, 8, 18.5);
INSERT INTO WORKS_ON VALUES(14, 5, 19.7);
INSERT INTO WORKS_ON VALUES(20, 2, 14.6);
INSERT INTO WORKS_ON VALUES(8, 1, 11.9);
INSERT INTO WORKS_ON VALUES(5, 7, 16.3);

INSERT INTO DEPENDENTS VALUES(3,'shalini','M','1994-09-23','wife');
INSERT INTO DEPENDENTS VALUES(2,'rohit','F','1988-03-12','husband');
INSERT INTO DEPENDENTS VALUES(6,'rekha','M','1992-02-15','wife');
INSERT INTO DEPENDENTS VALUES(4,'suresh','M','2001-04-23','parent');
INSERT INTO DEPENDENTS VALUES(9,'Shailaja','M','1984-05-30','wife');
INSERT INTO DEPENDENTS VALUES(11,'prathik','F','1986-03-13','husband');
INSERT INTO DEPENDENTS VALUES(12,'megha','M','1988-08-08','wife');
INSERT INTO DEPENDENTS VALUES(19,'ranga','F','1980-09-15','husband');
INSERT INTO DEPENDENTS VALUES(15,'sharin','f','1983-01-19','wife');
INSERT INTO DEPENDENTS VALUES(17,'rekha','M','1982-02-02','husband');
INSERT INTO DEPENDENTS VALUES(18,'mallika','f','1979-03-29','wife');
INSERT INTO DEPENDENTS VALUES(13,'veena','M','1984-09-23','husband');

INSERT INTO PAY_GRADE VALUES(1, 32561.00, 1800.00, 1500.00, 1000.00, 1900.00);
INSERT INTO PAY_GRADE VALUES(2, 36321.00, 2800.00, 1300.00, 1200.00, 1800.00);
INSERT INTO PAY_GRADE VALUES(3, 27168.00, 1800.00, 1400.00, 1300.00, 1000.00);
INSERT INTO PAY_GRADE VALUES(4, 23747.00, 1300.00, 1500.00, 1000.00, 1200.00);
INSERT INTO PAY_GRADE VALUES(5, 23533.00, 1100.00, 1700.00, 1200.00, 1500.00);
INSERT INTO PAY_GRADE VALUES(6, 34356.00, 1200.00, 1100.00, 1000.00, 1900.00);

--Calculating Salary

create view temp as select emp_id, p_id, p_incremental_sal from project natural join works_on;
create view tempq1 as select emp_id, sum(p_incremental_sal) as sum from temp group by emp_id;
create view temp2 as select emp_id, d_id as dept_id, sum from tempq1 natural join employee;
create view temp3 as select emp_id, dept_id, base_sal, sum as total_incremental_salary from temp2 natural join department;
create view temp4 as select emp_id, dept_id, total_incremental_salary + base_sal as total_sal from temp3;
create view temp5 as select emp_id, dept_id, total_sal+grade_ta+grade_da+grade_pf+grade_ma as total_sal_per_month from temp4 natural join pay_grade;
insert into pay_roll select emp_id, total_sal_per_month, total_sal_per_month*12 as total_sal_per_annum, floor(rand()*(10000000000 -1000000000 +1))+1 from temp5;

--Join Qeuries
--1.Employees currently working on a project
SELECT First_Name,Last_Name,D_ID from Employee join Works_On on Employee.Emp_ID = Works_On.Emp_ID;

--2.Employees who have dependents
SELECT First_Name,Last_Name,D_ID from Employee join Dependents on Employee.Emp_ID = Dependents.Emp_ID;

--3.Departments who have projects
SELECT Dept_Name,Number_of_emp from Department join project on Department.Dept_ID = Project.Dept_ID;

--4.Departments who have a location in Bengaluru
SELECT Dept_Name,Number_of_emp from Department join Dept_Locations on Department.Dept_ID=Dept_Locations.Dept_Location = 'bengaluru'


--Aggregate Functions
--1.Total number of employees working in all departments combined
SELECT COUNT(Number_of_emp) from Department;

--2.Employee who spend more hours in work compared to the average works spent by a employee
SELECT * from Works_On where Works_On.Work_Hours > (SELECT Avg(Work_Hours) from Works_On);

--3.Employees having Annual Salary more than the average salary
select Emp_ID,Sal_Per_Annum from PAY_ROLL where PAY_ROLL.Sal_Per_Annum > (SELECT Avg(Sal_Per_Annum) from PAY_ROLL);

--4.Department having the highest Base salary
SELECT Dept_ID,max(Base_Sal) from PAY_GRADE;


--Set operators
--1.Employee Details who are male and work in Finance Department
SELECT Emp_ID,First_Name,Last_Name from Employee where Gender='M' INTERSECT  SELECT Emp_ID,First_Name,Last_Name from Employee where D_ID=3;

--2.Female Employees who have joined company after 2010
 SELECT Emp_ID,First_Name,Last_Name,Emp_DOJ from Employee where Gender='F' INTERSECT  SELECT Emp_ID,First_Name,Last_Name,Emp_DOJ from Employee where year(Emp_DOJ)>=2010;

--3.Employee Details who work more than 20 hours a week and have no dependents
SELECT Emp_ID from Works_On where Work_Hours >=20 EXCEPT SELECT Emp_ID from Dependents;

--4.Employees who have female dependents and earn more than 70000 rupees per month
select Emp_ID from Dependents where Gender = 'F' INTERSECT SELECT Emp_ID from PAY_ROLL where Sal_Per_Month >=70000;


--Function
--Write a function to find number of projects a employee is working in  
-- If no of projects is more than 1 for  then display error message 

DELIMITER $$
CREATE FUNCTION sf_no_of_projects(EmpID VARCHAR(100))
RETURNS VARCHAR(50)
DETERMINISTIC 
BEGIN 
 DECLARE sf_value VARCHAR(100);
 DECLARE rt_value VARCHAR(100); 
 DECLARE cnt INT; 

SET cnt=(SELECT COUNT(Emp_ID) 
FROM Works_On 
WHERE Works_On.Emp_ID=EmpID );  

    IF cnt > 1 THEN 
	SET rt_value = 'Maximum project limit reached for a employee';	   
    ELSEIF cnt <= 1 THEN 
	SET rt_value = 'Employee can Work in the project';	   
	END IF;
    
	RETURN rt_value;
	
END; $$

DELIMITER ;

--Procedure
--Have created a procedure which takes input of Employee ID and Date of Joining of Employee and calculates the years of experience of the Employee

DELIMITER $$
CREATE procedure cal_Years_of_Exp( Empid INT, DOJ date, msg varchar(100))
BEGIN
DECLARE yoe int;
DECLARE val int;

set yoe=(select (year(curdate())-year(DOJ)) from Employee where Emp_ID=Empid);


set val=(SELECT Years_of_Exp from Employee WHERE Emp_ID=Empid);

IF val=0 THEN
   update Employee
   set Years_of_Exp=yoe
   where Emp_ID=Empid;
   set msg=concat('Years of Experience of Employee is=',yoe) ;
ELSE
    set msg='Years of experience already calculated' ;
END IF;

END$$
DELIMITER ; 

--Trigger
--Working Hours for a employee cannot be greater than 50 hours . 
--Have created a trigger which displays a warning message when working hours for a employee is updated for more than 50 hours .

DELIMITER $$
CREATE TRIGGER before_update_workson  
BEFORE UPDATE  
ON Works_On FOR EACH ROW  
BEGIN  
    DECLARE error_msg VARCHAR(255);  
    SET error_msg = ('The nworking hours  cannot be greater than 50 hours');  
    IF new.Work_Hours > 50 THEN  
    SIGNAL SQLSTATE '45000'   
    SET MESSAGE_TEXT = error_msg;  
    END IF;  
END $$   
DELIMITER ;
