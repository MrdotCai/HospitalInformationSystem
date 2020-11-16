<template>
  <div>
    <el-container style="position: absolute;height:100%;width:100%" direction="vertical">
      <el-header>
        <b style="color:white;position:absolute;left:150px;top:2px;font-size:18px;"> REGISTER </b>
      </el-header>
      <el-main>
            <el-card class="box-card" >
              <el-form ref="registerform" :model="form" label-width="80px" :rules="rules">
                <b >请输入注册信息</b>
                <el-form-item label="姓名" style="margin-top: 15px" prop="name">
                  <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="年龄" prop="age">
                  <el-input v-model="form.age"></el-input>
                </el-form-item>
                <el-form-item label="性别" prop="sex">
                  <el-radio-group v-model="form.sex">
                    <el-radio label="男"></el-radio>
                    <el-radio label="女"></el-radio>
                  </el-radio-group>
                </el-form-item>
                <el-form-item label="手机号码" prop="phone">
                  <el-input v-model="form.phone"></el-input>
                </el-form-item>
                <el-form-item label="用户名" prop="username">
                  <el-input v-model="form.username"></el-input>
                </el-form-item>
                <el-form-item label="输入密码" prop="password">
                  <el-input v-model="form.password" show-password></el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="password_check">
                  <el-input v-model="form.password_check" show-password></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="onSubmit('registerform')">立即注册</el-button>
                  <el-button @click="exit">取消</el-button>
                </el-form-item>
              </el-form>
            </el-card>
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
// age,sex,phone,username,password
export default {
  data () {
    return {
      form: {
        name: '',
        age: '',
        sex: '',
        phone: '',
        username: '',
        password: '',
        password_check: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入姓名', trigger: 'blur' }
        ],
        age: [
          { required: true, message: '请选择年龄', trigger: 'blur' }
        ],
        sex: [
          { required: true, message: '请选择性别', trigger: 'change' }
        ],
        phone: [
          { required: true, message: '请输入手机号', trigger: 'change' },
          { max: 11, message: '长度在11个字符', trigger: 'blur' }
        ],
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ],
        password_check: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    register () {
    },
    exit () {
      this.$router.push({path: '/patientlogin'})
    },
    onSubmit (formName) {
      var vm = this
      vm.axios({
        method: 'post',
        url: 'http://localhost:8080/add_user',
        data: {
          'name': vm.form.name,
          'age': vm.form.age,
          'sex': vm.form.sex,
          'phone': vm.form.phone,
          'username': vm.form.username,
          'password': vm.form.password,
          'password_check': vm.form.password_check
        }
      })
        .then(function (response) {
          let ifsuccess = JSON.parse(JSON.stringify(response.data.flag))
          let id = JSON.parse(JSON.stringify(response.data.id))
          console.log(ifsuccess)
          if (ifsuccess === 'success') {
            var url1 = '/patientindex/' + id
            vm.$router.push({ path: url1 })
          } else {
            vm.$message({
              message: '注册失败！',
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
  margin: 100px auto;
  width: 500px;
}

</style>
