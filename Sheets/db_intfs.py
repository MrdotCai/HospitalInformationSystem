import json
import datetime

from django.contrib import auth
from django.contrib.auth.models import User

from .models import Department
from .models import Doctor
from .models import Patient
from .models import Drug
from .models import MedicalRecord

# --- create ---
def depa_insert_value(name, desc='暂无描述'):
    "新建科室项，参数均为字符串格式"
    Department.objects.create(name=name, desc=desc)

def doctor_insert_value(name, sex, tel, email, department, age, user_key):
    "新建医生项，除了user_key与age为整形，其它参数均为字符串格式，sex一定要传'm'或者'f'"
    depa_obj = Department.objects.filter(name=department).first()
    Doctor.objects.create(name=name, sex=sex, tel=tel, email=email, department=depa_obj, age=age, user_key=user_key)

def patient_insert_value(name, sex, tel, email, age, user_key):
    "新建患者项，最后两个参数为整形，参数均为字符串格式"
    Patient.objects.create(name=name, sex=sex, tel=tel, email=email, age=age, user_key=user_key)

def drug_insert_value(name, price=100.00, desc='暂无描述'):
    "新建药品项，price为xxx.xx的浮点数，其它均为字符串" 
    Drug.objects.create(name=name, price=price, desc='暂无描述')

def medi_insert_value(doctor_id, patient_id, submit_time, appo_time, comfirm, 
        symptom, message):
    "新建病历项，前两个参数为doctor和patient的主键，两个time参数为字符串，格式为'YYY-MM-DD HH:MM:SS'"
    doctor = Doctor.objects.filter(pk=doctor_id).first()
    patient = Patient.objects.filter(pk=patient_id).first()
    MedicalRecord.objects.create(appo_confirm=comfirm, appo_cancel=False, appo_complete=False,
        doctor_key=doctor, patient_key=patient, submit_time=submit_time, appo_time=appo_time,
        symptom=symptom, appo_message=message, cancel_message='',
        disease='', detail='', diag_message='', prescription='[]')

def create_superuser(username, password, email):
    "创建超级用户，所有参数均为字符串类型"
    User.objects.create_superuser(username=username, password=password, email=email)

def create_new_doctor(username, password, name, sex, tel, email, department, age):
    "创建医生用户，除了age为整形，所有参数均为字符串类型，sex请传'f'或'm'"
    user = User.objects.create_user(username=username, password=password)
    doctor_insert_value(name, sex, tel, email, department, age, user.pk)

def create_new_patient(username, password, name, sex, tel, email, age):
    "创建患者用户，除了age为整形，所有参数均为字符串类型，sex请传'f'或'm'"
    user = User.objects.create_user(username=username, password=password)
    patient_insert_value(name, sex, tel, email, age, user.pk)

def make_appointment(patient_id, doctor_id, appo_time, submit_time='1970-01-01 00:00:00',
        comfirm=True, problem='患者暂未描述症状', message='无消息'):
    "患者预约医生，前两个参数分别为患者id和医生id,appo_time格式为'YYY-MM-DD HH:MM:SS'"
    medi_insert_value(doctor_id, patient_id, submit_time, appo_time, comfirm, problem, message)

initialized = False
def init_database():
    "初始化数据库"
    global initialized
    if initialized == False:
        create_superuser('yangyizhe', '123', 'yangyizhe@627.com')
        create_superuser('guotiezheng', '123', 'guotiezheng@627.com')
        create_superuser('caijian', '123', 'caijian@629.com')
        depa_insert_value('内科')
        depa_insert_value('外科')
        depa_insert_value('口腔科')
        depa_insert_value('妇科')
        depa_insert_value('儿科')
        depa_insert_value('五官科')
        depa_insert_value('放射科')
        depa_insert_value('皮肤科')
        create_new_doctor('zhangsan', '123', '张三', 'm', '13389654217', 'zhangsan@null.com', '内科', 35)
        create_new_doctor('lisi', '123', '李四', 'f', '19745632564', 'lisi@null.com', '妇科', 32)
        create_new_patient('wangwu', '123', '王五', 'm', '18569423659', 'wangwu@null.com', 24)
        make_appointment(1,1,"2020-11-22 00:00:00")
        make_appointment(1,2,"2020-11-22 12:00:00")
        drug_insert_value('999感冒灵')
        drug_insert_value('康泰克')
        drug_insert_value('板蓝根')
        drug_insert_value('扑热息痛片')
        drug_insert_value('阿莫西林胶囊')
        drug_insert_value('息斯敏')
        drug_insert_value('氯雷他定片')
        drug_insert_value('泻立停')
        drug_insert_value('黄连素')
        drug_insert_value('藿香正气水')
        drug_insert_value('医用酒精')
        drug_insert_value('医用棉签')
        drug_insert_value('医用纱布')
        drug_insert_value('创可贴')
        drug_insert_value('止疼药')
        drug_insert_value('皮炎平')
        initialized = True
    else:
        raise Exception("重复初始化数据库")


