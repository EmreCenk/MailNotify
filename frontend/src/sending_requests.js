import axios from 'axios'

const url = "https://jsonplaceholder.typicode.com/posts"; // for testing
const parameters = {
    name: "Emre",
    id: 21,
};

const result = axios.get(url, parameters)
.then(data => console.log(data));
// console.log(result);
console.log("yes");