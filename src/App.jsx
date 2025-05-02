import React from 'react';
import { Routes, Route, Link } from 'react-router-dom'; 
import Loginpage from './newone/login';
import SignInPage from './newone/Signin page';
import StudentRegistrationForm from './newone/Register';
import RegisterPage from './newone/Registerview';



function App() {
  return (
   
      <div>
{/* <RegisterPage/> */}
<Routes>
  <Route path='/' element={<Loginpage/>}/>
  <Route path='/signin page' element={<SignInPage />}/>
  <Route path='/Register' element={<StudentRegistrationForm/>}/>
  <Route path='/Registerview' element={<RegisterPage />}/>

</Routes>












        {/* <LoginPage/>
      <Routes>
        <Route>
         <Route path="/" element={<Home/>}></Route>
         <Route path='/loginpage'element={<LoginPage/>}></Route>
        <Route path='/signup' element={<Signup/>}></Route>
        <Route path='/register' element={<Register/>}></Route>
         <Route path='/forgetpassword' element={<ForgetPassword/>}></Route>

       </Route>
       </Routes> */}
    </div>
  )
}

export default App;
