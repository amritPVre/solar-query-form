# -*- coding: utf-8 -*-
"""
Created on Mon May 22 01:47:14 2023

@author: amrit
"""

import streamlit as st

st.set_page_config(page_title="Disclaimer", page_icon="🧑🏻‍💻🦱")

def about_me():
    st.write("# Welcome to My App Collections! 👋")
    st.markdown('____')
    st.title("About Me")

    st.header("Amrit Mandal")
    st.markdown("""
    - Phone: +91 8116401052
    - Email: [amrit.mandal0191@gmail.com](mailto:amrit.mandal0191@gmail.com)
    - LinkedIn: [https://www.linkedin.com/in/amritmandal](https://www.linkedin.com/in/amritmandal)
    """)
    st.markdown('____')
    st.subheader("Solar PV Professional")
    st.markdown("""
    - Software Skills: Pvsyst, PlantPredict, Helioscope, AutoCAD, SketchUp, SolarGIS, HOMER, MS Office & Project & Other various Solar PV Engg. Related Tools
    - Soft Skills: Creativity, Collaboration, Problem Solving, Communication
    """)
    st.markdown('____')
    st.subheader("Objective")
    st.markdown("""
    With over 10 years of experience and involvement in 2 GW+ Solar Projects from 18 different countries in various Technical Managerial roles and capabilities, while working closely with Industry leaders I’m focused to take charge of A Senior Management role in Techno commercial functions with growth oriented Solar/ Renewable Energy Company, where my strong business acumen, ability to organize, implement and developing managing people can help create drive Industry leading transactions profits.
    """)
    st.markdown('____')
    

    st.subheader("Work Experience")
    st.markdown("""
    - HTC (Hussam Technology Company), Muscat, Oman: Engineering Manager, Solar (January 2020 - Present)
    - AMPL Cleantech Pvt Ltd (ATHAGROUP), Kolkata, India: Assistant Manager, Design & Development (October 2016 - December 2019)
    - Kirti Solar Limited, Kolkata, India: Technical Lead (March 2016 - October 2016)
    - O3 Energy Solutions, LLC (Under DSSPL), Chandigarh, India: Senior Design Engineer (December 2015 - March 2016)
    - OhmSolar & Technologies, Burdwan, India: Co-Founder & Sr. Consultant (May 2014 - November 2015)
    - Annapurna Export, Kolkata, India: Project Engineer (December 2013 - April 2014)
    - ONergy (Punam Energy Pvt Ltd), Kolkata, India: Project Coordinator (July 2013 - November 2013)
    """)
    st.markdown('____')
    st.subheader("Education & Professional Certifications")
    st.markdown("""
    - B.Tech in Electrical Engineering, St. Thomas College of Engineering & Technology, MAKAUT, WB, IN (Received Degree in 2013)
    - MicroMasters in General Business Management, IIM Bangalore, via EDX (2017 - 2018)
    - Professional Certificate in Business & Financial Modelling, Wharton Business School, via Coursera (2017 - 2018)
    - Professional Certificate in Data Analysis & Presentation skills, PwC Academy, via Coursera (2017 - 2018)
    - Certificate in Data Science (R Basics), Harvard T.Chan Medical School, via EDX
    - Certificate in Advanced Solar Energy, TUDELFT, via EDX (2013 - 2014)
    """)

    

# Call the function to display the page
about_me()
