<template>
  <div class="container">
    <el-container style="position: absolute;height:100%;width:100%" direction="vertical">
      <el-container>
        <el-aside width="200px">
          <el-avatar class="avatar" :size="100" :src="require('../assets/doctor.png')"></el-avatar>
          <b class="asidetext">医师姓名：{{doctor.name}}</b><br>
          <b class="asidetext">科室：{{doctor.department}}</b>
        </el-aside>
        <el-container>
          <el-header>
            <b style="color:white;position:absolute;left:230px;top:2px;font-size:18px;"> Hospital Management </b>
          </el-header>
          <el-main>
            <el-row style="margin-top: 30px">
              <b style="margin-left:20%;">待处理患者</b>
            </el-row>
            <el-row>
              <el-table :data="formdata" height="650" style="width: 60%;margin: 0 auto;"  stripe>
                <el-table-column prop="name" label="患者姓名" style="width: 15%;" ></el-table-column>
                <el-table-column prop="age" label="患者年龄" style="width: 15%;"></el-table-column>
                <el-table-column prop="sex" label="患者性别" style="width: 15%;"></el-table-column>
                <el-table-column  style="width: 15%;">
                  <template slot-scope="scope">
                  <el-button type="primary" @click="getindex(scope.$index, scope.row)">进入诊断</el-button>
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
      user_id: '',
      doctor: {
        name: '',
        department: ''
      },
      formdata: []
      /* formdata: [{
        id: '',
        name: '张三',
        sex: '男',
        age: '10000'
      }
      ] */
    }
  },
  mounted () {
    this.user_id = this.$route.params['aid']
    console.log(this.diagnose_id)
    var vm = this
    this.axios({
      method: 'post',
      url: 'http://localhost:8080/doctor_index',
      data: {'id': vm.user_id}
    })
      .then(function (response) {
        console.log(response)
        let doctor_info = JSON.parse(JSON.stringify(response.data.doctor))
        vm.formdata = response.data['formdata']
        vm.doctor = response.data['doctor']
        // let form_info = JSON.parse(JSON.stringify(response.data.formdata))
        //vm.doctor = doctor_info
        // vm.formdata = form_info
      })
  },
  methods: {
    getindex (a, b) {
      var url1 = '/diagnoseinfo/' + this.user_id + '/' + b.id
      // var url1 = '/medirecord'
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
