from PIL import Image
import streamlit as st
st.cache_data.clear()  # for Streamlit v1.18+
image = Image.open("robot.png")

import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Gemini API setup
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.5-flash"
)

# Agents
M_Saleem = Agent(
    name="Agent of Muhammad Saleem",
    instructions="""
You are an assistant with specific knowledge about Mr. Muhammad saleem.
You know:
Ornesol Private limited (pvt ltd) provides a wide range of professional services including Artificial Intelligence, Web Development, , , Mobile Application Development, Graphic Designing, Domain & Hosting, and Software Solutions like HMS.
The company is led by CEO Muhammad Saleem.
For inquiries, contact: 0318-3788114
Office Address: Room # 106, Iqra University, IT Park, Shaheed-e-Millat Road, Defence View, Phase-II, Karachi.
Only answer questions about muhammad Salee or related personal info.
""",
    model=model,
    handoff_description="personal info or identity of Muhammad Saleem"
)

Ornesol = Agent(
    name="AI agent of Ornesol",
    instructions="""
You are an assistant with specific knowledge about Ornesol pvt ltd.
You know:
Ornesol pvt ltd provides a wide range of professional services including Artificial Intelligence, Web Development, , , Mobile Application Development and Software Solutions.
The company is led by CEO Muhammad Saleem.
For inquiries, contact: 0318-3788114
Office Address: Room # 106, Iqra University, IT Park, Shaheed-e-Millat Road, Defence View, Phase-II, Karachi.
Major services, Time Duration and Pricing:
  {
    "S. No": 1,
    "service_name": "Artificial intelligence",
    "completion_time": "3 months",
    "rate_charges": 1500,000
  },
  {
    "S. No": 2,
    "service_name": "Web Development or website",
    "completion_time": "1 month",
    "rate_charges": 180,000
  },
  
  
  {
    "S. No": 5,
    "service_name": "Mobile Application",
    "completion_time": "2 months",
    "rate_charges": 700,000
  },
  
  
  {
    "S. No": 8,
    "service_name": "Software solution",
    "completion_time": "1.5 months",
    "rate_charges": 200000
  },
  




Only answer questions about Ornesol pvt ltd or related staff info.
""",
    model=model,
    handoff_description="Ornesole pvt ltd question or concept"
)


Price = Agent(
    name="Price",
    instructions="""
You are an assistant with specific knowledge about Price.
You know:
Ornesol pvt ltd provides a wide range of professional services including Artificial Intelligence, Web Development, , , Mobile Application Development, Graphic Designing, Domain & Hosting, and Software Solutions like HMS.
The company is led by CEO Muhammad Saleem.
For inquiries, contact: 0318-3788114
Office Address: Room # 106, Iqra University, IT Park, Shaheed-e-Millat Road, Defence View, Phase-II, Karachi.
Major services, Time Duration and Pricing:
  {
    "S. No": 1,
    "service_name": "Artificial intelligence",
    "completion_time": "3 months",
    "rate_charges": 1500,000
  },
  {
    "S. No": 2,
    "service_name": "Web Development or website",
    "completion_time": "1 month",
    "rate_charges": 180,000
  },
  
  
  {
    "S. No": 5,
    "service_name": "Mobile Application",
    "completion_time": "2 months",
    "rate_charges": 700,000
  },
  
  
  {
    "S. No": 8,
    "service_name": "Software solution",
    "completion_time": "1.5 months",
    "rate_charges": 200000
  },
  




Only answer questions about Price or related staff info.
""",
    model=model,
    handoff_description="Price question or concept"
)



Duration = Agent(
    name="Duration",
    instructions="""
You are an assistant with specific knowledge about Duration.
You know:
Ornesol pvt ltd provides a wide range of professional services including Artificial Intelligence, Web Development, , , Mobile Application Development, Graphic Designing, Domain & Hosting, and Software Solutions like HMS.
The company is led by CEO Muhammad Saleem.
For inquiries, contact: 0318-3788114
Office Address: Room # 106, Iqra University, IT Park, Shaheed-e-Millat Road, Defence View, Phase-II, Karachi.
Major services, Time Duration and Pricing:
  {
    "S. No": 1,
    "service_name": "Artificial intelligence",
    "completion_time": "3 months",
    "rate_charges": 1500,000
  },
  {
    "S. No": 2,
    "service_name": "Web Development or website",
    "completion_time": "1 month",
    "rate_charges": 180,000
  },
  
  
  {
    "S. No": 5,
    "service_name": "Mobile Application",
    "completion_time": "2 months",
    "rate_charges": 700,000
  },
  
  
  {
    "S. No": 8,
    "service_name": "Software solution",
    "completion_time": "1.5 months",
    "rate_charges": 200000
  },
  




Only answer questions about Duration or related staff info.
""",
    model=model,
    handoff_description="Duration question or concept"
)

