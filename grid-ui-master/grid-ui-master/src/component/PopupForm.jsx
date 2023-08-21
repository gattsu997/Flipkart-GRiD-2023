import React, { useState } from "react";
import "./PopupForm.css"; // You can create this CSS file for styling

const PopupForm = ({ onClose }) => {
  const [formData, setFormData] = useState({
    name: "",
    address: "",
    phoneNumber: "",
    age: "",
    bodySize: "",
    sex: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleBodySizeChange = (option) => {
    setFormData((prevData) => ({
      ...prevData,
      bodySize: option,
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // You can perform any necessary actions with the form data here
    console.log(formData);
    onClose();
  };

  return (
    <div className="popup">
      <div className="popup-inner">
        <h2>Popup Form</h2>
        <form onSubmit={handleSubmit}>
          <label>
          Name:
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required/>
          </label>
          <label>
            Address:
            <input
              type="text"
              name="address"
              value={formData.address}
              onChange={handleChange}
              required
            />
          </label>
          <label>
            Phone Number:
            <input
              type="text"
              name="phoneNumber"
              value={formData.phoneNumber}
              onChange={handleChange}
              required
            />
          </label>
          <label>
            Age:
            <input
              type="text"
              name="age"
              value={formData.age}
              onChange={handleChange}
              required
            />
          </label>
          <label>
            Body Size:
            <div className="radio-group">
              <label>
                <input
                  type="radio"
                  name="bodySize"
                  value="small"
                  checked={formData.bodySize === "small"}
                  onChange={() => handleBodySizeChange("small")}
                />
                Small
              </label>
              <label>
                <input
                  type="radio"
                  name="bodySize"
                  value="medium"
                  checked={formData.bodySize === "medium"}
                  onChange={() => handleBodySizeChange("medium")}
                />
                Medium
              </label>
              <label>
                <input
                  type="radio"
                  name="bodySize"
                  value="large"
                  checked={formData.bodySize === "large"}
                  onChange={() => handleBodySizeChange("large")}
                />
                Large
              </label>
              <label>
                <input
                  type="radio"
                  name="bodySize"
                  value="extraLarge"
                  checked={formData.bodySize === "extraLarge"}
                  onChange={() => handleBodySizeChange("extraLarge")}
                />
                Extra Large
              </label>
            </div>
          </label>
          <label>
            Sex:
            <select
              name="sex"
              value={formData.sex}
              onChange={handleChange}
              required
            >
              <option value="">Select</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </label>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
};

export default PopupForm;
