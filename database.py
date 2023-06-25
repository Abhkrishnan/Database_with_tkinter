from tkinter import *
import sqlite3

root = Tk()
root.title('DATABASE')
root.geometry('400x400')

#Creating/ Connecting Database

conn = sqlite3.connect('Address_book.db')

#Create cursor
cursor = conn.cursor()

#Create Table

# cursor.execute(""" CREATE TABLE addresses ( 
#                 first_name text,
#                 last_name text,
#                 address text,
#                 city text,
#                 state text,
#                 zipcode integer)""")

#fUNTION To delete the reecord

def update():
    conn = sqlite3.connect('Address_book.db')

    #Create cursor
    cursor = conn.cursor()
    record_id = delete_box.get()
    cursor.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode

            WHERE oid = :oid""",

        {'first':f_name_editor.get(),
         'last':l_name_editor.get(),
         'address':address_editor.get(),
         'city': city_editor.get(),
         'state':state_editor.get(),   
         'zipcode':zipcode_editor.get(),
         'oid' : record_id

        })
    
    
    
    conn.commit()

    #Close Connection
    conn.close()
    editor.destroy()
    

def edit():
    global editor
    editor = Tk()
    editor.title('Update')
    editor.geometry('300x400')
    
    conn = sqlite3.connect('Address_book.db')

    #Create cursor
    cursor = conn.cursor()

    record_id = delete_box.get()
    cursor.execute("SELECT *,oid FROM addresses WHERE oid = "+record_id)

    #Loop through Results
    






    #cREATE Global variable for text box 
    global f_name_editor,l_name_editor,    address_editor,    city_editor,    state_editor,   zipcode_editor
  

    f_name_editor = Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))

    l_name_editor = Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)

    address_editor = Entry(editor,width=30)
    address_editor.grid(row=2,column=1)

    city_editor     = Entry(editor,width=30)
    city_editor.grid(row=3,column=1)

    state_editor = Entry(editor,width=30)
    state_editor.grid(row=4,column=1)

    zipcode_editor = Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1)



    #Text  box label

    f_nane_label = Label(editor,text='First Name')
    f_nane_label.grid(row=0,column=0,pady=(10,0))

    l_name_label = Label(editor,text='l_name')
    l_name_label.grid(row=1,column=0)

    address_label = Label(editor,text='address')
    address_label.grid(row=2,column=0)

    city_label = Label(editor,text='city')
    city_label.grid(row=3,column=0)

    State_label = Label(editor,text='State')
    State_label.grid(row=4,column=0)

    Zipcode_label = Label(editor,text='Zipcode')
    Zipcode_label.grid(row=5,column=0)

    submit_button = Button(editor,text= 'update',command=update)
    submit_button.grid(row=6,column = 0,columnspan=2,pady=10,padx=10,ipadx=134)

    
    records = cursor.fetchall()

    for record in records:
        f_name_editor.insert(0,record[0])


        l_name_editor.insert(0,record[1])


        address_editor.insert(0,record[2])
    
        city_editor.insert(0,record[3])


        state_editor.insert(0,record[4])
        
        zipcode_editor.insert(0,record[5])
  

    print(records)

    





    
     #Commit Changes
    conn.commit()

    #Close Connection
    conn.close()

 
def delete():
    conn = sqlite3.connect('Address_book.db')

    #Create cursor
    cursor = conn.cursor()

    #Delete a record
    
    cursor.execute("DELETE from addresses WHERE oid = " +delete_box.get())
   
    delete_box.delete(0,END)
    
    
    conn.commit()

    #Close Connection
    conn.close()


def submit():

    #Creating/ Connecting Database

    conn = sqlite3.connect('Address_book.db')

    #Create cursor
    cursor = conn.cursor()

    cursor.execute('INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)',
                   {'f_name':f_name.get(),
                    'l_name':l_name.get(),
                    'address':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'zipcode':zipcode.get()
                       

                   }


                   )


    
    #Commit Changes
    conn.commit()

    #Close Connection
    conn.close()

    #Clear the Text Box
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)


def query():
    conn = sqlite3.connect('Address_book.db')

    #Create cursor
    cursor = conn.cursor()


    cursor.execute("SELECT *,oid FROM addresses")

    records = cursor.fetchall()
    print(records)

    #Loop through Results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + "\t"+ str(record[-1]) + '\n'

    query_label = Label(root,text=print_records)
    query_label.grid(row=12,column=0,columnspan=2)






     #Commit Changes
    conn.commit()

    #Close Connection
    conn.close()


#Create text box
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))

l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)

address = Entry(root,width=30)
address.grid(row=2,column=1)

city     = Entry(root,width=30)
city.grid(row=3,column=1)

state = Entry(root,width=30)
state.grid(row=4,column=1)

zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1)

delete_box = Entry(root,width=10)
delete_box.grid(row=9,column=1)

#Text  box label

f_nane_label = Label(root,text='First Name')
f_nane_label.grid(row=0,column=0,pady=(10,0))

l_name_label = Label(root,text='l_name')
l_name_label.grid(row=1,column=0)

address_label = Label(root,text='address')
address_label.grid(row=2,column=0)

city_label = Label(root,text='city')
city_label.grid(row=3,column=0)

State_label = Label(root,text='State')
State_label.grid(row=4,column=0)

Zipcode_label = Label(root,text='Zipcode')
Zipcode_label.grid(row=5,column=0)

delete_btn_label = Label(root,text='SELECT ID')
delete_btn_label.grid(row=9,column=0)

# Create Submit Button
submit_button = Button(root,text= 'Add record to Database',command=submit)
submit_button.grid(row=6,column = 0,columnspan=2,pady=10,padx=10,ipadx=134)


#Create a Query Button

query_btn = Button(root,text='Show Records',command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=160)

#cREATE Delete textbox and Button


delete_btn = Button(root,text = 'Delete Record',command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=134)

#Create an Update button

delete_btn = Button(root,text = 'Update Record' ,command=edit)
delete_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=170)








root.mainloop()