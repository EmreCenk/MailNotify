import React from "react"
import './App.css';
import Signup from "./Signup"
import { Container } from "react-bootstrap"
import { AuthProvider } from "../contexts/AuthContext"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"
import { useHistory } from "react-router-dom"
import Dashboard from "./Dashboard"
import Login from "./Login"
import Home from "./Home"
import get_photos from './sending_requests';

function App() {
  // let new_photos;

  // get_photos("emrecenk9@gmail.com").then(response => {
  //   new_photos = response;
  // })

  return (
      <div className="w-100">
        <Router>
          <AuthProvider>
            <Switch>
              <Route exact path="/" component={Home} />
              <Route path="/signup" component={Signup} />
              <Route path="/login" component={Login} />
              <Route path="/dash" component={Dashboard} />
            </Switch>
          </AuthProvider>
        </Router>
      </div>
  )
}

export default App
