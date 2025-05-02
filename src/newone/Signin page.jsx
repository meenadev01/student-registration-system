// import React, { useState } from 'react';
// import axios from 'axios';
// import './signin.css'
// import { Link } from 'react-router-dom';

// const SignInPage = () => {
//   const [username, setusername] = useState('');
//   const [password, setPassword] = useState('');
//   const [error, setError] = useState('');
//   const [loading, setLoading] = useState(false);

//   const handleLogin = async (e) => {
//     e.preventDefault();
//     setError('');
//     setLoading(true);

//     try {
//       const response = await axios.post('http://127.0.0.1:8000/sign', {
//         username,
//         password
//       });
//       console.log('Login successful:', response.data);
//     } catch (err) {
//       setError('Invalid username or password');
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className='container2'>
//       <form onSubmit={handleLogin}>
//         <h2>Sign In</h2>

//         {error && <div>{error}</div>}

//         <div className='inp'> 
//           <label>Username</label>
//           <input
//             type="username"
//             value={username}
//             onChange={(e) => setusername(e.target.value)}
//             required
//           />
//         </div>

//         <div className='inp'>
//           <label>Password</label>
//           <input
//             type="password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//             required
//           />
//         </div>

//         <button type="submit" className='bu' disabled={loading}>
//           {loading ? 'Signing in...' : 'Sign In'}
//         </button>
//       </form>
//     </div>
//   );
// };

// export default SignInPage;


import React, { useState } from 'react';
import axios from 'axios';
import './signin.css';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const SignInPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate(); // Initialize navigate

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await axios.post('http://127.0.0.1:8000/sign', {
        username,
        password
      });

      console.log('Login successful:', response.data);
      
      // ✅ Navigate to /register if login is successful
      navigate('/register');
    } catch (err) {
      setError('Invalid username or password');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className='container2'>
      <form onSubmit={handleLogin}>
        <h2>Sign In</h2>

        {error && <div>{error}</div>}

        <div className='inp'> 
          <label>Username</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>

        <div className='inp'>
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        <button type="submit" className='bu' disabled={loading}>
          {loading ? 'Signing in...' : 'Sign In'}
        </button>
      </form>
    </div>
  );
};

export default SignInPage;
