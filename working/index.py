import streamlit as st
import multipage
import check_seats,first_page,booking_check


app=multipage.MultiPage()


app.add_page("Home",first_page.app)
app.add_page("Book tickets",check_seats.app)
app.add_page("Check Booking",booking_check.app)

app.run()

if "pcount" not in st.session_state:
    st.session_state["pcount"]=1

if st.session_state["pcount"]==1:

            first_page.app()
            st.session_state["pcount"]=2
