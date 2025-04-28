import streamlit as st
def convert_units(value: float ,unit_from: str,unit_to: str):
# #     # print("value>>>",value)
#     # print("unit_from>>>,unit_from")
#     # print("unit_to>>>",unit_to)
    if unit_from =="kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from =="meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from =="kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_from =="grams" and unit_to == "kilograms":
        return value * 0.001
    elif unit_from =="meters" and unit_to == "centimeters":
        return value * 100
    elif unit_from =="centimeters" and unit_to == "meters":
        return value * 0.01
    else:
        return "conversion is not supported"
# result = convert_units(2.5, "kilometers", "meters")   
# print("The value in meters is",result) 
def main():
    st.title("unit converter")
    st.write("Welcome to Unit Converter!")
    value=st.number_input("Enter the Value you Want to convert:",min_value=0.0)
    unit_from=st.text_input("Enter the value you want to convert from(e.g meters,kilometers,grams,kilograms,meters,centimeters)")
    unit_to=st.text_input("Enter the value you want from conversion(e.g meters,kilometers,grams,kilograms,meters,centimeters )") 
    if st.button("convert"):
        result= convert_units(value,unit_from,unit_to)
        st.write("conveteted value is",result)
    # print("unit converter")
    # print("Welcome to Unit Converter!")
    # value=float(input("Enter the Value you Want to convert:"))
    # unit_from=input("Enter the value you want to convert from(e.g meters,kilometers,grams,kilograms,meters,centimeters)")
    # unit_to=input("Enter the value you want from conversion(e.g meters,kilometers,grams,kilograms,meters,centimeters )") 
    # print("value",value)
    # print("unit_from",unit_from)
    # print("unit_to",unit_to)
    
main()    