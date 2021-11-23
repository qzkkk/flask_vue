"use strict";
import $axios from '~/axios';

const utils = {
    getDate(){
        return $axios.get('/day')
    }
}

export default utils