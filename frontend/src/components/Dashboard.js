import React from 'react';
import { useHistory } from "react-router-dom"
import Gallery from "react-photo-gallery";
import ImageWithCaption from "./ImageWithCaption";
import "./styles.css";
// import get_photos from './sending_requests';
// import { get_user_information, parse_photos } from "./sending_requests"
import get_user_information from "./sending_requests"
// import parse_photos from "./sending_requests"
export default class Dashboard extends React.Component {
    state = {
      photos: []
    };




    
    componentDidMount() {
        // console.log(typeof(get_user_information))
        get_user_information("emrecenk9@gmail.com").then(result => {
            const photos = result;
            this.setState({ photos });
            console.log("what we wanted", result);
            console.log("what we got", this.state.photos)
            var imgs = document.getElementsByTagName("img");
            var captions = document.getElementsByClassName("react-photo-gallery--gallery")[0].firstElementChild.childNodes;
            console.log("alpha", captions);
            for (let i = 0; i < imgs.length; i++){
                imgs[i].src = photos[i].image_url;
                imgs[i].style = "width: 50%; margin-left: 25% "
                // console.log(captions[i].innerHTML, captions[i].nodeValue);
                captions[i].innerHTML += "<div style='font-size:65px; text-align:center'> Delivered on " + photos[i].date_string + "</div>";
                // imgs[i].outerText = "yAH";
                // imgs[i].caption = photos[i].date_string;
            }
        }   
            )
        ;
    }


    render() {

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

        return (
            <section className="hero">
                <nav>
                    <h2>Welcome back to MailNotify!</h2>
                    <button className="herobutton" onClick={() => {this.props.history.push("/")}}>Logout</button>
                </nav>
                <Gallery photos={this.state.photos} renderImage={imageRenderer}></Gallery>
            </section>
        // <ul>
        //   { this.state.persons.map(person => <li>{person.name}</li>)}
        // </ul>
      )
    }
  }

// const Dashboard = ({loginHandler}) => {
//     const history = useHistory();

//     const imageRenderer = ({ index, left, top, key, photo }) => (
//         <ImageWithCaption
//           key={key}
//           margin={"20px"}
//           index={index}
//           photo={photo}
//           left={left}
//           top={top}
//         />
//       );
    
//     console.log("yes");
//     // get_photos("emrecenk9@gmail.com").then(response => console.log(response));
//     // let response = await get_photos("emrecenk9@gmail.com");
//     // console.log(response);
//     console.log("no");

//     return(
//         <section className="hero">
//             <nav>
//                 <h2>Welcome back to MailNotify!</h2>
//                 <button className="herobutton" onClick={() => {
//                     history.push("/")
//                 }}>Logout</button>
//             </nav>
//             <Gallery photos={photos} renderImage={imageRenderer}></Gallery>
//         </section>
//     )
// }

// export default Dashboard;