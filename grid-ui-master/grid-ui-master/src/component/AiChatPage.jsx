import React, { useState, useRef, useEffect } from "react";
import CardGrid from "./CardGrid"; // Make sure to import your CardGrid component
import ChatbotUI from "./ChatBotUI"; // Make sure to import your ChatbotUI component
import "./AiChatPage.css"; // Create a CSS file for styling

const AiChatPage = () => {
  const [BotRes, setBotRes] = useState()
  function setdata(data){
    setBotRes(data);
    console.log("botres: ",{BotRes});
  }
  return (
    <div className="content-container">
      <CardGrid botres={BotRes?.links} setdata={setdata} />
      <ChatbotUI botres={BotRes} setdata={setdata} />
    </div>
  );
};

export default AiChatPage;
