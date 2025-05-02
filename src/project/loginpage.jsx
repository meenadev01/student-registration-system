import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from "axios";
import './login.css'

const LoginPage = () => {
  const [username, setUsername] = useState(""); 
  const [password, setPassword] = useState(""); 
  const [error, setError] = useState(""); 
  const [loading, setLoading] = useState(false); 

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    
    e.preventDefault(); 
    setLoading(true); 

    try {
      const response = await axios.post(" http://127.0.0.1:8000/sampledata", { username, password });


      if (response.data.status === "Success") {
        
        setError(""); 
        navigate("/register"); 
      } else {
        
        setError("Invalid username or password");
      }
    } catch (err) {
      
      console.error(err);
      setError("Something went wrong, please try again.");
    } finally {
      setLoading(false); 
    }
  };

  return (
    <div className="glass-container">             
      <div className="user"><h2>USER LOGIN</h2></div>
     
      <div className="login-box">
        <form onSubmit={handleLogin} action="#" method="POST">
          <div className='in'>
            <label htmlFor="username"></label>
            <input 
              type="text"   placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)}  />
          
          
          <div>
            <label htmlFor="password"></label>
            <input type="password"  placeholder="Password"  value={password}  onChange={(e) => setPassword(e.target.value)} />
          </div>
          </div>

          <div className="options">
            <input type="checkbox"  />
          <label htmlFor="remember">Remember me</label>

            <Link to="/forgetpassword">Forgot Password?</Link>
          </div>

          <button type="submit" disabled={loading}>
            {loading ? "Loading..." : "Login"}  
          </button>

          <h5>Don't have an Account? <Link to="/signup">SignUp</Link></h5>
        </form>

        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>
    </div>
  );
};

export default LoginPage;
