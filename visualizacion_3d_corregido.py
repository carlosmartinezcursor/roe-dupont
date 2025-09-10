"""
Módulo para la visualización 3D del Prisma ROE.
Implementa la Funcionalidad 2 del proyecto ROE DuPont Interactivo.

Este módulo crea un prisma tridimensional que representa visualmente
la descomposición del ROE en sus tres componentes del modelo DuPont.
"""

import streamlit as st
import plotly.graph_objects as go
import numpy as np
from calculadora_ratios import CalculadoraRatiosDuPont


class VisualizadorPrismaROE:
    """
    Clase para crear y gestionar la visualización 3D del prisma ROE.
    
    El prisma representa los tres componentes del modelo DuPont:
    - Margen Neto (eje X)
    - Rotación de Activos (eje Y) 
    - Apalancamiento Financiero (eje Z)
    """
    
    def __init__(self):
        """Inicializa el visualizador del prisma ROE."""
        self.colores_componentes = {
            'margen_neto': '#1f77b4',      # Azul
            'rotacion_activos': '#ff7f0e',  # Naranja
            'apalancamiento': '#2ca02c',    # Verde
            'roe': '#d62728'               # Rojo
        }
    
    def crear_prisma_roe(self, calculadora):
        """
        Crea el prisma 3D que representa la descomposición del ROE.
        
        Args:
            calculadora (CalculadoraRatiosDuPont): Instancia con los ratios calculados
            
        Returns:
            plotly.graph_objects.Figure: Figura 3D del prisma ROE
        """
        # Obtener los ratios calculados
        ratios = calculadora.obtener_todos_los_ratios()
        
        # Normalizar los valores para la visualización 3D
        # Usar escalas apropiadas para cada componente
        margen_neto_norm = min(ratios['margen_neto'] / 20, 1.0)  # Máximo 20%
        rotacion_norm = min(ratios['rotacion_activos'] / 3, 1.0)  # Máximo 3x
        apalancamiento_norm = min(ratios['apalancamiento_financiero'] / 4, 1.0)  # Máximo 4x
        
        # Crear la figura 3D
        fig = go.Figure()
        
        # Agregar el prisma principal
        fig.add_trace(go.Mesh3d(
            x=[0, margen_neto_norm, margen_neto_norm, 0, 0, margen_neto_norm, margen_neto_norm, 0],
            y=[0, 0, rotacion_norm, rotacion_norm, 0, 0, rotacion_norm, rotacion_norm],
            z=[0, 0, 0, 0, apalancamiento_norm, apalancamiento_norm, apalancamiento_norm, apalancamiento_norm],
            i=[0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 5, 4, 2, 3, 7, 6, 0, 3, 7, 4, 1, 2, 6, 5],
            j=[1, 2, 3, 0, 5, 6, 7, 4, 1, 5, 4, 0, 3, 7, 6, 2, 3, 0, 4, 7, 2, 6, 5, 1],
            k=[2, 3, 0, 1, 6, 7, 4, 5, 5, 4, 0, 1, 7, 6, 2, 3, 7, 4, 0, 3, 6, 5, 1, 2],
            opacity=0.7,
            color='lightblue',
            name='Prisma ROE',
            hovertemplate='<b>Prisma ROE</b><br>' +
                         'Margen Neto: %{x:.2f}<br>' +
                         'Rotación: %{y:.2f}<br>' +
                         'Apalancamiento: %{z:.2f}<br>' +
                         '<extra></extra>'
        ))
        
        # Agregar ejes de referencia para cada componente
        self._agregar_ejes_componentes(fig, margen_neto_norm, rotacion_norm, apalancamiento_norm)
        
        # Agregar etiquetas de los componentes usando Scatter3d
        self._agregar_etiquetas_componentes(fig, margen_neto_norm, rotacion_norm, apalancamiento_norm, ratios)
        
        # Agregar punto central que representa el ROE
        self._agregar_punto_roe(fig, margen_neto_norm, rotacion_norm, apalancamiento_norm, ratios['roe'])
        
        # Configurar el layout de la figura
        self._configurar_layout(fig, ratios)
        
        return fig
    
    def _agregar_ejes_componentes(self, fig, margen_norm, rotacion_norm, apalancamiento_norm):
        """
        Agrega ejes de referencia para visualizar cada componente.
        
        Args:
            fig: Figura de Plotly
            margen_norm: Valor normalizado del margen neto
            rotacion_norm: Valor normalizado de la rotación
            apalancamiento_norm: Valor normalizado del apalancamiento
        """
        # Eje X - Margen Neto
        fig.add_trace(go.Scatter3d(
            x=[0, margen_norm],
            y=[0, 0],
            z=[0, 0],
            mode='lines+markers',
            line=dict(color=self.colores_componentes['margen_neto'], width=8),
            marker=dict(size=6, color=self.colores_componentes['margen_neto']),
            name='Margen Neto',
            hovertemplate='<b>Margen Neto</b><br>Valor: %{x:.2f}<br><extra></extra>'
        ))
        
        # Eje Y - Rotación de Activos
        fig.add_trace(go.Scatter3d(
            x=[0, 0],
            y=[0, rotacion_norm],
            z=[0, 0],
            mode='lines+markers',
            line=dict(color=self.colores_componentes['rotacion_activos'], width=8),
            marker=dict(size=6, color=self.colores_componentes['rotacion_activos']),
            name='Rotación de Activos',
            hovertemplate='<b>Rotación de Activos</b><br>Valor: %{y:.2f}<br><extra></extra>'
        ))
        
        # Eje Z - Apalancamiento Financiero
        fig.add_trace(go.Scatter3d(
            x=[0, 0],
            y=[0, 0],
            z=[0, apalancamiento_norm],
            mode='lines+markers',
            line=dict(color=self.colores_componentes['apalancamiento'], width=8),
            marker=dict(size=6, color=self.colores_componentes['apalancamiento']),
            name='Apalancamiento Financiero',
            hovertemplate='<b>Apalancamiento Financiero</b><br>Valor: %{z:.2f}<br><extra></extra>'
        ))
    
    def _agregar_etiquetas_componentes(self, fig, margen_norm, rotacion_norm, apalancamiento_norm, ratios):
        """
        Agrega etiquetas explicativas para cada componente usando Scatter3d.
        
        Args:
            fig: Figura de Plotly
            margen_norm: Valor normalizado del margen neto
            rotacion_norm: Valor normalizado de la rotación
            apalancamiento_norm: Valor normalizado del apalancamiento
            ratios: Diccionario con los ratios calculados
        """
        # Etiqueta para Margen Neto
        fig.add_trace(go.Scatter3d(
            x=[margen_norm + 0.15],
            y=[0],
            z=[0],
            mode='markers+text',
            marker=dict(size=1, color='rgba(0,0,0,0)'),
            text=[f"Margen Neto<br>{ratios['margen_neto']:.2f}%"],
            textposition='middle right',
            textfont=dict(size=12, color=self.colores_componentes['margen_neto']),
            name='Etiqueta Margen Neto',
            showlegend=False,
            hovertemplate=f"<b>Margen Neto</b><br>{ratios['margen_neto']:.2f}%<br><extra></extra>"
        ))
        
        # Etiqueta para Rotación de Activos
        fig.add_trace(go.Scatter3d(
            x=[0],
            y=[rotacion_norm + 0.15],
            z=[0],
            mode='markers+text',
            marker=dict(size=1, color='rgba(0,0,0,0)'),
            text=[f"Rotación de Activos<br>{ratios['rotacion_activos']:.2f}x"],
            textposition='middle right',
            textfont=dict(size=12, color=self.colores_componentes['rotacion_activos']),
            name='Etiqueta Rotación',
            showlegend=False,
            hovertemplate=f"<b>Rotación de Activos</b><br>{ratios['rotacion_activos']:.2f}x<br><extra></extra>"
        ))
        
        # Etiqueta para Apalancamiento Financiero
        fig.add_trace(go.Scatter3d(
            x=[0],
            y=[0],
            z=[apalancamiento_norm + 0.15],
            mode='markers+text',
            marker=dict(size=1, color='rgba(0,0,0,0)'),
            text=[f"Apalancamiento<br>{ratios['apalancamiento_financiero']:.2f}x"],
            textposition='top center',
            textfont=dict(size=12, color=self.colores_componentes['apalancamiento']),
            name='Etiqueta Apalancamiento',
            showlegend=False,
            hovertemplate=f"<b>Apalancamiento Financiero</b><br>{ratios['apalancamiento_financiero']:.2f}x<br><extra></extra>"
        ))
    
    def _agregar_punto_roe(self, fig, margen_norm, rotacion_norm, apalancamiento_norm, roe):
        """
        Agrega un punto que representa el ROE calculado.
        
        Args:
            fig: Figura de Plotly
            margen_norm: Valor normalizado del margen neto
            rotacion_norm: Valor normalizado de la rotación
            apalancamiento_norm: Valor normalizado del apalancamiento
            roe: Valor del ROE calculado
        """
        fig.add_trace(go.Scatter3d(
            x=[margen_norm],
            y=[rotacion_norm],
            z=[apalancamiento_norm],
            mode='markers',
            marker=dict(
                size=15,
                color=self.colores_componentes['roe'],
                symbol='diamond',
                line=dict(width=2, color='white')
            ),
            name='ROE',
            hovertemplate=f'<b>ROE Calculado</b><br>{roe:.2f}%<br><extra></extra>'
        ))
        
        # Etiqueta para el ROE usando Scatter3d
        fig.add_trace(go.Scatter3d(
            x=[margen_norm],
            y=[rotacion_norm],
            z=[apalancamiento_norm + 0.2],
            mode='markers+text',
            marker=dict(size=1, color='rgba(0,0,0,0)'),
            text=[f"ROE<br>{roe:.2f}%"],
            textposition='top center',
            textfont=dict(size=14, color=self.colores_componentes['roe'], family="Arial Black"),
            name='Etiqueta ROE',
            showlegend=False,
            hovertemplate=f"<b>ROE Total</b><br>{roe:.2f}%<br><extra></extra>"
        ))
    
    def _configurar_layout(self, fig, ratios):
        """
        Configura el layout de la figura 3D.
        
        Args:
            fig: Figura de Plotly
            ratios: Diccionario con los ratios calculados
        """
        fig.update_layout(
            title={
                'text': 'Prisma 3D del Modelo DuPont',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20, 'color': '#2c3e50'}
            },
            scene=dict(
                xaxis=dict(
                    title='Margen Neto (normalizado)',
                    titlefont=dict(color=self.colores_componentes['margen_neto']),
                    tickfont=dict(color=self.colores_componentes['margen_neto']),
                    range=[0, 1.2]
                ),
                yaxis=dict(
                    title='Rotación de Activos (normalizada)',
                    titlefont=dict(color=self.colores_componentes['rotacion_activos']),
                    tickfont=dict(color=self.colores_componentes['rotacion_activos']),
                    range=[0, 1.2]
                ),
                zaxis=dict(
                    title='Apalancamiento Financiero (normalizado)',
                    titlefont=dict(color=self.colores_componentes['apalancamiento']),
                    tickfont=dict(color=self.colores_componentes['apalancamiento']),
                    range=[0, 1.2]
                ),
                bgcolor='rgba(240, 240, 240, 0.1)',
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.5)
                )
            ),
            width=800,
            height=600,
            margin=dict(l=0, r=0, b=0, t=50),
            showlegend=True,
            legend=dict(
                x=0.02,
                y=0.98,
                bgcolor='rgba(255, 255, 255, 0.8)',
                bordercolor='rgba(0, 0, 0, 0.2)',
                borderwidth=1
            )
        )


