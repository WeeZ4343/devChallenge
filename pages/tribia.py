import streamlit as st

preguntas = ("¿Cuál es la provincia con mayor emisión de CO2 en el año 2021?: ",
             "¿Cuál fue la cantidad promedio de CO2 emitido en 2022 por todas las provincias?: ",
             "En 2023, ¿qué provincia tuvo la menor emisión de CO2?: ",
             "¿Cuántas provincias emitieron más de 1,000,000 toneladas de CO2 en 2021?: ",
             "¿En qué año la emisión total de CO2 en Ecuador fue la mayor?: ")

opciones = (("Guayas", "Pichincha", "Manabí", "Esmeraldas"),
            ("950,000 toneladas", "800,000 toneladas", "1,100,000 toneladas", "1,200,000 toneladas"),
            ("Galápagos", "Carchi", "Bolívar", "Imbabura"),
            ("10 provincias", "8 provincias", "12 provincias", "14 provincias"),
            ("2023", "2021", "2022", "Son iguales en todos los años"))

respuestas = ("A", "C", "A", "C", "B")

# Estado de inicio
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "guesses" not in st.session_state:
    st.session_state.guesses = []

# Css para los botones y preguntas
st.markdown("""
    <style>
        /* Blue rectangle for the question */
        .pregunta-container {
            background-color: #e0f7fa; /* Light blue */
            border: 2px solid #0288d1; /* Blue border */
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #004d40; /* Dark teal text */
        }

        .option-button {
            background-color: yellow;
            color: black;
            border: 2px solid black;
            padding: 20px;
            font-weight: bold;
            text-align: center;
            width: 100%;
            height: 70px;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }
        .option-button:hover {
            background-color: #f4e042;
        }
        .col-container {
            display: flex;
            justify-content: space-between;
            gap: 10px;
        }
        .col-container > div {
            width: 48%;  /* Ensures equal width for all buttons */
        }
    </style>
""", unsafe_allow_html=True)

# Boton para regresar al inicio
if st.button("Regresar al inicio"):
    st.session_state.clear()  # Clears session state variables
    st.rerun()  # Forces a reload of the page

# Pregunta actual
if st.session_state.current_question < len(preguntas):
    question = preguntas[st.session_state.current_question]
    options = opciones[st.session_state.current_question]

    # contenedor css de pregutna
    st.markdown(f'<div class="pregunta-container">{question}</div>', unsafe_allow_html=True)

    # Crea estructura 2x2
    col1, col2 = st.columns(2)
    with col1:
        option1 = st.button(options[0], key=f"opt1_{st.session_state.current_question}", help="Select this option", use_container_width=True)
    with col2:
        option2 = st.button(options[1], key=f"opt2_{st.session_state.current_question}", help="Select this option", use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        option3 = st.button(options[2], key=f"opt3_{st.session_state.current_question}", help="Select this option", use_container_width=True)
    with col2:
        option4 = st.button(options[3], key=f"opt4_{st.session_state.current_question}", help="Select this option", use_container_width=True)

    # Chequea la respuesta seleccionada (boton)
    selected_option = None
    if option1:
        selected_option = options[0]
    elif option2:
        selected_option = options[1]
    elif option3:
        selected_option = options[2]
    elif option4:
        selected_option = options[3]

    # Boton de seleccion de respuesta
    if selected_option:
        st.session_state.guesses.append(selected_option)  #almacena los intentos
        
        # Obtener la respuesta correcta
        correct_answer = opciones[st.session_state.current_question][ord(respuestas[st.session_state.current_question]) - ord('A')]  # Correct answer
        
        if selected_option == correct_answer:
            st.session_state.score += 1
            st.success("¡Correcto!")
        else:
            st.error(f"Incorrecto. La respuesta correcta es: {correct_answer}")
        
        # Seguir a la siguiente pregunta
        st.session_state.current_question += 1
else:
    st.write("### RESULTADOS")
    st.write("Respuestas correctas:", " ".join(respuestas))
    st.write("Tus respuestas:", " ".join(st.session_state.guesses))
    score_percentage = int(st.session_state.score / len(preguntas) * 100)
    st.write(f"Tu puntaje final es: {score_percentage}%")
