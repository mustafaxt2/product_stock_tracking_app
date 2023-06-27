import os,customtkinter
from PIL import Image
class Images:
    def __init__(self):
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "home.png")),
                                                    dark_image=Image.open(os.path.join(self.image_path, "home.png")), size=(20, 20))

        self.add_user_image20 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "addUser.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "addUser.png")), size=(20, 20))
        self.add_user_image50 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "addUser.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "addUser.png")), size=(50, 50))

        self.most_sale_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "growth.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "growth.png")), size=(20, 20))

        self.brand_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "tag.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "tag.png")), size=(20, 20))

        self.product_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "package.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "package.png")), size=(20, 20))

        self.users_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "group.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "group.png")), size=(20, 20))

        self.login_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "login.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "login.png")), size=(75,75))

        self.logout_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "logout.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "logout.png")), size=(40,40))

        self.calendar_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "calendar.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "calendar.png")), size=(20,20))

        self.sell_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "exchange.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "exchange.png")), size=(50,50)) 
            
        self.history_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "clock.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "clock.png")), size=(20,20)) 

        self.edit_image20 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "wrench.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "wrench.png")), size=(20,20)) 
        self.edit_image50 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "wrench.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "wrench.png")), size=(50,50))

        self.add_button_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "addButton.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "addButton.png")), size=(20,20))

        self.add_product_image20 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "addProduct.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "addProduct.png")), size=(20,20))       
        self.add_product_image50 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "addProduct.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "addProduct.png")), size=(50,50))  

        self.update_price_image20 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "pen.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "pen.png")), size=(20,20))
                
        self.update_price_image50 = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "pen.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "pen.png")), size=(50,50))  

        self.list_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "list.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "list.png")), size=(20,20))

        self.save_changes_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "diskette.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "diskette.png")), size=(20,20))

        self.sell_button_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "coin.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "coin.png")), size=(20,20))

        self.user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "user.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "user.png")), size=(20,20))

        self.unaccessible_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "vision.png")),
                                                        dark_image=Image.open(os.path.join(self.image_path, "vision.png")), size=(20,20))
