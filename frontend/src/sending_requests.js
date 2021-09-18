import axios from 'axios'


async function get_user_information(email_of_user){
    /*
    email_of_user [string]: email of the user you would like to receive information on

    Returns: an object in the following format:
    {
        '694394747906926353': {
        date_string: '2021-09-18 12-34-18-296168',
        image_url: 'uploads/emrecenk9/2021-09-18 12-33-22-693446.png',      weight_string: '12 kg'
        },
        '694401203183298321': {
        date_string: '2021-09-18 13-07-08-145157',
        image_url: 'uploads/emrecenk9/2021-09-18 12-34-18-296168.png',      weight_string: '12 kg'
        }
    }

    each entry is an id (you don't have to worry about what they are. )

    */
    let url = "http://127.0.0.1:5000/"; 
    //TODO: When deploying, change url from localhost to actual domain
    url+="userInfo";
    const parameters = {email: email_of_user};
    console.log("starting");
    
    const response = await axios.get(url, {params: parameters});
    let final_list = [];

    for (const id_ in response.data) {
        final_list.push(response.data[id_]);
      }
    // console.log(typeof(response.data));
    console.log(response.data);
    console.log(final_list);
    
    return final_list;
}

get_user_information("emrecenk9@gmail.com")