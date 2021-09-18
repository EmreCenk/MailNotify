import axios from 'axios'


function get_user_information(email_of_user){
    
    let url = "http://127.0.0.1:5000/"; 
    //TODO: When deploying, change url from localhost to actual domain
    url+="userInfo";
    const parameters = {email: email_of_user};
    console.log("starting");
    
    const result = axios.get(url, {params: parameters})
    .then(data => console.log(data))
    .catch(err => console.log(err));

    console.log("yes");
}

get_user_information("emrecenk9@gmail.com")