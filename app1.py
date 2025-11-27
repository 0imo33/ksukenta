import streamlit as st

st.title("こんにちは、吉村ゼミ")

name = st.text_input("名前を入力")
st.write(name)

st.checkbox("同意します")
address = st.selectbox("次の中から住所を教えて",["京都府","大阪府","滋賀県"])
st.write(address)

st.multiselect("趣味を選んでね",["映画","マンガ","散歩"])

camera = st.camera_input("写真を撮影します！")
if camera:
  st.image(camera, caption="写真", use_column_width=true)

           
                    
