from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework import views, status
import joblib
import os
from django.conf import settings


model_path = os.path.join(settings.BASE_DIR, 'ml_models/model_ava.pkl')
model_avocado = joblib.load(model_path)
scaler_path = os.path.join(settings.BASE_DIR, 'ml_models/scaler_ava.pkl')
scaler_avocado = joblib.load(scaler_path)

model_path = os.path.join(settings.BASE_DIR, 'ml_models/model_stu.pkl')
model_student = joblib.load(model_path)
scaler_path = os.path.join(settings.BASE_DIR, 'ml_models/scaler_stu.pkl')
scaler_student = joblib.load(scaler_path)

model_path = os.path.join(settings.BASE_DIR, 'ml_models/model_bank.pkl')
model_bank = joblib.load(model_path)
scaler_path = os.path.join(settings.BASE_DIR, 'ml_models/scaler_bank.pkl')
scaler_bank = joblib.load(scaler_path)

model_path = os.path.join(settings.BASE_DIR, 'ml_models/model_tita.pkl')
model_titanic = joblib.load(model_path)
scaler_path = os.path.join(settings.BASE_DIR, 'ml_models/scaler_tita.pkl')
scaler_titanic = joblib.load(scaler_path)

model_path = os.path.join(settings.BASE_DIR, 'ml_models/model_tele.pkl')
model_telecom = joblib.load(model_path)
scaler_path = os.path.join(settings.BASE_DIR, 'ml_models/scaler_tele.pkl')
scaler_telecom = joblib.load(scaler_path)

model_path = os.path.join(settings.BASE_DIR, 'ml_models/model_mash.plk')
model_mash = joblib.load(model_path)
scaler_path = os.path.join(settings.BASE_DIR, 'ml_models/scaler_mash.pkl')
scaler_mash = joblib.load(scaler_path)

model_path = os.path.join(settings.BASE_DIR, 'ml_models/model_dia.pkl')
model_diabet = joblib.load(model_path)
scaler_path = os.path.join(settings.BASE_DIR, 'ml_models/scaler_dia.pkl')
scaler_diabet = joblib.load(scaler_path)

model_path = os.path.join(settings.BASE_DIR, 'ml_models/model_house.pkl')
model_house = joblib.load(model_path)
scaler_path = os.path.join(settings.BASE_DIR, 'ml_models/scaler_house.pkl')
scaler_house = joblib.load(scaler_path)



#House
Neighborhoods = [
    'Blueste', 'BrDale', 'CollgCr', 'Gilbert', 'Mitchel', 'NWAmes', 'OldTown', 'SawyerW',
    'Timber', 'BrkSide', 'Crawfor', 'IDOTRR', 'NAmes', 'NoRidge', 'SWISU', 'Somerst',
    'Veenker', 'ClearCr', 'Edwards', 'MeadowV', 'NPkVill', 'NridgHt', 'Sawyer', 'StoneBr'
]

#mashroom
cap_shape_list = ['c', 'f', 'k', 's', 'x']
cap_surface_list = ['g', 's', 'y']
cap_color_list = ['c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y']
bruises_list = ['t']
odor_list = ['c', 'f', 'l', 'm', 'n', 'p', 's', 'y']
gill_attachment_list= ['f']
gill_spacing_list = ['w']
gill_size_list = ['n']
gill_color_list = ['e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y']
stalk_shape_list = ['t']
stalk_root_list = ['c', 'e', 'r']
stalk_surface_above_ring_list = ['k', 's', 'y']
stalk_surface_below_ring_list = ['k', 's', 'y']
stalk_color_above_ring_list = ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
stalk_color_below_ring_list = ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y']
veil_color_list = ['o', 'w', 'y']
ring_number_list = ['o', 't']
ring_type_list = ['f', 'l', 'n', 'p']
spore_print_color_list = ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y']
population_list = ['c', 'n', 's', 'v', 'y']
habitat_list = ['g', 'l', 'm', 'p', 'u', 'w']

#avacado
color_categories = ['green', 'dark green', 'purple']

#titanic
embarked_categories = ['S', 'Q']
sex_categories = ['male']

