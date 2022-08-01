import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split


#st.title("Predictor")

data = pd.read_csv("Housing.csv")



nav=st.sidebar.radio("Navigation",["Home","About","Prediction","Contribute"])
if nav=="Home":
    st.title("Welcome!")
    st.image("Yellow and Black Home Loans Tri-fold Brochure.png",width=800)
    if st.checkbox("SHOW RECENT DATASET"):
        st.table(data)

    graph = st.selectbox("What kind of graph ?",["Non-Interactive","Interactive"])
    val = st.slider("Filter data using area",2000,16000)
    data = data.loc[data["area"]>= val]
    if graph == "Non-Interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["area"],data["price"])
        plt.ylim(0)
        plt.xlabel("Area of the house (in feet²)")
        plt.ylabel("Market Price")
        plt.tight_layout()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    if graph == "Interactive":
        layout = go.Layout(
            xaxis=dict(range=[2000, 12000]),
            yaxis=dict(range=[2000000, 12000000])
        )
        fig = go.Figure(data=go.Scatter(x=data["area"], y=data["price"], mode='markers'), layout = layout)
        st.plotly_chart(fig)
        
if nav == "About":
    st.title("About")
    st.image("Yellow and Black Home Loans Tri-fold Brochure (3).png",width=1000)


if nav == "Prediction":
    st.header("Know the Price")

    # Mainroad
    data.mainroad.replace(['yes','no'],[1,0], inplace=True) 
    # Guestroom
    data.guestroom.replace(['yes','no'],[1,0], inplace=True)
    # Basement
    data.basement.replace(['yes','no'],[1,0], inplace=True)
    # hotwaterheating
    data.hotwaterheating.replace(['yes','no'],[1,0], inplace=True)
    # airconditioning
    data.airconditioning.replace(['yes','no'],[1,0], inplace=True)
    # prefarea
    data.prefarea.replace(['yes','no'],[1,0], inplace=True)
    # furnishingstatus
    data.furnishingstatus.replace(['furnished','unfurnished','semi-furnished'],[1,0,2], inplace=True)
    X = data.drop('price', axis=1)
    y = data.price
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    pred_y = model.predict(X_test)

    ar = st.number_input("Enter the Area", 2000, 120000)
    bd = st.number_input("Enter no of Bedrooms", 0, 4)
    bt = st.number_input("Enter no of Bathrooms", 0, 2)
    sr = st.number_input("Enter no of stories", 0, 4)
    main = st.number_input("Mainroad is present or not? (yes(1) / no(0))", 0, 1)
    guest = st.number_input("Guestroom is present or not? (yes(1) / no(0))", 0, 1)
    base = st.number_input("Basement is present or not? (yes(1) / no(0))", 0, 1)
    water = st.number_input("Hotwaterheating is present or not? (yes(1) / no(0))", 0, 1)
    ac = st.number_input("Airconditioning is present or not? (yes(1) / no(0))", 0, 1)
    parking = st.number_input("No of parking lots", 0, 4)
    parea = st.number_input("Preferred area? (yes(1) / no(0))", 0, 1)
    furstatus = st.number_input("Furnishing status? (furnished(1) / semi-furnished(2) / unfurnished(0)", 0, 2)

    b=model.predict([[ar,bd,bt,sr,main,guest,base,water,ac,parking,parea,furstatus]])

    if st.button("Predict"):
        st.success(f"The predicted price for your home is {b}")


if nav == "Contribute":
    st.header("Contribute to our dataset")
    pr = st.number_input("Enter the Price", 2000000, 12000000, step=1000)
    ar = st.number_input("Enter the Area", 2000, 120000)
    bd = st.number_input("Enter no of Bedrooms", 0, 4)
    bt = st.number_input("Enter no of Bathrooms", 0, 2)
    sr = st.number_input("Enter no of stories", 0, 4)
    main = st.text_input("Mainroad is present or not? (yes / no)")
    guest = st.text_input("Guestroom is present or not? (yes / no)")
    base = st.text_input("Basement is present or not? (yes / no)")
    water = st.text_input("Hotwaterheating is present or not? (yes / no)")
    ac = st.text_input("Airconditioning is present or not? (yes / no)")
    parking = st.number_input("No of parking lots",0,4)
    parea = st.text_input("Preferred area? (yes / no)")
    furstatus = st.text_input("Furnishing status? (furnished / semi-furnished / unfurnished")
    if st.button("submit"):
        to_add = {"price": [pr], "area": [ar],"bedrooms":[bd],"bathrooms":[bt],"stories":[sr],"mainroad":[main],"guestroom":[guest],"basement":[base],"hotwaterheating":[water],"airconditioning":[ac],"parking":[parking],"prefarea":[parea],"furnishingstatus":[furstatus]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("Housing.csv", mode='a', header=False, index=False)
        st.success("Submitted")

# Mainroad
data.mainroad.replace([1,0],['yes','no'], inplace=True)
# Guestroom
data.guestroom.replace([1,0],['yes','no'], inplace=True)
# Basement
data.basement.replace([1,0],['yes','no'], inplace=True)
# hotwaterheating
data.hotwaterheating.replace([1,0],['yes','no'], inplace=True)
# airconditioning
data.airconditioning.replace([1,0],['yes','no'], inplace=True)
# prefarea
data.prefarea.replace([1,0],['yes','no'], inplace=True)
# furnishingstatus
data.furnishingstatus.replace([1,0,2],['furnished','unfurnished','semi-furnished'], inplace=True)