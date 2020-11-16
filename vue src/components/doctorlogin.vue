<template>
  <div>
    <el-container style="position: absolute;height:100%;width:100%" direction="vertical">
      <el-header>
        <b style="color:white;position:absolute;left:150px;top:2px;font-size:18px;"> DOCTOR LOGIN </b>
      </el-header>
      <el-main>
        <el-row style="margin-top: 200px">
          <el-col>
            <el-card class="box-card">
              <b>请输入医生用户名与密码</b>
              <el-input placeholder="请输入内用户名" v-model="input_username" clearable style="margin-top: 20px"></el-input>
              <el-input placeholder="请输入密码" v-model="input_password" show-password style="margin-top: 20px"></el-input>
              <el-row>
                <el-col :span="2" :offset="20" class="login_button" >
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
      var vm = this
      vm.axios({
        method: 'post',
        url: 'http://localhost:8080/check_user',
        data: {'username': vm.input_username, 'password': vm.input_password, 'flag': 1}
      })
        .then(function (response) {
          let ifsuccess = JSON.parse(JSON.stringify(response.data.flag))
          let id = JSON.parse(JSON.stringify(response.data.id))
          console.log(ifsuccess)
          if (ifsuccess === 'success') {
            var url1 = '/doctorindex/' + id
            vm.$router.push({ path: url1 })
          } else {
            vm.$message({
              message: '登录失败，请检查用户名及密码',
              type: 'warning'
            })
          }
        })
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
