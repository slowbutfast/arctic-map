import React, { useState } from "react";
import "../styles/ChatBot.css";

const ChatBot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Hello! I am the Arctic Map GIS assistant. Ask me about layers, spatial queries, thematic maps, or dataset downloads.",
    },
  ]);
  const [input, setInput] = useState("");
  const [isSending, setIsSending] = useState(false);

  const toggleOpen = () => setIsOpen((prev) => !prev);

  const addMessage = (message) => {
    setMessages((prevMessages) => [...prevMessages, message]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const trimmedInput = input.trim();
    if (!trimmedInput || isSending) {
      return;
    }

    const userMessage = { role: "user", content: trimmedInput };
    addMessage(userMessage);
    setInput("");
    setIsSending(true);

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ messages: [userMessage] }),
      });

      if (!response.ok) {
        throw new Error(`Chat backend returned ${response.status}`);
      }

      const data = await response.json();
      addMessage({ role: "assistant", content: data.reply || "I could not generate an answer." });
    } catch (error) {
      console.error("Chat request failed:", error);
      addMessage({
        role: "assistant",
        content: "Sorry, I couldn't reach the chat service. Please try again later.",
      });
    } finally {
      setIsSending(false);
    }
  };

  return (
    <div className="chatbot-container">
      <button className="chatbot-toggle" onClick={toggleOpen} type="button">
        {isOpen ? "✕" : "💬"}
      </button>

      {isOpen && (
        <div className="chatbot-panel">
          <div className="chatbot-header">Arctic Map Assistant</div>
          <div className="chatbot-messages">
            {messages.map((message, index) => (
              <div
                key={index}
                className={`chatbot-message ${message.role === "user" ? "chatbot-user" : "chatbot-assistant"}`}
              >
                <div className="chatbot-role">{message.role === "user" ? "You" : "Assistant"}</div>
                <div className="chatbot-text">{message.content}</div>
              </div>
            ))}
            {isSending && (
              <div className="chatbot-message chatbot-assistant">
                <div className="chatbot-role">Assistant</div>
                <div className="chatbot-text">Typing…</div>
              </div>
            )}
          </div>

          <form className="chatbot-input-row" onSubmit={handleSubmit}>
            <input
              className="chatbot-input"
              type="text"
              value={input}
              onChange={(event) => setInput(event.target.value)}
              placeholder="Ask about Arctic Map..."
              disabled={isSending}
            />
            <button className="chatbot-send-button" type="submit" disabled={!input.trim() || isSending}>
              Send
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default ChatBot;
