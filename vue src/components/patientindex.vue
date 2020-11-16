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
          </el-header>
          <el-main>
            <el-row style="margin-top: 30px">
              <b style="margin-left:20%;">挂号记录</b>
              <el-button type="primary" class="newbutton" @click="newform()">挂号</el-button>
            </el-row>
            <el-row>
              <el-table :data="formdata" height="650" style="width: 60%;margin: 0 auto;"  stripe>
                <el-table-column prop="date" label="日期" style="width: 15%;" ></el-table-column>
                <el-table-column prop="department" label="科室" style="width: 15%;"></el-table-column>
                <el-table-column prop="doctor" label="主治医师" style="width: 15%;"></el-table-column>
                <el-table-column prop="done" label="是否已处理" style="width: 15%;"></el-table-column>
                <el-table-column  style="width: 15%;">
                  <template slot-scope="scope">
                  <el-button type="primary" @click="formindex(scope.$index, scope.row)">详细信息</el-button>
                  </template>
                </el-table-column>
              </el-table>
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
      formdata: [],
      /* formdata: [{
        id: '',
        date: '',
        department: '',
        doctor: '',
        done: ''
      }
      ], */
      user_id: ''
    }
  },
  created () {
  },
  mounted () {
    this.user_id = this.$route.params['aid']
    console.log(this.user_id)
    var vm = this
    this.axios({
      method: 'post',
      url: 'http://localhost:8080/patient_info',
      data: {'id': vm.user_id}
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
    newform () {
      var url1 = '/newform/' + this.user_id
      this.$router.push({path: url1})
    },
    formindex (a, b) {
      var url1 = '/formindex/' + this.user_id + '/' + b.id
      // var url1 = '/formindex'
      this.$router.push({ path: url1 })
    }
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
</style>
