<template>
  <div class="container">
    <el-container style="position: absolute;height:100%;width:100%" direction="vertical">
      <el-container>
        <el-aside width="200px">
          <el-avatar class="avatar" :size="100" :src="require('../assets/patient.jpg')"></el-avatar>
          <b class="asidetext">姓名：{{patient.name}}</b><br>
          <b class="asidetext">性别：{{patient.sex}}</b><br>
          <b class="asidetext">年龄：{{patient.age}}</b>
        </el-aside>
        <el-container>
          <el-header>
            <b style="color:white;position:absolute;left:230px;top:2px;font-size:18px;"> Hospital Management </b>
            <el-button type="text" style="color: white;margin-left:1100px;">logout</el-button>
          </el-header>
          <el-main>
            <el-card class="boxcard">
              <el-form ref="newform" :model="newform" label-width="100px" :rules="rules">
                <el-form-item label="科室/医生" prop="doctor">
                  <el-cascader
                  v-model="section"
                  :options="options"
                  @change="handlechange()"></el-cascader>
                </el-form-item>
                <el-form-item label="就诊时间" prop="date">
                    <el-date-picker placeholder="选择日期" v-model="newform.date1" style="width: 40%;" type="date" value-format="yyyy-MM-dd"></el-date-picker>-
                  <el-time-select v-model="newform.date2" :picker-options="{start: '08:30',step: '00:15',end: '18:30'}" placeholder="选择时间" style="width: 40%;"></el-time-select>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit('newform')" style="float:right;margin-right:30px;margin-top:5px">提交</el-button>
                </el-form-item>
              </el-form>
            </el-card>
          </el-main>
        </el-container>
      </el-container>
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
      user_id: '',
      newform: {
        date1: '',
        date2: ''
      },
      patient: {
        name: '',
        sex: '',
        age: ''
      },
      // 输出是一个数组，第一个值是科室，第二个值是医生
      section: [],
      options: [],
      /* options: [{
        value: '外科',
        label: '外科',
        children: [{
          value: '张三',
          label: '张三'
        },
        {
          value: '李四',
          label: '李四'
        }
        ]
      }], */
      rules: {
        date1: [
          {type: 'date', required: true, message: '请选择就诊时间', trigger: 'change'}
        ],
        date2: [
          {type: 'date', required: true, message: '请选择就诊时间', trigger: 'change'}
        ]
      }
    }
  },
  methods: {
    onSubmit (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          var vm = this
          this.axios({
            method: 'post',
            url: 'http://localhost:8080/add_register',
            data: {'department': vm.section[0], 'doctor': vm.section[1], 'date': vm.newform.date1, 'time': vm.newform.date2}
          })
            .then(function (response) {
              let ifsuccess = JSON.parse(JSON.stringify(response.data.flag))
              console.log(ifsuccess)
              if (ifsuccess === 'success') {
                var url1 = '/patientindex/' + vm.user_id
                vm.$router.push({ path: url1 })
              } else {
                vm.$message({
                  message: '挂号失败',
                  type: 'warning'
                })
              }
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    }
  },
  mounted () {
    this.user_id = this.$route.params['aid']
    var vm = this
    this.axios({
      method: 'post',
      url: 'http://localhost:8080/get_patient',
      data: {'id': vm.user_id}
    })
      .then(function (response) {
        //let patient_info = JSON.parse(JSON.stringify(response.data.patient))
        vm.options = response.data['options']
        vm.patient = response.data['patient']
        // let options_info = JSON.parse(JSON.stringify(response.data.options))
        //vm.options = response.data['options']
        //vm.patient = patient_info
        // vm.options = options_info
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .container{
    height:100%;
  }
  .avatar {
    margin: 30px 50px 50px 50px;
  }
  .el-aside {
    background-color: #52b586;
    width: 200px;
  }
  .el-header{
    background-color: #337ab7;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  .el-footer{
    background-color: black;
    color: #333;
    text-align: center;
  }
  .el-main {
    background-color: white;
    color: #333;
  }
  .asidetext{
    color:white;
    margin-left: 20px;
  }
  .newbutton{
    float: right;
    margin-right: 20%;
  }
  .boxcard {
    width: 500px;
    margin: 200px auto;
  }
</style>