# --- query ---
def all_departments():
    "获取所有科室信息，返回字典列表：[{第一个科室信息},{第二个科室信息}，...]"
    depa_infos = Department.objects.all()
    department = []
    for info in depa_infos:
        tmp = {}
        tmp['depa_name'] = info.name
        tmp['desc'] = info.desc
        department.append(tmp)
    return department 

def doctor_of_depa(depa_name):
    "通过科室名称获取相关科室的所有医生，返回字典列表：[{第一个医生信息}，{第二个医生信息}，...]"
    depa = Department.objects.filter(name=depa_name).first()
    doctor_infos = depa.doctor_set.all()
    doctor = []
    for info in doctor_infos:
        tmp = {}
        tmp['user_id'] = info.user_key
        tmp['doctor_id'] = info.pk
        tmp['doctor_name'] = info.name
        tmp['doctor_sex'] = info.sex
        tmp['doctor_tel'] = info.tel
        tmp['doctor_email'] = info.email
        tmp['doctor_department'] = info.department.name
        tmp['doctor_age'] = info.age
        doctor.append(tmp)
    return  doctor

def get_user_info(user_id):
    "通过user_id获取用户信息，若不存在此用户则返回空字典"
    user_info = {}
    doctor = Doctor.objects.filter(user_key=user_id).first()
    patient = Patient.objects.filter(user_key=user_id).first()
    if doctor:
        user_info['group'] = 'doctor'
        user_info['user_id'] = doctor.user_key
        user_info['doctor_id'] = doctor.pk
        user_info['doctor_name'] = doctor.name
        user_info['doctor_sex'] = doctor.sex
        user_info['doctor_tel'] = doctor.tel
        user_info['doctor_email'] = doctor.email
        user_info['doctor_department'] = doctor.department.name
        user_info['doctor_age'] = doctor.age
    elif patient:
        user_info['group'] = 'patient'
        user_info['user_id'] = patient.user_key
        user_info['patient_id'] = patient.pk
        user_info['patient_name'] = patient.name
        user_info['patient_sex'] = patient.sex
        user_info['patient_tel'] = patient.tel
        user_info['patient_email'] = patient.email
        user_info['patient_age'] = patient.age
    return user_info

def doc_ask_newappo(doctor_id):
    "通过医生ID获取新的预约记录，返回：[{患者1的预约情况},{患者2的},{患者3的},...]"
    doctor = Doctor.objects.get(pk=doctor_id)
    newappo_records = doctor.medicalrecord_set.filter(appo_confirm=False, appo_cancel=False, appo_complete=False)
    newappo = []
    for record in newappo_records:
        tmp = {}
        # 获取记录id
        tmp['record_id'] = record.pk
        # 获取患者基本信息
        tmp['patient_id'] = record.patient_key.pk
        tmp['patient_name'] = record.patient_key.name
        tmp['patient_sex'] = record.patient_key.sex
        tmp['patient_tel'] = record.patient_key.tel
        tmp['patient_email'] = record.patient_key.email
        tmp['patient_age'] = record.patient_key.age
        # 获取预约信息
        tmp['submit_time'] = datetime.datetime.strftime(record.submit_time,'%Y-%m-%d %H:%M:%S')
        tmp['appo_time'] = datetime.datetime.strftime(record.appo_time,'%Y-%m-%d %H:%M:%S')
        tmp['problem'] = record.symptom
        tmp['appo_message'] = record.appo_message
        newappo.append(tmp)
    return newappo

