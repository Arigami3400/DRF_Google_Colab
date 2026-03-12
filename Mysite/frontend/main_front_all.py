import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from Mysite.frontend.house_front import check_house
from Mysite.frontend.student_front import check_student
from Mysite.frontend.titanic_front import check_titanic
from Mysite.frontend.bank_front import check_bank
from Mysite.frontend.mash_front import check_mashrooms
from Mysite.frontend.diabet_front import check_diabet
from Mysite.frontend.avocado_front import check_avocado
from Mysite.frontend.telecom_front import check_telecom
from Mysite.frontend.staff_front import check_staff

with st.sidebar:
    name = st.radio('ML models:', ['Info', 'House', 'Student', 'Titanic', 'Bank',
                                   'Mashrooms', 'Diabet', 'Avocado', 'Telecom', 'Staff'])

if name =='Info':
    st.title('Welcome')
    st.text('Student — предсказание успеваемости студентов')
    st.text('Titanic — предсказание выживаемости на борту корабля')
    st.text('House — предсказание стоимости недвижимости')
    st.text('Bank — банковская аналитика')
    st.text('Diabet — диагностика диабета')
    st.text('Avocado — предсказание зрелости авокадо')
    st.text('Mushroom — классификация грибов')
    st.text('Telecom — отток клиентов телеком')
    st.text('Staff — отток сотрудников в компании')


elif name == 'House':
    check_house()

elif name == 'Student':
    check_student()

elif name == 'Titanic':
    check_titanic()

elif name == 'Bank':
    check_bank()

elif name == 'Mashrooms':
    check_mashrooms()

elif name == 'Diabet':
    check_diabet()

elif name == 'Avocado':
    check_avocado()

elif name == 'Telecom':
    check_telecom()

elif name == 'Staff':
    check_staff()