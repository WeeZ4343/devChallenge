import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="EcoCO2Explorer", page_icon=":tada:", layout="wide"
)

#---- imagenes--
img_video = Image.open("imagenes/video1.png")
img_co2 = Image.open("imagenes/co2.png")
img_carbono0 = Image.open("imagenes/ecu-cabrono.png")

#----- header----
with st.container():
    st.title("Pagina Principal")
    st.subheader("Hola :wave:, Bienvenidos a nuestra aplicaccion web")
    st.write("Somos un grupo de estudiantes de la PUCE apasionados por el desarrollo web")

# ---- descripcion---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Impacto y creacion co2")
        st.write(
            """
            El siguiente trabajo de desarrollo se encuentra enfocado en los siguientes aspectos:\n
            -Concientizar sobre el impacto medioambiental del CO2 producido en Ecuador.\n
            -Brindar información confiable sobre la producción de CO2 en los últimos años.\n
            -Brindar herramientas multimedia para la educación ambiental de los usuarios.\n
            """
        )
    with right_column:
        st.image(img_co2)

#---- Recursos---
with st.container():
    st.write("---")
    st.header("Recursos Multimedia")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_video)

    with text_column:
        st.subheader("Emisiones de gases de efecto invernadero en Ecuador")
        st.write(

        )
        st.markdown("[Ver Video informativo...](https://youtu.be/Gqtxn8THy0Y)")

with st.container():
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_carbono0)

    with text_column:
        st.subheader("Programa Ecuador Carbono 0")
        st.write(

        )
        st.markdown("[Ver Video Informativo...](https://youtu.be/v0Fnm8Thlz8)")

st.sidebar.success("seleccione una pagina.")