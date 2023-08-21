import React from 'react'
import "./Recommendationspage.css";
function RecommendationsPage() {
const pastOrders = [
  {
    orderNumber: "12345",
    date: "2023-08-15",
    items: [
      { name: "US POLO Tshirt", price: "₹2500"  },
      { name: "NIKE AIR FORCE 1", price: "₹10000" },
    ],
    total: "₹12500",
  },
  {
    orderNumber: "12345",
    date: "2023-08-15",
    items: [
      { name: "US POLO Tshirt", price: "₹2500"  },
      { name: "NIKE AIR FORCE 1", price: "₹10000" },
    ],
    total: "₹12500",
  }
  // Add more dummy order data here
];

return (
  <div className="user-profile-container">
    <div className="user-header">
      <div className="user-icon">
        <img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnIzLd2AEYnEMBJWAhnZH5Gg9txQdwWZLVxQ&usqp=CAU"
          alt="User Icon"
        />
      </div>
      <div className="user-details">
        <h2 className="user-name">Jaswanth Reddy S</h2>
        <p className="user-email">jaswanthreddysomula@gmail.com</p>
      </div>
    </div>
    <div className="past-orders-card">
      <h2 className="card-title">Past Orders</h2>
      <div className="order-list">
        {pastOrders.map((order, index) => (
          <div key={index} className="order-item">
            <div className="order-number">Order #{order.orderNumber}</div>
            <div className="order-date">Date: {order.date}</div>
            <ul className="order-items">
              {order.items.map((item, itemIndex) => (
                <li key={itemIndex}>
                  <span className="item-name">{item.name}</span>
                  <span className="item-price">{item.price}</span>
                </li>
              ))}
            </ul>
            <div className="order-total">Total: {order.total}</div>
          </div>
        ))}
      </div>
    </div>
  </div>
);
}

export default RecommendationsPage