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
                    <b>姓名：</b>
                    <div>{{patient.name}}</div>
                  </el-row>
                  <el-row>
                    <b>性别：</b>
                    <div>{{patient.sex}}</div>
                  </el-row>
                  <el-row>
                    <b>年龄：</b>
                    <div>{{patient.age}}</div>
                  </el-row>
                </el-card>
              </el-col>
              <el-col :span="8">
               <el-card class="card2">
                  <b slot="header">药品信息</b>
                  <el-button type="text" @click="addmedicine()">添加处方</el-button>
                  <el-row v-for="(item,index) in medicine" :key="index">
                    <b>{{count}}</b>
                    <el-select v-model="item.name" placeholder="请选择药品">
                      <el-option
                        v-for="item1 in options"
                        :key="item1.value"
                        :label="item1.label"
                        :value="item1.value">
                      </el-option>
                    </el-select>
                    <el-input placeholder="请输入用法用量" vmodel='medicinnum' class="inputnum" v-model="item.use"></el-input>
                  </el-row>
                </el-card>
              </el-col>
            </el-row>
            <el-row>
              <el-card class="card3">
                <b slot="header">病情诊断</b>
                <el-input type="textarea" placeholder="请输入诊断内容" v-model="detail" :rows="12"></el-input>
              </el-card>
            </el-row>
            <el-button type="primary" class="updatebutton"   @click="update()">提交</el-button>
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
      doctor: {
        name: '',
        department: ''
      },
      patient: {
        name: '',
        sex: '',
        age: ''
      },
      detail: '',
      medicine_count: '',
      diagnose_id: '',
      doctor_id: '',
      medicine: [{
        name: '',
        use: ''
      }],
      options: []
      /* options: [{
        value: '感冒灵',
        label: '感冒灵'
      },
      {
        value: '退烧药',
        label: '退烧药'
      }] */
    }
  },
  created () {
    console.log('1111')
    this.medicine_count = 0
  },
  mounted () {
    this.doctor_id = this.$route.params['aid']
    this.diagnose_id = this.$route.params['bid']
    var vm = this
    this.axios({
      method: 'post',
      url: 'http://localhost:8080/get_diagnose',
      data: {'id': vm.doctor_id, 'diagnose_id': vm.diagnose_id}
    })
      .then(function (response) {
        console.log(response)
        //let doctor_info = JSON.parse(JSON.stringify(response.data.doctor))
        vm.options = response.data['options']
        vm.patient = response.data['patient']
        vm.doctor = response.data['doctor']
        // let options_info = JSON.parse(JSON.stringify(response.data.options))
        //vm.doctor = doctor_info
        // vm.options = options_info
      })
  },
  methods: {
    addmedicine () {
      if (this.medicine_count < 4) {
        this.medicine_count = this.medicine_count + 1
      } else {
        this.$message({
          message: '到达处方上限',
          type: 'warning'
        })
      }
      this.medicine.push({
        name: '',
        num: ''
      })
    },
    update () {
      console.log(this.medicine)
      console.log(this.detail)
      var vm = this
      this.axios({
        method: 'post',
        url: 'http://localhost:8080/update_diagnose',
        data: {'id': vm.diagnose_id, 'medicine': vm.medicine, 'detail': vm.detail}
      })
        .then(function (response) {
          let ifsuccess = JSON.parse(JSON.stringify(response.data.flag))
          console.log(ifsuccess)
          if (ifsuccess === 'success') {
            var url1 = '/doctorindex/' + vm.doctor_id
            vm.$router.push({ path: url1 })
          } else {
            vm.$message({
              message: '提交失败',
              type: 'warning'
            })
          }
        })
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
.inputnum {
  width: 150px;
}
.updatebutton {
  margin-left: 91%;
}
</style>
