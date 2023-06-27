import customtkinter
from images import Images

def grid_frames(obj):
        # add product
    obj.add_product_frame=customtkinter.CTkFrame(obj.second_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

    obj.add_product_label1=customtkinter.CTkLabel(obj.add_product_frame,
                                                    fg_color="transparent",
                                                    anchor="center",
                                                    text=" Add Product",
                                                    font=("Bold",20),
                                                    corner_radius=3,
                                                    image=Images().add_product_image50,
                                                    compound="top")
    obj.add_product_label1.grid(row=0,column=0,columnspan=5,padx=20,pady=10)

    obj.add_product_entry1=customtkinter.CTkEntry(obj.add_product_frame,placeholder_text="Product",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.add_product_entry1.grid(row=1,column=0,columnspan=5,padx=20,pady=5)

    obj.add_product_entry2=customtkinter.CTkEntry(obj.add_product_frame,placeholder_text="Cost",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.add_product_entry2.grid(row=2,column=0,padx=10,pady=5)

    obj.add_product_entry3=customtkinter.CTkEntry(obj.add_product_frame,placeholder_text="Price",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.add_product_entry3.grid(row=2,column=1,padx=10,pady=5)

    obj.add_product_entry4=customtkinter.CTkEntry(obj.add_product_frame,placeholder_text="Quantity",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.add_product_entry4.grid(row=3,column=0,columnspan=5,padx=20,pady=5)

    obj.add_product_entry5=customtkinter.CTkEntry(obj.add_product_frame,placeholder_text="Category",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.add_product_entry5.grid(row=4,column=0,columnspan=5,padx=20,pady=5)

    obj.add_product_button=customtkinter.CTkButton(obj.add_product_frame,
                                                    image=Images().add_button_image,
                                                    text="Add",
                                                    compound="left",
                                                    font=("Bold",15),
                                                    fg_color=obj.default_color,
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    command=obj.add_product)
    obj.add_product_button.grid(row=5,column=0,columnspan=5,padx=20,pady=5)

    # update price
    obj.update_price_frame=customtkinter.CTkFrame(obj.second_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

    obj.update_price_frame_label1=customtkinter.CTkLabel(obj.update_price_frame,
                                                            fg_color="transparent",
                                                            anchor="center",
                                                            text=" Update Price",
                                                            font=("Bold",20),
                                                            corner_radius=3,
                                                            image=Images().update_price_image50,
                                                            compound="top")
    obj.update_price_frame_label1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

    obj.update_price_frame_entry1=customtkinter.CTkEntry(obj.update_price_frame,placeholder_text="Product",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.update_price_frame_entry1.grid(row=1,column=0,padx=5,pady=5)

    obj.update_price_frame_entry2=customtkinter.CTkEntry(obj.update_price_frame,placeholder_text="Cost",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.update_price_frame_entry2.grid(row=2,column=0,columnspan=5,padx=5,pady=5)

    obj.update_price_frame_entry3=customtkinter.CTkEntry(obj.update_price_frame,placeholder_text="Price",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.update_price_frame_entry3.grid(row=3,column=0,columnspan=5,padx=5,pady=5)
    
    obj.update_price_frame_optionmenu1Var=customtkinter.StringVar(obj.update_price_frame,value="Select Product")
    obj.update_price_frame_optionmenu1=customtkinter.CTkOptionMenu(obj.update_price_frame,
                                                                    values=[x.name for x in obj.products]if len(obj.products)!=0 else [],
                                                                    fg_color=obj.default_color,
                                                                    text_color=("gray10", "gray90"),
                                                                    button_color=obj.default_color,
                                                                    button_hover_color=("gray70", "gray30"),
                                                                    command=obj.update_price_name_event,
                                                                    variable=obj.update_price_frame_optionmenu1Var
                                                                    )
    obj.update_price_frame_optionmenu1.grid(row=1,column=1,padx=5,pady=5)

    obj.update_price_frame_button=customtkinter.CTkButton(obj.update_price_frame,
                                                            image=Images().save_changes_image,
                                                            text="Update",
                                                            compound="left",
                                                            font=("Bold",15),
                                                            fg_color=obj.default_color,
                                                            text_color=("gray10", "gray90"),
                                                            hover_color=("gray70", "gray30"),
                                                            command=obj.update_price)
    obj.update_price_frame_button.grid(columnspan=5,padx=5,pady=5)

    # edit product
    obj.edit_product_frame=customtkinter.CTkFrame(obj.second_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

    obj.edit_product_frame_label1=customtkinter.CTkLabel(obj.edit_product_frame,
                                                            fg_color="transparent",
                                                            anchor="center",
                                                            text=" Edit Product",
                                                            font=("Bold",20),
                                                            corner_radius=3,
                                                            image=Images().edit_image50,
                                                            compound="top")
    obj.edit_product_frame_label1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

    obj.edit_product_frame_entry1=customtkinter.CTkEntry(obj.edit_product_frame,placeholder_text="Name",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.edit_product_frame_entry1.grid(row=1,column=0,padx=5,pady=5)

    obj.edit_product_frame_entry2=customtkinter.CTkEntry(obj.edit_product_frame,placeholder_text="Cost",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.edit_product_frame_entry2.grid(row=2,column=0,padx=5,pady=5)

    obj.edit_product_frame_entry3=customtkinter.CTkEntry(obj.edit_product_frame,placeholder_text="Price",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.edit_product_frame_entry3.grid(row=2,column=1,padx=5,pady=5)

    obj.edit_product_frame_entry4=customtkinter.CTkEntry(obj.edit_product_frame,placeholder_text="Quantity",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.edit_product_frame_entry4.grid(row=3,column=0,columnspan=5,padx=5,pady=5)

    obj.edit_product_frame_entry5=customtkinter.CTkEntry(obj.edit_product_frame,placeholder_text="Category",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.edit_product_frame_entry5.grid(row=4,column=0,columnspan=5,padx=5,pady=5)

    obj.edit_product_frame_id=None
    obj.edit_product_frame_optionmenu1Var=customtkinter.StringVar(obj.edit_product_frame,value="Choose Product")
    obj.edit_product_frame_optionmenu1=customtkinter.CTkOptionMenu(obj.edit_product_frame,
                                                                    values=[x.name for x in obj.products]if len(obj.products)!=0 else [],
                                                                    fg_color=obj.default_color,
                                                                    text_color=("gray10", "gray90"),
                                                                    button_color=obj.default_color,
                                                                    button_hover_color=("gray70", "gray30"),
                                                                    command=obj.edit_product_name_event,
                                                                    variable=obj.edit_product_frame_optionmenu1Var,
                                                                    )
    obj.edit_product_frame_optionmenu1.grid(row=1,column=1,padx=5,pady=5)

    obj.edit_product_frame_button=customtkinter.CTkButton(obj.edit_product_frame,
                                                            image=Images().save_changes_image,
                                                            text="Save Changes",
                                                            compound="left",
                                                            font=("Bold",15),
                                                            fg_color=obj.default_color,
                                                            text_color=("gray10", "gray90"),
                                                            hover_color=("gray70", "gray30"),
                                                            command=obj.edit_product)
    obj.edit_product_frame_button.grid(row=5,columnspan=5,padx=5,pady=5)
    # add client
    obj.add_client_frame=customtkinter.CTkFrame(obj.third_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

    obj.add_client_label1=customtkinter.CTkLabel(obj.add_client_frame,
                                                    fg_color="transparent",
                                                    anchor="center",
                                                    text=" Add Client",
                                                    font=("Bold",20),
                                                    corner_radius=3,
                                                    image=Images().add_user_image50,
                                                    compound="top")
    obj.add_client_label1.grid(row=0,column=0,columnspan=5,padx=20,pady=10)

    obj.add_client_entry1=customtkinter.CTkEntry(obj.add_client_frame,placeholder_text="Client",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.add_client_entry1.grid(row=1,column=0,columnspan=5,padx=20,pady=5)

    obj.add_client_entry2=customtkinter.CTkEntry(obj.add_client_frame,placeholder_text="Phone",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.add_client_entry2.grid(row=2,column=0,columnspan=5,padx=20,pady=5)

    obj.add_client_entry3=customtkinter.CTkEntry(obj.add_client_frame,placeholder_text="Address",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.add_client_entry3.grid(row=3,column=0,columnspan=5,padx=20,pady=5)

    obj.add_client_button=customtkinter.CTkButton(obj.add_client_frame,
                                                    image=Images().add_button_image,
                                                    text="Add",
                                                    compound="left",
                                                    font=("Bold",15),
                                                    fg_color=obj.default_color,
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    command=obj.add_client)
    obj.add_client_button.grid(row=5,column=0,columnspan=5,padx=20,pady=5)

    # edit client
    obj.edit_client_frame=customtkinter.CTkFrame(obj.third_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

    obj.edit_client_frame_label1=customtkinter.CTkLabel(obj.edit_client_frame,
                                                            fg_color="transparent",
                                                            anchor="center",
                                                            text=" Edit Client",
                                                            font=("Bold",20),
                                                            corner_radius=3,
                                                            image=Images().edit_image50,
                                                            compound="top")
    obj.edit_client_frame_label1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

    obj.edit_client_frame_entry1=customtkinter.CTkEntry(obj.edit_client_frame,placeholder_text="Name",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.edit_client_frame_entry1.grid(row=1,column=0,padx=5,pady=5)

    obj.edit_client_frame_entry2=customtkinter.CTkEntry(obj.edit_client_frame,placeholder_text="Phone",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.edit_client_frame_entry2.grid(row=2,column=0,columnspan=5,padx=5,pady=5)

    obj.edit_client_frame_entry3=customtkinter.CTkEntry(obj.edit_client_frame,placeholder_text="Address",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.edit_client_frame_entry3.grid(row=3,column=0,columnspan=5,padx=5,pady=5)
    
    obj.edit_client_frame_id=None
    obj.edit_client_frame_optionmenu1Var=customtkinter.StringVar(obj.edit_client_frame,value="Client Name")
    obj.edit_client_frame_optionmenu1=customtkinter.CTkOptionMenu(obj.edit_client_frame,
                                                                    values=[x.name for x in obj.clients]if len(obj.clients)!=0 else [],
                                                                    fg_color=obj.default_color,
                                                                    text_color=("gray10", "gray90"),
                                                                    button_color=obj.default_color,
                                                                    button_hover_color=("gray70", "gray30"),
                                                                    command=obj.edit_client_name_event,
                                                                    variable=obj.edit_client_frame_optionmenu1Var,
                                                                    )
    obj.edit_client_frame_optionmenu1.grid(row=1,column=1,padx=5,pady=5)

    obj.edit_client_frame_button=customtkinter.CTkButton(obj.edit_client_frame,
                                                            image=Images().save_changes_image,
                                                            text="Save Changes",
                                                            compound="left",
                                                            font=("Bold",15),
                                                            fg_color=obj.default_color,
                                                            text_color=("gray10", "gray90"),
                                                            hover_color=("gray70", "gray30"),
                                                            command=obj.edit_client)
    obj.edit_client_frame_button.grid(columnspan=5,padx=5,pady=5)

def grid_employee_list(obj,db,keyword):
    obj.employees=db.getEmployees()
    obj.employee_list_scrollable_frame=customtkinter.CTkScrollableFrame(obj.fourth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
    obj.employee_list_scrollable_frame.grid_columnconfigure(7,weight=1)

    obj.employee_list_scrollable_frame_label1=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text="ID",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.employee_list_scrollable_frame_label2=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text="Name",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.employee_list_scrollable_frame_label3=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text="Phone",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.employee_list_scrollable_frame_label4=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text="Email",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.employee_list_scrollable_frame_label5=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text="Username",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.employee_list_scrollable_frame_label6=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text="Password",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

    obj.employee_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
    obj.employee_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
    obj.employee_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
    obj.employee_list_scrollable_frame_label4.grid(row=0,column=3,padx=5,pady=5)
    obj.employee_list_scrollable_frame_label5.grid(row=0,column=8,padx=5,pady=5)
    obj.employee_list_scrollable_frame_label6.grid(row=0,column=9,padx=5,pady=5)
    
    if len(obj.employees)!=0:
        if keyword is not None:
            obj.employees=db.getEmployeesByName(keyword)
            
        k=1
        for i in obj.employees:
            lbl1=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text=i.id,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl2=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text=i.name,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl3=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text=i.phone,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl4=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text=i.email,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl5=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text=i.username,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl6=customtkinter.CTkLabel(obj.employee_list_scrollable_frame,text=i.password,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

            lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
            lbl2.grid(row=k,column=1,padx=5,pady=5)
            lbl3.grid(row=k,column=2,padx=5,pady=5)
            lbl4.grid(row=k,column=3,padx=5,pady=5)
            lbl5.grid(row=k,column=8,padx=5,pady=5)
            lbl6.grid(row=k,column=9,padx=5,pady=5)
            k+=1

def grid_product_list(obj,db,keyword):
    obj.products=db.getProducts()
    obj.product_list_scrollable_frame=customtkinter.CTkScrollableFrame(obj.second_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
    obj.product_list_scrollable_frame.grid_columnconfigure(7,weight=1)
    
    obj.product_list_scrollable_frame_label1=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text="ID",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.product_list_scrollable_frame_label2=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text="Product Name",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.product_list_scrollable_frame_label3=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text="Product Cost",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.product_list_scrollable_frame_label4=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text="Product Price",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.product_list_scrollable_frame_label5=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text="Category",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.product_list_scrollable_frame_label6=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text="Quantity",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

    obj.product_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5)
    obj.product_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
    obj.product_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
    obj.product_list_scrollable_frame_label4.grid(row=0,column=3,padx=5,pady=5)
    obj.product_list_scrollable_frame_label5.grid(row=0,column=4,padx=5,pady=5)
    obj.product_list_scrollable_frame_label6.grid(row=0,column=9,padx=5,pady=5,sticky="e")

    if len(obj.products)!=0:
        if keyword is not None:
            obj.products=db.getProductsByName(keyword)
        k=1
        for i in obj.products:
            lbl1=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text=i.id,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl2=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text=i.name,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl3=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text=f"{i.cost}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl4=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text=f"{i.price}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl5=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text=i.category,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl6=customtkinter.CTkLabel(obj.product_list_scrollable_frame,text=i.quantity,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

            lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
            lbl2.grid(row=k,column=1,padx=5,pady=5)
            lbl3.grid(row=k,column=2,padx=5,pady=5)
            lbl4.grid(row=k,column=3,padx=5,pady=5)
            lbl5.grid(row=k,column=4,padx=5,pady=5)
            lbl6.grid(row=k,column=9,padx=5,pady=5,sticky="e")
            k+=1

def grid_client_list(obj,db,keyword):
    obj.clients=db.getClients()
    obj.client_list_scrollable_frame=customtkinter.CTkScrollableFrame(obj.third_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
    obj.client_list_scrollable_frame.grid_columnconfigure(7,weight=1)

    obj.client_list_scrollable_frame_label1=customtkinter.CTkLabel(obj.client_list_scrollable_frame,text="ID",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.client_list_scrollable_frame_label2=customtkinter.CTkLabel(obj.client_list_scrollable_frame,text="Name",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.client_list_scrollable_frame_label3=customtkinter.CTkLabel(obj.client_list_scrollable_frame,text="Phone",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.client_list_scrollable_frame_label4=customtkinter.CTkLabel(obj.client_list_scrollable_frame,text="Address",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

    obj.client_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
    obj.client_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
    obj.client_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
    obj.client_list_scrollable_frame_label4.grid(row=0,column=9,padx=5,pady=5)
    
    if len(obj.clients) !=0:
        if keyword is not None:
            obj.clients=db.getClientsByName(keyword)

        k=1
        for i in obj.clients:
            lbl1=customtkinter.CTkLabel(obj.client_list_scrollable_frame,text=i.id,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl2=customtkinter.CTkLabel(obj.client_list_scrollable_frame,text=i.name,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl3=customtkinter.CTkLabel(obj.client_list_scrollable_frame,text=i.phone,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl4=customtkinter.CTkLabel(obj.client_list_scrollable_frame,text=i.address,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

            lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
            lbl2.grid(row=k,column=1,padx=5,pady=5)
            lbl3.grid(row=k,column=2,padx=5,pady=5)
            lbl4.grid(row=k,column=9,padx=5,pady=5)
            k+=1

def grid_history_list(obj,db,keyword):
    obj.history=db.getLatestProductsSold()
    obj.history_list_scrollable_frame=customtkinter.CTkScrollableFrame(obj.fifth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
    obj.history_list_scrollable_frame.grid_columnconfigure(7,weight=1)

    def calculate_profit():
        totalProfit=0.0
        for i in obj.history:
            totalProfit+=i[-1]
        return totalProfit
    
    totalProfit=calculate_profit()
    obj.history_list_scrollable_frame_label1=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text="Sold Date",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_list_scrollable_frame_label2=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text="Product",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_list_scrollable_frame_label3=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text="Cost",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_list_scrollable_frame_label4=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text="Price",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_list_scrollable_frame_label5=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text="Quantity",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_list_scrollable_frame_label6=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text="Sold To",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_list_scrollable_frame_label7=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text="Sold By",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_list_scrollable_frame_label8=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text=f"Total Profit\n{totalProfit}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    
    obj.history_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
    obj.history_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
    obj.history_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
    obj.history_list_scrollable_frame_label4.grid(row=0,column=3,padx=5,pady=5)
    obj.history_list_scrollable_frame_label5.grid(row=0,column=4,padx=5,pady=5)
    obj.history_list_scrollable_frame_label6.grid(row=0,column=5,padx=5,pady=5)
    obj.history_list_scrollable_frame_label7.grid(row=0,column=6,padx=5,pady=5)
    obj.history_list_scrollable_frame_label8.grid(row=0,column=9,padx=5,pady=5,sticky="e")

    if len(obj.history)!=0:
        if keyword is not None:
            obj.history=db.getHistoryByDate(keyword)
            totalProfit=calculate_profit()
            obj.history_list_scrollable_frame_label8.configure(text=f"Total Profit\n{totalProfit}£")
        k=1
        for i in obj.history:
            lbl1=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text=i[0],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl2=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text=i[1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl3=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text=f"{i[2]}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl4=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text=f"{i[3]}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl5=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text=i[4],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl6=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text=i[5],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl7=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text=i[6],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl8=customtkinter.CTkLabel(obj.history_list_scrollable_frame,text=f'{i[-1]}£',fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

            lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
            lbl2.grid(row=k,column=1,padx=5,pady=5)
            lbl3.grid(row=k,column=2,padx=5,pady=5)
            lbl4.grid(row=k,column=3,padx=5,pady=5)
            lbl5.grid(row=k,column=4,padx=5,pady=5)
            lbl6.grid(row=k,column=5,padx=5,pady=5)
            lbl7.grid(row=k,column=6,padx=5,pady=5)
            lbl8.grid(row=k,column=9,padx=5,pady=5,sticky="e")
            k+=1

def grid_history_lists(obj,db):
    obj.history_products=db.getHistoryProducts()
    obj.history_clients=db.getTopCustomers()
    obj.history_employees=db.getTopSellingEmployees()
    obj.history_product_list_scrollable_frame=customtkinter.CTkScrollableFrame(obj.fifth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
    obj.history_product_list_scrollable_frame.grid_columnconfigure(4,weight=1)
    
    obj.history_product_list_scrollable_frame_label1=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text="Product",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_product_list_scrollable_frame_label2=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text="Cost",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_product_list_scrollable_frame_label3=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text="Price",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_product_list_scrollable_frame_label4=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text="Total Sold",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_product_list_scrollable_frame_label5=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text="Total Profit",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

    obj.history_product_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
    obj.history_product_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
    obj.history_product_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
    obj.history_product_list_scrollable_frame_label4.grid(row=0,column=3,padx=5,pady=5,sticky="e")
    obj.history_product_list_scrollable_frame_label5.grid(row=0,column=4,padx=5,pady=5,sticky="e")

    if len(obj.history_products)!=0:
        k=1
        for i in obj.history_products:
            lbl1=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text=i[1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl2=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text=f"{i[2]}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl3=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text=f"{i[3]}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl4=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text=i[5],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl5=customtkinter.CTkLabel(obj.history_product_list_scrollable_frame,text=i[4],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

            lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
            lbl2.grid(row=k,column=1,padx=5,pady=5)
            lbl3.grid(row=k,column=2,padx=5,pady=5)
            lbl4.grid(row=k,column=3,padx=5,pady=5,sticky="e")
            lbl5.grid(row=k,column=4,padx=5,pady=5,sticky="e")
            k+=1
            
    obj.history_client_list_scrollable_frame=customtkinter.CTkScrollableFrame(obj.fifth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
    obj.history_client_list_scrollable_frame.grid_columnconfigure(3,weight=1)
    
    obj.history_client_list_scrollable_frame_label1=customtkinter.CTkLabel(obj.history_client_list_scrollable_frame,text="Client",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_client_list_scrollable_frame_label2=customtkinter.CTkLabel(obj.history_client_list_scrollable_frame,text="Bought",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_client_list_scrollable_frame_label3=customtkinter.CTkLabel(obj.history_client_list_scrollable_frame,text="Total Profit",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

    obj.history_client_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
    obj.history_client_list_scrollable_frame_label2.grid(row=0,column=3,padx=5,pady=5,sticky="e")
    obj.history_client_list_scrollable_frame_label3.grid(row=0,column=4,padx=5,pady=5,sticky="e")

    if len(obj.history_clients)!=0:
        k=1
        for i in obj.history_clients:
            lbl1=customtkinter.CTkLabel(obj.history_client_list_scrollable_frame,text=i[-1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl2=customtkinter.CTkLabel(obj.history_client_list_scrollable_frame,text=i[1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl3=customtkinter.CTkLabel(obj.history_client_list_scrollable_frame,text=f'{i[0]}£',fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

            lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
            lbl2.grid(row=k,column=3,padx=5,pady=5,sticky="e")
            lbl3.grid(row=k,column=4,padx=5,pady=5,sticky="e")
            k+=1

    # create history_employee_list_scrollable_frame
    obj.history_employee_list_scrollable_frame=customtkinter.CTkScrollableFrame(obj.fifth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
    obj.history_employee_list_scrollable_frame.grid_columnconfigure(3,weight=1)
    
    obj.history_employee_list_scrollable_frame_label1=customtkinter.CTkLabel(obj.history_employee_list_scrollable_frame,text="Employee",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_employee_list_scrollable_frame_label2=customtkinter.CTkLabel(obj.history_employee_list_scrollable_frame,text="Sold",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
    obj.history_employee_list_scrollable_frame_label3=customtkinter.CTkLabel(obj.history_employee_list_scrollable_frame,text="Total Profit",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

    obj.history_employee_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
    obj.history_employee_list_scrollable_frame_label2.grid(row=0,column=3,padx=5,pady=5,sticky="e")
    obj.history_employee_list_scrollable_frame_label3.grid(row=0,column=4,padx=5,pady=5,sticky="e")

    if len(obj.history_employees)!=0:
        k=1
        for i in obj.history_employees:
            lbl1=customtkinter.CTkLabel(obj.history_employee_list_scrollable_frame,text=i[-1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl2=customtkinter.CTkLabel(obj.history_employee_list_scrollable_frame,text=i[-2],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
            lbl3=customtkinter.CTkLabel(obj.history_employee_list_scrollable_frame,text=f'{i[-3]}£',fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

            lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
            lbl2.grid(row=k,column=3,padx=5,pady=5,sticky="e")
            lbl3.grid(row=k,column=4,padx=5,pady=5,sticky="e")
            k+=1