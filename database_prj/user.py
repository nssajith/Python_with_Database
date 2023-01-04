import pymysql
from prettytable import PrettyTable
from datetime import date

con = pymysql.connect(host='localhost',user='root',password='',database='task1')

cur = con.cursor()

'''--------------------------------------------- Register -------------------------------------------'''

def register():

    u_name = input("Enter the User Name: ")
    u_mail = input("Enter the User Mail ID: ")
    u_phone =int(input("Enter the User Phone Number: "))
   
    query = f"insert into user(user_name,user_email,user_phone,user_password) values('{u_name}','{u_mail}','{u_phone}','{''}')"

    cur.execute(query)
    con.commit()
    
    print('Account Registered Succesfully')

    print('---------------------------------------------------------------------')

############################################################################################################################################   
    
'''--------------------------------------------- Add_activity -------------------------------------------'''

def add_activity(u_mail):
    a_name = input("Enter the Activity Name: ")
    a_desc = input("Enter the Activity Desc: ")

    today = date.today()
    a_date = today.strftime('%d/%m/20%y')
    
    qurey = f"insert into activity(activity_name,activity_desc,activity_date,activity_done_by) values('{a_name}','{a_desc}','{a_date}','{u_mail}')"
    
    cur.execute(qurey)
    con.commit()
    
    print("Activity added Succesfully")

    print('---------------------------------------------------------------------')
 
 
 
  
'''--------------------------------------------- Update_activity -------------------------------------------'''

def update_activity(u_mail):
    
    a_desc = input("Enter the (Activity Name) or (Activity ID): ")

    qurey = f"update activity set status = 'Completed' where (activity_done_by = '{u_mail}' and activity_name = '{a_desc}') or (activity_done_by= '{u_mail}' and activity_id = '{a_desc}')"

    check = cur.execute(qurey)
    con.commit()
    if  check:
        print('Status updated')
    else:
        print(f'" {a_desc.capitalize()} " is not in " {u_mail} " or Already status -> " COMPLETED "')    

    print('---------------------------------------------------------------------')



'''--------------------------------------------- All_activity -------------------------------------------'''

def all_activity(u_mail):

    qurey = f"select * from activity where activity_done_by = '{u_mail}'"
     
    cur.execute(qurey)

    con.commit()
    rows = cur.rowcount

    pt = PrettyTable()
    pt.field_names = ('activity_id','activity_name','activity_desc','activity_date','activity_done_by','status')

    if rows > 0:

        for row in cur.fetchall():
             pt.add_row(row)
    
        print(pt)

    else:
        print("Record Not Found")
        
    print('---------------------------------------------------------------------')



'''--------------------------------------------- Completed_activity -------------------------------------------'''

def completed_activity(u_mail):


    qurey= f"select * from activity where activity_done_by = '{u_mail}' and status = 'Completed'"

    cur.execute(qurey)

    con.commit()

    row = cur.rowcount

    pt = PrettyTable()
    pt.field_names = ('activity_id','activity_name','activity_desc','activity_date','activity_done_by','status')

    if row > 0:
        for rows in cur.fetchall():
            pt.add_row(rows)

        print(pt)

    else:
        print("You Haven't  Completed any Activities")
        
    print('---------------------------------------------------------------------')



'''--------------------------------------------- Pending_activity -------------------------------------------'''

def pending_activity(u_mail):

    qurey= f"select * from activity where activity_done_by = '{u_mail}' and status = 'Not Completed'"

    cur.execute(qurey)

    con.commit()

    row = cur.rowcount

    pt = PrettyTable()
    pt.field_names = ('activity_id','activity_name','activity_desc','activity_date','activity_done_by','status')

    if row > 0:
        for rows in cur.fetchall():
            pt.add_row(rows)

        print(pt)
    else:
        print("All  Activities Are Completed")
        
    print('---------------------------------------------------------------------')
    


'''--------------------------------------------- Datewise_activity -------------------------------------------'''
def datewise_activity(u_mail):
    
    check_date = input('Enter a date (00): ')
    check_month = input('Enter a month (00): ')
    check_year = input('Enter a year (1999): ')
    
    check = f'{check_date}/{check_month}/{check_year}'
    
    qurey= f"select * from activity where activity_done_by = '{u_mail}' and activity_date = '{check}'"

    cur.execute(qurey)

    con.commit()

    row = cur.rowcount

    pt = PrettyTable()
    pt.field_names = ('activity_id','activity_name','activity_desc','activity_date','activity_done_by','status')

    if row > 0:
        for rows in cur.fetchall():
            pt.add_row(rows)

        print(pt)
    else:
        print(f"With this {u_mail} no data entered at {check}")
        
    print('---------------------------------------------------------------------')
    


'''--------------------------------------------- Update_password -------------------------------------------'''

def update_password(u_mail):
    global old_pass
    old_pass =input("Enter the Old Password: ")
    new_pass = input("Enter the New Password: ")

    qurey = f"update user set user_password = '{new_pass}' where user_email = '{u_mail}' and user_password = '{old_pass}'"

    cur.execute(qurey)

    con.commit()
    
    print('---------------------------------------------------------------------')


    