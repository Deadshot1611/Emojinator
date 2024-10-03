document.addEventListener("DOMContentLoaded", () => {
  const chatBox = document.getElementById("chat-box");
  const userInput = document.getElementById("user-input");
  const sendBtn = document.getElementById("send-btn");
  const funFactsList = document.getElementById("fun-facts-list");

  const apiUrl = ""; // Replace with actual API URL

  const funFacts = [
    "Did you know? The first emoji was created in 1999 by Shigetaka Kurita in Japan.",
    "The 'Face with Tears of Joy' emoji 😂 was the Oxford Dictionaries Word of the Year in 2015!",
    "There are over 3,000 emojis in the Unicode Standard as of 2021.",
    "The word 'emoji' comes from Japanese e (絵, 'picture') + moji (文字, 'character').",
    "Finland is the only country to have its own set of national emojis, including a sauna emoji 🧖!",
    // Add more facts here...
  ];

  // Load fun facts into the page as cards
  funFacts.forEach((fact) => {
    const card = document.createElement("div");
    card.classList.add("fact-card");
    card.textContent = fact;
    funFactsList.appendChild(card);
  });

  sendBtn.addEventListener("click", () => {
    const userMessage = userInput.value.trim();
    if (userMessage) {
      addMessage("user", userMessage);
      getApiResponse(userMessage)
        .then((response) => {
          addMessage("assistant", response);
        })
        .catch((error) => {
          addMessage(
            "assistant",
            "Oops! Something went wrong. Please try again."
          );
        });
    }
    userInput.value = "";
  });

  function addMessage(role, content) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", role);

    const messageContent = document.createElement("div");
    messageContent.classList.add("message-content");
    messageContent.textContent = content;

    messageDiv.appendChild(messageContent);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
  }

  async function getApiResponse(userMessage) {
    const requestBody = {
      message: userMessage,
    };

    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });

    if (!response.ok) {
      throw new Error("Failed to fetch response from API");
    }

    const data = await response.json();
    return data.response; // Assuming the API returns a JSON object with a "response" field
  }
});
