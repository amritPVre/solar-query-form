# -*- coding: utf-8 -*-
"""
Created on Sat May 20 01:24:08 2023

@author: amrit
"""

import streamlit as st
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import folium
from streamlit_folium import folium_static


st.set_page_config(page_icon='🛰️',page_title="Solar Project Query Form")

mail_pass=st.secrets['mail_pass']

st.markdown(
    """
    <div style="background-color:#464e59;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Solar Project Inquiry Form</h1>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write('\n')

# Form fields
project_types = ['Utility Scale', 'Commercial','Residential']
roof_types = ['Flat', 'Sloped', 'Other']
business_types = ['Retail', 'Office', 'Other']
financing_methods = ['Self-financed', 'Loan']
grid_interconnect_voltage_options = ['440V', '480V', '11kV', '20kV', '33kV', '66kV', '110kV', 'Other']
grid_frequency_options = ['50Hz', '60Hz']
install_types = ['Flat Roof', 'Factory/Warehouse Shed', 'Ground Mount']
hv_types = ['11kV','33kV','66kV', '110kV', '132kV','220kV', 'Other']
soil_types = ['Sandy', 'Clay', 'Slit', 'Loam', 'Rocky', 'Peat']
study_types = ['Site Survey Report', 'Hydrology Study Report', 'Contour Mapping', 'Flood Study','Topological Survey Report']

# Start the app
st.markdown("___")

st.markdown(
    """
    <div style="background-color:#464e59;padding:4px;border-radius:10px">
    <h3 style="color:white;text-align:center;">Client Details</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write('\n')

# User inputs
col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input('Name')
    email = st.text_input('Email')
    phone = st.text_input('Phone Number')
with col2:
    company_name = st.text_input('Company Name')
    website = st.text_input('Website (optional)')
    Address=  st.text_input('Website')
with col3:
    project_location_country = st.text_input('Project location Country')
    grid_interconnect_voltage = st.selectbox('Grid Interconnect Voltage', grid_interconnect_voltage_options)
    grid_frequency = st.selectbox('Grid Frequency', grid_frequency_options)

st.markdown("------")

st.markdown(
    """
    <div style="background-color:#464e59;padding:4px;border-radius:10px">
    <h3 style="color:white;text-align:center;">Technical Insights</h3>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write('\n')

col1, col2 = st.columns([1,1])
with col1:
    lat=st.number_input('latitude',22.5)
with col2:
    lon=st.number_input('longitude',73.8)


df_panels = pd.read_csv('solar_panel_list.csv')
df_inverters = pd.read_csv('solar_inverter_list.csv')

# Get the list of manufacturers
panel_manufacturers = df_panels['Manufacturers_list'].tolist()
inverter_manufacturers = df_inverters['Manufacturers_list'].tolist()


#css for submit & enter buttons
primaryColor = st.get_option("theme.primaryColor")
s = f"""
    <style>
    div.stButton > button:first-child {{ border: 5px solid {primaryColor};background: linear-gradient(90deg, #2e0088, #3c0392, #4a089d, #570da7, #6513b1, #7218bb, #7f1dc6, #8d22d0);
                                                                                                      color:#ffffff; border-radius:5px 5px 5px 5px; }}
    div.stButton > button:hover {{background: #f95d6a;color:#003f5c}}
                                                                                                      
    <style>
    """
st.markdown(s, unsafe_allow_html=True)




# Add the dropdowns to the Streamlit app
with col1:
    
    selected_panel_manufacturer = st.selectbox('Select a solar panel manufacturer', panel_manufacturers)
with col2:
    
    selected_inverter_manufacturer = st.selectbox('Select a solar inverter manufacturer', inverter_manufacturers)
#------------------------Location Map------------------------------------
# center on Coordinate
col1,col2,col3=st.columns([1.25,.5,1.25])
if col2.button('Enter'):
    m = folium.Map(location=(lat,lon), zoom_start=8,
                   width='100%',height='80%',control_scale=True,
                   position='relative',zoom_control=True,
                   )
    
      # add marker for Coordinate
    tooltip = "Proposed Solar PV Site"
    folium.Marker(
        (lat,lon), popup="Proposed Solar PV Site", tooltip=tooltip
       ).add_to(m)
    # call to render Folium map in Streamlit
    folium_static(m)


st.markdown("------")

#section Heading

st.markdown(
    """
    <div style="background-color:#464e59;padding:4px;border-radius:10px">
    <h3 style="color:white;text-align:center;">Project Specific Details</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write('\n')


#project specific details
project_type = st.selectbox('Project Type', project_types)



# Conditional inputs based on project type
if project_type == 'Residential':
    project_capacity = st.slider('Project Capacity (kW)', 10, 100, step=10)
    house_size = st.number_input('House Size (in sq. ft)')
    electricity_bill = st.number_input('Average Monthly Electricity Bill')
    roof_type = st.selectbox('Roof Type', roof_types)
    if roof_type=='sloped':
        slope=st.number_input('Please mention the slope angle of the shed roof',0,89,5)
    

elif project_type == 'Commercial':
    project_capacity = st.slider('Project Capacity (MW)', 0.1, 10.0, step=0.1)
    business_name = st.text_input('Business Name')
    business_type = st.selectbox('Business Type', business_types)
    facility_size = st.number_input('Facility Size (in sq. ft)')
    electricity_bill = st.number_input('Average Monthly Electricity Bill')
    install_type = st.selectbox('Type of Installation', install_types)
    if install_type =='Flat Roof':
        Usable_area=st.number_input('Available Shadow Free Roof Area (in sq. ft)')
        #roof_layout_plan = st.file_uploader('Please upload roof layout plan', type=['pdf'])
    elif install_type =='Factory/Warehouse Shed':
        Usable_area=st.number_input('Available Shadow Free Roof Area (in sq. ft)')
        slope=st.number_input('Please mention the slope angle of the shed roof',0,89,5)
        #roof_layout_plan = st.file_uploader('Please upload roof layout plan', type=['pdf'])
       #elevation_dwg = st.file_uploader('Please upload Building elevation Drawing', type=['pdf'])
    else:
        Usable_area = st.number_input('Land Area (in acres)')
        #land_map=st.file_uploader('Please upload land Map', type=['pdf'])
    

elif project_type == 'Utility Scale':
    col1, col2 = st.columns(2)
    with col1:
        
        project_capacity = st.slider('Project Capacity', 10, 1000, step=5)
        #project_size = st.number_input('Project Size (in MW)')
        land_area = st.number_input('Land Area (in acres)')
        interconnect_voltage=st.selectbox('Susbstation Voltage (kV)', hv_types)
        
    with col2:
        
        grid_connection_point = st.slider('Grid Connection Point (Substation proximity in km)',0.5,200.0,step=0.5)
        soil_type = st.selectbox('Please Select Type of Soil', soil_types)
        study_type = st.multiselect('Select the Options if already done/ Available', study_types)
                                                  
    
    
    
    
    
#Project Finance Related Inputs
st.markdown('___')
st.markdown(
    """
    <div style="background-color:#464e59;padding:4px;border-radius:10px">
    <h3 style="color:white;text-align:center;">Financial Questionnaires</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

budget = st.number_input('Expected Project Cost in $Millions')
financing_method = st.selectbox('Financing Method', financing_methods)

if financing_method == 'Loan':
    Expected_budget=st.number_input('Expected Project Cost in $Millions')
    debt_equity_ratio = st.number_input('Debt Equity Ratio')
    interest_rate = st.number_input('Interest Rate')
    term_period = st.number_input('Term Period')


st.markdown("------")

if project_type == 'Residential':
    roof_layout_plan = st.file_uploader('Please upload roof layout plan', type=['pdf'])
    elevation_dwg = st.file_uploader('Please upload Building elevation Drawing', type=['pdf'])
elif project_type == 'Utility Scale':
    land_map=st.file_uploader('Please upload land Map', type=['pdf'])
    




# Submit button
col1, col2,col3=st.columns([1.25,.5,1.25])
if col2.button('Submit'):
    # Save data to a CSV file
    data = {'Name': name, 'Email': email, 'Phone Number': phone, 'Project Type': project_type, 'Expected Project Budget $M': budget, 'Financing Method': financing_method,
            'company name':company_name, 'website':website,'project location country': project_location_country,
            'grid_interconnect_voltage':grid_interconnect_voltage, 'Grid Frequency':grid_frequency,
            'latitude':lat, 'longitude':lon,'panel_manufacturers':panel_manufacturers,'inverter_manufacturers':inverter_manufacturers
            }
    if financing_method == 'Loan':
        data.update({'Debt Equity Ratio': debt_equity_ratio, 'Interest Rate': interest_rate, 'Term Period': term_period})
    if project_type == 'Residential':
        data.update({'House Size': house_size, 'Average Monthly Electricity Bill': electricity_bill,'project capacity (kW)':project_capacity, 'Roof Type': roof_type})
        if roof_type=='Sloped':
            data.update({'slope':slope})
    elif project_type == 'Commercial':
        data.update({'project capacity(MW)':project_capacity,'Business Name': business_name, 'Business Type': business_type, 'Facility Size': facility_size, 'Average Monthly Electricity Bill': electricity_bill,'installation type':install_type})
        if install_type=='Flat Roof':
            data.update({'Usable Area':Usable_area})
        elif install_type=='Factory/Warehouse Shed':
            data.update({'Usable Area':Usable_area,'slope':slope})
        elif install_type=='Ground Mount':
            data.update({'Usable Area (Acres)':Usable_area})
    elif project_type == 'Utility Scale':
        data.update({'Project Capacity': project_capacity, 'Land Area': land_area, 'Grid Connection Point': grid_connection_point,'interconnect_voltage':interconnect_voltage,
                    'soil_type':soil_type, 'study_type':study_type 
                     })
    df = pd.DataFrame([data])
    df.to_csv('form_data.csv', index=False)

    # Send the CSV file as an email attachment
    msg = MIMEMultipart()
    msg['From'] = 'solarapp98@gmail.com'
    msg['To'] = 'minutes2energy@gmail.com'
    msg['Subject'] = 'New Solar Project Inquiry'

    with open('form_data.csv', 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="form_data.csv"')
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('solarapp98@gmail.com', mail_pass)
    text = msg.as_string()
    server.sendmail('solarapp98@gmail.com', 'minutes2energy@gmail.com', text)
    server.quit()

    st.success('Form submitted successfully.')
