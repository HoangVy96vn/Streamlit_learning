import streamlit as st

st.title("TESTING FIRST APP WITH STREAMLIT")
st.write("Welcome to the first app")

# Click button
st.header('Click button: True/False')
button1 = st.button("Click")
if button1:
    st.write("Done click")

# Checkbox
st.header('Checkbox: True/False')
check = st.checkbox("Did you study today?")
if check:
    st.write("Good job")
else: st.write('You need to start right now')

# radio button
st.header('Ratio button: Options & Single choice')
disk_list = ['chicken','burger','noodle','rice']
disks = st.radio("What did you have?", disk_list)

# selectbox
st.header('Selectbox: Options & Single choice')
st.selectbox('Pick what you want for dinner', disk_list)

# Multiselect
st.header('Multiselect: Options & Multiple choices')
choices = st.multiselect('Picks your favorites', disk_list)

if choices:
    st.write(choices)

# Slider
st.header('Slider to integrer')
num = st.slider('slide to get number', 1, 100, 10)
if st.button("Slider_button"):
    st.write(num)

# Input text
st.header('Input text: string')
text = st.text_input('What season do you like','This is default text')
if st.button('season'):
    st.write(text)

# Input number
st.header('Input number: numeric')
num_input = st.number_input('What is your height')
if st.button('Height'):
    st.write(num_input)

# Text area
txt = st.text_area('Describe','This should be a long text describing something')


