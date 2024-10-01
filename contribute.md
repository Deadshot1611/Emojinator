

# 🤝 Contributing to Emojinator

We’re glad you’re interested in contributing to **Emojinator**! Whether you’re a beginner in web development or a seasoned developer, this project provides tasks for everyone. Below, we’ve outlined the contribution process and what kind of contributions we’re looking for.

## 📌 Project Vision

The **Emojinator** chatbot is currently built using Python and Streamlit, with an integration of Mistral API to generate witty emoji-based responses. The initial goal is to enhance the user interface, make the app more dynamic, and offer more customization through CSS, HTML, and API integrations.

## 💻 Types of Contributions

### 1. **Absolute Beginners (HTML/CSS)**:
If you’ve just started learning HTML and CSS, you can contribute to improving the look and feel of the app.

- **Issues You Can Work On**:
  - Improve the visual style of the app using CSS.
  - Help design a simple HTML file to replicate the current UI of the app (this will be later integrated with FastAPI).
  - Add background colors, custom fonts, or layout improvements.
  
#### 💡 Guide: Injecting CSS in Streamlit

Streamlit allows limited customization through CSS, and you can inject CSS by using the `st.markdown()` function with `unsafe_allow_html=True`. Here’s a small example:
```python
st.markdown(
    """
    <style>
    .header { 
        font-size: 24px; 
        color: #FF5733;
    }
    </style>
    """,
    unsafe_allow_html=True
)
```
You can refer to [this blog](https://blog.streamlit.io/3-tips-for-better-streamlit-apps/) for more details on how to work with custom CSS in Streamlit.
###2. **Intermediate Developers (Python/Streamlit)**:
If you’re comfortable with Python and have a basic understanding of Streamlit, there are more interactive tasks you can take up.

-**Issues You Can Work On**:
-Improve the response logic of the chatbot.
-Add new features to the Streamlit app (e.g., favicon, different response types).
-Enhance the emoji recommendation system.
-Create better error handling and validation for user input.
###3. **Advanced Developers (FastAPI/Backend Integration)**:
If you have experience with backend frameworks like FastAPI, your task is to extend the app beyond Streamlit and integrate it with a more scalable backend solution.

-**Issues You Can Work On**:
-Convert the Streamlit app’s backend to FastAPI.
-Create an API endpoint for the chatbot’s functionality and migrate from a Streamlit-based system to an API-first architecture.
-Allow seamless integration of the FastAPI endpoints with the HTML-based front end.
💡 Guide: FastAPI Integration
FastAPI is a modern, high-performance web framework for building APIs with Python. Here’s how you can get started:

```bash
pip install fastapi uvicorn
```
Example FastAPI endpoint:
```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/predict/")
def get_prediction(user_input: str):
    # Use Mistral API to generate chatbot response
    response = mistral_api_call(user_input)
    return {"response": response}
```
For more detailed instructions, check the [official FastAPI documentation](https://fastapi.tiangolo.com/).
###⚙️ **Setting Up the Project Locally**
To contribute to Emojinator, follow these steps to set up the project locally:

1. **Fork the Repository**:
Click on the "Fork" button at the top right corner of this repository page.

2. **Clone Your Forked Repository**:
   ```bash
   git clone https://github.com/your-username/emojinator.git
   cd emojinator
   ```
3. **Create a Branch**:
```bash

git checkout -b feature/your-feature
```
4. **Make Your Changes and Commit**:
```bash

git add .
git commit -m "Added feature XYZ"
```
5. **Push to Your Forked Repository**:
```bash

git push origin feature/your-feature
```
6. Open a Pull Request:
Once your feature is complete, open a pull request from your branch to the main branch of the original repository.
##📝 **Code of Conduct**
Please be respectful of others when contributing, and adhere to the Code of Conduct when interacting with the community.