#Telecom
Paymentmethod_list = ['Credit_card_automatic', 'Electronic_check', 'Mailed_check']
Contract_list = ['One_year', 'Two_year']
InternetService_list = ['Fiber_optic', 'No']
MultipleLines_list = [ "Yes", "No phone service"]
gender = ['Female',]
partner = ['Yes',]
dependents = ['Yes',]
phoneservice = ['Yes',]
paperlessbilling = ['Yes',]
onlinesecurity = ['Yes',]
onlinebackup = ['Yes',]
deviceprotection = ['Yes',]
techsupport = ['Yes',]
streamingtv = ['Yes',]
streamingmovies = ['Yes']


#student
Gender = ['male']
race = ['group B', 'group C', 'group D', 'group E']
parental_education = ["bachelor's degree", "high school", "master's degree",
                      'some college', 'some high school']
lunch = ['standard']
test = ['none']


#Bank
person_gender = ['male']
person_education = ['Bachelor', 'Doctorate', 'High_School', 'Master']
person_home = ['OTHER', 'OWN', 'RENT']
loan_intent = ['HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE', 'EDUCATION']
previous_loan_defaults_on_file = ['Yes']





class PredictHouse(views.APIView):
    def post(self, request):
        instance = HouseSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            new_neighborhood = data.pop('Neighborhood')
            neighborhood1_0 = [1 if new_neighborhood == name else 0 for name in Neighborhoods]

            features = list(data.values()) + neighborhood1_0
            scaler_data = scaler_house.transform([features])
            predict_house = model_house.predict(scaler_data)[0]
            return Response({'Predict_Price': round(predict_house)}, status.HTTP_200_OK)
        if not instance.is_valid():
            print("Serializer errors:", instance.errors)
            return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)

class PredictStudent(views.APIView):
    def post(self, request):
        instance = StudentSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data

            new_gender = data.pop('gender')
            new_race = data.pop('race_ethnicity')
            new_parental_ed = data.pop('parental_level')
            new_lunch = data.pop('lunch')
            new_test = data.pop('test_preparation_course')

            gender1_0 = [1 if new_gender == name else 0 for name in Gender]
            race1_0 = [1 if new_race == name else 0 for name in race]
            parental1_0 = [1 if new_parental_ed == name else 0 for name in parental_education]
            lunch1_0 = [1 if new_lunch == name else 0 for name in lunch]
            test1_0 = [1 if new_test == name else 0 for name in test]

            features = list(data.values()) + gender1_0 + race1_0 +parental1_0 +lunch1_0 +test1_0
            scaler_data = scaler_student.transform([features])
            predict_student = model_student.predict(scaler_data)[0]
            return Response({'predict': round(predict_student)}, status=status.HTTP_200_OK)
        print(instance.errors)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)



class PredictBank(views.APIView):
    def post(self, request):
        instance = BankSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            new_gender = data.pop('person_gender')
            new_education = data.pop('person_education')
            new_home = data.pop('person_home_ownership')
            new_loan_intent = data.pop('loan_intent')
            new_previous_defaults = data.pop('previous_loan_defaults_on_file')
            gender1_0 = [1 if new_gender == name else 0 for name in person_gender]
            education1_0 = [1 if new_education == name else 0 for name in person_education]
            home1_0 = [1 if new_home == name else 0 for name in person_home]
            loan_intent1_0 = [1 if new_loan_intent == name else 0 for name in loan_intent]
            previous_defaults1_0 = [1 if new_previous_defaults == name else 0 for name in previous_loan_defaults_on_file]

            features = list(data.values()) +gender1_0 +education1_0 +home1_0 +loan_intent1_0 +previous_defaults1_0
            scaled_data = scaler_bank.transform([features])
            predict_bank = model_bank.predict(scaled_data)[0]
            if predict_bank == 1:
                predict_bank = 'Разрешено'
            else:
                predict_bank = 'Запрешено'
            return Response({'Predict': predict_bank}, status.HTTP_200_OK)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)



