import streamlit as st

import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('And I am loving it')

st.write('This is a normal text')

st.markdown("""

### My favourite movies
- Race 3
- Humshakals
- Housefull                        
""")


st.code(""" 

def foo(input):
    return foo**2

x = foo(2)

""")

st.latex('x^2 + y^2 + 2 = 0')


df = pd.DataFrame({

    'name':['Nitish','Ankit','Kaustav'],
    'marks':[50,60,70],
    'package':[10,12,14]

})

st.dataframe(df)

st.metric('Revenue','Rs 3L','-3%')

st.json({

    'name':['Nitish','Ankit','Kaustav'],
    'marks':[50,60,70],
    'package':[10,12,14]

})

st.image('kohli.jpg')

st.sidebar.title('Sidebar ka title')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('kohli.jpg')

with col2:
    st.image('kohli.jpg')

with col3:
    st.image('kohli.jpg')


st.error('Login Failed')

st.success('Login Successful')

st.info('Login Successful')

st.warning('Login Successful')

bar = st.progress(0)

for i in range(1,101):
    #time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter email')
number = st.number_input('Enter age')
st.date_input('Enter regis date')





email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender',['male','female','others'])

btn = st.button('Login Karo')

# if the button is clicked
if btn:
    if email == 'nitish@gmail.com' and password == '1234':
        st.success('Login successful')
        st.write(gender)
        st.balloons()

    else:
        st.error('Login Failed')

        

import streamlit as st
import pandas as pd

file = st.file_uploader('Upload a csv file')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())


