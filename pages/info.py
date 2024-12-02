import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Cargar imágenes
img_efecto = Image.open("imagenes/efecto.png")

# Cargar datos de Excel
file_path = "C:/Users/WeeZ/Desktop/devChallenge/data/Ecuador_CO2_Emissions_By_Category.xlsx"
data = pd.read_excel(file_path)

# Barra lateral para filtros 
st.sidebar.title("Filtros")
year = st.sidebar.selectbox("Seleccione el año", data["Year"].unique())
province = st.sidebar.multiselect("Seleccione Provincia(s)", data["Province"].unique(), default=data["Province"].unique())

# Filtrar datos según la selección del usuario
filtered_data = data[(data["Year"] == year) & (data["Province"].isin(province))]

# Mostrar datos filtrados
st.title(f"Dashboard de Emisiones de CO₂ - {year}")
st.dataframe(filtered_data)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:  # Crear gráfico de barras para emisiones por categoría
        st.subheader("Total de Emisiones de CO₂ por Categoría")
        category_columns = ["Energía", "Transporte", "Agricultura", "Industria y uso de productos", "Gestión de residuos"]
        category_totals = filtered_data[category_columns].sum()

        fig, ax = plt.subplots()
        category_totals.plot(kind="bar", ax=ax)
        ax.set_title("Emisiones de CO₂ por Categoría")
        ax.set_ylabel("Emisiones (toneladas)")
        ax.set_xlabel("Categoría")
        st.pyplot(fig)

    with right_column:  # Crear gráfico de líneas para provincias seleccionadas a lo largo del tiempo
        st.subheader("Emisiones de CO₂ a lo largo del tiempo")
        province_data = data[data["Province"].isin(province)].groupby(["Year", "Province"]).sum().reset_index()

        fig, ax = plt.subplots()
        for prov in province:
            subset = province_data[province_data["Province"] == prov]
            ax.plot(subset["Year"], subset["Total CO2 Emissions (tons)"], marker="o", label=prov)

        ax.set_title("Emisiones de CO₂ a lo largo del tiempo")
        ax.set_ylabel("Emisiones (toneladas)")
        ax.set_xlabel("Año")

        # Ajustar dinámicamente el tamaño de la fuente de la leyenda según el número de provincias seleccionadas
        num_provinces = len(province)
        if num_provinces <= 5:
            legend_font_size = 12
        elif num_provinces <= 10:
            legend_font_size = 10
        else:
            legend_font_size = 5

        ax.legend(fontsize=legend_font_size, loc="best")
        st.pyplot(fig)

st.write("---")

# Crear gráfico de pastel para emisiones totales por provincia
st.subheader("Emisiones de CO₂ Proporcionales (Provincias Seleccionadas)")

# Calcular emisiones totales para cada provincia
province_totals = filtered_data.groupby("Province")["Total CO2 Emissions (tons)"].sum()

# Ajustar dinámicamente el tamaño de la fuente según el número de provincias seleccionadas
num_provinces = len(province_totals)
if num_provinces <= 5:
    font_size = 10
elif num_provinces <= 10:
    font_size = 5
else:
    font_size = 2

# Graficar el pastel
fig, ax = plt.subplots()
colors = plt.cm.Pastel1(range(len(province_totals)))  # Usar colores pastel
province_totals.plot.pie(
    ax=ax,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    textprops={'fontsize': font_size}  # Ajustar dinámicamente el tamaño de la fuente
)
ax.set_ylabel("")  # Eliminar etiqueta predeterminada del eje y
ax.set_title("Emisiones de CO₂ Proporcionales por Provincia", fontsize=font_size + 2)  # Ajustar tamaño del título ligeramente mayor que las etiquetas
st.pyplot(fig)

# Resumen informativo
st.write("---")
st.subheader("Resumen Informativo")
st.write(f"### Total de Emisiones de CO₂ en {year}:")
st.write(f"{filtered_data['Total CO2 Emissions (tons)'].sum():,.0f} toneladas")

with st.container():
    text_column, image_column = st.columns((1,2))
    with text_column: 
        st.write("### Resumen de Emisiones de CO₂ por Categoría:")
        for category, value in category_totals.items():
            st.write(f"- **{category}**: {value:,.0f} toneladas")

    with image_column:
        st.image(img_efecto)
