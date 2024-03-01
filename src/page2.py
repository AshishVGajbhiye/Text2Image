import streamlit as st
import openai   
def page2():
    st.title("OpenAI DALL-E Image Generation")
    st.info("This is the second page.")

    with st.form(key='form'):
    
        prompt = st.text_input("Enter the text prompt for image generation")
        size = st.selectbox("Select the size of the images", ["512x512"])
        num_images = st.selectbox("Select the number of images to be generated", [1, 2, 3])
        submit_button = st.form_submit_button(label='Generate Images')

    if submit_button:
        if prompt:
            response = openai.images.generate(
                    model="dall-e-2",
                    prompt = prompt,
                    n = num_images,
                    size=size,
                    quality="standard"
                )
            for idx in range(num_images):
                image_url=response.data[idx].url

                st.image(image_url, caption=f"Generated Image: {idx+1}",
                        use_column_width=True)
                
uploaded_file=st.file_uploader("Choose an image file", type=['png', 'jpg'])