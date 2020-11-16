from Sheets import db_intfs
from django.views import View
from django.http import HttpResponse
from django.middleware.csrf import get_token
import json
from django.shortcuts import render

# Create your views here.


def getToken(request):
    token = get_token(request)
    return HttpResponse(
        json.dumps({"token": token}), content_type="application/json,charset=utf-8"
    )


class Index(View):
    """
    docstring
    """

    def get(self, request):
        """
        docstring
        """
        # db_intfs.init_database()
        return render(request=request, template_name="index.html")


class Regist(View):
    """
    docstring
    """

    def post(self, request):
        """
        docstring
        """
        data = json.loads(request.body.decode("utf-8"))
        name = data["name"]
        age = data["age"]
        sex = "m" if data["sex"] == "男" else "f"
        phone = data["phone"]
        username = data["username"]
        password = data["password"]
        db_intfs.create_new_patient(
            username=username,
            password=password,
            name=name,
            sex=sex,
            tel=phone,
            email="test@gmail.com",
            age=age,
        )
        id = db_intfs.verify_and_login(
            username=username, password=password, login_request=request
        )
        ret = {"flag": "success", "id": id}
        return HttpResponse(json.dumps(ret), content_type="application/json")


class Login(View):
    """
    docstring
    """

    def post(self, request):
        """
        docstring
        """
        data = json.loads(request.body.decode("utf-8"))
        username = data["username"]
        password = data["password"]
        flag = data["flag"]
        id = db_intfs.verify_and_login(
            username=username, password=password, login_request=request
        )
        if not id:
            ret = {"flag": "fail", "id": 0}
        else:
            user_info = db_intfs.get_user_info(id)
            if (flag == 0 and user_info["group"] == "patient") or (
                flag == 1 and user_info["group"] == "doctor"
            ):
                ret = {"flag": "success", "id": id}
            else:
                ret = {"flag": "fail", "id": 0}
        return HttpResponse(json.dumps(ret), content_type="application/json")


class PatientIndex(View):
    """
    docstring
    """

    def post(self, request):
        """
        docstring
        """
        data = json.loads(request.body.decode("utf-8"))
        id = data["id"]
        user_info = db_intfs.get_user_info(id)
        patient_id = user_info["patient_id"]
        history = db_intfs.pat_ask_record(patient_id)
        formdata = []
        for record in history["done"]:
            temp = {}
            temp["id"] = record["record_id"]
            temp["date"] = record["appo_time"]
            temp["depertment"] = record["doctor_department"]
            temp["doctor"] = record["doctor_name"]
            temp["done"] = "已完成"
            formdata.append(temp)
        for record in history["undone"]:
            temp = {}
            temp["id"] = record["record_id"]
            temp["date"] = record["appo_time"]
            temp["depertment"] = record["doctor_department"]
            temp["doctor"] = record["doctor_name"]
            temp["done"] = "未完成"
            formdata.append(temp)
        ret = {
            "patient": {
                "name": user_info["patient_name"],
                "sex": "男" if user_info["patient_sex"] == "m" else "女",
                "age": user_info["patient_age"],
            },
            "formdata": formdata,
        }
        return HttpResponse(json.dumps(ret), content_type="application/json")


class Dignosis(View):
    """
    docstring
    """

    def post(self, request):
        """
        docstring
        """
        data = json.loads(request.body.decode("utf-8"))
        record_id = data["diagnose_id"]
        user_id = data["user_id"]
        user_info = db_intfs.get_user_info(user_id)
        record = db_intfs.look_up_medi_record(record_id=record_id)
        medicines = ""
        for dict in record["prescription"]:
            print(dict)
            medicines += dict["drug"] + "\t" + dict["usage"] + "\n"
        print(medicines)
        ret = {
            "patient": {
                "name": user_info["patient_name"],
                "sex": "男" if user_info["patient_sex"] == "m" else "女",
                "age": user_info["patient_age"],
            },
            "formdata": {
                "doctorname": record["doctor_name"],
                "department": record["doctor_department"],
                "time": record["appo_time"],
                "medicine": medicines,
                "diagnose": record["diagnosis"],
            },
        }
        return HttpResponse(json.dumps(ret), content_type="application/json")


class Appointment(View):
    """
    docstring
    """

    def post(self, request):
        """
        docstring
        """
        data = json.loads(request.body.decode("utf-8"))
        user_id = data["id"]
        user_info = db_intfs.get_user_info(user_id)
        patient = {
            "name": user_info["patient_name"],
            "sex": "男" if user_info["patient_sex"] == "m" else "女",
            "age": user_info["patient_age"],
        }
        departments = [
            department["depa_name"] for department in db_intfs.all_departments()
        ]
        options = []
        for department in departments:
            option = {}
            option["value"] = user_info["patient_id"]
            option["label"] = department
            doctors = []
            for doctor in db_intfs.doctor_of_depa(depa_name=department):
                doctor_dict = {}
                doctor_dict["value"] = doctor["doctor_id"]
                doctor_dict["label"] = doctor["doctor_name"]
                doctors.append(doctor_dict)
            option["children"] = doctors
            options.append(option)
        ret = {"patient": patient, "options": options}
        print(ret)
        return HttpResponse(json.dumps(ret), content_type="application/json")


class MakeAppointment(View):
    """
    docstring
    """

    def post(self, request):
        """
        docstring
        """
        data = json.loads(request.body.decode("utf-8"))
        patient_id = data["department"]
        doctor_id = data["doctor"]
        appo_time = data["date"] + " " + data["time"] + ":00"
        print(appo_time)
        db_intfs.make_appointment(
            patient_id=patient_id, doctor_id=doctor_id, appo_time=appo_time
        )
        ret = {"flag": "success"}
        return HttpResponse(json.dumps(ret), content_type="application/json")


class DoctorIndex(View):
    """
    docstring
    """

    def post(self, request):
        """
        docstring
        """
        data = json.loads(request.body.decode("utf-8"))
        id = data["id"]
        user_info = db_intfs.get_user_info(id)
        doctor_id = user_info["doctor_id"]
        doctor = {
            "name": user_info["doctor_name"],
            "department": user_info["doctor_department"],
        }
        formdata=[]
        waiting_patients=db_intfs.doc_ask_waiting(doctor_id=doctor_id)
        for patient in waiting_patients:
            patient_dict={}
            patient_dict['id']=patient['record_id']
            patient_dict['name']=patient['patient_name']
            patient_dict['sex']="男" if patient["patient_sex"] == "m" else "女",
            patient_dict['age']=patient['patient_age']
            formdata.append(patient_dict)
        ret={
            'doctor':doctor,
            'formdata':formdata
        }
        return HttpResponse(json.dumps(ret), content_type="application/json")

class GetDiagnose(View):
    """
    docstring
    """
    
    def post(self, request):
        """
        docstring
        """
        data = json.loads(request.body.decode("utf-8"))
        record_id=data['diagnose_id']
        record=db_intfs.look_up_medi_record(record_id=record_id)
        doctor={
            'name':record['doctor_name'],
            'department':record['doctor_department'],
        }
        patient={
            'name':record['patient_name'],
            'sex':record['patient_sex'],
            'age':record['patient_age'],
        }
        