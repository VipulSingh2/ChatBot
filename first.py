import streamlit as st
import process

# Sidebar for file upload
st.sidebar.title("ChatBot Example")
file = st.sidebar.file_uploader("Upload a file",type="PDF")
text = None

# Extract text from PDF if fiel is uploaded
if file is not None:
    text = process.extracted_text(file)
    st.text_area("Extracted Text",text,height = 300)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]

#Display chat Message from history on app rerun 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input

if prompt:= st.chat_input("Ask a question about the document:"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})