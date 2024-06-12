import streamlit as st 
st.title("CALCULATOR")
st.markdown("Welcome To My First Streamlit App")   #here markdown is used as sub-heading

c1,c2=st.columns(2)
fnum=c1.number_input("Enter a first number")
snum=c2.number_input("Enter a second number")

options=["Add","Sub","Mult","Div"]
choice=st.radio("Select an operator", options, horizontal=True)  #if we remove horizontal we get in vertical

button=st.button("Calculate")

if button:
    if choice=="Add":
        result=fnum+snum
    if choice=="Sub":
        result=fnum-snum
    if choice=="Mult":
        result=fnum*snum
    if choice=="Div":
        result=fnum/snum
        
st.success(f"result is {result}")     #warning=yellow color,dangger =red success=green
            