def doc_ask_waiting(doctor_id):
    "通过医生ID获取待诊断的预约记录，返回：[{患者1的预约情况},{患者2的},{患者3的},...]"
    doctor = Doctor.objects.get(pk=doctor_id)
    waiting_records = doctor.medicalrecord_set.filter(appo_confirm=True, appo_cancel=False, appo_complete=False)
    waiting = []
    for record in waiting_records:
        tmp = {}
        # 获取记录id
        tmp['record_id'] = record.pk
        # 获取患者基本信息
        tmp['patient_id'] = record.patient_key.pk
        tmp['patient_name'] = record.patient_key.name
        tmp['patient_sex'] = record.patient_key.sex
        tmp['patient_tel'] = record.patient_key.tel
        tmp['patient_email'] = record.patient_key.email
        tmp['patient_age'] = record.patient_key.age
        # 获取预约信息
        tmp['submit_time'] = datetime.datetime.strftime(record.submit_time,'%Y-%m-%d %H:%M:%S')
        tmp['appo_time'] = datetime.datetime.strftime(record.appo_time,'%Y-%m-%d %H:%M:%S')
        tmp['problem'] = record.symptom
        tmp['appo_message'] = record.appo_message
        waiting.append(tmp)
    return waiting

def pat_ask_record(patient_id):
    "通过患者ID获取以处理与待处理的病历返回字典：{'undone':[{患者正在预约中的第一条记录},{第二条},..], 'done':[{患者已完成的第一条看病记录},{第二}, ...]}"
    patient = Patient.objects.get(pk=patient_id)
    records = {"undone":[], "done":[]}
    undone_records = patient.medicalrecord_set.filter(appo_confirm=True, appo_cancel=False, appo_complete=False)
    done_records = patient.medicalrecord_set.filter(appo_confirm=True, appo_cancel=False, appo_complete=True)
    for record in undone_records:
        tmp = {}
        # 获取记录id
        tmp['record_id'] = record.pk
        # 获取医生基本信息
        tmp['doctor_id'] = record.doctor_key.pk
        tmp['doctor_name'] = record.doctor_key.name
        tmp['doctor_sex'] = record.doctor_key.sex
        tmp['doctor_tel'] = record.doctor_key.tel
        tmp['doctor_email'] = record.doctor_key.email
        tmp['doctor_apartment'] = record.doctor_key.department.name
        tmp['doctor_age'] = record.doctor_key.age
        # 获取预约信息
        tmp['submit_time'] = datetime.datetime.strftime(record.submit_time,'%Y-%m-%d %H:%M:%S')
        tmp['appo_time'] = datetime.datetime.strftime(record.appo_time,'%Y-%m-%d %H:%M:%S')
        tmp['problem'] = record.symptom
        tmp['appo_message'] = record.appo_message
        records['undone'].append(tmp)
    for record in done_records:
        tmp = {}
        # 获取记录id
        tmp['record_id'] = record.pk
        # 获取医生基本信息
        tmp['doctor_id'] = record.doctor_key.pk
        tmp['doctor_name'] = record.doctor_key.name
        tmp['doctor_sex'] = record.doctor_key.sex
        tmp['doctor_tel'] = record.doctor_key.tel
        tmp['doctor_email'] = record.doctor_key.email
        tmp['doctor_department'] = record.doctor_key.department.name
        tmp['doctor_age'] = record.doctor_key.age
        # 获取预约信息
        tmp['submit_time'] = datetime.datetime.strftime(record.submit_time,'%Y-%m-%d %H:%M:%S')
        tmp['appo_time'] = datetime.datetime.strftime(record.appo_time,'%Y-%m-%d %H:%M:%S')
        tmp['problem'] = record.symptom
        tmp['appo_message'] = record.appo_message
        # 获取诊断信息
        tmp['symptom'] = record.disease
        tmp['detail'] = record.detail
        tmp['diagnosis'] = record.diag_message
        tmp['prescription'] = json.loads(record.prescription)
        records['done'].append(tmp)
    return records

