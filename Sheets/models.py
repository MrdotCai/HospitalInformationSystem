from django.db import models

# --- department sheet ---
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True) # 科室名称
    desc = models.TextField() # 描述

# --- doctor sheet ---
class Doctor(models.Model):
    gender = (
        ('m','male'),
        ('f','female')
    )
    name = models.CharField(max_length=20) # 医生姓名
    sex = models.CharField(max_length=5, choices=gender) # 医生性别
    tel = models.CharField(max_length=11) # 医生电话
    email = models.EmailField() # 医生邮件
    department = models.ForeignKey('Department', on_delete=models.CASCADE) # 科室外键
    age = models.IntegerField() # 医生年龄
    user_key = models.IntegerField() # 用户id,非外键

# --- patient sheet ---
class Patient(models.Model):
    gender = (
        ('m','male'),
        ('f','female')
    )
    name = models.CharField(max_length=20) # 患者姓名
    sex = models.CharField(max_length=5, choices=gender) # 患者性别
    tel = models.CharField(max_length=11) # 患者电话
    email = models.EmailField() # 患者邮件
    age = models.IntegerField() # 患者年龄
    user_key = models.IntegerField() # 用户id，非外键

# --- drug sheet ---
class Drug(models.Model):
    name = models.CharField(max_length=100, unique=True) # 药品名称
    price = models.DecimalField(max_digits=5, decimal_places=2) # 药品价格
    desc = models.TextField() # 描述

# --- medical record sheet ---
class MedicalRecord(models.Model):
    # 预约状态
    appo_confirm = models.BooleanField() # 此条预约是否被医生确认
    appo_cancel = models.BooleanField() # 此条预约是否被医生取消，一条被取消的预约成为一条历史病历记录，无论医生是否确认
    appo_complete = models.BooleanField() # 此条预约是否被医生完成，一条被确认的预约被完成就成为一条历史病历记录
    '''
    confirm     cancel      complete    status
    0           0           0           预约中（newappo）
    0           1           0           已拒绝（refused）
    1           0           0           待诊断（waiting）
    1           0           1           已诊断（handled）
    1           1           0           已作废（calloff）
    其它                                有误   (error)
    '''
    # 患者预约
    doctor_key = models.ForeignKey('Doctor', on_delete=models.CASCADE) # 本次预约的患者
    patient_key = models.ForeignKey('Patient', on_delete=models.CASCADE) # 本次预约的医生
    submit_time = models.DateTimeField(auto_now_add=True) # 预约提交时间
    appo_time = models.DateTimeField() # 预约看病时间
    appo_message = models.TextField(null=True) # 预约时的携带消息
    symptom = models.TextField(null=True) # 预约时的症状描述
    # 医生拒绝/取消
    cancel_message = models.TextField(null=True) # 医生拒绝/取消时的携带消息
    # 医生诊断
    disease = models.CharField(max_length=100, null=True) # 患病类型：主诉（感冒）
    detail = models.TextField(null=True) # 患病细节描述：病症（鼻塞、乏力、发热）
    diag_message = models.TextField(null=True) # 诊断（病毒性感染引发流感）
    prescription = models.CharField(max_length=1000, null=True) # 医生处方：药品+用法用量
    drugs_key = models.ManyToManyField('Drug')
