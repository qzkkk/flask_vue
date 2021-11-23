"use strict";
import $axios from '~/axios'

const Categories = {
    getCategories(){
        return  $axios.get('/categories')
    },
    addCategory( params = {} ){
        return $axios.put('/category', params)
    },
    change(params={}){
        return $axios({
            method:'put',
            url:'/category/'+params.id,
            data: params
        })
    },
    del( params={} ){
        return $axios.delete('/category/'+params.id)
    }
}


export default Categories;