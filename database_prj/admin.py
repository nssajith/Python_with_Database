from prettytable import PrettyTable
import pymysql
import pywhatkit,string,random

con = pymysql.connect(host="localhost",user="root",password="",database="task1")
cur = con.cursor()

'''--------------------------------------------- all_users -------------------------------------------'''

def all_user():
    qurey= f"select * from user"

    cur.execute(qurey)
    con.commit()
    
    row = cur.rowcount

    pt = PrettyTable()
    pt.field_names = ('user_id','user_name','user_email','user_phone','user_password')

    if row > 0:
        for rows in cur.fetchall():
            pt.add_row(rows)
        print(pt)
        
    print('----------------------------------')

'''--------------------------------------------- gen_pass -------------------------------------------'''

def gen_password():

    letter = string.ascii_letters
    digital = string.digits
    ip = letter + digital
    otp = random.sample(ip,6)
    a_otp = "".join(otp)

    get_value = input("Enter the (User Phone Number) or (User ID): ")

    query = f"select user_phone from user where user_id = '{get_value}' or user_phone = '{get_value}'" 
    
    cur.execute(query)
    con.commit()
    
    row = cur.rowcount
    
    if row >0:
        
        list_num = []
        
        fetch_num = cur.fetchall()
        
        for num in fetch_num :
            list_num.append(*num)
    
        pywhatkit.sendwhatmsg_instantly(f"+91{list_num[0]}",f'Hi this message is to inform You that your TO-DO list Account User-Password is "{a_otp}"')
        
        qurey= f'update user set user_password ="{a_otp}" where user_phone = "{list_num[0]}"'
        
        cur.execute(qurey)
        con.commit()
        
        print()
        print("Password Set Succesfully")

    else:
        print(f"User Account of User Phone Number or User ID : {get_value} Has Not Found")
    
    print('-----------------------------------')

'''--------------------------------------------- all_user_activity -------------------------------------------'''

def all_user_activity():
    
    qurey = f"select * from activity"

    cur.execute(qurey)
    con.commit()

    row = cur.rowcount
    pt =PrettyTable()
    pt.field_names = ('activity_id','activity_name','activity_desc','activity_date','activity_done_by','status')

    if row > 0:
        for rows in cur.fetchall():
            pt.add_row(rows)

        print(pt)
        
    print('-------------------------------')

'''--------------------------------------------- all_completed_activity -------------------------------------------'''

def all_completed_activity():
    qurey= f"select * from activity where status = 'Completed'"
    
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
        print("Completed Activitie's Not Found")
        
    print('------------------------------')

'''--------------------------------------------- all_pending_activity -------------------------------------------'''

def all_pending_activity():
    qurey = f"select * from activity where status = 'Not Completed'"
    
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
        print("Pending Activitie's Are not Found")

    print('------------------------------')
    
