# Example-1

# class Railway_Station:
#     stn_name="Visakhapatnam Railway Station"
#     def assignData(self, Train_No, Platform_No):
#         self.Train_Number = Train_No
#         self.Platform_Number = Platform_No
#     def displayDetails(self):
#         print("Station Name : ", Railway_Station.stn_name)
#         print("Train Number : ",self.Train_Number)
#         print("Platform Number : ",self.Platform_Number)
# train1 = Railway_Station()
# train1.assignData(12717, 7)
# print("---------Train-1 Details-----------")
# train1.displayDetails()

# train2 = Railway_Station()
# train2.assignData(14625, 3)
# print("---------Train-2 Deatils-----------")
# train2.displayDetails()





# Example-2

class Social_Media:
    app_name="Twitter"
    def assignData(self, name, Age):
        self.Username=name
        self.UserAge=Age
    def displayDetails(self):
        print("App Name :", Social_Media.app_name)
        print("Username :", self.Username)
        print("User Age :", self.UserAge)
user1=Social_Media()
user1.assignData("Ramesh", 22)
print("-----------User-1 details------------")
user1.displayDetails()

user2 = Social_Media()
user2.assignData("Naveen", 27)
print("-----------User-2 details------------")
user2.displayDetails()