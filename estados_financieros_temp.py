"""
MÃ³dulo para la generaciÃ³n de Estados Financieros Simplificados.
Implementa la Funcionalidad 3 del proyecto ROE DuPont Interactivo.

Este mÃ³dulo genera visualizaciones de:
- Estado de Resultados simplificado
- Balance General simplificado
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from calculadora_ratios import CalculadoraRatiosDuPont


class GeneradorEstadosFinancieros:
    """
    Clase para generar estados financieros simplificados.
    
    Genera visualizaciones de:
    - Estado de Resultados (Ventas, Gastos, Utilidad Neta)
    - Balance General (Activos, Deuda, Patrimonio)
    """
    
    def __init__(self):
        """Inicializa el generador de estados financieros."""
        self.colores = {
            'ventas': '#87CEEB',        # Celeste
            'gastos': '#FFB6C1',        # Rosado
            'utilidad_neta': '#98FB98', # Verde suave
            'activos': '#90EE90',       # Verde
            'deuda': '#FFB6C1',         # Rosado
            'patrimonio': '#87CEEB'     # Celeste
        }
    
    def calcular_estado_resultados(self, calculadora):
        """
        Calcula los valores del Estado de Resultados.
        
        Args:
            calculadora (CalculadoraRatiosDuPont): Instancia con los ratios calculados
            
        Returns:
            dict: Diccionario con los valores del estado de resultados
        """
        ventas = calculadora.ventas
        utilidad_neta = calculadora.utilidad_neta
        gastos = ventas - utilidad_neta  # Gastos = Ventas - Utilidad Neta
        
        return {
            'ventas': ventas,
            'gastos': gastos,
            'utilidad_neta': utilidad_neta
        }
    
    def calcular_balance_general(self, calculadora):
        """
        Calcula los valores del Balance General.
        
        Args:
            calculadora (CalculadoraRatiosDuPont): Instancia con los ratios calculados
            
        Returns:
            dict: Diccionario con los valores del balance general
        """
        activos = calculadora.activos_promedio
        patrimonio = calculadora.patrimonio_promedio
        deuda = activos - patrimonio  # Deuda = Activos - Patrimonio
        
        return {
            'activos': activos,
            'deuda': deuda,
            'patrimonio': patrimonio
        }
    
    def crear_grafico_estado_resultados(self, calculadora):
        """
        Crea el grÃ¡fico del Estado de Resultados.
        
        Args:
            calculadora (CalculadoraRatiosDuPont): Instancia con los ratios calculados
            
        Returns:
            plotly.graph_objects.Figure: GrÃ¡fico de barras horizontal
        """
        # Calcular valores
        valores = self.calcular_estado_resultados(calculadora)
        
        # Preparar datos para el grÃ¡fico en el orden especÃ­fico
        categorias = ['Utilidad Neta', 'Gastos', 'Ventas']  # Orden invertido para visualización
        valores_lista = [valores['ventas'], valores['gastos'], valores['utilidad_neta']]
        colores_lista = [self.colores['ventas'], self.colores['gastos'], self.colores['utilidad_neta']]
        
        # Crear grÃ¡fico de barras horizontal
        fig = go.Figure(data=[
            go.Bar(
                y=categorias,
                x=valores_lista,
                orientation='h',
                marker=dict(color=colores_lista),
                text=[f"${val:,.0f}" for val in valores_lista],
                textposition='auto',
                hovertemplate='<b>%{y}</b><br>Valor: $%{x:,.0f}<br><extra></extra>'
            )
        ])
        
        # Configurar layout
        fig.update_layout(
            title='Estado de Resultados Simplificado',
            xaxis_title='Valores ($)',
            yaxis_title='',
            height=300,
            margin=dict(l=0, r=0, b=0, t=50),
            showlegend=False,
            xaxis=dict(showgrid=True, gridcolor='rgba(128,128,128,0.2)'),
            yaxis=dict(showgrid=False, categoryorder='array', categoryarray=categorias)
        )
        
        return fig
    
    def crear_grafico_balance_general(self, calculadora):
        """
        Crea el grÃ¡fico del Balance General.
        
        Args:
            calculadora (CalculadoraRatiosDuPont): Instancia con los ratios calculados
            
        Returns:
            plotly.graph_objects.Figure: GrÃ¡fico apilado
        """
        # Calcular valores
        valores = self.calcular_balance_general(calculadora)
        
        # Crear grÃ¡fico apilado con dos barras
        fig = go.Figure()
        
        # Primera barra - Activos (verde)
        fig.add_trace(go.Bar(
            name='Activos',
            x=['Activos'],
            y=[valores['activos']],
            marker=dict(color=self.colores['activos']),
            text=f"${valores['activos']:,.0f}",
            textposition='auto',
            hovertemplate='<b>Activos</b><br>Valor: $%{y:,.0f}<br><extra></extra>'
        ))
        
        # Segunda barra - Patrimonio (celeste) en la base y Deuda (rosado) arriba
        fig.add_trace(go.Bar(
            name='Patrimonio',
            x=['Deuda + Patrimonio'],
            y=[valores['patrimonio']],
            marker=dict(color=self.colores['patrimonio']),
            text=f"${valores['patrimonio']:,.0f}",
            textposition='inside',
            hovertemplate='<b>Patrimonio</b><br>Valor: $%{y:,.0f}<br><extra></extra>'
        ))
        
        fig.add_trace(go.Bar(
            name='Deuda',
            x=['Deuda + Patrimonio'],
            y=[valores['deuda']],
            marker=dict(color=self.colores['deuda']),
            text=f"${valores['deuda']:,.0f}",
            textposition='auto',
            hovertemplate='<b>Deuda</b><br>Valor: $%{y:,.0f}<br><extra></extra>'
        ))
        
        # Configurar layout
        fig.update_layout(
            title='Balance General Simplificado',
            xaxis_title='',
            yaxis_title='Valores ($)',
            height=300,
            margin=dict(l=0, r=0, b=0, t=50),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(128,128,128,0.2)'),
            barmode='stack',
            bargap=0
        )
        
        return fig


def mostrar_estados_financieros(calculadora):
    """
    FunciÃ³n principal para mostrar los estados financieros simplificados.
    
    Args:
        calculadora (CalculadoraRatiosDuPont): Instancia con los ratios calculados
    """
    st.subheader("ðŸ“Š Estados Financieros Simplificados")
    st.markdown("""
    Estos grÃ¡ficos muestran la coherencia entre los inputs del modelo y los resultados 
    financieros. Los valores se actualizan dinÃ¡micamente con los cambios en las variables de entrada.
    """)
    
    # Crear el generador
    generador = GeneradorEstadosFinancieros()
    
    # Crear dos columnas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ðŸ“ˆ Estado de Resultados")
        fig_er = generador.crear_grafico_estado_resultados(calculadora)
        st.plotly_chart(fig_er, use_container_width=True)
        
        # Mostrar lÃ³gica del estado de resultados
        valores_er = generador.calcular_estado_resultados(calculadora)
        st.info(f"""
        **LÃ³gica contable**: Ventas = Gastos + Utilidad Neta  
        ${valores_er['ventas']:,.0f} = ${valores_er['gastos']:,.0f} + ${valores_er['utilidad_neta']:,.0f}
        """)
    
    with col2:
        st.markdown("### âš–ï¸ Balance General")
        fig_bg = generador.crear_grafico_balance_general(calculadora)
        st.plotly_chart(fig_bg, use_container_width=True)
        
        # Mostrar lÃ³gica del balance general
        valores_bg = generador.calcular_balance_general(calculadora)
        st.info(f"""
        **LÃ³gica contable**: Activos = Deuda + Patrimonio  
        ${valores_bg['activos']:,.0f} = ${valores_bg['deuda']:,.0f} + ${valores_bg['patrimonio']:,.0f}
        """)
    
    # InformaciÃ³n adicional sobre la interpretaciÃ³n
    with st.expander("ðŸ“– Â¿CÃ³mo interpretar los Estados Financieros?", expanded=False):
        st.markdown("""
        ### Estado de Resultados:
        - **Ventas**: Ingresos totales de la empresa
        - **Gastos**: Costos y gastos operativos (Ventas - Utilidad Neta)
        - **Utilidad Neta**: Beneficio despuÃ©s de todos los gastos
        
        ### Balance General:
        - **Activos**: Recursos que posee la empresa
        - **Deuda**: Obligaciones con terceros (Activos - Patrimonio)
        - **Patrimonio**: Capital propio de los accionistas
        
        ### Coherencia del Modelo:
        Los valores mostrados provienen directamente de los inputs del modelo DuPont,
        asegurando que las visualizaciones sean consistentes con los cÃ¡lculos de ratios.
        """)
