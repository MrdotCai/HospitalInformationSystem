<template>

</template>

<script>
export default {
  name: 'backup',
  methods: {
    login () {
      var vm = this
      vm.axios({
        method: 'post',
        url: 'http://localhost:8080/check_user',
        data: {'username': vm.input_username, 'password': vm.input_password, 'flag': 0}
      })
        .then(function (response) {
          let ifsuccess = JSON.parse(JSON.stringify(response.data.flag))
          console.log(ifsuccess)
          if (ifsuccess === 'success') {
            vm.$router.push({path: '/patientindex'})
          }
        })
    }
  }
}
</script>

<style scoped>

</style>
