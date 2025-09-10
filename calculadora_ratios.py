"""
Módulo para el cálculo de ratios financieros del modelo DuPont.
Implementa la Funcionalidad 1 del proyecto ROE DuPont Interactivo.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class CalculadoraRatiosDuPont:
    """
    Clase para calcular los ratios financieros del modelo DuPont.
    
    El modelo DuPont descompone el ROE en tres componentes:
    ROE = Margen Neto × Rotación de Activos × Apalancamiento Financiero
    """
    
    def __init__(self):
        """Inicializa la calculadora con valores por defecto."""
        self.utilidad_neta = 0
        self.ventas = 0
        self.activos_promedio = 0
        self.patrimonio_promedio = 0
        
    def calcular_margen_neto(self):
        """
        Calcula el margen neto.
        
        Margen Neto = Utilidad Neta / Ventas
        
        Returns:
            float: Margen neto como porcentaje
        """
        if self.ventas == 0:
            return 0
        return (self.utilidad_neta / self.ventas) * 100
    
    def calcular_rotacion_activos(self):
        """
        Calcula la rotación de activos.
        
        Rotación de Activos = Ventas / Activos Promedio
        
        Returns:
            float: Rotación de activos
        """
        if self.activos_promedio == 0:
            return 0
        return self.ventas / self.activos_promedio
    
    def calcular_apalancamiento_financiero(self):
        """
        Calcula el apalancamiento financiero.
        
        Apalancamiento Financiero = Activos Promedio / Patrimonio Promedio
        
        Returns:
            float: Apalancamiento financiero
        """
        if self.patrimonio_promedio == 0:
            return 0
        return self.activos_promedio / self.patrimonio_promedio
    
    def calcular_roe(self):
        """
        Calcula el ROE usando el modelo DuPont.
        
        ROE = Margen Neto × Rotación de Activos × Apalancamiento Financiero
        
        Returns:
            float: ROE como porcentaje
        """
        margen_neto = self.calcular_margen_neto()
        rotacion_activos = self.calcular_rotacion_activos()
        apalancamiento = self.calcular_apalancamiento_financiero()
        
        # Convertir margen neto a decimal para el cálculo
        margen_neto_decimal = margen_neto / 100
        
        roe = margen_neto_decimal * rotacion_activos * apalancamiento * 100
        return roe
    
    def obtener_todos_los_ratios(self):
        """
        Calcula todos los ratios del modelo DuPont.
        
        Returns:
            dict: Diccionario con todos los ratios calculados
        """
        return {
            'margen_neto': self.calcular_margen_neto(),
            'rotacion_activos': self.calcular_rotacion_activos(),
            'apalancamiento_financiero': self.calcular_apalancamiento_financiero(),
            'roe': self.calcular_roe()
        }


def crear_interfaz_sliders_sidebar():
    """
    Crea la interfaz de sliders en el sidebar para capturar las variables de entrada.
    
    Returns:
        CalculadoraRatiosDuPont: Instancia configurada con los valores de los sliders
    """
    with st.sidebar:
        st.subheader("📊 Variables de Entrada")
        st.markdown("Ajusta los valores usando los sliders para calcular los ratios financieros:")
        
        st.markdown("**💰 Variables de Rentabilidad**")
        utilidad_neta = st.slider(
            "Utilidad Neta ($)",
            min_value=0.0,
            max_value=1000000.0,
            value=100000.0,
            step=10000.0,
            help="Utilidad neta después de impuestos"
        )
        
        ventas = st.slider(
            "Ventas ($)",
            min_value=0.0,
            max_value=5000000.0,
            value=1000000.0,
            step=50000.0,
            help="Ventas totales de la empresa"
        )
        
        st.markdown("**🏢 Variables de Estructura**")
        activos_promedio = st.slider(
            "Activos Promedio ($)",
            min_value=0.0,
            max_value=3000000.0,
            value=800000.0,
            step=25000.0,
            help="Activos totales promedio durante el período"
        )
        
        patrimonio_promedio = st.slider(
            "Patrimonio Promedio ($)",
            min_value=0.0,
            max_value=1500000.0,
            value=400000.0,
            step=10000.0,
            help="Patrimonio promedio durante el período"
        )
    
    # Crear instancia de la calculadora y asignar valores
    calculadora = CalculadoraRatiosDuPont()
    calculadora.utilidad_neta = utilidad_neta
    calculadora.ventas = ventas
    calculadora.activos_promedio = activos_promedio
    calculadora.patrimonio_promedio = patrimonio_promedio
    
    return calculadora


def mostrar_resultados(calculadora):
    """
    Muestra los resultados de los cálculos en formato visual.
    
    Args:
        calculadora (CalculadoraRatiosDuPont): Instancia con los valores calculados
    """
    st.subheader("📈 Resultados del Modelo DuPont")
    
    # Calcular todos los ratios
    ratios = calculadora.obtener_todos_los_ratios()
    
    # Crear métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Margen Neto",
            value=f"{ratios['margen_neto']:.2f}%",
            help="Utilidad Neta / Ventas"
        )
    
    with col2:
        st.metric(
            label="Rotación de Activos",
            value=f"{ratios['rotacion_activos']:.2f}x",
            help="Ventas / Activos Promedio"
        )
    
    with col3:
        st.metric(
            label="Apalancamiento Financiero",
            value=f"{ratios['apalancamiento_financiero']:.2f}x",
            help="Activos Promedio / Patrimonio Promedio"
        )
    
    with col4:
        st.metric(
            label="🎯 ROE (Return on Equity)",
            value=f"{ratios['roe']:.2f}%",
            delta=None,
            help="Margen Neto × Rotación de Activos × Apalancamiento Financiero"
        )