class PredictAvocado(views.APIView):
    def post(self, request):
        instance = AvacadoSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            new_color = data.pop('color_category')
            color1_0 = [1 if new_color == name else 0 for name in color_categories]

            features = list(data.values()) + color1_0
            scaler_data = scaler_avocado.transform([features])
            predict_avocado = model_avocado.predict(scaler_data)[0]
            if predict_avocado == 1:
                predict_avocado = 'Hard'
            elif predict_avocado == 2:
                predict_avocado = 'pre-conditioned'
            elif predict_avocado == 3:
                predict_avocado = 'breaking'
            elif predict_avocado == 4:
                predict_avocado = 'firm-ripe'
            else:
                predict_avocado = 'ripe'
            return Response({'Predict_state': predict_avocado}, status.HTTP_200_OK)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictTitanic(views.APIView):
    def post(self, request):
        instance = TitanicSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            new_embarrked = data.pop('Embarked')
            new_sex = data.pop('Sex')
            embarked1_0 = [1 if new_embarrked == name else 0 for name in embarked_categories]
            sex1_0 = [1 if new_sex == name else 0 for name in sex_categories]

            features = list(data.values()) + embarked1_0 + sex1_0
            scaled_data = scaler_titanic.transform([features])
            predict_titanic = model_titanic.predict(scaled_data)[0]
            if predict_titanic == 0:
                predict_titanic = "Не Выжил"
            else:
                predict_titanic = "Выжил"
            return Response({'Predict_survival': predict_titanic}, status.HTTP_200_OK)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)




class PredictMashrooms(views.APIView):
    def post(self, request):
        instance = MashroomSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            new_cap_shape = data.pop('cap_shape')
            new_cap_surface = data.pop('cap_surface')
            new_cap_color = data.pop('cap_color')
            new_bruises = data.pop('bruises')
            new_odor = data.pop('odor')
            new_gill_attachment = data.pop('gill_attachment')
            new_gill_spacing = data.pop('gill_spacing')
            new_gill_size = data.pop('gill_size')
            new_gill_color = data.pop('gill_color')
            new_stalk_shape = data.pop('stalk_shape')
            new_stalk_root = data.pop('stalk_root')
            new_stalk_surface_above_ring = data.pop('stalk_surface_above_ring')
            new_stalk_surface_below_ring = data.pop('stalk_surface_below_ring')
            new_stalk_color_above_ring = data.pop('stalk_color_above_ring')
            new_stalk_color_below_ring = data.pop('stalk_color_below_ring')
            new_veil_color = data.pop('veil_color')
            new_ring_number = data.pop('ring_number')
            new_ring_type = data.pop('ring_type')
            new_spore_print_color = data.pop('spore_print_color')
            new_population = data.pop('population')
            new_habitat = data.pop('habitat')

            cap_shape1_0 = [1 if new_cap_shape == name else 0 for name in cap_shape_list]
            cap_surface1_0 = [1 if new_cap_surface == name else 0 for name in cap_surface_list]
            cap_color1_0 = [1 if new_cap_color == name else 0 for name in cap_color_list]
            bruises1_0 = [1 if new_bruises == name else 0 for name in bruises_list]
            odor1_0 = [1 if new_odor == name else 0 for name in odor_list]
            gill_attachment1_0 = [1 if new_gill_attachment == name else 0 for name in gill_attachment_list]
            gill_spacing1_0 = [1 if new_gill_spacing == name else 0 for name in gill_spacing_list]
            gill_size1_0 = [1 if new_gill_size == name else 0 for name in gill_size_list]
            gill_color1_0 = [1 if new_gill_color == name else 0 for name in gill_color_list]
            stalk_shape1_0 = [1 if new_stalk_shape == name else 0 for name in stalk_shape_list]
            stalk_root1_0 = [1 if new_stalk_root == name else 0 for name in stalk_root_list]
            stalk_surface_above_ring1_0 = [1 if new_stalk_surface_above_ring == name else 0 for name in stalk_surface_above_ring_list]
            stalk_surface_below_ring1_0 = [1 if new_stalk_surface_below_ring == name else 0 for name in stalk_surface_below_ring_list]
            stalk_color_above_ring1_0 = [1 if new_stalk_color_above_ring == name else 0 for name in stalk_color_above_ring_list]
            stalk_color_below_ring1_0 = [1 if new_stalk_color_below_ring == name else 0 for name in stalk_color_below_ring_list]
            veil_color1_0 = [1 if new_veil_color == name else 0 for name in veil_color_list]
            ring_number1_0 = [1 if new_ring_number == name else 0 for name in ring_number_list]
            ring_type1_0 = [1 if new_ring_type == name else 0 for name in ring_type_list]
            spore_print_color1_0 = [1 if new_spore_print_color == name else 0 for name in spore_print_color_list]
            population1_0 = [1 if new_population == name else 0 for name in population_list]
            habitat1_0 = [1 if new_habitat == name else 0 for name in habitat_list]

            features = [cap_shape1_0
                        +cap_surface1_0 +cap_color1_0 +bruises1_0
                        +odor1_0  +gill_attachment1_0 + gill_spacing1_0
                        +gill_size1_0 +gill_color1_0 +stalk_shape1_0 +stalk_root1_0
                        +stalk_surface_above_ring1_0 +stalk_surface_below_ring1_0
                        +stalk_color_above_ring1_0 +stalk_color_below_ring1_0 +veil_color1_0
                        +ring_number1_0 +ring_type1_0 +spore_print_color1_0 + population1_0+habitat1_0]
            scaled_data = scaler_mash.transform(features)
            predict_mash = model_mash.predict(scaled_data)[0]
            if predict_mash == 1:
                predict_mash = 'edible'
            else:
                predict_mash = 'poisonous'
            return Response({'Predict_mashroom': predict_mash}, status.HTTP_200_OK)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)




