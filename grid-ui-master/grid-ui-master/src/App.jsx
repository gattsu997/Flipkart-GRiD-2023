import React, { useState, useRef, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./component/Navbar";
// Importing pages
import AiChatPage from "./component/AiChatPage";
import TrendsPage from "./component/TrendsPage";

import RecommendationsPage from "./component/RecommendationsPage";
import PopupForm from "./component/PopupForm";
import Footer from "./component/Footer";

const App = () => {

  const [formCompleted, setFormCompleted] = useState(false);
    const handleFormCompletion = () => {
      setFormCompleted(true);
    };


  return (
    <>
      {/* {!formCompleted ? (
        <PopupForm onClose={handleFormCompletion} />
      ) : (
        <>
          { */}
            <Router>
              <Navbar />
              <div className="app-container">
                <Routes>
                  <Route exact path="/" element={<AiChatPage />} />
                  <Route path="/trends" element={<TrendsPage />} />
                  <Route
                    path="/recommendations"
                    element={<RecommendationsPage />}
                  />
                </Routes>
              </div>
              <Footer/>
            </Router>
          {/* }
        </>
      )} */}
    </>
  );
};

export default App;
