class Database:
    def __init__(self,master,*args,**kwargs):
         self.master=master
         self.heading=Label(master,text="Add the Details in Database",font=('arial 40 bold'),fg='Red')
         self.heading.place(x=250,y=0)


         #lables  for the window
         self.name_l=Label(master,text="Whats the product",font=('Calibri 20 bold'))
         self.name_l.place(x=0,y=100)

         self.stock_l=Label(master,text="What are the stocks",font=('Calibri 20 bold'))
         self.stock_l.place(x=0,y=180)

         self.cp_l = Label(master, text="Please enter the price ", font=('Calibri 20 bold'))
         self.cp_l.place(x=0, y=260)


        #enteries for window

         self.name_e=Entry(master,width=25,font=('Calibri 20 bold'))
         self.name_e.place(x=380,y=100)

         self.stock_e = Entry(master, width=25, font=('Calibri 20 bold'))
         self.stock_e.place(x=380, y=180)

         self.cp_e = Entry(master, width=25, font=('Calibri 20 bold'))
         self.cp_e.place(x=380, y=260)

         #button to add to the database
         self.btn_add=Button(master,text='Update the database',width=30,height=3,bg='Lightgreen',fg='Black',command=self.get_items,font=2)
         self.btn_add.place(x=800,y=100)

         self.btn_clear=Button(master,text="Reset the fields",width=30,height=3,bg='Orange',fg='Black',command=self.clear_all,font=2)
         self.btn_clear.place(x=800,y=180)

          #text box for the log
         self.tbBox=Text(master,width=50,height=10)
         self.tbBox.place(x=50,y=420)
         self.tbBox.insert(END,"ID number:"+str(id))

         self.master.bind('<Return>', self.get_items)
         self.master.bind('<Up>', self.clear_all)

Explanation:

The class Database: Here we create the layout of the database tabl