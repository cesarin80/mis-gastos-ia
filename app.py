import streamlit as st
import pandas as pd
import os

# Crea el archivo gastos.csv si no existe
if not os.path.isfile('gastos.csv'):
    df = pd.DataFrame(columns=['Descripción', 'Categoría', 'Monto'])
    df.to_csv('gastos.csv', index=False)

# Crea la aplicación Streamlit
st.title('Smart Expense Tracker')
st.header('Proyecto final de la asignatura de Desarrollo de aplicaciones web')

# Crea un formulario para ingresar los gastos
formulario = st.form('Formulario')
descripcion = formulario.text_input('Descripción')
categoria = formulario.selectbox('Categoría', ['Comida', 'Transporte', 'Ocio', 'Otros'])
monto = formulario.number_input('Monto')
boton_guardar = formulario.form_submit_button('Guardar Gasto')
# Crea una tabla para mostrar los gastos guardados
if boton_guardar:
    df = pd.read_csv('gastos.csv')
    nuevo_registro = pd.DataFrame({'Descripción': [descripcion], 'Categoría': [categoria], 'Monto': [monto]})
    df = pd.concat([df, nuevo_registro])
    df.to_csv('gastos.csv', index=False)

df = pd.read_csv('gastos.csv')
st.table(df)

# Muestra el total gastado
st.subheader('Análisis de Gastos')

df = pd.read_csv('gastos.csv')
df['Monto'] = df['Monto'].astype(float)

total_gastado_por_categoria = df.groupby('Categoría')['Monto'].sum()
st.bar_chart(total_gastado_por_categoria)
total_gastado = df['Monto'].sum()
st.header(f'Total Gastado: ${total_gastado:.2f}')

