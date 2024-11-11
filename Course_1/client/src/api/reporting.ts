import axios, { AxiosResponse } from "axios";

export const loadOrders = () => {
    return axios.get('http://localhost:8000/api/orders/')
    .then((response: AxiosResponse) => {
        return response.data
    })
}