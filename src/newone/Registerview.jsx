// import React, { useState, useEffect } from 'react';
// import './registerview.css';

// const RegisterPage = () => {
//   const [students, setStudents] = useState([]);
//   const [search, setSearch] = useState('');
//   const [filterDept, setFilterDept] = useState('');
//   const [sortField, setSortField] = useState('');
//   const [formData, setFormData] = useState({
//     name: '',
//     age: '',
//     email: '',
//     marks: '',
//     percentage: '',
//     department: '',
//     grade: '',
//   });

//   // Fetch students on load
//   useEffect(() => {
//     const fetchStudents = async () => {
//       try {
//         const response = await fetch('http://127.0.0.1:8000/students');
//         const data = await response.json();

//         // Check if the response contains the "students" property
//         if (data.students && Array.isArray(data.students)) {
//           const transformedData = data.students.map((student) => ({
//             name: student[0],
//             age: student[1],
//             email: student[2],
//             marks: student[3],
//             percentage: student[4],
//             department: student[5],
//             grade: student[6],
//           }));

//           setStudents(transformedData);
//         } else {
//           console.error('Unexpected data format:', data);
//         }
//       } catch (error) {
//         console.error('Error fetching students:', error);
//       }
//     };
//     fetchStudents();
//   }, []);

//   const handleChange = (e) => {
//     setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await fetch('http://127.0.0.1:8000/students', {
//         method: 'POST', // Use POST to create a new student
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify(formData),
//       });
//       if (!response.ok) {
//         throw new Error("Failed to add student");
//       }
//       const newStudent = await response.json();
//       setStudents(prev => [...prev, newStudent]);
//       setFormData({
//         name: '',
//         age: '',
//         email: '',
//         marks: '',
//         percentage: '',
//         department: '',
//         grade: '',
//       });
//     } catch (err) {
//       console.error(err.message);
//     }
//   };

//   const handleDelete = async (email) => {
//     try {
//       const response = await fetch(`http://127.0.0.1:8000/students/${email}`, {
//         method: 'DELETE', // Use DELETE to remove a student
//       });
//       if (!response.ok) {
//         throw new Error("Failed to delete student");
//       }
//       setStudents(prev => prev.filter(s => s.email !== email));
//     } catch (err) {
//       console.error(err.message);
//     }
//   };

//   const filteredStudents = students
//     .filter(s =>
//       (s.name && s.name.toLowerCase().includes(search.toLowerCase())) ||
//       (s.email && s.email.toLowerCase().includes(search.toLowerCase()))
//     )
//     .filter(s =>
//       filterDept ? s.department === filterDept : true
//     )
//     .sort((a, b) => {
//       if (!sortField) return 0;
//       if (sortField === 'name' || sortField === 'department') {
//         return a[sortField].localeCompare(b[sortField]);
//       } else {
//         return parseFloat(a[sortField]) - parseFloat(b[sortField]);
//       }
//     });

//   return (
//     <div className="register-page">
//       <h2>Student Registration</h2>

//       <form onSubmit={handleSubmit}>
//         <input
//           type="text"
//           name="name"
//           value={formData.name}
//           onChange={handleChange}
//           placeholder="Name"
//         />
//         <input
//           type="number"
//           name="age"
//           value={formData.age}
//           onChange={handleChange}
//           placeholder="Age"
//         />
//         <input
//           type="email"
//           name="email"
//           value={formData.email}
//           onChange={handleChange}
//           placeholder="Email"
//         />
//         <input
//           type="number"
//           name="marks"
//           value={formData.marks}
//           onChange={handleChange}
//           placeholder="Marks"
//         />
//         <input
//           type="number"
//           name="percentage"
//           value={formData.percentage}
//           onChange={handleChange}
//           placeholder="Percentage"
//         />
//         <input
//           type="text"
//           name="department"
//           value={formData.department}
//           onChange={handleChange}
//           placeholder="Department"
//         />
//         <input
//           type="text"
//           name="grade"
//           value={formData.grade}
//           onChange={handleChange}
//           placeholder="Grade"
//         />
//         <button type="submit">Register Student</button>
//       </form>

//       <div className="controls">
//         <input
//           placeholder="Search by name/email"
//           value={search}
//           onChange={(e) => setSearch(e.target.value)}
//         />
//         <select onChange={(e) => setFilterDept(e.target.value)} value={filterDept}>
//           <option value="">Filter by Department</option>
//           {[...new Set(students.map(s => s.department))].map((dept, i) => (
//             <option key={i} value={dept}>{dept}</option>
//           ))}
//         </select>
//         <select onChange={(e) => setSortField(e.target.value)} value={sortField}>
//           <option value="">Sort by</option>
//           <option value="name">Name</option>
//           <option value="age">Age</option>
//           <option value="marks">Marks</option>
//           <option value="percentage">Percentage</option>
//           <option value="department">Department</option>
//         </select>
//       </div>