def pat_ask_history(patient_id):
    "通过患者ID获取历史病历，返回：{'refused':[{患者第一条被拒记录},{第二条},..], 'handled':[{患者已完成的第一条看病记录},{第二}, ...], 'calloff':[{被医生取消的第一条预约记录},{第二条},...]}"
    patient = Patient.objects.get(pk=patient_id)
    history = {"refused":[], "handled":[], "calloff":[]}
    refused_records = patient.medicalrecord_set.filter(appo_confirm=False, appo_cancel=True, appo_complete=False)
    handled_records = patient.medicalrecord_set.filter(appo_confirm=True, appo_cancel=False, appo_complete=True)
    calloff_records = patient.medicalrecord_set.filter(appo_confirm=True, appo_cancel=True, appo_complete=False)
    for record in refused_records:
        tmp = {}
        # 获取记录id
        tmp['record_id'] = record.pk
        # 获取医生基本信息
        tmp['doctor_id'] = record.doctor_key.pk
        tmp['doctor_name'] = record.doctor_key.name
        tmp['doctor_sex'] = record.doctor_key.sex
        tmp['doctor_tel'] = record.doctor_key.tel
        tmp['doctor_email'] = record.doctor_key.email
        tmp['doctor_department'] = record.doctor_key.department.name
        tmp['doctor_age'] = record.doctor_key.age
        # 获取预约信息
        tmp['submit_time'] = datetime.datetime.strftime(record.submit_time,'%Y-%m-%d %H:%M:%S')
        tmp['appo_time'] = datetime.datetime.strftime(record.appo_time,'%Y-%m-%d %H:%M:%S')
        tmp['problem'] = record.symptom
        tmp['appo_message'] = record.appo_message
        # 获取拒绝信息
        tmp['refuse_message'] = record.cancel_message
        history['refused'].append(tmp)
    for record in handled_records:
        tmp = {}
        # 获取记录id
        tmp['record_id'] = record.pk
        # 获取医生基本信息
        tmp['doctor_id'] = record.doctor_key.pk
        tmp['doctor_name'] = record.doctor_key.name
        tmp['doctor_sex'] = record.doctor_key.sex
        tmp['doctor_tel'] = record.doctor_key.tel
        tmp['doctor_email'] = record.doctor_key.email
        tmp['doctor_department'] = record.doctor_key.department.name
        tmp['doctor_age'] = record.doctor_key.age
        # 获取预约信息
        tmp['submit_time'] = datetime.datetime.strftime(record.submit_time,'%Y-%m-%d %H:%M:%S')
        tmp['appo_time'] = datetime.datetime.strftime(record.appo_time,'%Y-%m-%d %H:%M:%S')
        tmp['problem'] = record.symptom
        tmp['appo_message'] = record.appo_message
        # 获取诊断信息
        tmp['symptom'] = record.disease
        tmp['detail'] = record.detail
        tmp['diagnosis'] = record.diag_message
        tmp['prescription'] = json.loads(record.prescription)
        history['handled'].append(tmp)
    for record in calloff_records:
        tmp = {}
        # 获取记录id
        tmp['record_id'] = record.pk
        # 获取医生基本信息
        tmp['doctor_id'] = record.doctor_key.pk
        tmp['doctor_name'] = record.doctor_key.name
        tmp['doctor_sex'] = record.doctor_key.sex
        tmp['doctor_tel'] = record.doctor_key.tel
        tmp['doctor_email'] = record.doctor_key.email
        tmp['doctor_department'] = record.doctor_key.department.name
        tmp['doctor_age'] = record.doctor_key.age
        # 获取预约信息
        tmp['submit_time'] = datetime.datetime.strftime(record.submit_time,'%Y-%m-%d %H:%M:%S')
        tmp['appo_time'] = datetime.datetime.strftime(record.appo_time,'%Y-%m-%d %H:%M:%S')
        tmp['problem'] = record.symptom
        tmp['appo_message'] = record.appo_message
        # 获取取消信息
        tmp['calloff_message'] = record.cancel_message
        history['calloff'].append(tmp)
    return history
    
