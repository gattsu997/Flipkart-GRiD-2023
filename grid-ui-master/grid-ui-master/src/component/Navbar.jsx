import "./Navbar.css";
import { Link } from "react-router-dom";
 import logo from "../assets/TrendSense-logos/logo.png";

const Navbar = () => {
  return (
    <div className="navbar">
      <div className="navbar-title">
        <img
        src={logo}
       
          className="brand-icon"
        />
        {""}
      </div>

      <div className="navbar-links">
        <div className="navbar-link">
          <Link className="link" to="/">
            Chat
          </Link>
        </div>
        <div className="navbar-link">
          <Link className="link" to="/trends">
            Trends
          </Link>
        </div>
        <div className="navbar-link">
          <Link className="link" to="/recommendations">
            <img
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnIzLd2AEYnEMBJWAhnZH5Gg9txQdwWZLVxQ&usqp=CAU"
              // Replace with the path to your user logo image
              alt="User Logo"
              className="user-logo"
            />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
