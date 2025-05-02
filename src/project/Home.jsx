import React from 'react'
import './home.css'
import { useNavigate } from 'react-router-dom'

function Home() {
 const Navigate=useNavigate();
    function Login1(){
        Navigate("/LoginPage")
    }
    function Signin(){
        Navigate("/Signup")
    }
  return (
    <div>
        <h2>WELCOME TO OUR PAGE</h2>
        <button onClick={Login1}>LOGIN PAGE</button>
        <button onClick={Signin}>SIGNIN PAGE</button>
    </div>
  )
}

export default Home