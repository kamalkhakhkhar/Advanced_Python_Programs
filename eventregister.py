from tkinter import *
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry('400x500')
  
# Information List
datas = []
  
# Add Information
def addEvent():
    global datas
    datas.append([Name.get(),Number.get(),address.get(1.0, "end-1c")])
    update_book()
  
# View Information
def viewEvent():
    Name.set(datas[int(select.curselection()[0])][0])
    Number.set(datas[int(select.curselection()[0])][1])
    address.delete(1.0,"end")
    address.insert(1.0, datas[int(select.curselection()[0])][2])
  
# Delete Information
def deleteEvent():
    del datas[int(select.curselection()[0])]
    update_book()
    
# Reset information
def resetColumn():
    Name.set('')
    Number.set('')
    address.delete(1.0,"end")
  
# Update Information
def update_book():
    select.delete(0,END)
    for n,p,a in datas:
        select.insert(END, n)
  
# Add Buttons, Label, ListBox
Name = StringVar()
Number = StringVar()
  
frame = Frame()
frame.pack(pady=10)
  
frame1 = Frame()
frame1.pack()
  
frame2 = Frame()
frame2.pack(pady=10)
  
Label(frame, text = 'Event Name', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = Name,width=50).pack()
  
Label(frame1, text = 'Phone No.', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = Number,width=50).pack()
  
Label(frame2, text = 'Address', font='arial 12 bold').pack(side=LEFT)
address = Text(frame2,width=37,height=10)
address.pack()
  
Button(root,text="Register Event",font="arial 12 bold",command=addEvent).place(x= 100, y=270)
Button(root,text="View Event",font="arial 12 bold",command=viewEvent).place(x= 100, y=310)
Button(root,text="Cancel Event",font="arial 12 bold",command=deleteEvent).place(x= 100, y=350)
Button(root,text="Reset",font="arial 12 bold",command=resetColumn).place(x= 100, y=390)
  
scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)
  
# Execute Tkinter
root.mainloop()
