import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
def extracted_text(file):

    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text +=page.extract_text() +"\n"
    return text

def chunks(text):
    # docs=None
    docs = [Document(page_content=text)]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512,chunk_overlap=50)
    chunks = text_splitter.split_documents(text_splitter)
    return chunks