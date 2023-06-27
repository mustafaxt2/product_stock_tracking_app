import customtkinter
from images import Images
from objects import Employee,Client,Product,History
from build import *
from tkinter.messagebox import showerror,showinfo
from frames import grid_frames,grid_history_list,grid_employee_list,grid_client_list,grid_product_list,grid_history_lists

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Product Management")
        self.iconbitmap("images/logo.ico")
        self.geometry("1000x450")
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.default_color=('#979DA2', '#565B5E')
        self.products=db.getProducts()
        self.employees=db.getEmployees()
        self.clients=db.getClients()
        self.history=db.getLatestProductsSold()
        self.history_products=db.getHistoryProducts()
        self.history_clients=db.getTopCustomers()
        self.history_employees=db.getTopSellingEmployees()
        self.logs=db.getLogs()

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame,
                                                             text="  Login Panel",
                                                             image=Images().home_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame,
                                                   corner_radius=0,
                                                   height=40,
                                                   border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent",
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=Images().home_image,
                                                   anchor="w",
                                                   command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame,
                                                      corner_radius=0,
                                                      height=40,
                                                      border_spacing=10,
                                                      text="Products",
                                                      fg_color="transparent",
                                                      text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=Images().product_image,
                                                      anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame,
                                                      corner_radius=0,
                                                      height=40,
                                                      border_spacing=10,
                                                      text="Clients",
                                                      fg_color="transparent",
                                                      text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=Images().users_image,
                                                      anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame,
                                                      corner_radius=0,
                                                      height=40,
                                                      border_spacing=10, text="Employees",
                                                      fg_color="transparent",
                                                      text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=Images().users_image,
                                                      anchor="w",
                                                      command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame,
                                                      corner_radius=0,
                                                      height=40,
                                                      border_spacing=10,
                                                      text="History",
                                                      fg_color="transparent",
                                                      text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=Images().history_image,
                                                      anchor="w",
                                                      command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame,
                                                      corner_radius=0,
                                                      height=40,
                                                      border_spacing=10,
                                                      text="Log Out",
                                                      fg_color="transparent",
                                                      text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=Images().logout_image,
                                                      anchor="center",
                                                      compound="top",
                                                      font=customtkinter.CTkFont(size=15, weight="bold"),
                                                      command=self.sign_out)

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Dark", "Light", "System"],
                                                                fg_color=self.default_color,
                                                                text_color=("gray10", "gray90"),
                                                                button_color=self.default_color,
                                                                button_hover_color=("gray70", "gray30"),
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")

        # ----------------------------create home_frame---------------------------
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_rowconfigure(1, weight=1)

        def on_enter(event):
            self.sign_in()

        # create login_frame
        self.login_frame = customtkinter.CTkFrame(self.home_frame,corner_radius=8,fg_color="transparent",border_width=2,border_color="#DB7AF2")
        self.login_frame.grid(row=0,column=0,rowspan=5,columnspan=5)

        self.home_label=customtkinter.CTkLabel(self.login_frame,text="",image=Images().login_image)
        self.home_label.grid(row=0,column=0,columnspan=3,padx=10,pady=30)

        self.home_entry1=customtkinter.CTkEntry(self.login_frame,placeholder_text="Username",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.home_entry1.grid(row=1, column=1,padx=20,pady=5)
        self.home_entry1.bind("<Return>", on_enter)

        self.home_entry2=customtkinter.CTkEntry(self.login_frame,show="*",placeholder_text="Password",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.home_entry2.grid(row=2, column=1,padx=20,pady=5)
        self.home_entry2.bind("<Return>", on_enter)

        self.home_button1=customtkinter.CTkButton(self.login_frame,text="Sign In",font=("Bold",15),command=self.sign_in,fg_color="#DB7AF2",hover_color="#7ADCF2")
        self.home_button1.grid(row=3, column=1,padx=20,pady=5)

        # If Login output is True,
        # create home_frame widgets
        self.home_frame1=customtkinter.CTkFrame(self.home_frame,corner_radius=0,border_width=3,border_color="#DB7AF2")

        self.home_frame1_frame1=customtkinter.CTkFrame(self.home_frame1,corner_radius=0)
        self.home_frame1_frame1.grid(row=0,column=0,sticky="ew",padx=5)
        self.home_frame1_frame1.grid_columnconfigure(1,weight=1)

        self.home_frame1_frame2=customtkinter.CTkFrame(self.home_frame1,corner_radius=0)
        self.home_frame1_frame2.grid(row=1,column=0,sticky="ew",padx=5)
        self.home_frame1_frame2.grid_columnconfigure(1,weight=1)

        # home_frame1 widgets
        self.home_frame1_label1=customtkinter.CTkLabel(self.home_frame1_frame1,
                                                       fg_color="transparent",
                                                       text=" Top-Selling Product",
                                                       font=("Bold",20),
                                                       corner_radius=3,
                                                       image=Images().most_sale_image,
                                                       compound="left")
        self.home_frame1_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")

        self.home_frame1_label2=customtkinter.CTkLabel(self.home_frame1_frame1,
                                                       image=Images().brand_image,
                                                       text=f' {db.getMostProductsSold()[0].name}' if len(self.history)!=0 else "None",
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),  
                                                       font=customtkinter.CTkFont("Roboto Condensed",15),
                                                       compound="left")
        self.home_frame1_label2.grid(row=1,column=0,padx=5,pady=5,sticky="w")

        self.home_frame1_label3=customtkinter.CTkLabel(self.home_frame1_frame1,
                                                         image=Images().product_image,
                                                         compound="left",
                                                         text=f' Sold: {db.getMostProductsSold()[0].quantity}'if len(self.history)!=0 else "None",  
                                                         fg_color="transparent",
                                                         text_color=("gray10", "gray90"),  
                                                         font=customtkinter.CTkFont("Roboto Condensed",15))
        self.home_frame1_label3.grid(row=2,column=0,padx=5,pady=5,sticky="w")

        # home_frame1 widgets
        self.home_frame1_label4=customtkinter.CTkLabel(self.home_frame1_frame1,
                                                       fg_color="transparent",
                                                       text="Top Customer ",
                                                       font=("Bold",20),
                                                       corner_radius=3,
                                                       image=Images().most_sale_image,
                                                       compound="right")
        self.home_frame1_label4.grid(row=0,column=2,padx=5,pady=5,sticky="e")

        self.home_frame1_label5=customtkinter.CTkLabel(self.home_frame1_frame1,
                                                       image=Images().user_image,
                                                       text=f'{db.getTopCustomers()[0][-1]} ' if len(db.getTopCustomers())!=0 else "None",
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),  
                                                       font=customtkinter.CTkFont("Roboto Condensed",15),
                                                       compound="right")
        self.home_frame1_label5.grid(row=1,column=2,padx=5,pady=5,sticky="e")

        self.home_frame1_label6=customtkinter.CTkLabel(self.home_frame1_frame1,
                                                       image=Images().sell_button_image,
                                                        text=f'Earned: {db.getTopCustomers()[0][0]}£ ' if len(db.getTopCustomers())!=0 else "None",
                                                        fg_color="transparent",
                                                        text_color=("gray10", "gray90"),  
                                                        font=customtkinter.CTkFont("Roboto Condensed",15),
                                                        compound="right")
        self.home_frame1_label6.grid(row=2,column=2,padx=5,pady=5,sticky="e")

        # home_frame1 widgets
        self.home_frame1_label7=customtkinter.CTkLabel(self.home_frame1_frame2,
                                                       fg_color="transparent",
                                                       text=" Last Sold Product",
                                                       font=("Bold",20),
                                                       corner_radius=3,
                                                       image=Images().calendar_image,
                                                       compound="left")
        self.home_frame1_label7.grid(row=0,column=0,padx=5,pady=5,sticky="w")

        self.home_frame1_label8=customtkinter.CTkLabel(self.home_frame1_frame2,
                                                       image=Images().brand_image,
                                                       text=f' {self.history[0][1]}' if len(self.history)!=0 else "None",
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),  
                                                       font=customtkinter.CTkFont("Roboto Condensed",15),
                                                       compound="left")
        self.home_frame1_label8.grid(row=1,column=0,padx=5,pady=5,sticky="w")

        self.home_frame1_label9=customtkinter.CTkLabel(self.home_frame1_frame2,
                                                       image=Images().history_image,
                                                       text=f' {self.history[0][0]}' if len(self.history)!=0 else "None",
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),  
                                                       font=customtkinter.CTkFont("Roboto Condensed",15),
                                                       compound="left")
        self.home_frame1_label9.grid(row=2,column=0,padx=5,pady=5,sticky="w")

        # home_frame1 widgets
        self.home_frame1_label10=customtkinter.CTkLabel(self.home_frame1_frame2,
                                                    fg_color="transparent",
                                                    text="Last Logged In ",
                                                    font=("Bold",20),
                                                    corner_radius=3,
                                                    image=Images().calendar_image,
                                                    compound="right")
        self.home_frame1_label10.grid(row=0,column=1,padx=5,pady=5,sticky="e")

        self.home_frame1_label11=customtkinter.CTkLabel(self.home_frame1_frame2,
                                                        image=Images().user_image,
                                                        text=f'{db.latestLog()[0].employee} ' if len(self.logs)!=0 else "None",
                                                        fg_color="transparent",
                                                        text_color=("gray10", "gray90"),  
                                                        font=customtkinter.CTkFont("Roboto Condensed",15),
                                                        compound="right")
        self.home_frame1_label11.grid(row=1,column=1,padx=5,pady=5,sticky="e")

        self.home_frame1_label12=customtkinter.CTkLabel(self.home_frame1_frame2,
                                                        image=Images().history_image,
                                                        text=f'{db.latestLog()[0].lastDate} ' if len(self.logs)!=0 else "None",
                                                        fg_color="transparent",
                                                        text_color=("gray10", "gray90"),  
                                                        font=customtkinter.CTkFont("Roboto Condensed",15),
                                                        compound="right")
        self.home_frame1_label12.grid(row=2,column=1,padx=5,pady=5,sticky="e")

        # If Login output is False,
        # create two frames into home_frame
        self.home_frame2=customtkinter.CTkFrame(self.home_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

        self.home_frame2_label1=customtkinter.CTkLabel(self.home_frame2,
                                                       fg_color="transparent",
                                                       anchor="center",
                                                       text=" Sell Product",
                                                       font=("Bold",20),
                                                       corner_radius=3,
                                                       image=Images().sell_image,
                                                       compound="top")
        self.home_frame2_label1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

        self.home_frame2_entry1=customtkinter.CTkEntry(self.home_frame2,placeholder_text="Product",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.home_frame2_entry1.grid(row=1,column=0,padx=5,pady=5)

        self.home_frame2_entry2=customtkinter.CTkEntry(self.home_frame2,placeholder_text="Quantity",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.home_frame2_entry2.grid(row=2,column=0,columnspan=5,padx=5,pady=5)

        self.home_frame2_entry3=customtkinter.CTkEntry(self.home_frame2,placeholder_text="Client",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.home_frame2_entry3.grid(row=3,column=0,padx=5,pady=5)

        self.home_frame2_optionmenu1Var=customtkinter.StringVar(self.home_frame2,value="Product Name")
        self.home_frame2_optionmenu1=customtkinter.CTkOptionMenu(self.home_frame2,
                                                                values=[x.name for x in self.products] if len(self.products)!=0 else [],
                                                                fg_color=self.default_color,
                                                                text_color=("gray10", "gray90"),
                                                                button_color=self.default_color,
                                                                button_hover_color=("gray70", "gray30"),
                                                                command=self.get_product_name_event,
                                                                variable=self.home_frame2_optionmenu1Var,
                                                                )
        self.home_frame2_optionmenu1.grid(row=1,column=1,padx=5,pady=5)

        self.home_frame2_optionmenu2Var=customtkinter.StringVar(self.home_frame2,value="Client Name")
        self.home_frame2_optionmenu2=customtkinter.CTkOptionMenu(self.home_frame2,
                                                                values=[x.name for x in self.clients]if len(self.clients)!=0 else [],
                                                                fg_color=self.default_color,
                                                                text_color=("gray10", "gray90"),
                                                                button_color=self.default_color,
                                                                button_hover_color=("gray70", "gray30"),
                                                                command=self.get_client_name_event,
                                                                variable=self.home_frame2_optionmenu2Var,
                                                                )
        self.home_frame2_optionmenu2.grid(row=3,column=1,padx=5,pady=5)

        self.home_frame2_button1=customtkinter.CTkButton(self.home_frame2,
                                                        image=Images().sell_button_image,
                                                        text="Sell",
                                                        compound="left",
                                                        font=("Bold",15),
                                                        fg_color=self.default_color,
                                                        text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        command=self.sell_product)
        self.home_frame2_button1.grid(columnspan=5,padx=5,pady=5)

        # --------------------create second frame----------------------------
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_rowconfigure(1,weight=1)
        self.second_frame.grid_columnconfigure(1,weight=1)


        # create second_frame navigation bar
        self.second_frame_navigation_bar = customtkinter.CTkFrame(self.second_frame,corner_radius=0)
        self.second_frame_navigation_bar.grid(row=0,columnspan=5,sticky="nsew")
        self.second_frame_navigation_bar.grid_rowconfigure(0,weight=1)
        self.second_frame_navigation_bar.grid_columnconfigure(5,weight=1)

        # create second_frame_navigation_bar buttons
        self.second_frame_navigation_bar_button1=customtkinter.CTkButton(self.second_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Product List",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().list_image,
                                                                        command=self.frame2_product_list_button_event)
        self.second_frame_navigation_bar_button1.grid(row=0,column=0,sticky="w")
        
        self.second_frame_navigation_bar_button2=customtkinter.CTkButton(self.second_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Add Product",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().add_product_image20,
                                                                        command=self.frame2_add_product_button_event)
        self.second_frame_navigation_bar_button2.grid(row=0,column=1,sticky="ew")

        self.second_frame_navigation_bar_button3=customtkinter.CTkButton(self.second_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Update Price",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().update_price_image20,
                                                                        command=self.frame2_update_price_button_event)
        self.second_frame_navigation_bar_button3.grid(row=0,column=2,sticky="ew")

        self.second_frame_navigation_bar_button4=customtkinter.CTkButton(self.second_frame_navigation_bar,height=20,
                                                                        border_spacing=10,
                                                                        text="Edit Product",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().edit_image20,
                                                                        command=self.frame2_edit_product_button_event)
        self.second_frame_navigation_bar_button4.grid(row=0,column=3,sticky="ew")

        def find_product(event):
            name=self.second_frame_navigation_bar_entry1.get()
            self.product_list_scrollable_frame.grid_forget()
            grid_product_list(app,db,name)
            self.frame2_product_list_button_event()

        self.second_frame_navigation_bar_entry1=customtkinter.CTkEntry(self.second_frame_navigation_bar,height=20,
                                                                        placeholder_text="Find Product",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15),
                                                                        fg_color="transparent",
                                                                        placeholder_text_color=("gray10", "gray90"),
                                                                        border_color="#DB7AF2")
        self.second_frame_navigation_bar_entry1.grid(row=0,column=6,padx=20,sticky="e")
        self.second_frame_navigation_bar_entry1.bind("<Return>",find_product)

        # create product list
        self.product_list_scrollable_frame=customtkinter.CTkScrollableFrame(self.second_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
        self.product_list_scrollable_frame.grid_columnconfigure(7,weight=1)

        self.product_list_scrollable_frame_label1=customtkinter.CTkLabel(self.product_list_scrollable_frame,text="ID",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.product_list_scrollable_frame_label2=customtkinter.CTkLabel(self.product_list_scrollable_frame,text="Product Name",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.product_list_scrollable_frame_label3=customtkinter.CTkLabel(self.product_list_scrollable_frame,text="Product Cost",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.product_list_scrollable_frame_label4=customtkinter.CTkLabel(self.product_list_scrollable_frame,text="Product Price",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.product_list_scrollable_frame_label5=customtkinter.CTkLabel(self.product_list_scrollable_frame,text="Category",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.product_list_scrollable_frame_label6=customtkinter.CTkLabel(self.product_list_scrollable_frame,text="Quantity",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

        self.product_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5)
        self.product_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
        self.product_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
        self.product_list_scrollable_frame_label4.grid(row=0,column=3,padx=5,pady=5)
        self.product_list_scrollable_frame_label5.grid(row=0,column=4,padx=5,pady=5)
        self.product_list_scrollable_frame_label6.grid(row=0,column=9,padx=5,pady=5,sticky="e")
        if len(self.products)!=0:
            k=1
            for i in self.products:
                lbl1=customtkinter.CTkLabel(self.product_list_scrollable_frame,text=i.id,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl2=customtkinter.CTkLabel(self.product_list_scrollable_frame,text=i.name,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl3=customtkinter.CTkLabel(self.product_list_scrollable_frame,text=f"{i.cost}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl4=customtkinter.CTkLabel(self.product_list_scrollable_frame,text=f"{i.price}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl5=customtkinter.CTkLabel(self.product_list_scrollable_frame,text=i.category,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl6=customtkinter.CTkLabel(self.product_list_scrollable_frame,text=i.quantity,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

                lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
                lbl2.grid(row=k,column=1,padx=5,pady=5)
                lbl3.grid(row=k,column=2,padx=5,pady=5)
                lbl4.grid(row=k,column=3,padx=5,pady=5)
                lbl5.grid(row=k,column=4,padx=5,pady=5)
                lbl6.grid(row=k,column=9,padx=5,pady=5,sticky="e")
                k+=1

        # add product
        self.add_product_frame=customtkinter.CTkFrame(self.second_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

        self.add_product_label1=customtkinter.CTkLabel(self.add_product_frame,
                                                       fg_color="transparent",
                                                       anchor="center",
                                                       text=" Add Product",
                                                       font=("Bold",20),
                                                       corner_radius=3,
                                                       image=Images().add_product_image50,
                                                       compound="top")
        self.add_product_label1.grid(row=0,column=0,columnspan=5,padx=20,pady=10)

        self.add_product_entry1=customtkinter.CTkEntry(self.add_product_frame,placeholder_text="Product",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_product_entry1.grid(row=1,column=0,columnspan=5,padx=20,pady=5)

        self.add_product_entry2=customtkinter.CTkEntry(self.add_product_frame,placeholder_text="Cost",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_product_entry2.grid(row=2,column=0,padx=10,pady=5)

        self.add_product_entry3=customtkinter.CTkEntry(self.add_product_frame,placeholder_text="Price",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_product_entry3.grid(row=2,column=1,padx=10,pady=5)

        self.add_product_entry4=customtkinter.CTkEntry(self.add_product_frame,placeholder_text="Quantity",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_product_entry4.grid(row=3,column=0,columnspan=5,padx=20,pady=5)

        self.add_product_entry5=customtkinter.CTkEntry(self.add_product_frame,placeholder_text="Category",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_product_entry5.grid(row=4,column=0,columnspan=5,padx=20,pady=5)

        self.add_product_button=customtkinter.CTkButton(self.add_product_frame,
                                                        image=Images().add_button_image,
                                                        text="Add",
                                                        compound="left",
                                                        font=("Bold",15),
                                                        fg_color=self.default_color,
                                                        text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        command=self.add_product)
        self.add_product_button.grid(row=5,column=0,columnspan=5,padx=20,pady=5)

        # update price
        self.update_price_frame=customtkinter.CTkFrame(self.second_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

        self.update_price_frame_label1=customtkinter.CTkLabel(self.update_price_frame,
                                                             fg_color="transparent",
                                                             anchor="center",
                                                             text=" Update Price",
                                                             font=("Bold",20),
                                                             corner_radius=3,
                                                             image=Images().update_price_image50,
                                                             compound="top")
        self.update_price_frame_label1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

        self.update_price_frame_entry1=customtkinter.CTkEntry(self.update_price_frame,placeholder_text="Product",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.update_price_frame_entry1.grid(row=1,column=0,padx=5,pady=5)

        self.update_price_frame_entry2=customtkinter.CTkEntry(self.update_price_frame,placeholder_text="Cost",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.update_price_frame_entry2.grid(row=2,column=0,columnspan=5,padx=5,pady=5)

        self.update_price_frame_entry3=customtkinter.CTkEntry(self.update_price_frame,placeholder_text="Price",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.update_price_frame_entry3.grid(row=3,column=0,columnspan=5,padx=5,pady=5)
        
        self.update_price_frame_optionmenu1Var=customtkinter.StringVar(self.update_price_frame,value="Select Product")
        self.update_price_frame_optionmenu1=customtkinter.CTkOptionMenu(self.update_price_frame,
                                                                        values=[x.name for x in self.products]if len(self.products)!=0 else [],
                                                                        fg_color=self.default_color,
                                                                        text_color=("gray10", "gray90"),
                                                                        button_color=self.default_color,
                                                                        button_hover_color=("gray70", "gray30"),
                                                                        command=self.update_price_name_event,
                                                                        variable=self.update_price_frame_optionmenu1Var
                                                                        )
        self.update_price_frame_optionmenu1.grid(row=1,column=1,padx=5,pady=5)

        self.update_price_frame_button=customtkinter.CTkButton(self.update_price_frame,
                                                               image=Images().save_changes_image,
                                                               text="Update",
                                                               compound="left",
                                                               font=("Bold",15),
                                                               fg_color=self.default_color,
                                                               text_color=("gray10", "gray90"),
                                                               hover_color=("gray70", "gray30"),
                                                               command=self.update_price)
        self.update_price_frame_button.grid(columnspan=5,padx=5,pady=5)

        # edit product
        self.edit_product_frame=customtkinter.CTkFrame(self.second_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

        self.edit_product_frame_label1=customtkinter.CTkLabel(self.edit_product_frame,
                                                             fg_color="transparent",
                                                             anchor="center",
                                                             text=" Edit Product",
                                                             font=("Bold",20),
                                                             corner_radius=3,
                                                             image=Images().edit_image50,
                                                             compound="top")
        self.edit_product_frame_label1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

        self.edit_product_frame_entry1=customtkinter.CTkEntry(self.edit_product_frame,placeholder_text="Name",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_product_frame_entry1.grid(row=1,column=0,padx=5,pady=5)

        self.edit_product_frame_entry2=customtkinter.CTkEntry(self.edit_product_frame,placeholder_text="Cost",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_product_frame_entry2.grid(row=2,column=0,padx=5,pady=5)

        self.edit_product_frame_entry3=customtkinter.CTkEntry(self.edit_product_frame,placeholder_text="Price",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_product_frame_entry3.grid(row=2,column=1,padx=5,pady=5)

        self.edit_product_frame_entry4=customtkinter.CTkEntry(self.edit_product_frame,placeholder_text="Quantity",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_product_frame_entry4.grid(row=3,column=0,columnspan=5,padx=5,pady=5)

        self.edit_product_frame_entry5=customtkinter.CTkEntry(self.edit_product_frame,placeholder_text="Category",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_product_frame_entry5.grid(row=4,column=0,columnspan=5,padx=5,pady=5)

        self.edit_product_frame_id=None
        self.edit_product_frame_optionmenu1Var=customtkinter.StringVar(self.edit_product_frame,value="Choose Product")
        self.edit_product_frame_optionmenu1=customtkinter.CTkOptionMenu(self.edit_product_frame,
                                                                        values=[x.name for x in self.products]if len(self.products)!=0 else [],
                                                                        fg_color=self.default_color,
                                                                        text_color=("gray10", "gray90"),
                                                                        button_color=self.default_color,
                                                                        button_hover_color=("gray70", "gray30"),
                                                                        command=self.edit_product_name_event,
                                                                        variable=self.edit_product_frame_optionmenu1Var,
                                                                        )
        self.edit_product_frame_optionmenu1.grid(row=1,column=1,padx=5,pady=5)

        self.edit_product_frame_button=customtkinter.CTkButton(self.edit_product_frame,
                                                               image=Images().save_changes_image,
                                                               text="Save Changes",
                                                               compound="left",
                                                               font=("Bold",15),
                                                               fg_color=self.default_color,
                                                               text_color=("gray10", "gray90"),
                                                               hover_color=("gray70", "gray30"),
                                                               command=self.edit_product)
        self.edit_product_frame_button.grid(row=5,columnspan=5,padx=5,pady=5)


        # --------------------create third frame------------------------------
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_rowconfigure(1,weight=1)
        self.third_frame.grid_columnconfigure(1,weight=1)

        # create third_frame navigation bar
        self.third_frame_navigation_bar = customtkinter.CTkFrame(self.third_frame,corner_radius=0)
        self.third_frame_navigation_bar.grid(row=0,columnspan=5,sticky="nsew")
        self.third_frame_navigation_bar.grid_rowconfigure(0,weight=1)
        self.third_frame_navigation_bar.grid_columnconfigure(5,weight=1)

        # create third_frame_navigation_bar buttons
        self.third_frame_navigation_bar_button1=customtkinter.CTkButton(self.third_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Client List",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().list_image,
                                                                        command=self.frame3_client_list_button_event)
        self.third_frame_navigation_bar_button1.grid(row=0,column=0,sticky="w")
        
        self.third_frame_navigation_bar_button2=customtkinter.CTkButton(self.third_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Add Client",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().add_user_image20,
                                                                        command=self.frame3_add_client_button_event)
        self.third_frame_navigation_bar_button2.grid(row=0,column=1,sticky="ew")

        self.third_frame_navigation_bar_button3=customtkinter.CTkButton(self.third_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Edit Client",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().edit_image20,
                                                                        command=self.frame3_edit_client_button_event)
        self.third_frame_navigation_bar_button3.grid(row=0,column=2,sticky="ew")

        def find_client(event):
            name=self.third_frame_navigation_bar_entry1.get()
            self.client_list_scrollable_frame.grid_forget()
            grid_client_list(app,db,name)
            self.frame3_client_list_button_event()

        self.third_frame_navigation_bar_entry1=customtkinter.CTkEntry(self.third_frame_navigation_bar,height=20,
                                                                        placeholder_text="Find Client",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15),
                                                                        fg_color="transparent",
                                                                        placeholder_text_color=("gray10", "gray90"),
                                                                        border_color="#DB7AF2")
        self.third_frame_navigation_bar_entry1.grid(row=0,column=5,padx=20,sticky="e")
        self.third_frame_navigation_bar_entry1.bind("<Return>",find_client)

        # create client list
        self.client_list_scrollable_frame=customtkinter.CTkScrollableFrame(self.third_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
        
        self.client_list_scrollable_frame.grid_columnconfigure(7,weight=1)

        self.client_list_scrollable_frame_label1=customtkinter.CTkLabel(self.client_list_scrollable_frame,text="ID",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.client_list_scrollable_frame_label2=customtkinter.CTkLabel(self.client_list_scrollable_frame,text="Name",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.client_list_scrollable_frame_label3=customtkinter.CTkLabel(self.client_list_scrollable_frame,text="Phone",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.client_list_scrollable_frame_label4=customtkinter.CTkLabel(self.client_list_scrollable_frame,text="Address",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

        self.client_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        self.client_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
        self.client_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
        self.client_list_scrollable_frame_label4.grid(row=0,column=9,padx=5,pady=5)
        
        if len(self.clients) !=0:
            k=1
            for i in self.clients:
                lbl1=customtkinter.CTkLabel(self.client_list_scrollable_frame,text=i.id,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl2=customtkinter.CTkLabel(self.client_list_scrollable_frame,text=i.name,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl3=customtkinter.CTkLabel(self.client_list_scrollable_frame,text=i.phone,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl4=customtkinter.CTkLabel(self.client_list_scrollable_frame,text=i.address,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

                lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
                lbl2.grid(row=k,column=1,padx=5,pady=5)
                lbl3.grid(row=k,column=2,padx=5,pady=5)
                lbl4.grid(row=k,column=9,padx=5,pady=5)
                k+=1

        # add client
        self.add_client_frame=customtkinter.CTkFrame(self.third_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

        self.add_client_label1=customtkinter.CTkLabel(self.add_client_frame,
                                                       fg_color="transparent",
                                                       anchor="center",
                                                       text=" Add Client",
                                                       font=("Bold",20),
                                                       corner_radius=3,
                                                       image=Images().add_user_image50,
                                                       compound="top")
        self.add_client_label1.grid(row=0,column=0,columnspan=5,padx=20,pady=10)

        self.add_client_entry1=customtkinter.CTkEntry(self.add_client_frame,placeholder_text="Client",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_client_entry1.grid(row=1,column=0,columnspan=5,padx=20,pady=5)

        self.add_client_entry2=customtkinter.CTkEntry(self.add_client_frame,placeholder_text="Phone",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_client_entry2.grid(row=2,column=0,columnspan=5,padx=20,pady=5)

        self.add_client_entry3=customtkinter.CTkEntry(self.add_client_frame,placeholder_text="Address",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_client_entry3.grid(row=3,column=0,columnspan=5,padx=20,pady=5)

        self.add_client_button=customtkinter.CTkButton(self.add_client_frame,
                                                        image=Images().add_button_image,
                                                        text="Add",
                                                        compound="left",
                                                        font=("Bold",15),
                                                        fg_color=self.default_color,
                                                        text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        command=self.add_client)
        self.add_client_button.grid(row=5,column=0,columnspan=5,padx=20,pady=5)

        # edit client
        self.edit_client_frame=customtkinter.CTkFrame(self.third_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

        self.edit_client_frame_label1=customtkinter.CTkLabel(self.edit_client_frame,
                                                             fg_color="transparent",
                                                             anchor="center",
                                                             text=" Edit Client",
                                                             font=("Bold",20),
                                                             corner_radius=3,
                                                             image=Images().edit_image50,
                                                             compound="top")
        self.edit_client_frame_label1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

        self.edit_client_frame_entry1=customtkinter.CTkEntry(self.edit_client_frame,placeholder_text="Name",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_client_frame_entry1.grid(row=1,column=0,padx=5,pady=5)

        self.edit_client_frame_entry2=customtkinter.CTkEntry(self.edit_client_frame,placeholder_text="Phone",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_client_frame_entry2.grid(row=2,column=0,columnspan=5,padx=5,pady=5)

        self.edit_client_frame_entry3=customtkinter.CTkEntry(self.edit_client_frame,placeholder_text="Address",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_client_frame_entry3.grid(row=3,column=0,columnspan=5,padx=5,pady=5)
        
        self.edit_client_frame_id=None
        self.edit_client_frame_optionmenu1Var=customtkinter.StringVar(self.edit_client_frame,value="Client Name")
        self.edit_client_frame_optionmenu1=customtkinter.CTkOptionMenu(self.edit_client_frame,
                                                                        values=[x.name for x in self.clients]if len(self.clients)!=0 else [],
                                                                        fg_color=self.default_color,
                                                                        text_color=("gray10", "gray90"),
                                                                        button_color=self.default_color,
                                                                        button_hover_color=("gray70", "gray30"),
                                                                        command=self.edit_client_name_event,
                                                                        variable=self.edit_client_frame_optionmenu1Var,
                                                                        )
        self.edit_client_frame_optionmenu1.grid(row=1,column=1,padx=5,pady=5)

        self.edit_client_frame_button=customtkinter.CTkButton(self.edit_client_frame,
                                                               image=Images().save_changes_image,
                                                               text="Save Changes",
                                                               compound="left",
                                                               font=("Bold",15),
                                                               fg_color=self.default_color,
                                                               text_color=("gray10", "gray90"),
                                                               hover_color=("gray70", "gray30"),
                                                               command=self.edit_client)
        self.edit_client_frame_button.grid(columnspan=5,padx=5,pady=5)

        # --------------------create fourth frame-------------------------------
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_rowconfigure(1,weight=1)
        self.fourth_frame.grid_columnconfigure(1,weight=1)

        # create fourth_frame navigation bar
        self.fourth_frame_navigation_bar = customtkinter.CTkFrame(self.fourth_frame,corner_radius=0)
        self.fourth_frame_navigation_bar.grid(row=0,columnspan=5,sticky="nsew")
        self.fourth_frame_navigation_bar.grid_rowconfigure(0,weight=1)
        self.fourth_frame_navigation_bar.grid_columnconfigure(5,weight=1)

        # create fourth_frame_navigation_bar buttons
        self.fourth_frame_navigation_bar_button1=customtkinter.CTkButton(self.fourth_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Employee List",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().list_image,
                                                                        command=self.frame4_employee_list_button_event)
        self.fourth_frame_navigation_bar_button1.grid(row=0,column=0,sticky="w")
        
        self.fourth_frame_navigation_bar_button2=customtkinter.CTkButton(self.fourth_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Add Employee",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().add_user_image20,
                                                                        command=self.frame4_add_employee_button_event)
        self.fourth_frame_navigation_bar_button2.grid(row=0,column=1,sticky="ew")

        self.fourth_frame_navigation_bar_button3=customtkinter.CTkButton(self.fourth_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Edit Employee",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().edit_image20,
                                                                        command=self.frame4_edit_employee_button_event)
        self.fourth_frame_navigation_bar_button3.grid(row=0,column=2,sticky="ew")
        
        def find_employee(event):
            name=self.fourth_frame_navigation_bar_entry1.get()
            self.employee_list_scrollable_frame.grid_forget()
            grid_employee_list(app,db,name)
            self.frame4_employee_list_button_event()

        self.fourth_frame_navigation_bar_entry1=customtkinter.CTkEntry(self.fourth_frame_navigation_bar,height=20,
                                                                        placeholder_text="Find Employee",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15),
                                                                        fg_color="transparent",
                                                                        placeholder_text_color=("gray10", "gray90"),border_color="#DB7AF2")
        self.fourth_frame_navigation_bar_entry1.grid(row=0,column=5,padx=20,sticky="e")
        self.fourth_frame_navigation_bar_entry1.bind("<Return>",find_employee)

        # create employee list
        self.employee_list_scrollable_frame=customtkinter.CTkScrollableFrame(self.fourth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
        
        self.employee_list_scrollable_frame.grid_columnconfigure(7,weight=1)

        self.employee_list_scrollable_frame_label1=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text="ID",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.employee_list_scrollable_frame_label2=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text="Name",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.employee_list_scrollable_frame_label3=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text="Phone",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.employee_list_scrollable_frame_label4=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text="Email",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.employee_list_scrollable_frame_label5=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text="Username",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.employee_list_scrollable_frame_label6=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text="Password",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

        self.employee_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        self.employee_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
        self.employee_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
        self.employee_list_scrollable_frame_label4.grid(row=0,column=3,padx=5,pady=5)
        self.employee_list_scrollable_frame_label5.grid(row=0,column=8,padx=5,pady=5)
        self.employee_list_scrollable_frame_label6.grid(row=0,column=9,padx=5,pady=5)

        if len(self.employees)!=0:
            k=1
            for i in self.employees:
                lbl1=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text=i.id,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl2=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text=i.name,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl3=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text=i.phone,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl4=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text=i.email,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl5=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text=i.username,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl6=customtkinter.CTkLabel(self.employee_list_scrollable_frame,text=i.password,fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

                lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
                lbl2.grid(row=k,column=1,padx=5,pady=5)
                lbl3.grid(row=k,column=2,padx=5,pady=5)
                lbl4.grid(row=k,column=3,padx=5,pady=5)
                lbl5.grid(row=k,column=8,padx=5,pady=5)
                lbl6.grid(row=k,column=9,padx=5,pady=5)
                k+=1

        # add employee
        self.add_employee_frame=customtkinter.CTkFrame(self.fourth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

        self.add_employee_label1=customtkinter.CTkLabel(self.add_employee_frame,
                                                       fg_color="transparent",
                                                       anchor="center",
                                                       text=" Add Employee",
                                                       font=("Bold",20),
                                                       corner_radius=3,
                                                       image=Images().add_user_image50,
                                                       compound="top")
        self.add_employee_label1.grid(row=0,column=0,columnspan=5,padx=20,pady=10)

        self.add_employee_entry1=customtkinter.CTkEntry(self.add_employee_frame,placeholder_text="Name",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_employee_entry1.grid(row=1,column=0,columnspan=5,padx=20,pady=5)

        self.add_employee_entry2=customtkinter.CTkEntry(self.add_employee_frame,placeholder_text="Phone",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_employee_entry2.grid(row=2,column=0,padx=20,pady=5)

        self.add_employee_entry3=customtkinter.CTkEntry(self.add_employee_frame,placeholder_text="Email",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_employee_entry3.grid(row=2,column=1,padx=20,pady=5)

        self.add_employee_entry4=customtkinter.CTkEntry(self.add_employee_frame,placeholder_text="Username",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_employee_entry4.grid(row=3,column=0,padx=20,pady=5)

        self.add_employee_entry5=customtkinter.CTkEntry(self.add_employee_frame,placeholder_text="Password",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.add_employee_entry5.grid(row=3,column=1,padx=20,pady=5)

        self.add_employee_button=customtkinter.CTkButton(self.add_employee_frame,
                                                        image=Images().add_button_image,
                                                        text="Add",
                                                        compound="left",
                                                        font=("Bold",15),
                                                        fg_color=self.default_color,
                                                        text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        command=self.add_employee)
        self.add_employee_button.grid(row=4,column=0,columnspan=5,padx=20,pady=5)

        # edit employee
        self.edit_employee_frame=customtkinter.CTkFrame(self.fourth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2")

        self.edit_employee_frame_label1=customtkinter.CTkLabel(self.edit_employee_frame,
                                                             fg_color="transparent",
                                                             anchor="center",
                                                             text=" Edit Employee",
                                                             font=("Bold",20),
                                                             corner_radius=3,
                                                             image=Images().edit_image50,
                                                             compound="top")
        self.edit_employee_frame_label1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

        self.edit_employee_frame_entry1=customtkinter.CTkEntry(self.edit_employee_frame,placeholder_text="Name",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_employee_frame_entry1.grid(row=1,column=0,padx=5,pady=5)

        self.edit_employee_frame_entry2=customtkinter.CTkEntry(self.edit_employee_frame,placeholder_text="Phone",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_employee_frame_entry2.grid(row=2,column=0,padx=5,pady=5)

        self.edit_employee_frame_entry3=customtkinter.CTkEntry(self.edit_employee_frame,placeholder_text="Email",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_employee_frame_entry3.grid(row=2,column=1,padx=5,pady=5)
        
        self.edit_employee_frame_entry4=customtkinter.CTkEntry(self.edit_employee_frame,placeholder_text="Username",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_employee_frame_entry4.grid(row=3,column=0,padx=20,pady=5)

        self.edit_employee_frame_entry5=customtkinter.CTkEntry(self.edit_employee_frame,placeholder_text="Password",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.edit_employee_frame_entry5.grid(row=3,column=1,padx=20,pady=5)

        self.edit_employee_frame_id=None
        self.edit_employee_frame_optionmenu1Var=customtkinter.StringVar(self.edit_employee_frame,value="Employee Name")
        self.edit_employee_frame_optionmenu1=customtkinter.CTkOptionMenu(self.edit_employee_frame,
                                                                        values=[x.name for x in self.employees]if len(self.employees)!=0 else [],
                                                                        fg_color=self.default_color,
                                                                        text_color=("gray10", "gray90"),
                                                                        button_color=self.default_color,
                                                                        button_hover_color=("gray70", "gray30"),
                                                                        command=self.edit_employee_name_event,
                                                                        variable=self.edit_employee_frame_optionmenu1Var,
                                                                        )
        self.edit_employee_frame_optionmenu1.grid(row=1,column=1,padx=5,pady=5)

        self.edit_employee_frame_button=customtkinter.CTkButton(self.edit_employee_frame,
                                                               image=Images().save_changes_image,
                                                               text="Save Changes",
                                                               compound="left",
                                                               font=("Bold",15),
                                                               fg_color=self.default_color,
                                                               text_color=("gray10", "gray90"),
                                                               hover_color=("gray70", "gray30"),
                                                               command=self.edit_employee)
        self.edit_employee_frame_button.grid(row=4,columnspan=5,padx=5,pady=5)

        # --------------------create fifth frame-----------------------------------
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifth_frame.grid_rowconfigure(1,weight=1)
        self.fifth_frame.grid_columnconfigure(1,weight=1)

        self.fifth_frame_navigation_bar = customtkinter.CTkFrame(self.fifth_frame,corner_radius=0)
        self.fifth_frame_navigation_bar.grid(row=0,columnspan=5,sticky="nsew")
        self.fifth_frame_navigation_bar.grid_rowconfigure(0,weight=1)
        self.fifth_frame_navigation_bar.grid_columnconfigure(5,weight=1)

        # create fifth_frame_navigation_bar buttons
        self.fifth_frame_navigation_bar_button1=customtkinter.CTkButton(self.fifth_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="History List",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().list_image,
                                                                        command=self.frame5_history_list_button_event)
        self.fifth_frame_navigation_bar_button1.grid(row=0,column=0,sticky="w")
        
        self.fifth_frame_navigation_bar_button2=customtkinter.CTkButton(self.fifth_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Products",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().product_image,
                                                                        command=self.frame5_products_button_event)
        self.fifth_frame_navigation_bar_button2.grid(row=0,column=1,sticky="ew")

        self.fifth_frame_navigation_bar_button3=customtkinter.CTkButton(self.fifth_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Clients",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().users_image,
                                                                        command=self.frame5_clients_button_event)
        self.fifth_frame_navigation_bar_button3.grid(row=0,column=2,sticky="ew")

        self.fifth_frame_navigation_bar_button4=customtkinter.CTkButton(self.fifth_frame_navigation_bar,
                                                                        height=20,
                                                                        border_spacing=10,
                                                                        text="Employees",
                                                                        fg_color="transparent",
                                                                        text_color=("gray10", "gray90"),
                                                                        hover_color=("gray70", "gray30"),
                                                                        anchor="n",
                                                                        image=Images().users_image,
                                                                        command=self.frame5_employees_button_event)
        self.fifth_frame_navigation_bar_button4.grid(row=0,column=3,sticky="ew")

        def find_log(event):
            name=self.fifth_frame_navigation_bar_entry1.get()
            self.history_list_scrollable_frame.grid_forget()
            grid_history_list(app,db,name)
            self.frame5_history_list_button_event()

        self.fifth_frame_navigation_bar_entry1=customtkinter.CTkEntry(self.fifth_frame_navigation_bar,height=20,
                                                                        placeholder_text="Find By Date",justify="center",font=customtkinter.CTkFont("Roboto Condensed",15),
                                                                        fg_color="transparent",
                                                                        placeholder_text_color=("gray10", "gray90"),border_color="#DB7AF2")
        self.fifth_frame_navigation_bar_entry1.grid(row=0,column=6,padx=20,sticky="e")
        self.fifth_frame_navigation_bar_entry1.bind("<Return>",find_log)

        # create history_list_scrollable_frame
        self.history_list_scrollable_frame=customtkinter.CTkScrollableFrame(self.fifth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
        self.history_list_scrollable_frame.grid_columnconfigure(7,weight=1)

        def calculate_profit():
            totalProfit=0.0
            for i in self.history:
                totalProfit+=i[-1]
            return totalProfit
        
        totalProfit=calculate_profit()
        self.history_list_scrollable_frame_label1=customtkinter.CTkLabel(self.history_list_scrollable_frame,text="Sold Date",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_list_scrollable_frame_label2=customtkinter.CTkLabel(self.history_list_scrollable_frame,text="Product",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_list_scrollable_frame_label3=customtkinter.CTkLabel(self.history_list_scrollable_frame,text="Cost",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_list_scrollable_frame_label4=customtkinter.CTkLabel(self.history_list_scrollable_frame,text="Price",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_list_scrollable_frame_label5=customtkinter.CTkLabel(self.history_list_scrollable_frame,text="Quantity",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_list_scrollable_frame_label6=customtkinter.CTkLabel(self.history_list_scrollable_frame,text="Sold To",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_list_scrollable_frame_label7=customtkinter.CTkLabel(self.history_list_scrollable_frame,text="Sold By",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_list_scrollable_frame_label8=customtkinter.CTkLabel(self.history_list_scrollable_frame,text=f"Total Profit\n{totalProfit}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

        self.history_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        self.history_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
        self.history_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
        self.history_list_scrollable_frame_label4.grid(row=0,column=3,padx=5,pady=5)
        self.history_list_scrollable_frame_label5.grid(row=0,column=4,padx=5,pady=5)
        self.history_list_scrollable_frame_label6.grid(row=0,column=5,padx=5,pady=5)
        self.history_list_scrollable_frame_label7.grid(row=0,column=6,padx=5,pady=5)
        self.history_list_scrollable_frame_label8.grid(row=0,column=9,padx=5,pady=5,sticky="e")
        
        if len(self.history)!=0:
            k=1
            for i in self.history:
                lbl1=customtkinter.CTkLabel(self.history_list_scrollable_frame,text=i[0],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl2=customtkinter.CTkLabel(self.history_list_scrollable_frame,text=i[1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl3=customtkinter.CTkLabel(self.history_list_scrollable_frame,text=f"{i[2]}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl4=customtkinter.CTkLabel(self.history_list_scrollable_frame,text=f"{i[3]}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl5=customtkinter.CTkLabel(self.history_list_scrollable_frame,text=i[4],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl6=customtkinter.CTkLabel(self.history_list_scrollable_frame,text=i[5],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl7=customtkinter.CTkLabel(self.history_list_scrollable_frame,text=i[6],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl8=customtkinter.CTkLabel(self.history_list_scrollable_frame,text=f'{i[-1]}£',fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

                lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
                lbl2.grid(row=k,column=1,padx=5,pady=5)
                lbl3.grid(row=k,column=2,padx=5,pady=5)
                lbl4.grid(row=k,column=3,padx=5,pady=5)
                lbl5.grid(row=k,column=4,padx=5,pady=5)
                lbl6.grid(row=k,column=5,padx=5,pady=5)
                lbl7.grid(row=k,column=6,padx=5,pady=5)
                lbl8.grid(row=k,column=9,padx=5,pady=5,sticky="e")
                k+=1

        # create history_product_list_scrollable_frame
        self.history_product_list_scrollable_frame=customtkinter.CTkScrollableFrame(self.fifth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
        self.history_product_list_scrollable_frame.grid_columnconfigure(4,weight=1)
        
        self.history_product_list_scrollable_frame_label1=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text="Product",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_product_list_scrollable_frame_label2=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text="Cost",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_product_list_scrollable_frame_label3=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text="Price",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_product_list_scrollable_frame_label4=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text="Total Sold",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_product_list_scrollable_frame_label5=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text="Total Profit",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

        self.history_product_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        self.history_product_list_scrollable_frame_label2.grid(row=0,column=1,padx=5,pady=5)
        self.history_product_list_scrollable_frame_label3.grid(row=0,column=2,padx=5,pady=5)
        self.history_product_list_scrollable_frame_label4.grid(row=0,column=3,padx=5,pady=5,sticky="e")
        self.history_product_list_scrollable_frame_label5.grid(row=0,column=4,padx=5,pady=5,sticky="e")

        if len(self.history_products)!=0:
            k=1
            for i in self.history_products:
                lbl1=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text=i[1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl2=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text=f"{i[2]}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl3=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text=f"{i[3]}£",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl4=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text=i[5],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl5=customtkinter.CTkLabel(self.history_product_list_scrollable_frame,text=i[4],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

                lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
                lbl2.grid(row=k,column=1,padx=5,pady=5)
                lbl3.grid(row=k,column=2,padx=5,pady=5)
                lbl4.grid(row=k,column=3,padx=5,pady=5,sticky="e")
                lbl5.grid(row=k,column=4,padx=5,pady=5,sticky="e")
                k+=1

        # create history_client_list_scrollable_frame
        self.history_client_list_scrollable_frame=customtkinter.CTkScrollableFrame(self.fifth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
        self.history_client_list_scrollable_frame.grid_columnconfigure(3,weight=1)
        
        self.history_client_list_scrollable_frame_label1=customtkinter.CTkLabel(self.history_client_list_scrollable_frame,text="Client",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_client_list_scrollable_frame_label2=customtkinter.CTkLabel(self.history_client_list_scrollable_frame,text="Bought",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_client_list_scrollable_frame_label3=customtkinter.CTkLabel(self.history_client_list_scrollable_frame,text="Total Profit",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

        self.history_client_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        self.history_client_list_scrollable_frame_label2.grid(row=0,column=3,padx=5,pady=5,sticky="e")
        self.history_client_list_scrollable_frame_label3.grid(row=0,column=4,padx=5,pady=5,sticky="e")

        if len(self.history_clients)!=0:
            k=1
            for i in self.history_clients:
                lbl1=customtkinter.CTkLabel(self.history_client_list_scrollable_frame,text=i[-1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl2=customtkinter.CTkLabel(self.history_client_list_scrollable_frame,text=i[1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl3=customtkinter.CTkLabel(self.history_client_list_scrollable_frame,text=f'{i[0]}£',fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

                lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
                lbl2.grid(row=k,column=3,padx=5,pady=5,sticky="e")
                lbl3.grid(row=k,column=4,padx=5,pady=5,sticky="e")
                k+=1

        # create history_employee_list_scrollable_frame
        self.history_employee_list_scrollable_frame=customtkinter.CTkScrollableFrame(self.fifth_frame,corner_radius=8,fg_color="transparent",border_width=3,border_color="#DB7AF2",scrollbar_button_color="#DB7AF2")
        self.history_employee_list_scrollable_frame.grid_columnconfigure(3,weight=1)
        
        self.history_employee_list_scrollable_frame_label1=customtkinter.CTkLabel(self.history_employee_list_scrollable_frame,text="Employee",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_employee_list_scrollable_frame_label2=customtkinter.CTkLabel(self.history_employee_list_scrollable_frame,text="Sold",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
        self.history_employee_list_scrollable_frame_label3=customtkinter.CTkLabel(self.history_employee_list_scrollable_frame,text="Total Profit",fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

        self.history_employee_list_scrollable_frame_label1.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        self.history_employee_list_scrollable_frame_label2.grid(row=0,column=3,padx=5,pady=5,sticky="e")
        self.history_employee_list_scrollable_frame_label3.grid(row=0,column=4,padx=5,pady=5,sticky="e")

        if len(self.history_employees)!=0:
            k=1
            for i in self.history_employees:
                lbl1=customtkinter.CTkLabel(self.history_employee_list_scrollable_frame,text=i[-1],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl2=customtkinter.CTkLabel(self.history_employee_list_scrollable_frame,text=i[-2],fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))
                lbl3=customtkinter.CTkLabel(self.history_employee_list_scrollable_frame,text=f'{i[-3]}£',fg_color="transparent",anchor="center",font=customtkinter.CTkFont("Roboto Condensed",15))

                lbl1.grid(row=k,column=0,padx=5,pady=5,sticky="w")
                lbl2.grid(row=k,column=3,padx=5,pady=5,sticky="e")
                lbl3.grid(row=k,column=4,padx=5,pady=5,sticky="e")
                k+=1
                
        # select default frame
        self.select_frame_by_name("Home")
        self.frame_2_button.configure(state="disabled")
        self.frame_3_button.configure(state="disabled")
        self.frame_4_button.configure(state="disabled")
        self.frame_5_button.configure(state="disabled")

        self.set_default_settings()
        self.control_list_sizes()

    def destroy_frames(self):
        self.add_product_frame.destroy()
        self.update_price_frame.destroy()
        self.edit_product_frame.destroy()
        self.add_client_frame.destroy()
        self.edit_client_frame.destroy()
        self.history_product_list_scrollable_frame.destroy()
        self.history_client_list_scrollable_frame.destroy()
        self.history_employee_list_scrollable_frame.destroy()
        self.history_list_scrollable_frame.destroy()
       
    def set_default_settings(self):
        self.frame2_product_list_button_event()
        self.frame3_client_list_button_event()
        self.frame4_employee_list_button_event()
        self.frame5_history_list_button_event()
        self.home_frame1_label2.configure(text=f' {db.getMostProductsSold()[0].name}' if len(self.history)!=0 else "None")
        self.home_frame1_label3.configure(text=f' Sold: {db.getMostProductsSold()[0].quantity}'if len(self.history)!=0 else "None")
        self.home_frame1_label5.configure(text=f'{db.getTopCustomers()[0][-1]} ' if len(db.getTopCustomers())!=0 else "None")
        self.home_frame1_label6.configure(text=f'Earned: {db.getTopCustomers()[0][0]}£ ' if len(db.getTopCustomers())!=0 else "None")
        self.home_frame1_label8.configure(text=f' {self.history[0][1]}' if len(self.history)!=0 else "None")
        self.home_frame1_label9.configure(text=f' {self.history[0][0]}' if len(self.history)!=0 else "None")
        self.home_frame1_label11.configure(text=f'{db.latestLog()[0].employee} ' if len(self.logs)!=0 else "None")
        self.home_frame1_label12.configure(text=f'{db.latestLog()[0].lastDate} ' if len(self.logs)!=0 else "None")


    def control_list_sizes(self):
        self.second_frame_navigation_bar_button3.configure(state="disabled" if len(self.products) ==0  else "enabled")
        self.second_frame_navigation_bar_button4.configure(state="disabled" if len(self.products) ==0  else "enabled")
        self.second_frame_navigation_bar_entry1.configure(state="disabled" if len(self.products) ==0  else "normal")

        self.third_frame_navigation_bar_button3.configure(state="disabled" if len(self.clients) ==0 else "enabled")
        self.third_frame_navigation_bar_entry1.configure(state="disabled" if len(self.clients) ==0  else "normal")
        
        self.fourth_frame_navigation_bar_button3.configure(state="disabled" if len(self.employees) ==0 else "enabled")
        self.fourth_frame_navigation_bar_entry1.configure(state="disabled" if len(self.employees) ==0  else "normal")

        self.fifth_frame_navigation_bar_button2.configure(state="disabled" if len(self.history) ==0 else "enabled")
        self.fifth_frame_navigation_bar_button3.configure(state="disabled" if len(self.history) ==0 else "enabled")
        self.fifth_frame_navigation_bar_button4.configure(state="disabled" if len(self.history) ==0 else "enabled")
        self.fifth_frame_navigation_bar_entry1.configure(state="disabled" if len(self.history) ==0 else "normal")

        self.login_state=None
        self.employee_username=None

    def sign_in(self):
        username=self.home_entry1.get()
        password=self.home_entry2.get()
        self.home_entry1.configure(placeholder_text_color="red",border_color="red"if len(username)==0 else self.default_color)
        self.home_entry2.configure(placeholder_text_color="red",border_color="red"if len(password)==0 else self.default_color)
        result=db.logIn(username,password)
        if result is True:
            self.login_state=True
            self.login_frame.grid_forget()
            self.frame_2_button.configure(state="active")
            self.frame_3_button.configure(state="active")
            self.frame_4_button.configure(state="active")
            self.frame_5_button.configure(state="active")
            self.frame_4_button.configure(image=Images().users_image)
            self.frame_5_button.configure(image=Images().history_image)
            self.frame_6_button.grid(row=6,column=0,sticky="s")
            self.home_frame1.grid(row=0,column=0,rowspan=5,columnspan=5)

        if result is False:
            self.login_state=False
            self.employee_username=username
            self.login_frame.grid_forget()
            db.addLog(username,time.strftime("%y-%m-%d %H:%M:%S"))
            self.frame_2_button.configure(state="active")
            self.frame_3_button.configure(state="active")
            self.frame_4_button.configure(image=Images().unaccessible_image)
            self.frame_5_button.configure(image=Images().unaccessible_image)

            self.frame_6_button.grid(row=6,column=0,sticky="s")
            self.home_frame2.grid(rowspan=5,columnspan=5)

        if result is None:
            showerror("Error!","There is no such user")

    def sign_out(self):
            self.home_button_event()
            self.frame_2_button.configure(state="disabled")
            self.frame_3_button.configure(state="disabled")
            self.frame_4_button.configure(state="disabled")
            self.frame_5_button.configure(state="disabled")
            self.frame_6_button.grid_forget()
            self.home_frame1.grid_forget()
            self.home_frame2.grid_forget()
            self.login_frame.grid(row=0,column=0,rowspan=5,columnspan=5)

            self.destroy_frames()
            grid_frames(app)
            grid_history_lists(app,db)
            grid_history_list(app,db,None)
            self.set_default_settings()

    # set button color for selected button
    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Products" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "Clients" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "Employees" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "History" else "transparent")
        
        self.home_frame1.configure(fg_color=("gray75", "gray25") if name == "Home" else "transparent")
        self.home_frame2.configure(fg_color=("gray75", "gray25") if name == "Home" else "transparent")

        self.navigation_frame_label.configure(text=f" {name}")

        # show selected frame
        if name == "Home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Products":
            if self.login_state==True:
                self.second_frame.grid(row=0, column=1, sticky="nsew")
            else:
                self.second_frame.grid(row=0, column=1, sticky="nsew")
                self.frame2_product_list_button_event()
        else:
            self.second_frame.grid_forget()
        if name == "Clients":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "Employees":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "History":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("Home")
        self.navigation_frame_label.configure(image=Images().home_image)

    def frame_2_button_event(self):
        self.select_frame_by_name("Products")
        self.navigation_frame_label.configure(image=Images().product_image)

    def frame_3_button_event(self):
        self.select_frame_by_name("Clients")
        self.navigation_frame_label.configure(image=Images().users_image)
        
    def frame_4_button_event(self):
        self.select_frame_by_name("Employees")
        self.navigation_frame_label.configure(image=Images().users_image)

    def frame_5_button_event(self):
        self.select_frame_by_name("History")
        self.navigation_frame_label.configure(image=Images().history_image)

    def frame2_product_list_button_event(self):
        self.frame2_change_button_colors("Product List")
        self.add_product_frame.grid_forget()
        self.update_price_frame.grid_forget() 
        self.edit_product_frame.grid_forget() 
        self.product_list_scrollable_frame.grid(row=1,column=0,rowspan=5,columnspan=5,sticky="nsew")

    def frame2_add_product_button_event(self):
        self.frame2_change_button_colors("Add Product")
        self.product_list_scrollable_frame.grid_forget()
        self.update_price_frame.grid_forget() 
        self.edit_product_frame.grid_forget() 
        self.add_product_frame.grid(row=1,column=0,rowspan=5,columnspan=5)

    def frame2_update_price_button_event(self):
        self.frame2_change_button_colors("Update Price")
        self.product_list_scrollable_frame.grid_forget()  
        self.add_product_frame.grid_forget() 
        self.edit_product_frame.grid_forget()
        self.update_price_frame_optionmenu1.configure(values=[x.name for x in self.products])
        self.update_price_frame.grid(row=1,column=0,rowspan=5,columnspan=5)

    def frame2_edit_product_button_event(self):
        self.frame2_change_button_colors("Edit Product")
        self.product_list_scrollable_frame.grid_forget() 
        self.add_product_frame.grid_forget() 
        self.update_price_frame.grid_forget()
        self.edit_product_frame_optionmenu1.configure(values=[x.name for x in self.products])
        self.edit_product_frame.grid(row=1,column=0,rowspan=5,columnspan=5)

    def frame3_client_list_button_event(self):
        self.frame3_change_button_colors("Client List")
        self.add_client_frame.grid_forget()
        self.edit_client_frame.grid_forget()
        self.client_list_scrollable_frame.grid(row=1,column=0,rowspan=5,columnspan=5,sticky="nsew")

    def frame3_add_client_button_event(self):
        self.frame3_change_button_colors("Add Client")
        self.client_list_scrollable_frame.grid_forget()
        self.edit_client_frame.grid_forget() 
        self.add_client_frame.grid(row=1,column=0,rowspan=5,columnspan=5)

    def frame3_edit_client_button_event(self):
        self.frame3_change_button_colors("Edit Client")
        self.client_list_scrollable_frame.grid_forget()  
        self.add_client_frame.grid_forget()  
        self.edit_client_frame_optionmenu1.configure(values=[x.name for x in self.clients])
        self.edit_client_frame.grid(row=1,column=0,rowspan=5,columnspan=5)

    def frame4_employee_list_button_event(self):
        self.frame4_change_button_colors("Employee List")
        self.add_employee_frame.grid_forget()
        self.edit_employee_frame.grid_forget()
        self.employee_list_scrollable_frame.grid(row=1,column=0,rowspan=5,columnspan=5,sticky="nsew")

    def frame4_add_employee_button_event(self):
        self.frame4_change_button_colors("Add Employee")
        self.employee_list_scrollable_frame.grid_forget()
        self.edit_employee_frame.grid_forget() 
        self.add_employee_frame.grid(row=1,column=0,rowspan=5,columnspan=5)

    def frame4_edit_employee_button_event(self):
        self.frame4_change_button_colors("Edit Employee")
        self.employee_list_scrollable_frame.grid_forget()  
        self.add_employee_frame.grid_forget()
        self.edit_employee_frame_optionmenu1.configure(values=[x.name for x in self.employees])
        self.edit_employee_frame.grid(row=1,column=0,rowspan=5,columnspan=5)

    def frame5_history_list_button_event(self):
        self.frame5_change_button_colors("History List")
        self.history_product_list_scrollable_frame.grid_forget()
        self.history_client_list_scrollable_frame.grid_forget()
        self.history_employee_list_scrollable_frame.grid_forget()
        self.history_list_scrollable_frame.grid(row=1,column=0,rowspan=5,columnspan=5,sticky="nsew")

    def frame5_products_button_event(self):
        self.frame5_change_button_colors("Products")
        self.history_list_scrollable_frame.grid_forget()
        self.history_client_list_scrollable_frame.grid_forget()
        self.history_employee_list_scrollable_frame.grid_forget()
        self.history_product_list_scrollable_frame.grid(row=1,column=0,rowspan=5,columnspan=5,sticky="nsew")

    def frame5_clients_button_event(self):
        self.frame5_change_button_colors("Clients")
        self.history_list_scrollable_frame.grid_forget()
        self.history_product_list_scrollable_frame.grid_forget()
        self.history_employee_list_scrollable_frame.grid_forget()
        self.history_client_list_scrollable_frame.grid(row=1,column=0,rowspan=5,columnspan=5,sticky="nsew")

    def frame5_employees_button_event(self):
        self.frame5_change_button_colors("Employees")
        self.history_list_scrollable_frame.grid_forget()
        self.history_product_list_scrollable_frame.grid_forget()
        self.history_client_list_scrollable_frame.grid_forget()
        self.history_employee_list_scrollable_frame.grid(row=1,column=0,rowspan=5,columnspan=5,sticky="nsew")

    # change the color of the frame2_navigation_bar_buttons when selected
    def frame2_change_button_colors(self,name):
        self.second_frame_navigation_bar_button1.configure(fg_color=("gray75", "gray25")if name=="Product List" else "transparent")
        self.second_frame_navigation_bar_button2.configure(fg_color=("gray75", "gray25")if name=="Add Product" else "transparent")
        self.second_frame_navigation_bar_button3.configure(fg_color=("gray75", "gray25")if name=="Update Price" else "transparent")
        self.second_frame_navigation_bar_button4.configure(fg_color=("gray75", "gray25")if name=="Edit Product" else "transparent")
    
    def frame3_change_button_colors(self,name):
        self.third_frame_navigation_bar_button1.configure(fg_color=("gray75", "gray25")if name=="Client List" else "transparent")
        self.third_frame_navigation_bar_button2.configure(fg_color=("gray75", "gray25")if name=="Add Client" else "transparent")
        self.third_frame_navigation_bar_button3.configure(fg_color=("gray75", "gray25")if name=="Edit Client" else "transparent")

    def frame4_change_button_colors(self,name):
        self.fourth_frame_navigation_bar_button1.configure(fg_color=("gray75", "gray25")if name=="Employee List" else "transparent")
        self.fourth_frame_navigation_bar_button2.configure(fg_color=("gray75", "gray25")if name=="Add Employee" else "transparent")
        self.fourth_frame_navigation_bar_button3.configure(fg_color=("gray75", "gray25")if name=="Edit Employee" else "transparent")

    def frame5_change_button_colors(self,name):
        self.fifth_frame_navigation_bar_button1.configure(fg_color=("gray75", "gray25")if name=="History List" else "transparent")
        self.fifth_frame_navigation_bar_button2.configure(fg_color=("gray75", "gray25")if name=="Products" else "transparent")
        self.fifth_frame_navigation_bar_button3.configure(fg_color=("gray75", "gray25")if name=="Clients" else "transparent")
        self.fifth_frame_navigation_bar_button4.configure(fg_color=("gray75", "gray25")if name=="Employees" else "transparent")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # get product name when selected on optionmenu
    def get_product_name_event(self,name):
        self.home_frame2_optionmenu1Var.set(name)
        product=db.getProductByName(name)
        self.home_frame2_entry1.delete(0,customtkinter.END)
        self.home_frame2_entry1.insert(0,product.name)

    # get client name when selected on optionmenu
    def get_client_name_event(self,name):
        self.home_frame2_optionmenu2Var.set(name)
        client=db.getClientByName(name)
        self.home_frame2_entry3.delete(0,customtkinter.END)
        self.home_frame2_entry3.insert(0,client.name)


    def edit_employee_name_event(self,name):
        self.edit_employee_frame_optionmenu1Var.set(name)
        employee=db.getEmployeeByName(name)
        self.edit_employee_frame_id=employee.id
        self.edit_employee_frame_entry1.delete(0,customtkinter.END)
        self.edit_employee_frame_entry2.delete(0,customtkinter.END)
        self.edit_employee_frame_entry3.delete(0,customtkinter.END)
        self.edit_employee_frame_entry4.delete(0,customtkinter.END)
        self.edit_employee_frame_entry5.delete(0,customtkinter.END)

        self.edit_employee_frame_entry1.insert(0,employee.name)
        self.edit_employee_frame_entry2.insert(0,employee.phone)
        self.edit_employee_frame_entry3.insert(0,employee.email)
        self.edit_employee_frame_entry4.insert(0,employee.username)
        self.edit_employee_frame_entry5.insert(0,employee.password)

    def edit_client_name_event(self,name):
        self.edit_client_frame_optionmenu1Var.set(name)
        client=db.getClientByName(name)
        self.edit_client_frame_id=client.id
        self.edit_client_frame_entry1.delete(0,customtkinter.END)
        self.edit_client_frame_entry2.delete(0,customtkinter.END)
        self.edit_client_frame_entry3.delete(0,customtkinter.END)

        self.edit_client_frame_entry1.insert(0,client.name)
        self.edit_client_frame_entry2.insert(0,client.phone)
        self.edit_client_frame_entry3.insert(0,client.address)

    def update_price_name_event(self,name):
        self.update_price_frame_optionmenu1Var.set(name)
        product=db.getProductByName(name)
        self.update_price_frame_entry1.delete(0,customtkinter.END)
        self.update_price_frame_entry1.insert(0,product.name)
        self.update_price_frame_entry2.delete(0,customtkinter.END)
        self.update_price_frame_entry2.insert(0,product.cost)
        self.update_price_frame_entry3.delete(0,customtkinter.END)
        self.update_price_frame_entry3.insert(0,product.price)

    def edit_product_name_event(self,name):
        self.edit_product_frame_optionmenu1Var.set(name)
        product=db.getProductByName(name)
        self.edit_product_frame_id=product.id
        self.edit_product_frame_entry1.delete(0,customtkinter.END)
        self.edit_product_frame_entry2.delete(0,customtkinter.END)
        self.edit_product_frame_entry3.delete(0,customtkinter.END)
        self.edit_product_frame_entry4.delete(0,customtkinter.END)
        self.edit_product_frame_entry5.delete(0,customtkinter.END)
        self.edit_product_frame_entry1.insert(0,product.name)
        self.edit_product_frame_entry2.insert(0,product.cost)
        self.edit_product_frame_entry3.insert(0,product.price)
        self.edit_product_frame_entry4.insert(0,product.quantity)
        self.edit_product_frame_entry5.insert(0,product.category)

    def add_product(self):
        name=self.add_product_entry1.get()
        cost=self.add_product_entry2.get()
        price=self.add_product_entry3.get()
        quantity=self.add_product_entry4.get()
        category=self.add_product_entry5.get()
        self.add_product_entry1.configure(placeholder_text_color="red",border_color="red" if len(name)==0 else self.default_color)
        self.add_product_entry2.configure(placeholder_text_color="red",border_color="red" if len(cost)==0 else self.default_color)
        self.add_product_entry3.configure(placeholder_text_color="red",border_color="red" if len(price)==0 else self.default_color)
        self.add_product_entry4.configure(placeholder_text_color="red",border_color="red" if len(quantity)==0 else self.default_color)
        self.add_product_entry5.configure(placeholder_text_color="red",border_color="red" if len(category)==0 else self.default_color)
        
        if len(name)==0 or len(cost)==0 or len(price)==0 or len(quantity)==0 or len(category)==0:
            print("False")
        else:
            try:
                db.addProduct(Product(None, name, cost, price, quantity, category))
                self.product_list_scrollable_frame.destroy()
                grid_product_list(app,db,None)
                self.control_list_sizes()
                self.home_frame2_optionmenu1.configure(values=[x.name for x in self.products])

                showinfo("Successfully added",f"{name} has been added")
            except:
                showerror("Error!","Please check your inputs")

            
    def update_price(self):
        name=self.update_price_frame_entry1.get()
        cost=self.update_price_frame_entry2.get()
        price=self.update_price_frame_entry3.get()

        self.update_price_frame_entry1.configure(placeholder_text_color="red",border_color="red" if len(name)==0 else self.default_color)
        self.update_price_frame_entry2.configure(placeholder_text_color="red",border_color="red" if len(cost)==0 else self.default_color)
        self.update_price_frame_entry2.configure(placeholder_text_color="red",border_color="red" if len(price)==0 else self.default_color)
        
        if len(name)==0 or len(cost)==0 or len(price)==0:
            print("False")
        else:
            try:
                product=db.getProductByName(name)
                db.updatePrice(Product(None,name,cost,price,None,None))
                self.update_price_frame_optionmenu1Var.set(name)
                self.update_price_frame_optionmenu1.configure(values=[x.name for x in self.products])
                self.product_list_scrollable_frame.destroy()
                grid_product_list(app,db,None)
                self.home_frame2_optionmenu1.configure(values=[x.name for x in self.products])
                showinfo("Successfully updated",f"{name} has been updated")
            except:
                showerror("Error!","Please check your inputs")

    def edit_product(self):
        name=self.edit_product_frame_entry1.get()
        cost=self.edit_product_frame_entry2.get()
        price=self.edit_product_frame_entry3.get()
        quantity=self.edit_product_frame_entry4.get()
        category=self.edit_product_frame_entry5.get()

        self.edit_product_frame_entry1.configure(placeholder_text_color="red",border_color="red" if len(name)==0 else self.default_color)
        self.edit_product_frame_entry2.configure(placeholder_text_color="red",border_color="red" if len(cost)==0 else self.default_color)
        self.edit_product_frame_entry3.configure(placeholder_text_color="red",border_color="red" if len(price)==0 else self.default_color)
        self.edit_product_frame_entry4.configure(placeholder_text_color="red",border_color="red" if len(quantity)==0 else self.default_color)
        self.edit_product_frame_entry5.configure(placeholder_text_color="red",border_color="red" if len(category)==0 else self.default_color)
        
        if len(name)==0 or len(cost)==0 or len(price)==0 or len(quantity)==0 or len(category)==0:
            print("False")
        else:
            try:
                db.editProduct(Product(self.edit_product_frame_id, name, cost, price, quantity, category))
                self.product_list_scrollable_frame.destroy()
                grid_product_list(app,db,None)
                self.edit_product_frame_optionmenu1Var.set(name)
                self.edit_product_frame_optionmenu1.configure(values=[x.name for x in self.products])
                self.home_frame2_optionmenu1.configure(values=[x.name for x in self.products])
                showinfo("Successfully edited",f"{name} has been updated")
            except:
                showerror("Error!","Please check your inputs")


    def add_client(self):
        name=self.add_client_entry1.get()
        phone=self.add_client_entry2.get()
        address=self.add_client_entry3.get()

        self.add_client_entry1.configure(placeholder_text_color="red",border_color="red" if len(name)==0 else self.default_color)
        self.add_client_entry2.configure(placeholder_text_color="red",border_color="red" if len(phone)==0 else self.default_color)
        self.add_client_entry3.configure(placeholder_text_color="red",border_color="red" if len(address)==0 else self.default_color)
        
        if len(name)==0 or len(phone)==0 or len(address)==0:
            print("False")
        else:
            try:
                db.addClient(Client(None,name,phone,address))
                self.client_list_scrollable_frame.destroy()
                grid_client_list(app,db,None)
                self.control_list_sizes()
                self.home_frame2_optionmenu2.configure(values=[x.name for x in self.clients])
                showinfo("Successfully Added",f"{name} has been added")
            except:
                showerror("Error!","Please check your inputs")

    def edit_client(self):
        name=self.edit_client_frame_entry1.get()
        phone=self.edit_client_frame_entry2.get()
        address=self.edit_client_frame_entry3.get()

        self.edit_client_frame_entry1.configure(placeholder_text_color="red",border_color="red" if len(name)==0 else self.default_color)
        self.edit_client_frame_entry2.configure(placeholder_text_color="red",border_color="red" if len(phone)==0 else self.default_color)
        self.edit_client_frame_entry3.configure(placeholder_text_color="red",border_color="red" if len(address)==0 else self.default_color)
        
        if len(name)==0 or len(phone)==0 or len(address)==0:
            print("False")
        else:
            try:
                db.editClient(Client(self.edit_client_frame_id,name,phone,address))
                self.client_list_scrollable_frame.destroy()
                grid_client_list(app,db,None)
                self.edit_client_frame_optionmenu1.set(name)
                self.edit_client_frame_optionmenu1.configure(values=[x.name for x in self.clients])
                self.home_frame2_optionmenu2.configure(values=[x.name for x in self.clients])
                showinfo("Successfully Updated",f"{name} has been Updated")
            except:
                showerror("Error!","Please check your inputs")

    def add_employee(self):
        name=self.add_employee_entry1.get()
        phone=self.add_employee_entry2.get()
        email=self.add_employee_entry3.get()
        username=self.add_employee_entry4.get()
        password=self.add_employee_entry5.get()

        self.add_employee_entry1.configure(placeholder_text_color="red",border_color="red" if len(name)==0 else self.default_color)
        self.add_employee_entry2.configure(placeholder_text_color="red",border_color="red" if len(phone)==0 else self.default_color)
        self.add_employee_entry3.configure(placeholder_text_color="red",border_color="red" if len(email)==0 else self.default_color)
        self.add_employee_entry4.configure(placeholder_text_color="red",border_color="red" if len(username)==0 else self.default_color)
        self.add_employee_entry5.configure(placeholder_text_color="red",border_color="red" if len(password)==0 else self.default_color)
        
        if len(name)==0 or len(phone)==0 or len(email)==0 or len(username)==0 or len(password)==0:
            print("False")
        else:
            try:
                db.addEmployee(Employee(None,name,phone,email,username,password))
                self.employee_list_scrollable_frame.destroy()
                grid_employee_list(app,db,None)
                self.control_list_sizes()
                showinfo("Successfully Added",f"{name} has been added")
            except:
                showerror("Error!","Please check your inputs")

    def edit_employee(self):
        name=self.edit_employee_frame_entry1.get()
        phone=self.edit_employee_frame_entry2.get()
        email=self.edit_employee_frame_entry3.get()
        username=self.edit_employee_frame_entry4.get()
        password=self.edit_employee_frame_entry5.get()
        self.edit_employee_frame_entry1.configure(placeholder_text_color="red",border_color="red" if len(name)==0 else self.default_color)
        self.edit_employee_frame_entry2.configure(placeholder_text_color="red",border_color="red" if len(phone)==0 else self.default_color)
        self.edit_employee_frame_entry3.configure(placeholder_text_color="red",border_color="red" if len(email)==0 else self.default_color)
        self.edit_employee_frame_entry4.configure(placeholder_text_color="red",border_color="red" if len(username)==0 else self.default_color)
        self.edit_employee_frame_entry5.configure(placeholder_text_color="red",border_color="red" if len(password)==0 else self.default_color)
        
        if len(name)==0 or len(phone)==0 or len(email)==0 or len(username)==0 or len(password)==0:
            print("False")
        else:
            try:
                db.editEmployee(Employee(self.edit_employee_frame_id,name,phone,email,username,password))
                self.employee_list_scrollable_frame.destroy()
                grid_employee_list(app,db,None)
                self.edit_employee_frame_optionmenu1.set(name)
                self.edit_employee_frame_optionmenu1.configure(values=[x.name for x in self.employees])
                showinfo("Successfully Updated",f"{name} has been Updated")
            except:
                showerror("Error","Could not update")

    def sell_product(self):
        name=self.home_frame2_entry1.get()
        quantity=self.home_frame2_entry2.get()
        client=self.home_frame2_entry3.get()
        if len(quantity)==0:
            quantity=1
        quantity=int(quantity)
        current_time=time.strftime("%Y-%m-%d %H:%M:%S")
        self.home_frame2_entry1.configure(placeholder_text_color="red",border_color="red" if len(name)==0 else self.default_color)
        self.home_frame2_entry3.configure(placeholder_text_color="red",border_color="red" if len(client)==0 else self.default_color)
        if len(name)==0 or len(client)==0:
            print("False")
        else:
            try:
                product=db.getProductByName(name)
                if quantity<=product.quantity:
                    isClient=db.getClientByName(client)
                    db.addIntoHistory(History(None,product.name,product.cost,product.price,quantity,product.category,client,
                    current_time,self.employee_username))
                    db.decreaseQuantity(name,quantity)
                    self.product_list_scrollable_frame.destroy()
                    grid_product_list(app,db,None)

                    self.home_frame2_optionmenu1Var.set(name)
                    self.home_frame2_optionmenu1.configure(values=[x.name for x in self.products])
                    self.home_frame2_optionmenu2Var.set(client)
                    self.home_frame2_optionmenu2.configure(values=[x.name for x in self.clients])
                    showinfo("Successfully Sold",f"{quantity} {name} have been sold")
                else:
                    showerror("Error",f"Only {product.quantity} {product.name} available")

            except:
                showerror("Error",f"Could not find product or client")
                
if __name__ == "__main__":
    app=App()
    app.mainloop()