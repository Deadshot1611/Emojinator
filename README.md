# 🤖 Emojinator: Your Witty Emoji-Based Chatbot

**Emojinator** is a fun, witty chatbot that generates short and humorous responses to user inputs using emojis. This project uses advanced language models to analyze user inputs and generate creative responses, adding a playful touch to the conversation with emoji suggestions.


[Visit the live app here!](https://deadshot2003-emojinator.hf.space)


## 📋 What Does Emojinator Do?

- Accepts user input and analyzes the sentiment or theme.
- Suggests an emoji that matches the input.
- Generates a witty and sarcastic response, incorporating the suggested emoji.
- Provides fun facts about emojis through an interactive and expanding section.
  
## 🛠️ Technologies Used

### **1. Streamlit:**
Streamlit is a fast and easy-to-use framework for building web applications. We use it to create the UI and handle user interaction for the Emojinator chatbot.

- **Why Streamlit?**
  - Quick to build interactive applications
  - Allows the integration of machine learning models seamlessly
  
### **2. Mistral API:**
We use the Mistral API, a lightweight API for interacting with powerful language models. It's responsible for generating the witty responses and suggesting emojis based on user inputs.

- **Why Mistral?**
  - Great performance and faster responses.
  - Allows the flexibility of using pre-trained language models without complex setup.
  
### **3. Python:**
This project is entirely built using Python. We use Python for:
  - Sending requests to the Mistral API.
  - Managing the chatbot logic and emoji suggestion.

### **4. Custom CSS (Optional):**
While Streamlit doesn't natively support extensive styling, we inject custom CSS to improve the look and feel of the app. Contributors can help by customizing the UI further with CSS.

## 🚀 Getting Started

To run the Emojinator locally, clone this repository and install the required packages:

```bash
git clone https://github.com/Deadshot1611/emojinator.git
cd emojinator
pip install -r requirements.txt
```
 **Add Your Mistral API Key**:
Replace the environment variable in the code with your own Mistral API key.
**Run the Application**:
```bash

streamlit run emojinator.py
```
## 🤝 Contributions

We welcome contributions from developers of all skill levels! Whether you're a beginner learning web development or an advanced Python developer, there's a task for everyone. Check the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

## 📑 License

This project is open-source and licensed under the MIT License.

