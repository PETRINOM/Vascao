import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def text_on_image(image, text, color, font_size):

    img = Image.open(image)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", font_size)
    draw.text((10, 10), text, fill=color, font=font)
    st.image(img, width=300)
    img.save("image.png") 
    return img

image = st.file_uploader("Escolhe uma imagem", type=["png", "jpeg", "jpg"])

text = st.text_input("Escreve um texto")

color = st.selectbox("Escolhe uma cor", ["red", "green", "blue"])
#st.write(color)
font_size = st.slider("Escolhe um tamanho de fonte", 10, 100, 20)
if image:
    st.image(image, width=300)
    result = st.button(
        "Gerar marca D'água",
        type="primary",
        help="Clique para gerar a marca D'água",
    on_click=text_on_image,
    args=(image, text, color, font_size),
)
    st.write(result)
    if result:
        st.image("image.png", width=300)
        with open("image.png", "rb") as f:
            st.download_button("baixar imagem", f.read(), mime="image/png")