//       <table className="student-table">
//         <thead>
//           <tr>
//             <th>Name</th><th>Age</th><th>Email</th><th>Marks</th>
//             <th>Percentage</th><th>Department</th><th>Grade</th><th>Action</th>
//           </tr>
//         </thead>
//         <tbody>
//           {filteredStudents.map((s, i) => (
//             <tr key={i}>
//               <td>{s.name}</td>
//               <td>{s.age}</td>
//               <td>{s.email}</td>
//               <td>{s.marks}</td>
//               <td>{s.percentage}</td>
//               <td>{s.department}</td>
//               <td>{s.grade}</td>
//               <td>
//                 <button onClick={() => handleDelete(s.email)}>Delete</button>
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// };

// export default RegisterPage;



import React, { useState, useEffect } from 'react';
import './registerview.css';

const RegisterPage = () => {
  const [students, setStudents] = useState([]);
  const [search, setSearch] = useState('');
  const [filterDept, setFilterDept] = useState('');
  const [sortField, setSortField] = useState('');
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    email: '',
    marks: '',
    percentage: '',
    department: '',
    grade: '',
  });

  // Fetch students on load
  useEffect(() => {
    const fetchStudents = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/students');
        const data = await response.json();
        if (Array.isArray(data.students)) {
          // Convert tuple-like array to objects
          const formatted = data.students.map(s => ({
            name: s[0],
            age: s[1],
            email: s[2],
            marks: s[3],
            percentage: s[4],
            department: s[5],
            grade: s[6],
          }));
          setStudents(formatted);
        } else {
          console.error("Unexpected data format:", data);
        }
      } catch (error) {
        console.error("Error fetching students:", error);
      }
    };
    fetchStudents();
  }, []);

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:8000/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      if (!response.ok) throw new Error("Failed to add student");

      const newStudent = await response.json();
      setStudents(prev => [...prev, newStudent]);

      setFormData({
        name: '',
        age: '',
        email: '',
        marks: '',
        percentage: '',
        department: '',
        grade: '',
      });
    } catch (err) {
      console.error(err.message);
    }
  };

  const handleDelete = async (email) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/students/${email}`, {
        method: 'DELETE',
      });
      if (!response.ok) throw new Error("Failed to delete student");

      setStudents(prev => prev.filter(s => s.email !== email));
    } catch (err) {
      console.error(err.message);
    }
  };

  const filteredStudents = students
    .filter(s =>
      (s.name && s.name.toLowerCase().includes(search.toLowerCase())) ||
      (s.email && s.email.toLowerCase().includes(search.toLowerCase()))
    )
    .filter(s =>
      filterDept ? s.department.toLowerCase() === filterDept.toLowerCase() : true
    )
    .sort((a, b) => {
      if (!sortField) return 0;
      if (sortField === 'name' || sortField === 'department') {
        return a[sortField].localeCompare(b[sortField]);
      } else {
        return parseFloat(a[sortField]) - parseFloat(b[sortField]);
      }
    });

  return (
    <div className="register-page">
      <h2>Student Registration</h2>

      

      <div className="controls">
        <input
          placeholder="Search by name/email"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <select onChange={(e) => setFilterDept(e.target.value)} value={filterDept}>
          <option value="">Filter by Department</option>
          {[...new Set(students.map(s => s.department))].map((dept, i) => (
            <option key={i} value={dept}>{dept}</option>
          ))}
        </select>
        <select onChange={(e) => setSortField(e.target.value)} value={sortField}>
          <option value="">Sort by</option>
          <option value="name">Name</option>
          <option value="age">Age</option>
          <option value="marks">Marks</option>
          <option value="percentage">Percentage</option>
          <option value="department">Department</option>
        </select>
      </div>

      <table className="student-table">
        <thead>
          <tr>
            <th>Name</th><th>Age</th><th>Email</th><th>Marks</th>
            <th>Percentage</th><th>Department</th><th>Grade</th>
          </tr>
        </thead>
        <tbody>
          {filteredStudents.map((s, i) => (
            <tr key={i}>
              <td>{s.name}</td>
              <td>{s.age}</td>
              <td>{s.email}</td>
              <td>{s.marks}</td>
              <td>{s.percentage}</td>
              <td>{s.department}</td>
              <td>{s.grade}</td>
             
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default RegisterPage;
