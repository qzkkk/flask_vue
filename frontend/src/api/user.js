import $axios from '~/axios'

const user = {
    login(params){
        return $axios.post('/login',{params})
    },
    register(params){
        return $axios.post('/register',{params})
    },
    get_list(){
        return $axios.get('/users')
    },
    update(params){
        return $axios.put('/user',{params})
    },
    del({_id}){
        return $axios.delete('/user/'+_id)
    },
    AdminLogin(params){
        return $axios.post('/admin/login', {params})
    }
}


export default user


