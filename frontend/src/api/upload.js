"use strict";
import $axios from '~/axios';

const upload = {
    img(data){
        return $axios({
            url:'/upload',
            method: 'post',
            data,
            headers:{'Content-Type':'multipart/form'}
        })
    }
}

export default upload