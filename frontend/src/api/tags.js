"use strict";
import $axios from '~/axios';
const Tags = {
    get(){
        return $axios.get('/tags')
    },
    add(params={}){
        return $axios.post('/tag',params)
    },
    delete(name){
        return $axios.delete('/tag/'+name)
    }
}
export default Tags;