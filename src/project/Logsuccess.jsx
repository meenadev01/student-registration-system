import React, { useState, useEffect } from 'react';
import axios from 'axios';

function LoginSuccess() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState('');
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/sampledata')
      .then((response) => {
        setUsers(response.data);
        setError('');
      })
      .catch((err) => {
        setError('Failed to fetch users');
        console.error('Error details:', err);
      });
  }, []);

  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);  // Update the search query state
  };

  // Filter users based on the search query
  const filteredUsers = users.filter((user) =>
    user.username.toLowerCase().includes(searchQuery.toLowerCase()) ||
    user.password.toString().includes(searchQuery)  // Case-insensitive search for username and password
  );

  return (
    <div className="succ">
      <h1>LOGIN SUCCESSFULL!!!</h1>
      <h2>ALL USERS</h2>

      {error && <p style={{ color: 'red' }}>{error}</p>}
      <br></br>
      <div>
        <input
          type="text"
          placeholder="Search by username or password"
          value={searchQuery}
          onChange={handleSearchChange}
        />
      </div>
       <br></br>
       <br></br>
       
      <table border="1">
        <thead>
          <tr>
                  
            <th>USERNAME</th>
            <th>PASSWORD</th>
          </tr>
        </thead>
        <tbody>
          {filteredUsers.length > 0 ? (
            filteredUsers.map((user, index) => (
              <tr key={index}>
                <td>{user.username}</td>
                <td>{user.password}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="2">No users available</td>
            </tr>
          )}
        </tbody>
      </table>
      </div>
   
  );
}

export default LoginSuccess;
