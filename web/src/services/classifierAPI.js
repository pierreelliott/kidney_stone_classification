import axios from 'axios';

const API_PATH = process.env.VUE_APP_API_PATH || 'localhost';
const API_PORT = process.env.VUE_APP_API_PORT || '5000';
const API_PROTOCOL = process.env.VUE_APP_API_PROTOCOL || 'http';

export const API_BASEURL = `${API_PROTOCOL}://${API_PATH}:${API_PORT}`;

export const sendForm = function (path, data) {
    if (typeof path !== 'string') {
        throw new TypeError(`Expected a string, got ${typeof path}`);
    }

    const formData = new FormData();

    if(data !== undefined && typeof data === 'object') {
        for(let key in data) {
            if(data.hasOwnProperty(key)) {
                formData.append(key, data[key]);
            }
        }
    }

    const config = {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    };
    return axios.post(`${API_BASEURL}${path}`, formData, config);
};
