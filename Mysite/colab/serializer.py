from rest_framework import serializers
from .models import *



class StudentSerializer(serializers.Serializer):
    gender = serializers.CharField(max_length=10)
    race_ethnicity = serializers.CharField(max_length=32)
    parental_level = serializers.CharField(max_length=32)
    lunch = serializers.CharField(max_length=15)
    test_preparation_course = serializers.CharField(max_length=15)
    reading_score = serializers.IntegerField()
    writing_score = serializers.IntegerField()

class HouseSerializer(serializers.Serializer):
     GrLivArea = serializers.IntegerField()
     YearBuilt = serializers.IntegerField()
     GarageCars = serializers.IntegerField()
     TotalBsmtSF = serializers.IntegerField()
     FullBath = serializers.IntegerField()
     OverallQual = serializers.IntegerField()
     Neighborhood = serializers.CharField(max_length=50)

class TitanicSerializer(serializers.Serializer):
    Pclass = serializers.IntegerField()
    Sex = serializers.CharField(max_length=10)
    Age = serializers.IntegerField()
    SibSp = serializers.IntegerField()
    Parch = serializers.IntegerField()
    Fare = serializers.FloatField()
    Embarked = serializers.CharField(max_length=5)

class DiabetSerializer(serializers.Serializer):
    Pregnancies = serializers.IntegerField()
    Glucose = serializers.IntegerField()
    BloodPressure = serializers.IntegerField()
    SkinThickness = serializers.IntegerField()
    Insulin = serializers.IntegerField()
    BMI = serializers.IntegerField()
    DiabetesPedigreeFunction = serializers.IntegerField()
    Age = serializers.IntegerField()

class BankSerializer(serializers.Serializer):
    person_age = serializers.IntegerField()
    person_gender = serializers.CharField(max_length=10)
    person_education = serializers.CharField(max_length=40)
    person_income = serializers.IntegerField()
    person_emp_exp = serializers.IntegerField()
    person_home_ownership = serializers.CharField(max_length=50)
    loan_amnt = serializers.IntegerField()
    loan_intent = serializers.CharField(max_length=50)
    loan_int_rate = serializers.IntegerField()
    loan_percent_income = serializers.IntegerField()
    cb_person_cred_hist_length = serializers.IntegerField()
    credit_score = serializers.IntegerField()
    previous_loan_defaults_on_file = serializers.CharField(max_length=10)

class TelecomSerializer(serializers.Serializer):
    gender = serializers.CharField(max_length=10)
    SeniorCitizen = serializers.IntegerField()
    Partner = serializers.CharField(max_length=10)
    Dependents = serializers.CharField(max_length=10)
    tenure = serializers.IntegerField()
    PhoneService = serializers.CharField(max_length=10)
    MultipleLines = serializers.CharField(max_length=100)
    InternetService = serializers.CharField(max_length=10)
    OnlineSecurity = serializers.CharField(max_length=10)
    OnlineBackup =  serializers.CharField(max_length=10)
    DeviceProtection = serializers.CharField(max_length=10)
    TechSupport = serializers.CharField(max_length=10)
    StreamingTV = serializers.CharField(max_length=10)
    StreamingMovies = serializers.CharField(max_length=10)
    Contract = serializers.CharField(max_length=100)
    PaperlessBilling = serializers.CharField(max_length=10)
    PaymentMethod = serializers.CharField(max_length=100)
    MonthlyCharges  = serializers.FloatField()
    TotalCharges = serializers.FloatField()

class MashroomSerializer(serializers.Serializer):
    cap_shape = serializers.CharField(max_length=10)
    cap_surface = serializers.CharField(max_length=10)
    cap_color = serializers.CharField(max_length=10)
    bruises = serializers.CharField(max_length=10)
    odor = serializers.CharField(max_length=10)
    gill_attachment = serializers.CharField(max_length=10)
    gill_spacing = serializers.CharField(max_length=10)
    gill_size = serializers.CharField(max_length=10)
    gill_color = serializers.CharField(max_length=10)
    stalk_shape = serializers.CharField(max_length=10)
    stalk_root = serializers.CharField(max_length=10)
    stalk_surface_above_ring = serializers.CharField(max_length=10)
    stalk_surface_below_ring = serializers.CharField(max_length=10)
    stalk_color_above_ring = serializers.CharField(max_length=10)
    stalk_color_below_ring = serializers.CharField(max_length=10)
    veil_type = serializers.CharField(max_length=10)
    veil_color = serializers.CharField(max_length=10)
    ring_number = serializers.CharField(max_length=10)
    ring_type = serializers.CharField(max_length=10)
    spore_print_color = serializers.CharField(max_length=10)
    population = serializers.CharField(max_length=10)
    habitat = serializers.CharField(max_length=10)

class AvacadoSerializer(serializers.Serializer):
    firmness = serializers.IntegerField()
    hue = serializers.IntegerField()
    saturation = serializers.IntegerField()
    brightness = serializers.IntegerField()
    color_category = serializers.CharField(max_length=10)
    sound_db = serializers.IntegerField()
    weight_g = serializers.IntegerField()
    size_cm3 = serializers.IntegerField()