class PredictTelecom(views.APIView):
    def post(self, request):
        instance = TelecomSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            new_paymentmethod = data.pop('PaymentMethod')
            new_contract = data.pop('Contract')
            new_internetservice = data.pop('InternetService')
            new_multiplelines = data.pop('MultipleLines')
            new_gender = data.pop('gender')
            new_partner = data.pop('Partner')
            new_dependents = data.pop('Dependents')
            new_phoneservice = data.pop('PhoneService')
            new_paperlessbilling = data.pop('PaperlessBilling')
            new_onlinesecurity = data.pop('OnlineSecurity')
            new_onlinebackup = data.pop('OnlineBackup')
            new_deviceprotection = data.pop('DeviceProtection')
            new_techsupport = data.pop('TechSupport')
            new_streamingtv = data.pop('StreamingTV')
            new_streamingmovies = data.pop('StreamingMovies')

            paymentmethod1_0 = [1 if new_paymentmethod == name else 0 for name in Paymentmethod_list]
            contract1_0 = [1 if new_contract == name else 0 for name in Contract_list]
            internetservice1_0 = [1 if new_internetservice == name else 0 for name in InternetService_list]
            multiplelines1_0 = [1 if new_multiplelines == name else 0 for name in MultipleLines_list]
            gender1_0 = [1 if new_gender == name else 0 for name in gender]
            partner1_0 = [1 if new_partner == name else 0 for name in partner]
            dependents1_0 = [1 if new_dependents == name else 0 for name in dependents]
            phoneservice1_0 = [1 if new_phoneservice == name else 0 for name in phoneservice]
            paperlessbilling1_0 = [1 if new_paperlessbilling == name else 0 for name in paperlessbilling]
            onlinesecurity1_0 = [1 if new_onlinesecurity == name else 0 for name in onlinesecurity]
            onlinebackup1_0 = [1 if new_onlinebackup == name else 0 for name in onlinebackup]
            deviceprotection1_0 = [1 if new_deviceprotection == name else 0 for name in deviceprotection]
            techsupport1_0 = [1 if new_techsupport == name else 0 for name in techsupport]
            streamingtv1_0 = [1 if new_streamingtv == name else 0 for name in streamingtv]
            streamingmovies1_0 = [1 if new_streamingmovies == name else 0 for name in streamingmovies]

            features = [list(data.values())  +paymentmethod1_0 +contract1_0
                        +internetservice1_0+multiplelines1_0 +gender1_0
                        +partner1_0+ dependents1_0 +phoneservice1_0 +paperlessbilling1_0
                        +onlinebackup1_0 +onlinesecurity1_0 +deviceprotection1_0 +techsupport1_0
                        +streamingtv1_0 +streamingmovies1_0 ]
            scaled_data = scaler_telecom.transform(features)
            predict_telecom = model_telecom.predict(scaled_data)[0]
            if predict_telecom == 1:
                predict_telecom = 'Останется'
            else:
                predict_telecom = 'Уйдет'
            return Response({ 'Predict': predict_telecom}, status.HTTP_200_OK)
        return Response(instance.errors,  status=status.HTTP_400_BAD_REQUEST)





class PredictDiabet(views.APIView):
    def post(self, request):
        instance = DiabetSerializer(data=request.data)
        if instance.is_valid():
            data = instance.validated_data
            features = list(data.values())
            scaled_data = scaler_diabet.transform([features])
            predict_diabet = model_diabet.predict(scaled_data)[0]
            if predict_diabet == 1:
                predict_diabet = 'Диабет'
            else:
                predict_diabet = 'Нет Диабета'
            return Response({'Predict': predict_diabet}, status.HTTP_200_OK)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)







