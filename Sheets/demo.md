 # 预约-看诊流程测试demo

## 导入数据库接口

```python
from Sheets import db_intfs
```

## 用户注册

```python
db_intfs.create_new_doctor
db_intfs.create_new_patient
```

## 验证登陆,获取用户id

```python 
user_id = db_intfs.verify_and_login
```

  ## 获取用户id后获取用户信息显示在用户主页上

```python
user_data = db_intfs.get_user_info(user_id)
```

## 患者预约

```python
"假设现在患者登陆获取到了自己的患者id"
patient_id = user_data['patient_id']
#查看所有科室
all_depa = db_intfs.all_departments()
print(all_depa)
# 获取到科室名后通过科室看医生
neike_doc = db_intfs.doctor_of_depa('内科')
print(neike_doc)
# 获取到医生信息后根据医生id和患者id（之前登陆时获取的信息）进行预约
db_intfs.make_appointment(patient_id,neike_doc[0]['doctor_id'],"2020-11-13 00:00:00")
```

 ## 医生看病

```python
"现在假设患者预约的医生登陆了"
doctor_id = neike_doc[0]['doctor_id']
# 医生登陆后可以得到自己的医生id,根据这个id获取已预约的患者,
appo = db_intfs.doc_ask_waiting(doctor_id)
print(appo)
# 医生访问对第零号等待患者进行诊断
db_intfs.doctor_diagnose(appo[0]['record_id'],'感冒','发烧，流鼻涕，四肢乏力', '病毒性感冒',[{"drug": "999感冒灵", "usage":"一天三次，一次一包"},{"drug":"阿莫西林胶囊", "usage":"一天两次，一次一粒"}])
```

## 患者查看诊断结果

```python
history = db_intfs.pat_ask_history(patient_id)
print(history)
```

## 注销登出

```python
db_intfs.logout
```

