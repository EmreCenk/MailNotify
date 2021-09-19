import axios from 'axios'

function parse_date_string(date_string){
    date_string = date_string.split(" ");
    date_string[0] = date_string[0].split("-")
    date_string[1] = date_string[1].split("-")
    var monthNames = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ];
    //console.log(date_string);
    return String(monthNames[parseInt(date_string[0][1])-1] +
    " " + date_string[0][2] + ", " + date_string[0][0] + " | " + date_string[1][0] + ":" + date_string[1][1] )
}
async function get_user_information(email_of_user){
    /*
    email_of_user [string]: email of the user you would like to receive information on

    Returns: an array of objects. The return value is in the following format:
    
    [
    {
        date_string: 'September 18, 2021 | 12:34',
        image_url: 'uploads/emrecenk9/2021-09-18 12-33-22-693446.png',
        weight_string: '12 kg'
    },
    {
        date_string: 'September 18, 2021 | 13:07',
        image_url: 'uploads/emrecenk9/2021-09-18 12-34-18-296168.png',
        weight_string: '12 kg'
    }
    ]

    each entry is an id (you don't have to worry about what they are. )

    */
    let url = "http://127.0.0.1:5000/"; 
    //TODO: When deploying, change url from localhost to actual domain
    url+="userInfo";
    const parameters = {email: email_of_user};
    //console.log("starting");
    
    const response = await axios.get(url, {params: parameters});
    let final_list = [];
    let some_var;
    for (const id_ in response.data) {
        some_var = response.data[id_];
        // console.log("HERE", some_var.date_string, parse_date_string(some_var.date_string));
        some_var.date_string = String(parse_date_string(some_var.date_string));
        final_list.push(some_var);
      }
    //console.log(final_list);
    
    return final_list;
}

function parse_photos(user_information){
    let given_width = 4;
    let given_height = 3;
    let deliver = "Delivery Time: "

    let photos = [
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        },
        {
          src: "",
          width: given_width,
          height: given_height,
          caption: deliver
        }
      ];

    for (let i = 0; i < user_information.length && i < photos.length; i++){
        photos[i].src = user_information[i].image_url;
        photos[i].caption += user_information[i].date_string;
        photos[i].caption += "<br>Weight: " + user_information[i].weight_string;

    };

    return photos;
}
function get_photos(email_of_user){



    return get_user_information(email_of_user)
    .then(response => parse_photos(response));

    


}
export default get_photos;
// get_user_information("emrecenk9@gmail.com")
// console.log(parse_date_string('2021-09-18 13-07-08-145157',))
// let a = get_photos("emrecenk9@gmail.com");
// console.log("\n\n\nHERE")
// console.log(a);

// get_photos("emrecenk9@gmail.com").then(response => console.log(response));