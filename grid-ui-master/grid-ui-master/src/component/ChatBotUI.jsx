import React, { useState, useRef, useEffect } from "react";
import io from "socket.io-client";
import "./ChatBotUI.css"; // Create a CSS file for styling
const socket = io("http://127.0.0.1:3000"); // Replace with your Flask server URL

const ChatbotUI = ({botres,setdata}) => {
  const [messages, setMessages] = useState([
    { text: "Hii I am an AI, Let me be your versache", type: "incoming" },
  ]);
  const [userInput, setUserInput] = useState("");
  const [imageLinks, setImageLinks] = useState([]);

  const chatHistoryRef = useRef(null); // Ref for chat history

  const handleBotReply = (botData) => {
    setMessages((prevMessages) => [
      ...prevMessages,
      { text: botData.Message, type: "incoming" },
    ]);
    console.log(botData.links);

    if (botData.links && botData.links.length > 0) {
      setImageLinks([...botData.links[0]]);
      console.log("imageLinks:", imageLinks);
    }
  };

  const handleSendMessage = () => {
    if (userInput.trim() !== "") {
      const newUserMessage = { text: userInput, type: "outgoing" };

      setMessages((prevMessages) => [...prevMessages, newUserMessage]);
      socket.emit("message", { user_input: userInput }); // Send user input to server
      setUserInput("");
    }
  };

  // Scroll to the bottom of chat history when messages are updated
  useEffect(() => {
    chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
  }, [messages]);

  useEffect(() => {
    // Listen for incoming bot messages from the server
    socket.on("bot", (data) => {
      handleBotReply(data);
      console.log(data);
      setdata(data);
     
      setImageLinks(data.links); // Pass the response data to handleBotReply
    },[]);

    return () => {
      socket.off("bot");
    };
  }, []);

  return (
    <div className="chatbot-container">
      <div class="msg-header">
        <div class="container1">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUW0u5Eiiy3oM6wcpeEE6sXCzlh8G-tX1_Iw&usqp=CAU"
            class="msgimg"
          />
          <div class="active ">
            <p>Jaswanth</p>
          </div>
        </div>
      </div>

      <div className="chat-history" ref={chatHistoryRef}>
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.type}`}>
            {message.text}
          </div>
        ))}
      </div>
      <div className="user-input">
        <input
          type="text"
          placeholder="Type your message..."
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
        />
        <button onClick={handleSendMessage}>
✈️
</button>
      </div>
    </div>
  );
};

export default ChatbotUI;
