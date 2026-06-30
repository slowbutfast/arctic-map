import React, { useState } from "react";
import "../styles/ChatBot.css";

const ChatBot = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleOpen = () => setIsOpen((prev) => !prev);

  return (
    <div className="chatbot-container">
      <button className="chatbot-toggle" onClick={toggleOpen} type="button" aria-label="Toggle Chatbot">
        {isOpen ? "✕" : "💬"}
      </button>

      {isOpen && (
        <div className="chatbot-panel">
          <iframe
            src="https://udify.app/chatbot/g2Iy3LsSE9moCO16"
            style={{ width: "100%", height: "100%", border: "none" }}
            frameBorder="0"
            allow="microphone"
            title="Arctic Map Assistant"
          />
        </div>
      )}
    </div>
  );
};

export default ChatBot;
