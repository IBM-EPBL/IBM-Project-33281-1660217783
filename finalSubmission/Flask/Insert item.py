def add_to_cart(self,*args,**kwargs):
    self.quantity_value=int(self.quantity_e.get())

    if  self .quantity_value >int(self.get_stock):
        tkinter.messagebox.showinfo("Error","Not that any products in our stock.")
    else:
        #calculate the price first
        self.final_price=(float(self.quantity_value) * float(self.get_price))-(float(self.discount_e.get()))
        products_list.append(self.get_name)
        product_price.append(self.final_price)
        product_quantity.append(self.quantity_value)
        product_id.append(self.get_id)

        self.x_index=0
        self.y_index=100
        self.counter=0
        for self.p in products_list:
            self.tempname=Label(self.right,text=str(products_list[self.counter]),font=('arial 18 bold'),bg='gray',fg='white')
            self.tempname.place(x=0,y=self.y_index)
            self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg='gray', fg='white')
            self.tempqt.place(x=150, y=self.y_index)
            self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), bg='gray', fg='white')
            self.tempprice.place(x=300, y=self.y_index)

            self.y_index+=40
            self.counter+=1


            #total confugure
            self.total_l.configure(text="Final amount=Rs. "+str(sum(product_price)),bg='gray',fg='white',font=('20'))
            self.total_l.place(x=180,y=450)
            #delete
            self.quantity_e.place_forget()
            self.discount_l.place_forget()
            self.discount_e.place_forget()
            self.productname.configure(text="")
            self.pprice.configure(text="")
            self.add_to_cart_btn.destroy()
            #autofocus to the enter id
            self.enteride.focus()
            self.quantityl.focus()
            self.enteride.delete(0,END)

def change_func(self,*args,**kwargs):
    self.amount_given=float(self.change_e.get())
    self.our_total=float(sum(product_price))

    self.to_give=self.amount_given-self.our_total

    #label change
    self.c_amount=Label(self.left,text="Change is Rs. "+str(self.to_give),font=('Calibri 20 bold'),fg='Black',bg='white')
    self.c_amount.place(x=0 ,y=500)

def generate_bill(self,*args,**kwargs):
    self.mycursor.execute("SELECT * FROM inventory WHERE id=%s",[self.get_id])
    self.pc = self.mycursor.fetchall()
    for r in self.pc:
        self.old_stock=r[2]
    for i in products_list:
        for r in self.pc:
            self.old_stock = r[2]
        self.new_stock=int(self.old_stock) - int(self.quantity_value)
        #updating the stock
        self.mycursor.execute("UPDATE inventory SET stock=%s WHERE id=%s",[self.new_stock,self.get_id])
        self.conn.commit()

        #inster into transcation
        self.mycursor.execute("INSERT INTO transaction (product_name,quantity,amount,date) VALUES(%s,%s,%s,%s)",[self.get_name,self.quantity_value,self.get_price,date])
        self.conn.commit()
        print("Decreased")

    tkinter.messagebox.showinfo("successfully done")