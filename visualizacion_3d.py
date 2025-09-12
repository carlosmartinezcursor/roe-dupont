"""
Módulo simple para la visualización 3D del Prisma ROE.
Implementa la Funcionalidad 2 del proyecto ROE DuPont Interactivo.
"""

import streamlit as st
import plotly.graph_objects as go
from calculadora_ratios import CalculadoraRatiosDuPont


def crear_prisma_roe_simple(calculadora):
    """
    Crea un prisma 3D simple que representa la descomposición del ROE.
    
    Args:
        calculadora (CalculadoraRatiosDuPont): Instancia con los ratios calculados
        
    Returns:
        plotly.graph_objects.Figure: Figura 3D del prisma ROE
    """
    # Obtener los ratios calculados
    ratios = calculadora.obtener_todos_los_ratios()
    
    # Normalizar los valores para la visualización 3D (escalas simples)
    margen_norm = min(ratios['margen_neto'] / 20, 1.0)  # Máximo 20%
    rotacion_norm = min(ratios['rotacion_activos'] / 3, 1.0)  # Máximo 3x
    apalancamiento_norm = min(ratios['apalancamiento_financiero'] / 4, 1.0)  # Máximo 4x
    
    # Crear la figura 3D
    fig = go.Figure()
    
    # Agregar el prisma principal (cubo)
    fig.add_trace(go.Mesh3d(
        x=[0, margen_norm, margen_norm, 0, 0, margen_norm, margen_norm, 0],
        y=[0, 0, rotacion_norm, rotacion_norm, 0, 0, rotacion_norm, rotacion_norm],
        z=[0, 0, 0, 0, apalancamiento_norm, apalancamiento_norm, apalancamiento_norm, apalancamiento_norm],
        i=[0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 5, 4, 2, 3, 7, 6, 0, 3, 7, 4, 1, 2, 6, 5],
        j=[1, 2, 3, 0, 5, 6, 7, 4, 1, 5, 4, 0, 3, 7, 6, 2, 3, 0, 4, 7, 2, 6, 5, 1],
        k=[2, 3, 0, 1, 6, 7, 4, 5, 5, 4, 0, 1, 7, 6, 2, 3, 7, 4, 0, 3, 6, 5, 1, 2],
        opacity=0.7,
        color='lightblue',
        name='Prisma ROE'
    ))
    
    # Agregar ejes simples
    fig.add_trace(go.Scatter3d(
        x=[0, margen_norm], y=[0, 0], z=[0, 0],
        mode='lines+markers',
        line=dict(color='blue', width=6),
        marker=dict(size=4, color='blue'),
        name='Margen Neto'
    ))
    
    fig.add_trace(go.Scatter3d(
        x=[0, 0], y=[0, rotacion_norm], z=[0, 0],
        mode='lines+markers',
        line=dict(color='orange', width=6),
        marker=dict(size=4, color='orange'),
        name='Rotación de Activos'
    ))
    
    fig.add_trace(go.Scatter3d(
        x=[0, 0], y=[0, 0], z=[0, apalancamiento_norm],
        mode='lines+markers',
        line=dict(color='green', width=6),
        marker=dict(size=4, color='green'),
        name='Apalancamiento Financiero'
    ))
    
    
    # Obtener los ratios para la leyenda
    ratios = calculadora.obtener_todos_los_ratios()
    
    # Configuración simple del layout
    fig.update_layout(
        title='Prisma 3D del Modelo DuPont',
        scene=dict(
            xaxis=dict(title='Margen Neto', range=[0, 1.2]),
            yaxis=dict(title='Rotación de Activos', range=[0, 1.2]),
            zaxis=dict(title='Apalancamiento Financiero', range=[0, 1.2])
        ),
        width=800,
        height=600,
        showlegend=True,
        legend=dict(
            x=1.02,
            y=1,
            xanchor='left',
            yanchor='top',
            bgcolor='rgba(255, 255, 255, 0.8)',
            bordercolor='rgba(0, 0, 0, 0.2)',
            borderwidth=1,
            font=dict(size=14)
        )
    )
    
    # Actualizar los nombres de las leyendas con los valores
    fig.update_traces(
        name=f"Margen Neto: {ratios['margen_neto']:.1f}%",
        selector=dict(name="Margen Neto")
    )
    fig.update_traces(
        name=f"Rotación de Activos: {ratios['rotacion_activos']:.2f}",
        selector=dict(name="Rotación de Activos")
    )
    fig.update_traces(
        name=f"Apalancamiento: {ratios['apalancamiento_financiero']:.2f}",
        selector=dict(name="Apalancamiento Financiero")
    )
    fig.update_traces(
        name=f"ROE (volumen): {ratios['roe']:.1f}%",
        selector=dict(name="Prisma ROE")
    )
    
    return fig


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
    
    # Generar la figura 3D
    fig = crear_prisma_roe_simple(calculadora)
    
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
    