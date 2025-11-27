import streamlit as st

st.title("こんにちは、吉村ゼミ")

name = st.text_input("名前を入力")
st.write(name)

st.checkbox("同意します")
address = st.selectbox("次の中から住所を教えて",["京都府","大阪府","滋賀県"])
st.write(address)

hobby = st.multiselect("趣味を選んでね",["映画","マンガ","散歩"])
st.write(hobby) 

score = st.slider("この映画を１０点満点で評価すると",0,10,0)
st.write(score)

st.radio("性別を選んでね",["おとこ","おんな","どっちも"])

list = [
  {"latitude":35,05, "longitude":135,76},
  {"latitude":35,04, "longitude":135,75},
]
st.map(list)

camera = st.camera_input("写真を撮影します！")
if camera:
  st.image(camera, caption="写真", use_column_width=true)

           
                    
