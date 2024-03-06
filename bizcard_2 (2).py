

!pip install streamlit_option_menu
!pip install streamlit
!pip install easyocr
!pip install streamlit
!pip install pyngrok
!npm install localtunnel


# %%writefile app.py
# import os
# import easyocr
# import cv2
# from matplotlib import pyplot as plt
# import numpy as np
# import streamlit as st
# import psycopg2
# import re
# from streamlit_option_menu import option_menu
# import pandas as pd
# import sqlite3
# 
# 
# IMAGE_PATH = "/content/img.png"
# 
# reader = easyocr.Reader(['en'])
# result = reader.readtext(IMAGE_PATH,paragraph="False")
# result
# 
# 
# 
# # SETTING PAGE CONFIGURATIONS
# 
# IMAGE_PATH = "/content/img.png"
# 
# st.set_page_config(
#     page_title="BizCardX: Extracting Business Card Data with OCR | By Geethapriyan",
#     page_icon=IMAGE_PATH,
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={'About': """# This OCR app is created by *Geethapriyan*!"""})
# 
# st.markdown("<h1 style='text-align: center; color: white;'>BizCardX: Extracting Business Card Data with OCR</h1>", unsafe_allow_html=True)
# 
# 
# 
# # SETTING-UP BACKGROUND IMAGE
# def setting_bg():
#     st.markdown(f""" <style>.stApp {{
#                         background: url("https://cutewallpaper.org/22/plane-colour-background-wallpapers/189265759.jpg");
#                         background-size: cover}}
#                      </style>""",unsafe_allow_html=True)
# setting_bg()
# 
# # CREATING OPTION MENU
# selected = option_menu(None, ["Home","Upload & Extract","Modify"],
#                        icons=["house","cloud-upload","pencil-square"],
#                        default_index=0,
#                        orientation="horizontal",
#                        styles={"nav-link": {"font-size": "35px", "text-align": "centre", "margin": "0px", "--hover-color": "#6495ED"},
#                                "icon": {"font-size": "35px"},
#                                "container" : {"max-width": "6000px"},
#                                "nav-link-selected": {"background-color": "#6495ED"}})
# 
# 
# 
# import sqlite3
# con = sqlite3.connect("/content/drive/MyDrive/bizcard/tutorial.db")
# 
# 
# cursor=con.cursor()
# 
# #table creation
# cursor.execute('''CREATE TABLE IF NOT EXISTS card_data
#                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     company_name TEXT,
#                     card_holder TEXT,
#                     designation TEXT,
#                     mobile_number VARCHAR(50),
#                     email TEXT,
#                     website TEXT,
#                     area TEXT,
#                     city TEXT,
#                     state TEXT,
#                     pin_code VARCHAR(10),
#                     image BLOB
#                     )''')
# 
# 
# # HOME MENU
# if selected == "Home":
#     col1,col2 = st.columns(2)
#     with col1:
#         st.markdown("## :green[**Technologies Used :**] Python,easy OCR, Streamlit, SQL, Pandas")
#         st.markdown("## :green[**Overview :**] In this streamlit web app you can upload an image of a business card and extract relevant information from it using easyOCR. You can view, modify or delete the extracted data in this app. This app would also allow users to save the extracted information into a database along with the uploaded business card image. The database would be able to store multiple entries, each with its own business card image and extracted information.")
#     with col2:
#         st.image("/content/img.png")
# 
# 
# # UPLOAD AND EXTRACT MENU
# if selected == "Upload & Extract":
#     st.markdown("### Upload a Business Card")
#     uploaded_card = st.file_uploader("upload here",label_visibility="collapsed",type=["png","jpeg","jpg"])
#     if uploaded_card is not None:
# 
#         def save_card(uploaded_card):
#             with open(os.path.join("/content",uploaded_card.name), "wb") as f:
#                 f.write(uploaded_card.getbuffer())
#         save_card(uploaded_card)
# 
#         def image_preview(image,res):
#             for (bbox, text, prob) in res:
#               # unpack the bounding box
#                 (tl, tr, br, bl) = bbox
#                 tl = (int(tl[0]), int(tl[1]))
#                 tr = (int(tr[0]), int(tr[1]))
#                 br = (int(br[0]), int(br[1]))
#                 bl = (int(bl[0]), int(bl[1]))
#                 cv2.rectangle(image, tl, br, (0, 255, 0), 2)
#                 cv2.putText(image, text, (tl[0], tl[1] - 10),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
#             plt.rcParams['figure.figsize'] = (15,15)
#             plt.axis('off')
#             plt.imshow(image)
# 
# 
#         # DISPLAYING THE UPLOADED CARD
#         col1,col2 = st.columns(2,gap="large")
#         with col1:
#             st.markdown("#     ")
#             st.markdown("#     ")
#             st.markdown("### You have uploaded the card")
#             st.image(uploaded_card)
# 
# 
#         # DISPLAYING THE CARD WITH HIGHLIGHTS
#         with col2:
#             st.markdown("#     ")
#             st.markdown("#     ")
#             with st.spinner("Please wait processing image..."):
#                 st.set_option('deprecation.showPyplotGlobalUse', False)
#                 saved_img = "/content/"+ uploaded_card.name
#                 image = cv2.imread(saved_img)
#                 res = reader.readtext(saved_img)
#                 st.markdown("### Image Processed and Data Extracted")
#                 st.pyplot(image_preview(image,res))
# 
# 
#          #easy OCR
#         saved_img = "/content/"+ uploaded_card.name
#         result = reader.readtext(saved_img,detail = 0,paragraph=False)
# 
# 
#         # CONVERTING IMAGE TO BINARY TO UPLOAD TO SQL DATABASE
#         def img_to_binary(file):
#             # Convert image data to binary format
#             with open(file, 'rb') as file:
#                 binaryData = file.read()
#             return binaryData
# 
#             data = {"company_name" : [],
#                 "card_holder" : [],
#                 "designation" : [],
#                 "mobile_number" :[],
#                 "email" : [],
#                 "website" : [],
#                 "area" : [],
#                 "city" : [],
#                 "state" : [],
#                 "pin_code" : [],
#                 "image" : img_to_binary(saved_img)
#         }
# 
# 
# 
# 
#  #FUNCTION TO CREATE DATAFRAME
# def create_df(data):
#         df = pd.DataFrame(data)
#         return df
#         df = create_df(data)
#         st.success("### Data Extracted!")
#         st.write(df)
# 
#         if st.button("Upload to Database"):
#             for i,row in df.iterrows():
#                 #here %S means string values
#                 sql = """INSERT INTO card_data(company_name,card_holder,designation,mobile_number,email,website,area,city,state,pin_code,image)
#                             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#                 mycursor.execute(sql, tuple(row))
#                 # the connection is not auto committed by default, so we must commit to save our changes
#                 mydb.commit()
#             st.success("#### Uploaded to database successfully!")
# 
# 
# 
# # MODIFY MENU
# if selected == "Modify":
#     col1, col2, col3 = st.columns([3, 3, 2])
#     col2.markdown("## Alter or Delete the data here")
#     column1, column2 = st.columns(2, gap="large")
#     try:
#         with column1:
#             cursor.execute("SELECT card_holder FROM card_data")
#             result = cursor.fetchall()
#             business_cards = {}
#             for row in result:
#                 business_cards[row[0]] = row[0]
#             selected_card = st.selectbox("Select a card holder name to update", list(business_cards.keys()))
#             st.markdown("#### Update or modify any data below")
#             cursor.execute("select company_name,card_holder,designation,mobile_number,email,website,area,city,state,pin_code from card_data WHERE card_holder=%s",
#                            (selected_card,))
#             result = cursor.fetchone()
# 
#             # DISPLAYING ALL THE INFORMATIONS
# 
#             company_name = st.text_input("Company_Name", result[0])
#             card_holder = st.text_input("Card_Holder", result[1])
#             designation = st.text_input("Designation", result[2])
#             mobile_number = st.text_input("Mobile_Number", result[3])
#             email = st.text_input("Email", result[4])
#             website = st.text_input("Website", result[5])
#             area = st.text_input("Area", result[6])
#             city = st.text_input("City", result[7])
#             state = st.text_input("State", result[8])
#             pin_code = st.text_input("Pin_Code", result[9])
# 
#             if st.button("Commit changes to DB"):
#                 # Update the information for the selected business card in the database
#                 cursor.execute("""UPDATE card_data SET company_name=%s,card_holder=%s,designation=%s,mobile_number=%s,email=%s,website=%s,area=%s,city=%s,state=%s,pin_code=%s
#                                     WHERE card_holder=%s""", (company_name, card_holder, designation, mobile_number, email, website, area, city, state, pin_code, selected_card))
#                 con.commit()
#                 st.success("Information updated in database successfully.")
# 
#         with column2:
#             cursor.execute("SELECT card_holder FROM card_data")
#             result = cursor.fetchall()
#             business_cards = {}
#             for row in result:
#                 business_cards[row[0]] = row[0]
#                 selected_card = st.selectbox("Select a card holder name to Delete", list(business_cards.keys()))
#                 st.write(f"### You have selected :green[**{selected_card}'s**] card to delete")
#                 st.write("#### Proceed to delete this card?")
# 
#             if st.button("Yes Delete Business Card"):
#                 cursor.execute(f"DELETE FROM card_data WHERE card_holder='{selected_card}'")
#                 con.commit()
#                 st.success("Business card information deleted from database.")
# 
#     except:
#         st.warning("There is no data available in the database")
# 
#     if st.button("View updated data"):
#         cursor.execute("select company_name,card_holder,designation,mobile_number,email,website,area,city,state,pin_code from card_data")
#         updated_df = pd.DataFrame(cursor.fetchall(), columns=["Company_Name", "Card_Holder", "Designation", "Mobile_Number", "Email", "Website", "Area", "City", "State", "Pin_Code"])
#         st.write(updated_df)
#

!streamlit run /content/app.py &>/content/logs.txt & npx localtunnel --port 8501 & curl ipv4.icanhazip.com