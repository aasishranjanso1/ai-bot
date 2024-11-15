import streamlit as st
import google.generativeai as genai
import os
from streamlit_chat import message

gemini_api_key = "AIzaSyARHE1Tx2ZurElq6-0a2QIM-9Lm0_a53t4"

genai.configure(api_key = gemini_api_key)

model = genai.GenerativeModel('gemini-pro')

# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")
# else:
#     prompt = "who are you?"
# response = model.generate_content(prompt)
# message = st.chat_message("ai")
# message.write(response.text)

def chat_actions():
    st.session_state["chat_history"].append(
        {"role": "user", "content": st.session_state["chat_input"]},
    )

    response = model.generate_content(st.session_state["chat_input"])
    st.session_state["chat_history"].append(
        {
            "role": "assistant",
            "content": response.text,
        },  # This can be replaced with your chat response logic
    )


if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


st.chat_input("Enter your message", on_submit=chat_actions, key="chat_input")

for i in st.session_state["chat_history"]:
    with st.chat_message(name=i["role"]):
        st.write(i["content"])


# import numpy as np
# from PIL import Image

# img_file_buffer = st.file_uploader('Upload a PNG image', on_change= type=['png','jpg'])
# if img_file_buffer is not None:
#     image = Image.open(img_file_buffer)
#     img_array = np.array(image)
