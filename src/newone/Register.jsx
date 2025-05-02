import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './register.css';

const StudentRegistrationForm = () => {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [email, setEmail] = useState('');
  const [marks, setMarks] = useState('');
  const [percentage, setPercentage] = useState('');
  const [department, setDepartment] = useState('');
  const [grade, setGrade] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await axios.post('http://127.0.0.1:8000/students/register', {
        name,
        age,
        email,
        marks,
        percentage,
        department,
        grade,
      });
      navigate('/registerview'); // Navigate to view page
    } catch (err) {
      setError('Registration failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="student-container">
      <form onSubmit={handleSubmit} className="student-form">
        <h2 className="form-title">Student Registration</h2>
        {error && <div className="form-error">{error}</div>}

        <input placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} required />
        <input placeholder="Age" type="number" value={age} onChange={(e) => setAge(e.target.value)} required />
        <input placeholder="Email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <input placeholder="Marks" type="number" value={marks} onChange={(e) => setMarks(e.target.value)} required />
        <input placeholder="Percentage" type="number" step="0.01" value={percentage} onChange={(e) => setPercentage(e.target.value)} required />
        <input placeholder="Department" value={department} onChange={(e) => setDepartment(e.target.value)} required />
        <input placeholder="Grade" value={grade} onChange={(e) => setGrade(e.target.value)} required />

        <button type="submit" disabled={loading}>
          {loading ? 'Submitting...' : 'Submit'}
        </button>
      </form>
    </div>
  );
};

export default StudentRegistrationForm;
