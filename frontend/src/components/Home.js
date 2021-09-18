import React from "react"
import SVG from "./img/Svgpic.svg"
import { useHistory } from "react-router-dom"

const Home = () => {
    const history = useHistory();

    return(
        <div className="home">
            <div className="text">
                <p id="one">MailNotify</p>
                <p id="two">Check your mailbox anywhere.</p>    
                <button className="herobutton" onClick={() => {
                    history.push("/login")
                }}>Login or Signup</button>
            </div>

            <div className="picture">
                <img src={SVG} alt="Svg" />
            </div>
        </div>
    )
}

export default Home;