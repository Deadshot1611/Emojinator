// app/page.tsx
"use client";

import { useState, useEffect } from "react";

const emoji_facts = [
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
];

export default function Home() {
    const [userInput, setUserInput] = useState("");
    const [chatHistory, setChatHistory] = useState<{ role: string; content: string }[]>([]);
    const [loading, setLoading] = useState(false);
    const [randomFact, setRandomFact] = useState("");

    useEffect(() => {
        // Pick a random fact when the page loads
        const randomIndex = Math.floor(Math.random() * emoji_facts.length);
        setRandomFact(emoji_facts[randomIndex]);
    }, []);

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();
        if (!userInput.trim()) return;

        // Add user message to chat history
        setChatHistory([...chatHistory, { role: "user", content: userInput }]);
        setLoading(true);

        // Send user input to backend to generate response
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: userInput }),
        });

        const data = await response.json();
        setChatHistory([...chatHistory, { role: "user", content: userInput }, { role: "assistant", content: `${data.response} ${data.emoji}` }]);

        setUserInput("");
        setLoading(false);
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen w-full">
            <h1 className="text-4xl font-bold text-white mb-8">🤖 Emojinator: Your Witty Companion</h1>

            {/* Display the random emoji fact */}
            <div className="bg-yellow-100 p-4 rounded-lg mb-6 text-center w-full max-w-3xl">
                <p className="text-lg font-semibold">💡 Fun Emoji Fact</p>
                <p>{randomFact}</p>
            </div>

            <div className="bg-white w-full max-w-4xl rounded-lg shadow-lg p-6 mb-6">
                <div className="chat-box h-80 overflow-y-auto">
                    {chatHistory.map((message, index) => (
                        <div key={index} className={`p-3 my-2 rounded-md ${message.role === "user" ? "bg-blue-100 text-blue-900" : "bg-gray-100 text-gray-900"}`}>
                            <p>{message.content}</p>
                        </div>
                    ))}
                </div>
            </div>

            <form onSubmit={handleSubmit} className="w-full max-w-4xl flex">
                <input
                    type="text"
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)}
                    placeholder="Say something, I dare you! 😏"
                    className="flex-grow p-3 rounded-l-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-purple-500"
                />
                <button
                    type="submit"
                    disabled={loading}
                    className={`p-3 ml-1 rounded-r-lg text-white ${loading ? "bg-gray-400 cursor-not-allowed" : "bg-purple-600 hover:bg-purple-700"} transition-all duration-300`}
                >
                    {loading ? "Generating..." : "Send"}
                </button>
            </form>
        </div>
    );
}
