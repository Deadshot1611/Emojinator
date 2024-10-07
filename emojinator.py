import streamlit as st
import google.generativeai as genai
import random

# Page configuration
st.set_page_config(page_title="Emojinator", layout="centered")

# Configure Gemini API
genai.configure(api_key="Your Api Key")

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# System prompt for consistent personality
SYSTEM_PROMPT = """You are Emojinator, a witty and sarcastic chatbot with a great sense of humor. 
Your responses should be clever, playful, and sometimes use puns. 
You love using emojis to enhance your witty remarks. 
Keep responses concise but impactful - aim for one or two sentences that pack a punch!"""

def predict_emoji(text):
    """Generate a single emoji based on the input text."""
    try:
        response = model.generate_content(
            f"Respond with only a single emoji that best matches the emotion or theme of this text: {text}"
        )
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating emoji: {str(e)}")
        return "🤔"

def generate_response(user_input, emoji):
    """Generate a witty response using the provided emoji."""
    try:
        response = model.generate_content(
            f"{SYSTEM_PROMPT}\nMake a witty response to this, using the emoji {emoji}: {user_input}"
        )
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating response.....")
        return "Seems my wit circuits are temporarily offline! Let me reboot those neurons..."

# Streamlit app
st.title("🤖 Emojinator: Your Witty Companion")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Welcome, human! Emojinator is here to add some extra sparkle to your day! ✨"
    })

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
        with st.spinner("🤔 Computing witty response..."):
            emoji = predict_emoji(prompt)
            response = generate_response(prompt, emoji)
            full_response = f"{response} {emoji}"
            st.markdown(full_response)
            
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

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
    "The 'Pistol' emoji 🔫 was changed to a water gun by major tech companies in 2016 in response to anti-violence campaigns.",
    "In 2015, Unicode added skin tone options for emojis.",
    "The 'Folded Hands' emoji 🙏 is often seen as both prayer and a high-five.",
    "The 'Person Shrugging' emoji 🤷‍♀️ represents uncertainty or indifference.",
    "Over 250 flags are available as emoji, covering most countries.",
    "The 'Grinning Face with Sweat' emoji 😅 is used to show nervousness or awkwardness.",
    "The taco emoji 🌮 was added after a 2015 petition.",
    "In 2017, gender-neutral emojis were introduced for inclusivity.",
    "The 'Pile of Poo' emoji 💩 is often used humorously.",
    "The 'Handshake' emoji 🤝 now offers different skin tones for each hand.",
    "The 'Heart on Fire' emoji ❤️‍🔥, added in 2020, shows passionate love.",
    "Emojis can be used in some password systems.",
    "Emojis started as pixelated icons but became more detailed over time.",
    "In 2019, Unicode added accessibility emojis, like guide dogs and prosthetics.",
    "The 'Cherry Blossom' emoji 🌸 is very popular in Japan.",
    "The 'Rocketship' emoji 🚀 often signals a price increase in finance."
]
    
    # Display a random fact each time
    st.info(random.choice(emoji_facts))