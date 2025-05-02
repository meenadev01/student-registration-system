import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Signup = () => {
  const Navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

   
    if (password !== confirmPassword) {
      setMessage('Passwords do not match!');
      return;
    }

    try {
      
      const response = await axios.post('http://127.0.0.1:8000/insert', {
        username: username,
        password: password,
      });

      setMessage(response.data.message || 'Signup successful!');
      setTimeout(() => {
        Navigate('/LoginPage');
      }, 2000); 
    } catch (error) {
      
      setMessage('Error inserting data. Please try again.');
      console.error(error);
    }
  };

  function goToLogin() {
    Navigate('/LoginPage');
  }

  return (
    <div>
      <div className="glass-container">
        <div className="user">
          <h2>SignUp</h2>
        </div>
        <div className="image">
          <img
            src="data:image/png;base64,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"
            height="80px"
            width="80px"
          />
        </div>

        <div className="login-box">
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              id="username"
              name="username"
              required
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <input
              type="password"
              id="password"
              name="password"
              required
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <input
              type="password"
              id="confirmPassword"
              name="confirmPassword"
              required
              placeholder="Confirm Password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
            <div className="options">
              <input type="checkbox" id="remember" name="remember" />
              <label htmlFor="remember">Remember me</label>
              
            </div>

            <button type="submit">Submit</button>
            <button type="button" onClick={goToLogin}>Login</button>
          </form>
          {message && (
            <p style={{ color: message.includes('Error') ? 'red' : 'green' }}>
              {message}
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Signup;
