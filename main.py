import streamlit as st
from src.page1 import page1
from src.page2 import page2
from src.page3 import page3
import openai   
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

    
pages ={
    "Introduction": page1,
    "Text to Image": page2,
    "Image Variation": page3
}
page = st.sidebar.selectbox("Select a page", list(pages.keys()))

pages[page]()

#def main():
#    st.sidebar.title("Navigation")
 #   page = st.sidebar.selectbox("Go to", ["Page One", "Page Two", "Page Three"])

  #  if page == "Page One":
   #     page_one()
    #elif page == "Page Two":
     #   page_two()
    #elif page == "Page Three":
     #   page_three()

#if __name__ == "__main__":
 #   main()