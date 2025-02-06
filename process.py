import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1",token = "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")
pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1",device_map="auto",torch_dtype="auto")
def extracted_text(file):

    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            # text +=page.extract_text() +"\n"
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text

def chunks(text):
    # docs=None
    docs = [Document(page_content=text)]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512,chunk_overlap=50)
    chunked_docs = text_splitter.split_documents(text_splitter)
    return chunked_docs
def answer_question_from_chunk(chunks,question):
   # result = pipe({
        #'context'=chunks,
        #'question':question
           # })
   # return result['answer']
    context = "\n".join([chunk.page_content for chunk in chunks])  # Combine chunk texts
    prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    
    result = pipe(prompt, max_length=200, temperature=0.7)
    return result[0]["generated_text"].split("Answer:")[-1].strip()  
