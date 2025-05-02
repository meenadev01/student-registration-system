import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const ForgetPassword = () => {
    const [username, setUsername] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [reEnterPassword, setReEnterPassword] = useState('');
    const [message, setMessage] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setMessage('');

        // Check if passwords match
        if (newPassword !== reEnterPassword) {
            setMessage('Passwords do not match');
            setLoading(false);
            return;
        }

        try {
            const response = await axios.post('http://127.0.0.1:8000/forgot_password', { username, new_password:newPassword
            }, {
                headers: {
                    'Content-Type': 'application/json'  // Ensure the correct header is set
                }

            });
            setMessage(response.data.message);
        } catch (error) {
            setMessage('An error occurred. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className='forgot-password-container'>
            <h2>FORGET  PASSWORD</h2>
            <br></br>
            <br></br>
            <form onSubmit={handleSubmit} className='forgot-password-form'>
                <label htmlFor="username">Username:</label>
                <input
                    type="text"
                    id="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <br />
                
                <label htmlFor="newPassword">New Password:</label>
                <input
                    type="password"
                    id="newPassword"
                    value={newPassword}
                    onChange={(e) => setNewPassword(e.target.value)}
                    required
                    className='input-field'
                />
                <br />
                
                <label htmlFor="reEnterPassword">Re-enter New Password:</label>
                <input
                    type="password"
                    id="reEnterPassword"
                    value={reEnterPassword}
                    onChange={(e) => setReEnterPassword(e.target.value)}
                    required
                    className='input-field'
                />
                <br />

                <button type="submit" disabled={loading}>
                    {loading ? 'Submitting...' : 'Submit'}
                </button>
            </form>
            {message && <p>{message}</p>}
            <br></br>
           
            <Link to="/">back</Link>
            
        </div>
    );
    
};

export default ForgetPassword;
