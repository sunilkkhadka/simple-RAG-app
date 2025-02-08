import streamlit as st
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain.schema.runnable import RunnableMap

loader = WebBaseLoader("https://research.ibm.com/blog/retrieval-augmented-generation-RAG")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(docs)

embeddings = OllamaEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

retriever = vectorstore.as_retriever()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question using the provided context."),
    ("user", "Question: {question}\n\nContext: {context}")
])

llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()

document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

rag_chain = RunnableMap({
    "context": retriever,
    "question": lambda x: x["question"]
}) | document_chain | output_parser

st.title("Langchain Demo With FAISS & Llama3.2")
input_text = st.text_input("What question do you have in your mind?")

if input_text:
    result = rag_chain.invoke({"question": input_text})
    st.write(result) 