def look_up_medi_record(record_id):
    "通过病历ID调取整条病历记录，返回：{'prescription':[{具体用药方式}], ..., }"
    whole_record = MedicalRecord.objects.filter(pk=record_id).first()
    record = {}
    # 获取记录id
    record['record_id'] = whole_record.pk
    # 获取预约状态
    record['appo_confirm'] = whole_record.appo_confirm
    record['appo_complete'] = whole_record.appo_complete
    record['appo_cancel'] = whole_record.appo_cancel
    # 获取医生信息
    record['doctor_id'] = whole_record.doctor_key.pk
    record['doctor_name'] = whole_record.doctor_key.name
    record['doctor_sex'] = whole_record.doctor_key.sex
    record['doctor_tel'] = whole_record.doctor_key.tel
    record['doctor_email'] = whole_record.doctor_key.email
    record['doctor_department'] = whole_record.doctor_key.department.name
    record['doctor_age'] = whole_record.doctor_key.age
    # 获取患者信息
    record['patient_id'] = whole_record.patient_key.pk
    record['patient_name'] = whole_record.patient_key.name
    record['patient_sex'] = whole_record.patient_key.sex
    record['patient_tel'] = whole_record.patient_key.tel
    record['patient_email'] = whole_record.patient_key.email
    record['patient_age'] = whole_record.patient_key.age
    # 获取预约信息
    record['submit_time'] = datetime.datetime.strftime(whole_record.submit_time,'%Y-%m-%d %H:%M:%S')
    record['appo_time'] = datetime.datetime.strftime(whole_record.appo_time,'%Y-%m-%d %H:%M:%S')
    record['problem'] = whole_record.symptom
    record['appo_message'] = whole_record.appo_message
    # 获取拒绝/取消信息
    record['cancel_message'] = whole_record.cancel_message
    # 获取诊断信息
    record['symptom'] = whole_record.disease
    record['detail'] = whole_record.detail
    record['diagnosis'] = whole_record.diag_message
    record['prescription'] = json.loads(whole_record.prescription)
    return record

# --- update ---
def verify_and_login(username, password, login_request):
    "检验用户信息是否合法：若合法则调用auth.login登陆且返回用户id，否则返回False"
    verify = auth.authenticate(username=username, password=password)
    if not verify:
        return False
    else:
        auth.login(login_request, verify)
        return verify.pk

def logout(logout_request):
    "注销用户登陆"
    auth.logout(logout_request)

def doctor_confirm(record_id):
    "医生确认预约"
    record = MedicalRecord.objects.get(pk=record_id)
    if record.appo_confirm==True:
        raise Exception('重复确认')
    if record.appo_cancel==True:
        raise Exception('预约已取消')
    if record.appo_complete==True:
        raise Exception('已完成诊断')
    record.appo_confirm = True
    record.save()

def doctor_diagnose(record_id, symptom, detail, diagnosis, prescription=[{"drug":'*',"usage":"*","dosage":"*"}]):
    "医生记录病历信息，完成诊断"
    '''
    record_id: 整形
    prescription: 列表类型[ 
        字典1{
            'drug'：''
            'usage'：''
            'dosage': ''
        },
        字典2{
            'drug'：''
            'usage'：''
            'dosage': ''
        },
        ...
    ]
    其它参数为字符串
    '''
    record = MedicalRecord.objects.get(pk=record_id)
    if record.appo_confirm==False:
        raise Exception('预约未确认')
    if record.appo_cancel==True:
        raise Exception('预约已取消')
    if record.appo_complete==True:
        raise Exception('重复诊断')
    record.diag_message = diagnosis
    if type(prescription)==list and type(prescription[0])==dict:
        for drug in prescription:
            drug_obj = Drug.objects.filter(name=drug['drug']).first()
            record.drugs_key.add(drug_obj)
        record.prescription = json.dumps(prescription)
    else:
        raise Exception('处方必须为字典列表')
    record.disease = symptom
    record.detail = detail
    record.appo_complete = True
    record.save()
    
def doctor_cancel(record_id, cancel_message='更多信息请联系您预约的医生'):
    "医生取消或者拒绝一次预约，第一个参数为整形，第二个参数为字符串类型"
    record = MedicalRecord.objects.get(pk=record_id)
    if record.appo_cancel==True:
        raise Exception('重复取消')
    if record.appo_complete==True:
        raise Exception('已完成诊断')
    if record.appo_confirm==False:
        record.cancel_message = "本条预约已被医生拒绝：" + cancel_message
    else:
        record.cancel_message = "本条预约已被医生取消：" + cancel_message
    record.appo_cancel = True
    record.save()


# --- delete ---
def delete_doctor(doctor_id):
    "通过医生id删除医生"
    Doctor.objects.filter(pk=doctor_id).delete()

def delete_patient(patient_id):
    "通过患者id删除患者"
    Patient.objects.filter(pk=patient_id).delete()

def delete_department(name):
    "通过部门字符串名称删除部门"
    Department.objects.filter(name=name).delete()

def delete_medi_record(record_id):
    "通过id删除一条病历记录"
    MedicalRecord.objects.filter(pk=record_id).delete()

def delete_drug(name):
    "通过药品名删除药品"
    Drug.objects.filter(name=name).delete()
