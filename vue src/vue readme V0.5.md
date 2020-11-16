# vue readme

## 1. django+vue连接

https://blog.csdn.net/Jack_wise/article/details/80690826

https://blog.csdn.net/weixin_41004350/article/details/79626656?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param

## 2. url

### 首页 

首页： http://localhost:8080

### 患者登录 http://localhost:8080/patientlogin

点击登录案件调用：http://localhost:8080/check_user

数据传递：
```
'username': vm.input_username, 
'password': vm.input_password, 
'flag': 0
```

如果成功，返回json：flag=success id=用户id

失败：返回json：flag=fail

### 医生登录 http://localhost:8080/doctorlogin

点击登录案件调用：http://localhost:8080/check_user

数据传递：
```
'username': vm.input_username, 
'password': vm.input_password, 
'flag': 1
```

如果成功跳转医生主页： 返回json：flag=success id=用户id

失败：返回json：flag=fail

### 患者注册 http://localhost:8080/patientregister

点击注册案件调用：http://localhost:8080/add_user

数据传递：

```
'name': vm.form.name,
'age': vm.form.age,
'sex': vm.form.sex,
'phone': vm.form.phone,
'username': vm.form.username,
'password': vm.form.password，
'password_check': vm.form.password_check
```

如果成功跳转： 返回json：flag=success id=患者id

失败：返回json：flag=fail

### 患者主页 http://localhost:8080/patientindex/:aid

渲染前调用：http://localhost:8080/patient_info

数据传递：'id': vm.user_id

返回数据：返回当前患者信息，他的所有病例信息

```
patient: {
  name: '',
  sex: '',
  age: ''
},
formdata: [{
        id: '',(病例id)
        date: '',(病例时间)
        department: '',(科室)
        doctor: '',
        done: ''(是否已完成，填写汉字)
},{...},{...}]
```

### 患者主页->查看某病例详情 http://localhost:8080/formindex/:aid/:bid

渲染前调用：http://localhost:8080/diagnose_info

数据传递：'diagnose_id': vm.diagnose_id, 'user_id': vm.user_id

返回数据：返回当前患者信息、当前病例信息

```
patient: {
  name: '',
  sex: '',
  age: ''
},
formdata: {
  doctorname: '',
  department: '',(科室)
  time: '',
  medicine: '',(处方处理成字符串)
  diagnose: ''(病情诊断)
}
```

### 患者主页->挂号 http://localhost:8080/newform/:aid

渲染前调用：http://localhost:8080/get_patient

数据传递：'id': vm.user_id

返回数据：返回当前患者信息，以及所有科室、医生信息

```
patient: {
  name: '',
  sex: '',
  age: ''
}，
options: [{
        value: '',
        label: '',
        children: [{
          value: '',
          label: ''
        },
        {
          value: '',
          label: ''
        }
        ]
      }]
      【options: [{value:'科室1id(如果没有就也返回名)',
      			  label：'科室1名',
      			  children:[{
      			  value:'医生1id'，
      			  label:'医生1名'
      			  }，
      			  {医生2...}]},
      			  {
      			  value:'科室2',
      			  label：'科室2',
      			  children:[{...}}
      			  }]】
```

挂号提交时调用：http://localhost:8080/add_register

数据传递：
```
'department': vm.section[0], 
'doctor': vm.section[1], 
'date': vm.newform.date1, 
'time': vm.newform.date2
```

如果成功跳转： 返回json：flag=success

失败：返回json：flag=fail

### 医生主页 http://localhost:8080/doctorindex/:aid

渲染前调用：http://localhost:8080/doctor_index

数据传递：'id': vm.user_iddoctor_index

返回数据：返回当前医生信息以及待他处理的挂号基本信息

```
doctor: {
  name: '',
  department: ''
},
formdata: [{
        id: '',(待处理挂号id)
        name: '',(患者姓名)
        sex: '',(患者性别)
        age: ''(患者年龄)
      },{...},{...}
      ] 
```

### 医生主页->进行诊断 http://localhost:8080/diagnoseinfo/:aid/:bid

渲染前调用：http://localhost:8080/get_diagnose

数据传递：'id': vm.doctor_id, 'diagnose_id': vm.diagnose_id

返回数据：返回当前医生信息与所有药品信息

```
doctor: {
  name: '',
  department: ''
},
patient: {
        name: '',
        sex: '',
        age: ''
      },
options: [{
label: '药1名',
value: '药1id'
},{...},{...}
]
```

提交时调用：http://localhost:8080/update_diagnose

数据传递：
```
'id': vm.diagnose_id, 
'medicine': vm.medicine, (medicine是一个数组：[{name:'',use:''},{...},{...}])
'detail': vm.detail
```

如果成功跳转： 返回json：flag=success

失败：返回json：flag=fail