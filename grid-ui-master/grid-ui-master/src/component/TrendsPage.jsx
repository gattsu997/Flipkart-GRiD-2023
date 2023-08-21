import React, { useState, useEffect } from "react";
import "./TrendsPage.css";
import axios from "axios"; // Import Axios for making HTTP requests

function TrendsPage() {
  const [imageLinks, setImageLinks] = useState([]);
  const [scrollPosition, setScrollPosition] = useState(0);

  useEffect(() => {
    // Fetch image links from the server
    axios
      .get("http://127.0.0.1:3000/trends")
      .then((response) => {
        setImageLinks([...response.data, ...response.data]); // Duplicate the image links
      })
      .catch((error) => {
        console.error("Error fetching image links:", error);
      });
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setScrollPosition((prevScrollPosition) =>
        prevScrollPosition === imageLinks.length / 2 - 1
          ? 0
          : prevScrollPosition + 1
      );
    }, 3000);

    return () => clearInterval(interval);
  }, [imageLinks]);

  return (
    <div className="carousel-container">
      <div
        className="carousel-content"
        style={{
          transform: `translateX(-${scrollPosition * 33.33}%)`, // Assuming each card takes 33.33% width
        }}
      >
        {imageLinks.map((link, index) => (
          <div key={index} className="card">
            <a href={link} target="_blank" rel="noopener noreferrer">
              <img src={link} alt={`Card ${index + 1}`} />
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default TrendsPage;
