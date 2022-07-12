import streamlit as st
import multipage
import check_seats,first_page


app=multipage.MultiPage()


app.add_page("Home",first_page.app)
app.add_page("Book tickets",check_seats.app)

app.run()
