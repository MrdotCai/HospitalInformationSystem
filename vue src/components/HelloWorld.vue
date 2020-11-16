<template>
  <div class="container">
    <el-container style="position: absolute;height:100%;width:100%" direction="vertical">
    <el-container>
      <el-aside width="200px">
        <el-avatar class="avatar" :size="100" :src="require('../assets/patient_avatar.png')"></el-avatar>
      </el-aside>
      <el-container>
        <el-header>
          <b style="color:white;position:absolute;left:230px;top:2px;font-size:18px;"> Hospital Management </b>
          <el-button type="text" style="color: white;margin-left:1100px;">logout</el-button>
        </el-header>
        <el-main>Main</el-main>
      </el-container>
    </el-container>
      <el-footer>
        <div style="color:#ffffff;">
          <p>Copyright &copy; 2020 GTZ </p>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
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
  text-align: center;
}
</style>
