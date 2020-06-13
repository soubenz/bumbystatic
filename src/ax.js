// const API_URL = 'http://localhost:8000'

import qs from "qs";
const api = require('axios');
// api.defaults.baseURL = API_URL;
api.defaults.paramsSerializer = params => {
    return qs.stringify(params)
}

api.interceptors.request.use(function (config) {
    config.headers.Authorization = "Basic Zm5BRHRxUnA1MkFDRTBrMzlmWkVTMnR4bXNHZ2JScEVVUGRvZ1d4WjpidW1ieTpzZXJ2ZXI=";

    return config;
});
export default api;