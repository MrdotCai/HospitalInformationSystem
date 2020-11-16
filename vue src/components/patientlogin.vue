<template>
  <div>
    <el-container style="position: absolute;height:100%;width:100%" direction="vertical">
      <el-header>
        <b style="color:white;position:absolute;left:150px;top:2px;font-size:18px;">PATIENT LOGIN </b>
      </el-header>
      <el-main>
        <el-row style="margin-top: 200px">
          <el-col>
            <el-card class="box-card">
              <b>请输入患者用户名与密码</b>
              <el-input placeholder="请输入用户名" v-model="input_username" clearable style="margin-top: 20px"></el-input>
              <el-input placeholder="请输入密码" v-model="input_password" show-password style="margin-top: 20px"></el-input>
              <el-row>
                <el-col :span="3">
                  <el-button type="text" @click.native="register()">未有账户？点击注册</el-button>
                </el-col>
                <el-col :span="2" :offset="17" class="login_button">
                  <el-button type="primary" style="margin-top: 30px" @click.native="login()">登录</el-button>
                </el-col>
              </el-row>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <el-footer >
        <div style="color:#ffffff;" >
          <p>Made by GTZ/YYZ/CJ<br>
            Copyright &copy; 2020</p>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      input_username: '',
      input_password: ''
    }
  },
  methods: {
    login () {
      console.log(this.input_username)
      console.log(this.input_password)
      var vm = this
      this.axios({
        method: 'get',
        url: 'http://localhost:8080/get_token'
      })
        .then(function (response) {
          console.log('in post')
          // let csrftoken = response['token']
          let csrftoken = vm.$cookie.get('csrftoken')
          vm.axios({
            method: 'post',
            headers: {'X-CSRFtoken': csrftoken},
            url: 'http://localhost:8080/check_user',
            data: {'username': vm.input_username, 'password': vm.input_password, 'flag': 0}
          })
            .then(function (response) {
              let ifsuccess = JSON.parse(JSON.stringify(response.data.flag))
              let id = JSON.parse(JSON.stringify(response.data.id))
              console.log(id)
              console.log(ifsuccess)
              if (ifsuccess === 'success') {
                var url1 = '/patientindex/' + id
                vm.$router.push({ path: url1 })
              } else {
                vm.$message({
                  message: '登录失败，请检查用户名及密码',
                  type: 'warning'
                })
              }
            })
        })
    },
    register () {
      this.$router.push({path: '/patientregister'})
    }
  }
}
</script>

<style scoped>
.el-footer{
  background-color: black;
  color: #333;
  text-align: center;
}
.el-header{
  background-color: #337ab7;
  color: #333;
  text-align: center;
  line-height: 60px;

}
.el-main{
  background: url("../assets/background.jpg");
  background-size: 100% 100%;
}
.box-card{
  width: 500px;
  margin: auto;
}
.login_button{
  width: 50px;
}
</style>
