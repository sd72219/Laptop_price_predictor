import pickle, os
from sklearn.preprocessing import StandardScaler
model_folder_name = 'model'


def get_price(Company, TypeName, Inches, ScreenResolution, Cpu, Ram,
       Memory, Gpu, OpSys, Weight):
    print("Price API Testing")
   #  std_scale = StandardScaler()

   #  scale = std_scale.transform([[Company, TypeName, Inches, ScreenResolution, Cpu, Ram,
   #     Memory, Gpu, OpSys, Weight]])
    
    ran_model = pickle.load(open(f"{model_folder_name}/laptop_pickle2.pkl", 'rb'))
    
    res = ran_model.predict([[Company, TypeName, Inches, ScreenResolution, Cpu, Ram, Memory, Gpu, OpSys, Weight]])
    return res[0]


# def get_charges(Avg_Session_Length, Time_on_App, Length_of_Membership):
#     print("Charges API Testing")

#     linear_model = pickle.load(open(f"{model_folder_name}/pricepickle.pkl", 'rb'))

#     pred = linear_model.predict([[Avg_Session_Length, Time_on_App, Length_of_Membership]])

#     return pred[0] 