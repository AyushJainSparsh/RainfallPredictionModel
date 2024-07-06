import streamlit as st
from streamlit_option_menu import option_menu

import home , about , UPEast , UPWest

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_apps(self , title , function):
        self.apps.append ({
            'title' : title ,
            'function' : function 
            })
    def run():
        with st.sidebar :
            app = option_menu(
                menu_title = 'Rain Prediction' ,
                options=['Home','About','UP East Climate','UP West Climate'] ,
                icons = ['house-fill','info-circle-fill','cloud-lightning-rain-fill','cloud-lightning-rain-fill'],
                menu_icon='cloud-rain-fill',
                default_index=1,
                styles = {
                    "Container":{'Padding':'5!important','background-color' : 'blue'},
                    'icon':{'color':'white','font-size' : '25px'},
                    'nav-link':{'color':'white','font-size':'20px','text-align':'left','margin':'0px','--hover-color':'blue'},
                    'nav-link-selected':{'background-color':'#02ab21'}}
            )
        if app == 'Home':
            home.app()
        if app == 'About':
            about.app()
        if app == 'UP East Climate' :
            UPEast.app()
        if app == 'UP West Climate' :
            UPWest.app()
    run()