import streamlit as st
import home
def app():
    #st.header(':blue[About Us :]')
    st.markdown('# :blue[About :]')
    st.write(':red[As we all well aware that rainfall is a natural phenomenon]'
             +':red[no one can give the prediction anything regard that like]'
              +':red[ how much rainfall occur this year.]')
    st.write(':red[So our team just prepare a model which predict that how much]'
             +':red[ occur on monsoon months to meet the required annual rainfall]'
             +':red[supply.]')
    
    st.markdown('##### :blue[How our app work :]')
    st.write(':red[1. You First have to select a region from where you want prediction.]')
    st.write(':red[2. Then you have to enter Annual Rainfall you want this year as input.]')
    st.write(':red[3. As a Output you will get monsoon months of that reason and the rainfall]'
             +':red[ required in that month to reach that level of annual rainfall]')
    
    st.markdown('##### :blue[Precaution :]')
    st.warning('Annual Rainfall is only accepted in integer or decimal format other'
               +' than these format will lead to error and you will don\'t get you required output you want.')
    
    st.markdown('#### :rainbow[Thank You]')