def mostrar_visualizacion_3d(calculadora):
    """
    Función principal para mostrar la visualización 3D del prisma ROE.
    
    Args:
        calculadora (CalculadoraRatiosDuPont): Instancia con los ratios calculados
    """
    st.subheader("🎯 Visualización 3D del Prisma ROE")
    st.markdown("""
    Esta visualización representa gráficamente cómo se combinan los tres componentes 
    del modelo DuPont para determinar el ROE. El **volumen del prisma** es proporcional 
    al ROE calculado.
    """)
    
    # Crear el visualizador
    visualizador = VisualizadorPrismaROE()
    
    # Generar la figura 3D
    fig = visualizador.crear_prisma_roe(calculadora)
    
    # Mostrar la figura
    st.plotly_chart(fig, use_container_width=True)
    
    # Información adicional sobre la interpretación
    with st.expander("📖 ¿Cómo interpretar el Prisma 3D?", expanded=False):
        st.markdown("""
        ### Interpretación del Prisma 3D:
        
        **🔵 Eje X (Margen Neto)**: Representa la eficiencia en la generación de utilidades.
        - Un prisma más ancho indica mayor margen de rentabilidad.
        
        **🟠 Eje Y (Rotación de Activos)**: Representa la eficiencia en el uso de activos.
        - Un prisma más profundo indica mejor utilización de los activos.
        
        **🟢 Eje Z (Apalancamiento Financiero)**: Representa el uso de deuda.
        - Un prisma más alto indica mayor apalancamiento (y mayor riesgo).
        
        **🔴 Punto ROE**: El punto rojo muestra la combinación exacta de los tres factores.
        
        **📦 Volumen del Prisma**: Es proporcional al ROE total.
        - Un prisma más grande = mayor ROE
        - Un prisma más pequeño = menor ROE
        
        ### Consejos de Interpretación:
        - **Prisma equilibrado**: Los tres componentes contribuyen de manera balanceada
        - **Prisma alargado**: Un componente domina sobre los otros
        - **Prisma pequeño**: Todos los componentes son bajos
        - **Prisma grande**: Todos los componentes son altos
        """)
    
    # Mostrar valores actuales
    ratios = calculadora.obtener_todos_los_ratios()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Margen Neto", f"{ratios['margen_neto']:.2f}%")
    with col2:
        st.metric("Rotación de Activos", f"{ratios['rotacion_activos']:.2f}x")
    with col3:
        st.metric("Apalancamiento", f"{ratios['apalancamiento_financiero']:.2f}x")
    with col4:
        st.metric("ROE Total", f"{ratios['roe']:.2f}%")