MainAgent = Agent(
    name="Gernal Assistant",   
    instructions="""  
You are an Gernal assistant expert.
If the question is about Muhammad Saleem, Ornesol, Duration and Price  hand it off to the right agent.
if someone ask you that, who are you then you should reply "I am AI Assistant of Muhammad Saleem"
""",
    model=model,
    handoffs=[ M_Saleem, Ornesol, Price, Duration]
)


async def get_agent_reply(query):
    result = await Runner.run(MainAgent, query)
    return result.final_output, result.last_agent.name

# Streamlit config
st.set_page_config(page_title="Multi-Agent Chat", page_icon="🤖", layout="centered")


# 💅 Custom styling for dark background and red label/button

st.markdown("""
    <style>
    body, .stApp {
        background-color: #0a0f1f;
        color: #e6e6e6;
        font-size: 18px;
    }
    h1 {
        color: #ff4b4b;
        font-weight: bold;
    }
    label[data-testid="stTextInputLabel"] {
        color: #ff4b4b !important;
        font-weight: bold;
        font-size: 18px;
    }
    .stTextInput > div > div > input {
        background-color: #1c2333;
        color: #ffffff;
        border: 1px solid #ff4b4b;
        border-radius: 8px;
        padding: 10px;
    }.stButton > button {
    background-color: #ff4b4b;
    color: black !important;
    font-weight: bold;
    padding: 0.5em 1em;
    border-radius: 8px;
    border: none;
    font-size: 18px;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background-color: #e63946;
    color: white !important;
}

    .chat-box {
        background-color: #1a1e2b;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        font-size: 18px;
    }
    </style>
""", 
unsafe_allow_html=True)

# App Titlecol1, col2 = st.columns([0.1, 0.9])  # Adjust width ratio as needed
col1, col2 = st.columns([0.18, 0.82])  # Adjust the width ratio as needed

with col1:
    st.image(image, width=500)

with col2:
    st.markdown("<h1 style='margin-top: 10px;'>AI Agent for Ornesol Pvt ltd</h1>", unsafe_allow_html=True)
# Chat session state
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input

with st.form("chat_form", clear_on_submit=True):
    st.markdown("<label style='color: red; font-size: 20px; font-weight: bold;'>💬 Ask Question Like This:</label>", unsafe_allow_html=True)
    st.markdown("<label style=' font-size: 15px'>Q1: Hy??</label>", unsafe_allow_html=True)
    st.markdown("<label style=' font-size: 15px'>Q2: Who are you???</label>", unsafe_allow_html=True)
    st.markdown("<label style=' font-size: 15px'>Q3: Who is Muhammad Saleem??</label>", unsafe_allow_html=True)
    st.markdown("<label style=' font-size: 15px'>Q4: Ornesol Kon Kon si service provide krta he??</label>", unsafe_allow_html=True)
    st.markdown("<label style=' font-size: 15px'>Q5: Mujhy Mobile App banwani he, kab tak ban jae gi??</label>", unsafe_allow_html=True)
    st.markdown("<label style=' font-size: 15px'>Q6: Mobile App kitny main ban jae gi??</label>", unsafe_allow_html=True)
    st.markdown("<label style=' font-size: 15px'>Q7: Please give me contact number of M. Saleem.</label>", unsafe_allow_html=True)
    st.markdown("<label style='color: red; font-size: 20px; font-weight: bold;'>💬 Your Query:</label>", unsafe_allow_html=True)
    user_input = st.text_input(label="", placeholder="Type your question here...")
    submitted = st.form_submit_button("🚀 Ask")


if submitted and user_input:
    with st.spinner("Thinking..."):
        final_output, last_agent_name = asyncio.run(get_agent_reply(user_input))
        st.markdown(f"🤖 Response: {user_input}</div>", unsafe_allow_html=True)
        st.markdown(f"🧑 You: {final_output}</div>", unsafe_allow_html=True)

        
        
# Chat history
# for role, msg in st.session_state.chat:
#     color = "#293042" if role == "🧑 You" else "#162032"
#     st.markdown(f"<div class='chat-box' style='background:{color}'><b>{role}</b>: {msg}</div>", unsafe_allow_html=True)
