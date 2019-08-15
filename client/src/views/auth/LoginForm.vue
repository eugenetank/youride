<template>
  <form @sumbit.prevent>
    <h1>Sign in</h1>
    <div>
      <label for="username">username</label>
      <input required id="username" type="text" v-model="username" placeholder="username" />
    </div>
    <div>
      <label for="password">password</label>
      <input required id="password" type="password" v-model="password" placeholder="password" />
    </div>
    <input type="submit" value="get token" @click="getToken()">
  </form>
</template>

<script>
  import axios from 'axios'

    export default {
        name: "LoginForm",
        data() {
            return {
                username: '',
                password: ''
            }
        },
        methods: {
            getToken() {
              const {username, password} = this;
              axios.post('http://localhost:8000/auth/token/', {username, password})
                .then(response => {
                    console.log(response);
                })
                .catch(err => {
                    console.log(err);
                })
            }
        }
    }
</script>

<style scoped>

</style>
