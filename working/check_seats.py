import streamlit as st
import mysql.connector as mys
import datetime as dt
import passenger_details
import time


def check(src,dest,tdate,seats,seat_type):

    if st.session_state["count"]==1 and src==dest:
        app()

    else:

        if src==dest:
            st.warning("Invalid seat selection")
        else:
            conn=mys.connect(host="localhost",user="root",password="fc7daa66c184",database="comp_project")
            mycursor=conn.cursor()
            mycursor.execute("""select * from seats where date like "{}";""".format(tdate))
            data=mycursor.fetchall()
            basic_fare=40
            source_list=["Bengaluru","Mysore","Tumkur","Mangalore","Gulbarga"]
            ticket_fare=(seats)*(basic_fare+(abs(source_list.index(src)-source_list.index(dest)))*20)
            st.success("Seats available")
            st.write("total ticket fare:",ticket_fare)
            st.session_state["travel_details"]={"source":src,"destination":dest,"travel_date":tdate,"number_of_seats":seats,"seat_type":seat_type}
            time.sleep(2)
            passenger_details.app()

def app():
    if "count" not in st.session_state:

        st.session_state["count"]=1

    else:
        print(st.session_state["count"])

        st.title("Railway Booking")

        with st.form(key="form_seat"):
            col1,col2=st.columns(2)
            src=col1.selectbox(
                 'Source',
                 ('Bengaluru',"Mysore","Tumkur","Mangalore","Gulbarga"),key="source")
            dest=col2.selectbox(
                 'Source',
                 ('Bengaluru',"Mysore","Tumkur","Mangalore","Gulbarga"),key="destination")
            seat_type=col1.selectbox("Seat type",("AC","Sleeping","Sitting"))

            tdate=col2.date_input("Travel date",value=dt.datetime.today(),min_value=dt.datetime.today(),max_value=dt.datetime(2022,3,31))
            sno=st.slider("Number of seats",min_value=1,max_value=5)
            st.form_submit_button("submit",on_click=check,args=(src,dest,tdate,sno,seat_type))
