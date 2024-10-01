import streamlit as st
import random
import os
from mistralai import Mistral

# Page configuration
st.set_page_config(page_title="Emojinator", layout="centered")

# Mistral API configuration
client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
model = "mistral-large-2407"  # Using small model for faster responses

def mistral_api_call(messages):
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
        temperature=0.9,    # Higher temperature for more creative responses
        max_tokens=150,     # Increased slightly for more complete responses
        top_p=0.95          # Slightly higher top_p for more varied vocabulary
    )
    return chat_response.choices[0].message.content

SYSTEM_PROMPT = """You are Emojinator, a witty and sarcastic chatbot with a great sense of humor. 
Your responses should be clever, playful, and sometimes use puns. 
You love using emojis to enhance your witty remarks.
Keep responses concise but impactful - aim for one or two sentences that pack a punch!"""

@st.cache_data
def predict_emoji(text):
    messages = [
        {"role": "system", "content": "You are an emoji expert. Respond with only a single emoji that best matches the emotion or theme of the text."},
        {"role": "user", "content": text}
    ]
    return mistral_api_call(messages)

def generate_response(user_input, emoji):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Make a witty response to this, using the emoji {emoji}: {user_input}"}
    ]
    return mistral_api_call(messages)

# Streamlit app
st.title("🤖 Emojinator: Your Witty Companion")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Say something, I dare you! 😏"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate emoji and response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.text("🤔")
        emoji = predict_emoji(prompt)
        message_placeholder.text("✍️")
        response = generate_response(prompt, emoji)
        message_placeholder.markdown(f"{response} {emoji}")
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": f"{response} {emoji}"})

# Fun facts in an expander
with st.expander("🎯 Did You Know?", expanded=False):
    st.write("While I craft my witty responses, enjoy these emoji facts:")
    emoji_facts = [
    "Did you know? The first emoji was created in 1999 by Shigetaka Kurita in Japan.",
    "The 'Face with Tears of Joy' emoji 😂 was the Oxford Dictionaries Word of the Year in 2015!",
    "There are over 3,000 emojis in the Unicode Standard as of 2021.",
    "The word 'emoji' comes from Japanese e (絵, 'picture') + moji (文字, 'character').",
    "Finland is the only country to have its own set of national emojis, including a sauna emoji 🧖!",
    "Emojis were first introduced on mobile phones by NTT Docomo, Japan’s leading mobile operator.",
    "The most-used emoji on Twitter is the 'Face with Tears of Joy' 😂, followed by the 'Red Heart' ❤️.",
    "In 2016, the Museum of Modern Art (MoMA) in New York added the original 176 emoji set into its permanent collection.",
    "World Emoji Day is celebrated every year on July 17, the date shown on the 📅 Calendar Emoji.",
    "The Unicode Consortium, a non-profit organization, is responsible for maintaining and approving new emojis.",
    "The 'Eggplant' 🍆 and 'Peach' 🍑 emojis are often used as innuendos due to their suggestive shapes.",
    "An emoji film titled *The Emoji Movie* was released in 2017, featuring the adventures of emojis inside a smartphone.",
    "There are even emoji-only messaging apps, such as Emojli, where users communicate exclusively with emojis!",
    "The 'Fire' 🔥 emoji became widely associated with expressing excitement or something being 'cool' or 'awesome.'",
    "The 'Pistol' emoji 🔫 was changed to a water gun by major tech companies in 2016 in response to anti-violence campaigns."
]

    for fact in emoji_facts:
        st.info(fact)