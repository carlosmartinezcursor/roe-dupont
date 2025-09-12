"""
Aplicación principal del proyecto ROE DuPont Interactivo.
Implementa la Funcionalidad 1: Cálculo de ratios financieros básicos.

Autor: Proyecto ROE DuPont
Versión: 1.0
"""

import streamlit as st
from calculadora_ratios import (
    crear_interfaz_sliders_sidebar, 
    mostrar_resultados
)
from visualizacion_3d import mostrar_visualizacion_3d
from estados_financieros import mostrar_estados_financieros

# Configuración de la página
st.set_page_config(
    page_title="ROE DuPont Interactivo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """
    Función principal de la aplicación Streamlit.
    """
    # Título principal
    st.title("📊 ROE DuPont Interactivo")
    st.markdown("### Análisis Financiero con el Modelo DuPont")
    
    # Información sobre el modelo DuPont
    with st.expander("ℹ️ ¿Qué es el Modelo DuPont?", expanded=False):
        st.markdown("""
        El **Modelo DuPont** es una herramienta de análisis financiero que descompone 
        el Return on Equity (ROE) en tres componentes clave:
        
        **ROE = Margen Neto × Rotación de Activos × Apalancamiento Financiero**
        
        - **Margen Neto**: Mide la eficiencia en la generación de utilidades
        - **Rotación de Activos**: Mide la eficiencia en el uso de los activos
        - **Apalancamiento Financiero**: Mide el uso de deuda para financiar activos
        
        Esta descomposición permite identificar qué factores están impulsando 
        o limitando la rentabilidad del patrimonio.
        """)
    
    # Crear la interfaz de sliders en el sidebar
    calculadora = crear_interfaz_sliders_sidebar()
    
    # Mostrar resultados
    mostrar_resultados(calculadora)
    
    # Separador visual
    st.markdown("---")
    
    # Mostrar visualización 3D del prisma ROE
    mostrar_visualizacion_3d(calculadora)
    
    # Separador visual
    st.markdown("---")
    
    # Mostrar estados financieros simplificados
    mostrar_estados_financieros(calculadora)


if __name__ == "__main__":
    main()
