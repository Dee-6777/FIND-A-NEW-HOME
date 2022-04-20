import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("data//Housing.csv")
x = np.array(data[data.columns[1:]]).reshape(-1, 1)
lr = LinearRegression()
lr.fit(x, np.array(data['price']))

import pandas as pd
data = pd.read_csv("Housing.csv")

nav=st.sidebar.radio("Navigation",["Home","About","Prediction","Contribute"])
if nav=="Home":
    st.title("Welcome!")
    st.image("Yellow and Black Home Loans Tri-fold Brochure.png",width=800)
    if st.checkbox("SHOW RECENT DATASET"):
        st.table(data)

    graph = st.selectbox("What kind of graph ?",["Non-Interactive","Interactive"])
    if graph == "Non-Interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["area"],data["price"])
        plt.ylim(0)
        plt.xlabel("Area of the house (in feet²)")
        plt.ylabel("Market Price")
        plt.tight_layout()
        st.pyplot()

    if graph == "Interactive":
        layout = go.Layout(
            xaxis=dict(range=[2000, 16000]),
            yaxis=dict(range=[2000000, 12000000])

        fig = go.Figure(data=go.Scatter(x=data["area"], y=data["price"], mode='markers'), layout=layout)
        st.plotly_chart(fig)
        )
if nav == "About":
    st.title("About")
    st.image("Yellow and Black Home Loans Tri-fold Brochure (3).png",width=1000)


if nav == "Prediction":
    st.header("Know your Salary")
    val = st.number_input("Enter you exp", 0.00, 20.00, step=0.25)
    val = np.array(val).reshape(1, -1)
    pred = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"The predicted price for your home is {round(pred)}")

if nav == "Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your Experience", 0.0, 20.0)
    sal = st.number_input("Enter your Salary", 0.00, 1000000.00, step=1000.0)
    if st.button("submit"):
        to_add = {"YearsExperience": [ex], "Salary": [sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data//Housing.csv", mode='a', header=False, index=False)
        st.success("Submitted")