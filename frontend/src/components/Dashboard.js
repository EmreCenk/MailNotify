import React from 'react';
import { useHistory } from "react-router-dom"

const Dashboard = ({handleLogout}) => {
    const history = useHistory();

    return(
        <section className="hero">
            <nav>
                <h2>Welcome to Mail Notification</h2>
                <button className="herobutton" onClick={() => {
                    history.push("/")
                }}>Logout</button>
            </nav>
        </section>
    )
}

export default Dashboard;