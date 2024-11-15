import streamlit as st
import streamlit_option_menu as som

import UPEast , UPWest


def app():
    app = som.option_menu(
        menu_title = 'Home :' ,
        options=['Uttar Pradesh Eastern Climate','Uttar Pradesh Western Climate'] ,
        icons = ['cloud-lightning-rain','cloud-lightning-rain'],
        menu_icon='house-fill',
        default_index=0,
        styles = {
            "Container":{'Padding':'5!important','background-color' : 'blue'},
            'icon':{'font-size' : '25px'},
            'nav-link':{'font-size':'20px','text-align':'left','margin':'0px','--hover-color':'blue'},
            'nav-link-selected':{'background-color':'red'}}
    )
    if app == 'Uttar Pradesh Eastern Climate':
        UPEast.app()
    if app == 'Uttar Pradesh Western Climate':
        UPWest.app()
