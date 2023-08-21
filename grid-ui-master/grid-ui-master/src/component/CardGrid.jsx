import React from "react";
import "./CardGrid.css"; // Import your CSS styles for the card grid here

function CardGrid({ botres, setdata }) {
  const imageLinks = botres?.slice(0, 4) || [
    "https://m.media-amazon.com/images/I/71g30rr3CqL._UX679_.jpg",
    "https://m.media-amazon.com/images/I/41x6+V39yNL.jpg",
    "https://m.media-amazon.com/images/I/61KIViYc9wL.jpg",
    "https://m.media-amazon.com/images/I/61LxYOkwnKL._UX569_.jpg",
  ];

  return (
    <div className="card-grid dot-pattern-background">
      {imageLinks.map((link, index) => (
        <div key={index} className="card">
          <div className="card-image translucent-image">
            <a
              key={index}
              href={link}
              target="_blank"
              rel="noopener noreferrer"
            >
              <img
                className="scaled-image"
                src={link}
                alt={`Card ${index + 1}`}
              />
            </a>
          </div>
        </div>
      ))}
    </div>
  );
}

export default CardGrid;
