import psycopg2

# connection to the database
con = psycopg2.connect(host="localhost",user="postgres",password="postgres",port=5432,database="admin_dashboard_db")
# creating cursor 
cur = con.cursor()

#creating Employee table
emp_query = "create table emp_table(e_id varchar(20) primary key,emp_name varchar(20),desig_id varchar(20),email varchar(50),host varchar(50),user_name varchar(50),password varchar(50),assigned_sw varchar(50000),used_sw varchar(50000),invalid_sw varchar(50000),cpu varchar(5000),ram varchar(5000))"
cur.execute(emp_query)
con.commit()

#creating desiganations table
desig_query = "create table designations_table(desg_id varchar(50) primary key,desig_name varchar(50),assigned_sw varchar(50000))"
cur.execute(desig_query)
con.commit()

#Creating softwares table
query="create table softwares_table(sw_id varchar(50) primary key,sw_name varchar(50),lic_no varchar(50),exp_date varchar(50))"
cur.execute(query)
con.commit()


'''
#creating valid softwares table
valid_softwares_query = "create table valid_softwares_table(software_id varchar(10) primary key, software_name varchar(50),license_number varchar(50),expiry_date date)"
cur.execute(valid_softwares_query)
con.commit()

#creating Team table
team_query="create table team_table(team_id varchar(20),team_name varchar(50),eid varchar(50),software_id varchar(50))"
cur.execute(team_query)
con.commit()
'''
