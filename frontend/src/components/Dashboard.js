import React from 'react';
import { useHistory } from "react-router-dom"
import Gallery from "react-photo-gallery";
import ImageWithCaption from "./ImageWithCaption";
import { photos } from "./photos";
import "./styles.css";

const Dashboard = ({handleLogout}) => {
    const history = useHistory();

    const imageRenderer = ({ index, left, top, key, photo }) => (
        <ImageWithCaption
          key={key}
          margin={"20px"}
          index={index}
          photo={photo}
          left={left}
          top={top}
        />
      );

    return(
        <section className="hero">
            <nav>
                <h2>Welcome back to MailNotify!</h2>
                <button className="herobutton" onClick={() => {
                    history.push("/")
                }}>Logout</button>
            </nav>
            <Gallery photos={photos} renderImage={imageRenderer}></Gallery>
        </section>
    )
}

export default Dashboard;