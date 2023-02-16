import requests
import streamlit as st 


st.title("Minsk Apartment Price Prediction")
st.image("img.jpg")

with st.form(key='columns_in_form'):
    cols = st.columns(3)
    total_area = cols[0].number_input('Total area', min_value=1, max_value=500, step=1)
    living_area = cols[1].number_input('Living area', min_value=1, max_value=500, step=1)
    kitchen_area = cols[2].number_input('Kitchen area', min_value=1, max_value=500, step=1)

    cols = st.columns(3)
    number_of_rooms = cols[0].number_input('Number of rooms', min_value=1, max_value=10, step=1)
    floor = cols[1].number_input('Floor', min_value=1, max_value=30, step=1)
    number_of_storeys = cols[2].number_input('Number of storeys', min_value=1, max_value=30, step=1)

    cols = st.columns(3)
    year_built = cols[0].number_input('Year build', min_value=1900, max_value=2022, step=1)
    ceiling_height = cols[1].number_input('Ceiling height', min_value=2.0, max_value=4.0, step=0.01)
    balcony = cols[2].selectbox('Balcony',
                      ('Without', 'Loggia', 'Balcony', 'Two balconies'))

    cols = st.columns(3)
    bathroom = cols[0].selectbox('Bathroom',
                      ('separate', 'combined', '2', '>2'))
    house_type = cols[1].selectbox('House type',
                      ('frame-block', 'panel', 'brick', 'monolithic', 'block-rooms', 'silicate'))
    district = cols[2].selectbox('District',
                      ('Sovetsky', 'Oktyabrsky', 'Pervomaisky', 'Tsentralny', 'Partizansky', 
                       'Leninsky', 'Zavodskoy', 'Moskovsky', 'Frunzensky'))
    cols = st.columns(3)
    subway = cols[0].selectbox('Near Subway', ('No', 'Yes'))

    cols = st.columns(2)
    submitted = cols[0].form_submit_button('Get price')
    price_text = cols[1]


if submitted:
    data = {
        "year_built": year_built, 
        "floor": floor,
        "ceiling_height": ceiling_height, 
        "total_area": total_area, 
        "living_area": living_area, 
        "kitchen_area": kitchen_area,
        "bathroom": bathroom,
        "balcony": balcony,
        "near_the_subway": subway,
        "house_type": house_type, 
        "district": district,
        "number_of_rooms": number_of_rooms, 
        "number_of_storeys": number_of_storeys, 
    }
    
    resp = requests.post("https://model-predict-api.onrender.com/minsk_apartment/predict", json=data)
    price = resp.json()["price"]

    text = f'<p style="font-family:sans-serif; color:Red; font-size: 24px;">{price} $</p>'
    price_text.markdown(text, unsafe_allow_html=True)