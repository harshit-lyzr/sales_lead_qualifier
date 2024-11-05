import os
from lyzr_agent_api import AgentAPI, ChatRequest
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
LYZR_API_KEY = os.getenv("LYZR_API_KEY")
AGENT_ID = os.getenv("AGENT_ID")

# Streamlit page configuration
st.set_page_config(
    page_title="Sales Lead Qualifier Agent",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

st.title("Sales Lead Qualifier Agent")
st.markdown("### Welcome to the Sales Lead Qualifier Agent!")

# Initialize the LyzrAgentAPI
client = AgentAPI(x_api_key=LYZR_API_KEY)


# Input area for the product description and target audience
email = st.sidebar.text_input("Enter the lead's email address:")
criteria = st.sidebar.text_area("Describe your lead qualification criteria")

if st.sidebar.button("Check"):
    with st.spinner("Performing Github Tasks...."):
        response = client.chat_with_agent(
            json_body=ChatRequest(
                user_id="user@example.com",
                agent_id=AGENT_ID,
                message=f"email: {email}, Lead Qualification Criteria: {criteria}",
                session_id="sdfw",
            )
        )
        # Display the generated email
        st.markdown(f"\n\n{response['response']}")

# Optional footer or credits
st.markdown("---")
st.markdown("Powered by Lyzr Agent API and OpenAI")
