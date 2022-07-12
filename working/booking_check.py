import streamlit as st
import mysql.connector as mysq
conn=mysq.connect(host="localhost",user="root",password="fc7daa66c184",database="comp_project")
mycursor=conn.cursor()
def check():
    if st.session_state["ticket_no"]!="":
        mycursor.execute("select * from passenger where ticketno like {}".format(st.session_state["ticket_no"]))
        data=mycursor.fetchall()[0]
        print(data)
        st.write("Name:{}".format(data[2]))
        st.write("Age:{}".format(data[3]))
        st.write("Phone number:{}".format(data[4]))
        st.write("Source:{}".format(data[5]))
        st.write("Destination:{}".format(data[6]))
        st.write("Seat type:{}".format(data[7]))
        st.write("Date:{}".format(data[8]))
        app()
#delhi bombay jaipur bengaluru chennai kolkata uttarakand kashmir darjeeling

    else:
        app()

def app():
    print("app entered")
    if "rcheck" not in st.session_state:
        st.session_state["rcheck"]=1
        print("rcheck added")
    #else:
    #    st.session_state["rcheck"]+=1



    #with st.form(key=str(st.session_state["rcheck"])):
    ticket=st.text_input("Enter ticket number",key=st.session_state["rcheck"])
    st.session_state["ticket_no"]=ticket
    b=st.button("submit",on_click=check)
    print(b)
    #st.form_submit_button("submit",on_click=check,args=(ticket))
