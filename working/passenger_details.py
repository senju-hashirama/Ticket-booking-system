import streamlit as st
import mysql.connector as mys
import pdb
import random
conn=mys.connect(host="localhost",user="root",password="fc7daa66c184",database="comp_project")
mycursor=conn.cursor()
def check(name,age,phone):



            if st.session_state["bcount"]<st.session_state["travel_details"]["number_of_seats"] and st.session_state["prev_name"].count(name)==1:
                if name=="":
                    st.warning("try again")
                    app()


                else:

                    mycursor.execute("select ticketno from passenger")
                    try:
                        ticketnos=mycursor.fetchall()[0]
                    except:
                        ticketnos=[]
                    while True:
                        ticketno=random.randint(1000,9999)
                        if(ticketno in ticketnos) :
                            pass
                        else:
                            break
                    st.session_state["bcount"]+=1
                    mycursor.execute("""select {} from seats where date like "{}";""".format(st.session_state["travel_details"]["seat_type"],st.session_state["travel_details"]["travel_date"]))
                    seatno=25-mycursor.fetchall()[0][0]+1
                    mycursor.execute("""update seats set {}={} where date like "{}";""".format(st.session_state["travel_details"]["seat_type"],25-seatno,st.session_state["travel_details"]["travel_date"]))

                    print("""insert into passenger values("{}",{},"{}",{},"{}","{}","{}","{}");""".format(ticketno,seatno,name,age,phone,st.session_state["travel_details"]["source"],st.session_state["travel_details"]["destination"],st.session_state["travel_details"]["seat_type"],st.session_state["travel_details"]["travel_date"]))
                    mycursor.execute("""insert into passenger values("{}",{},"{}",{},"{}","{}","{}","{}","{}");""".format(ticketno,seatno,name,age,phone,st.session_state["travel_details"]["source"],st.session_state["travel_details"]["destination"],st.session_state["travel_details"]["seat_type"],st.session_state["travel_details"]["travel_date"]))
                    conn.commit()


                    if  st.session_state["bcount"]==st.session_state["travel_details"]["number_of_seats"]:
                        st.success("All tickets have been booked ")
                        st.header("Happy journey")
                    else:
                        app()
            else:
                app()












            #if st.session_state["bcount"]<=st.session_state["travel_details"]["number_of_seats"]:

            #            st.session_state["bcount"]+=1
            #            mycursor.execute("select ticketno from passenger")
            #            ticketnos=mycursor.fetchall()
            #            while True:
            #                ticketno=random.randint(1000,9999)
            #                if(ticketno in ticketnos):
            #                    pass
            #                else:
            #                    break
            #            mycursor.execute("""select {} from seats where date like {}""".format(st.session_state["travel_details"]["seat_type"],st.session_state["travel_details"]["travel_date"]))
            #            seatno=25-mycursor.fetchall()[0][0]+1
            #            mycursor.execute("""Inset into passengers Values ("{}",{},"{}",{},"{}","{}","{}","{}")""".format(ticketno,seatno,name,age,phone,st.session_state["travel_details"]["source"],st.session_state["travel_details"]["destination"],st.session_state["travel_details"]["seat_type"],st.session_state["travel_details"]["travel_date"]))
            #            mycursor.execute("""update table seats set {}={} where date like {};""".format(st.session_state["travel_details"]["seat_type"],25-seatno,st.session_state["travel_details"]["travel_date"]))
            #            conn.commit()
            #            st.success("seat booked for {}".format(name))


def app():

    if "bcount" not in st.session_state:
        st.session_state["bcount"]=0
    if "prev_name" not in st.session_state:
        st.session_state["prev_name"]=[]

    print(st.session_state["bcount"])



    print(st.session_state["travel_details"]["number_of_seats"])
    st.write("Passenger {}".format(st.session_state["bcount"]+1))

    with st.form(key="form1"):
            col1,col2=st.columns(2)
            name = col1.text_input("Name")
            age=col2.text_input("Age")
            ph=col1.text_input("Phone Number")
            st.session_state["prev_name"].append(name)
            st.form_submit_button("book",on_click=check,args=(name,age,ph))
