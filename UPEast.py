import streamlit as st
import pickle as pkl

def app():
    st.header(':blue[UP east] :red[Rain Prediction model]')
    value = st.text_input('Enter Annual Rainfall you want :')
    if st.button('Predict Rainfall This Year') :
        if value == '':
            st.warning('Please Enter Annual Rainfall')
        else :
            try :
                model = pkl.load(open('UPEastModel.pkl','rb'))
                value = float(value)
                input = [[]]
                input[0].append(value)
                output = model.predict(input)
                st.success('Rainfall in June      : '+str(output[0][0]))
                st.success('Rainfall in July      : '+str(output[0][1]))
                st.success('Rainfall in August    : '+str(output[0][2]))
                st.success('Rainfall in September : '+str(output[0][3]))
            except :
                st.warning('Enter Annual Rainfall in Decimal Format')
