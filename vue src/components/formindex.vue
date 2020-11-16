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
            <el-row>
              <el-col :span="3">
                <el-card class="card1">
                  <b slot="header">
                    <span>基本信息</span>
                  </b>
                  <el-row>
                    <b>科室：</b><br>
                    <div>{{formdata.department}}</div>
                  </el-row>
                  <el-row>
                    <b>主治医师：</b><br>
                    <div>{{formdata.doctorname}}</div>
                  </el-row>
                  <el-row>
                    <b>就诊时间：</b><br>
                    <div>{{formdata.time}}</div>
                  </el-row>
                </el-card>
              </el-col>
              <el-col :span="8">
                <el-card class="card2">
                  <b slot="header">药品信息</b>
                  <div style="white-space: pre">{{formdata.medicine}}</div>
                </el-card>
              </el-col>
            </el-row>
            <el-row>
              <el-card class="card3">
                <b slot="header">病情诊断</b>
                <div style="white-space: pre">{{formdata.diagnose}}</div>
              </el-card>
            </el-row>
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
      patient: {
        name: '',
        sex: '',
        age: ''
      },
      formdata: {
        doctorname: '',
        department: '',
        time: '',
        medicine: '',
        diagnose: ''
      },
      diagnose_id: '',
      user_id: ''
    }
  },
  mounted () {
    this.user_id = this.$route.params['aid']
    this.diagnose_id = this.$route.params['bid']
    console.log(this.diagnose_id)
    var vm = this
    this.axios({
      method: 'post',
      url: 'http://localhost:8080/diagnose_info',
      data: {'diagnose_id': vm.diagnose_id, 'user_id': vm.user_id}
    })
      .then(function (response) {
        console.log(response)
        vm.patient = response.data['patient']
        vm.formdata = response.data['formdata']
        //let patient_info = JSON.parse(JSON.stringify(response.data.patient))
        //let form_info = JSON.parse(JSON.stringify(response.data.formdata))
        //vm.patient = patient_info
        //vm.formdata = form_info
      })
  },
  methods: {
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
  .card1 {
    width: 300px;
    height: 300px;
    margin-left: 22%;
  }
  .card2 {
    width: 1000px;
    height: 300px;
    margin-left: 30%;
  }
  .card3 {
    width: 94%;
    height: 400px;
    margin: 30px auto;
  }
</style>
