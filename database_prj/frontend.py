import pymysql 
import admin as adm
import user as usr

con = pymysql.connect(host="localhost",user="root",password="",database="task1")

cur = con.cursor()

input_begin = int(input('''Press... 
                         1) If You Are Admin:  
                         2) If You Are User: 
                                   '''))

if input_begin == 1:
    a_email = input('Enter the Admin User Mail ID: ')
    a_pass = input('Enter the Admin User Password: ')

    qurey = f"select * from admin where email = '{a_email}' and password = '{a_pass}'"
    
    cur.execute(qurey)
    con.commit()

    row = cur.rowcount    
    
    if row > 0:
        while True:
            admin_choice = int(input('''Press....
                                     1) View All Users: 
                                     2) Genrate/Set Password: 
                                     3) View All User's Activitie's: 
                                     4) View All User's Completed Activitie's:  
                                     5) View All User's Pending Activitie's: 
                                                          '''))
            
            if admin_choice == 1:
                adm.all_user()

                retry = input('''
                      Want to continue " S "  
                      Other letters to stop: 
                                    ''').upper()
                
                if retry != "S":
                    break
                
            elif admin_choice == 2:
                adm.gen_password()
                
                retry = input('''
                      Want to continue " S "  
                      Other letters to stop: 
                                    ''').upper()
                
                if retry != "S":
                    break

            elif admin_choice == 3:
                adm.all_user_activity()
                
                retry = input('''
                      Want to continue " S "  
                      Other letters to stop: 
                                    ''').upper()
                
                if retry != "S":
                    break

            elif admin_choice == 4:
                adm.all_completed_activity()
                
                retry = input('''
                      Want to continue " S "  
                      Other letters to stop: 
                                    ''').upper()
                
                if retry != "S":
                    break

            elif admin_choice == 5:
                adm.all_pending_activity()
                
                retry = input('''
                      Want to continue " S "  
                      Other letters to stop: 
                                    ''').upper()
                
                if retry != "S":
                    break

            else:
                print("Please Select the Correct Option....")
                
                retry = input('''
                      Retry to press " S "  
                      Other letters to stop: 
                                    ''').upper()
                
                if retry != "S":
                    break
                
    else:
        print("You Are Not Admin")
        
elif input_begin == 2:
    user_choice = int(input('''Press...
                            1) New Registration: 
                            2) Log-in: 
                                    '''))
    
    if user_choice == 1:
        usr.register()

    elif user_choice == 2:
        u_mail = input('Enter User Mail ID: ')
        u_pass = input('Enter the User Password: ')

        qurey = f"select * from user where user_email = '{u_mail}' and user_password = '{u_pass}'"

        cur.execute(qurey)
        con.commit()
        
        row = cur.rowcount

        if row > 0:
            
            print()
            print('Login succesfully.......')
            
            while True:
                user_work = int(input('''Press....
                                      1) To Add a Activity: 
                                      2) Update Activity Status: 
                                      3) View All Activitie's:
                                      4) View All Completed Activitie's:
                                      5) View All Pending Activitie's:
                                      6) View Datewise Activity:
                                      7) Update User Password: 
                                                    '''))
                if user_work == 1:
                    usr.add_activity(u_mail)
                    
                    retry = input('''
                        Want to continue " S "  
                        Other letters to stop: 
                                        ''').upper()
                    
                    if retry != "S":
                        break
                    
                elif user_work == 2:
                    usr.update_activity(u_mail) 
                    
                    retry = input('''
                        Want to continue " S "  
                        Other letters to stop: 
                                        ''').upper()
                    
                    if retry != "S":
                        break
                                     
                elif user_work == 3:
                    usr.all_activity(u_mail) 
                    
                    retry = input('''
                        Want to continue " S "  
                        Other letters to stop: 
                                        ''').upper()
                    
                    if retry != "S":
                        break
                                    
                elif user_work == 4:
                    usr.completed_activity(u_mail)
                    
                    retry = input('''
                        Want to continue " S "  
                        Other letters to stop: 
                                        ''').upper()
                    
                    if retry != "S":
                        break
                    
                elif user_work == 5:
                    usr.pending_activity(u_mail)
                    
                    retry = input('''
                        Want to continue " S "  
                        Other letters to stop: 
                                        ''').upper()
                    
                    if retry != "S":
                        break
                    
                elif user_work == 6:
                    usr.datewise_activity(u_mail)
                    
                    retry = input('''
                        Want to continue " S "  
                        Other letters to stop: 
                                        ''').upper()
                    
                    if retry != "S":
                        break
                    
                elif user_work == 7:
                    usr.update_password(u_mail)
                    
                    if u_pass == usr.old_pass :
                        print("Password Updated Succesfully")
                    else:
                        print(f"Old Password is not linked with entered {u_mail}....")
    
                    
                    retry = input('''
                        Want to continue " S "  
                        Other letters to stop: 
                                        ''').upper()
                    
                    if retry != "S":
                        break
                    
                else:
                    print("Please Select the Correct Option")
                    
                    retry = input('''
                        Want to continue " S "  
                        Other letters to stop: 
                                        ''').upper()
                    
                    if retry != "S":
                        break
                            
        else:
            print("You Don't Have a Account")
    else:
        print("Please Choose the Correct Option")     
else:
    print("Please Choose the Correct Option")
    

con.close()
