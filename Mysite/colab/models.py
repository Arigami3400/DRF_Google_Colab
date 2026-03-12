from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    gender = models.CharField(max_length=10)
    race_ethnicity = models.CharField(max_length=32)
    parental_level = models.CharField(max_length=32)
    lunch = models.CharField(max_length=15)
    test_preparation_course = models.CharField(max_length=15)
    reading_score = models.IntegerField()
    writing_score = models.IntegerField()

class House(models.Model):
     GrLivArea = models.IntegerField()
     YearBuilt = models.IntegerField()
     GarageCars = models.IntegerField()
     TotalBsmtSF = models.IntegerField()
     FullBath = models.IntegerField()
     OverallQual = models.IntegerField()
     Neighborhood = models.CharField(max_length=50)

class Titanic(models.Model):
    Pclass = models.IntegerField()
    Sex = models.CharField(max_length=10)
    Age = models.IntegerField()
    SibSp = models.IntegerField()
    Parch = models.IntegerField()
    Fare = models.FloatField()
    Embarked = models.CharField(max_length=5)

class Diabet(models.Model):
    Pregnancies = models.IntegerField()
    Glucose = models.IntegerField()
    BloodPressure = models.IntegerField()
    SkinThickness = models.IntegerField()
    Insulin = models.IntegerField()
    BMI = models.IntegerField()
    DiabetesPedigreeFunction = models.IntegerField()
    Age = models.IntegerField()

class Bank(models.Model):
    person_age = models.IntegerField()
    person_gender = models.CharField(max_length=10)
    person_education = models.CharField(max_length=40)
    person_income = models.IntegerField()
    person_emp_exp = models.IntegerField()
    person_home_ownership = models.CharField(max_length=50)
    loan_amnt = models.IntegerField()
    loan_intent = models.CharField(max_length=50)
    loan_int_rate = models.IntegerField()
    loan_percent_income = models.IntegerField()
    cb_person_cred_hist_length = models.IntegerField()
    credit_score = models.IntegerField()
    previous_loan_defaults_on_file = models.CharField(max_length=10)

class Telecom(models.Model):
    gender = models.CharField(max_length=10)
    SeniorCitizen = models.IntegerField()
    Partner = models.CharField(max_length=10)
    Dependents = models.CharField(max_length=10)
    tenure = models.IntegerField()
    PhoneService = models.CharField(max_length=10)
    OnlineSecurity = models.CharField(max_length=10)
    OnlineBackup =  models.CharField(max_length=10)
    DeviceProtection = models.CharField(max_length=10)
    TechSupport = models.CharField(max_length=10)
    StreamingTV = models.CharField(max_length=10)
    StreamingMovies = models.CharField(max_length=10)
    PaperlessBilling = models.CharField(max_length=10)
    MonthlyCharges  = models.IntegerField()
    TotalCharges = models.IntegerField()
    PaymentMethod = models.CharField(max_length=100)
    Contract = models.CharField(max_length=50)
    InternetService = models.CharField(max_length=10)
    MultipleLines = models.CharField(max_length=100)


class Mashrooms(models.Model):
    cap_shape = models.CharField(max_length=10)
    cap_surface = models.CharField(max_length=10)
    cap_color = models.CharField(max_length=10)
    bruises = models.CharField(max_length=10)
    odor = models.CharField(max_length=10)
    gill_attachment = models.CharField(max_length=10)
    gill_spacing = models.CharField(max_length=10)
    gill_size = models.CharField(max_length=10)
    gill_color = models.CharField(max_length=10)
    stalk_shape = models.CharField(max_length=10)
    stalk_root = models.CharField(max_length=10)
    stalk_surface_above_ring = models.CharField(max_length=10)
    stalk_surface_below_ring = models.CharField(max_length=10)
    stalk_color_above_ring = models.CharField(max_length=10)
    stalk_color_below_ring = models.CharField(max_length=10)
    veil_type = models.CharField(max_length=10)
    veil_color = models.CharField(max_length=10)
    ring_number = models.CharField(max_length=10)
    ring_type = models.CharField(max_length=10)
    spore_print_color = models.CharField(max_length=10)
    population = models.CharField(max_length=10)
    habitat = models.CharField(max_length=10)

class Avacado(models.Model):
    firmness = models.IntegerField()
    hue = models.IntegerField()
    saturation = models.IntegerField()
    brightness = models.IntegerField()
    color_category = models.CharField(max_length=10)
    sound_db = models.IntegerField()
    weight_g = models.IntegerField()
    size_cm3 = models.IntegerField()

from django.db import models

class DSHremploye(models.Model):
    age = models.IntegerField()
    business_travel = models.CharField(max_length=50)
    daily_rate = models.IntegerField()
    department = models.CharField(max_length=50)
    distance_from_home = models.IntegerField()
    education = models.IntegerField()
    education_field = models.CharField(max_length=50)
    environment_satisfaction = models.IntegerField()
    gender = models.CharField(max_length=10)
    hourly_rate = models.IntegerField()
    job_involvement = models.IntegerField()
    job_level = models.IntegerField()
    job_role = models.CharField(max_length=50)
    job_satisfaction = models.IntegerField()
    marital_status = models.CharField(max_length=50)
    monthly_income = models.IntegerField()
    monthly_rate = models.IntegerField()
    num_companies_worked = models.IntegerField()
    over_time = models.CharField(max_length=10)
    percent_salary_hike = models.IntegerField()
    performance_rating = models.IntegerField()
    relationship_satisfaction = models.IntegerField()
    stockoption_level = models.IntegerField()
    total_working_years = models.IntegerField()
    training_times_lastyear = models.IntegerField()
    work_life_balance = models.IntegerField()
    years_atcompany = models.IntegerField()
    years_incurrent_role = models.IntegerField()
    years_since_lastpromotion = models.IntegerField()
    years_with_currmanager = models.IntegerField()









