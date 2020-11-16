<template>
  <div>
    <el-container style="position: absolute;height:100%;width:100%" direction="vertical">
      <el-header>
        <b style="color:white;position:absolute;left:150px;top:2px;font-size:18px;"> LOGIN </b>
      </el-header>
      <el-main>
        <el-row style="margin-top: 110px">
          <el-col :span="6" :offset="4">
            <el-card :body-style="{ padding: '0px' }" @click.native="patientlogin()">
              <img src="../assets/patient.jpg" class="image">
              <div style="padding: 20px;">
                <b>患者点击登录>></b>
              </div>
            </el-card>
          </el-col>
          <el-col :span="6" :offset="4">
            <el-card :body-style="{ padding: '0px' }" @click.native="doctorlogin()">
              <img src="../assets/doctor.png" class="image">
              <div style="padding: 20px;" >
                <b>医生点击登录>></b>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <el-footer>
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
  methods: {
    patientlogin () {
      this.$router.push({path: '/patientlogin'})
    },
    doctorlogin () {
      this.$router.push({path: '/doctorlogin'})
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
  .image{
    width: 100%;
    display: block;
  }
</style>
