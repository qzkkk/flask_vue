"use strict";
import $axios from '~/axios';

const article = {
    get(id){
        return $axios.get('/article/'+id)
    },
    save(params){
        return $axios.post('/article', {params} )
    },
    get_list(pid){
        if(pid){
            return $axios.get('/articles?pid='+pid)
        }
        return $axios.get('/articles')
    },
}

export default article