# ROE DuPont Interactivo

## 📊 Funcionalidad 1: Cálculo de Ratios Financieros Básicos

Este proyecto implementa una aplicación interactiva para el análisis financiero utilizando el **Modelo DuPont**. La aplicación permite calcular y visualizar los componentes del Return on Equity (ROE) de forma dinámica.

## 🚀 Características

- **Sliders interactivos** para ajustar variables financieras
- **Cálculo automático** de los ratios del modelo DuPont
- **Visualización en tiempo real** de resultados
- **Interpretación automática** de los indicadores
- **Gráficos dinámicos** con Plotly

## 📋 Requisitos

- Python 3.8 o superior
- Streamlit
- Plotly
- Pandas
- NumPy

## 🛠️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone [url-del-repositorio]
   cd roe-dupont
   ```

2. **Crear entorno virtual**:
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**:
   - Windows: `venv\\Scripts\\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Uso

1. **Ejecutar la aplicación**:
   ```bash
   streamlit run app.py
   ```

2. **Abrir en el navegador**: La aplicación se abrirá automáticamente en `http://localhost:8501`

3. **Ajustar variables**: Usa los sliders para modificar:
   - Utilidad Neta
   - Ventas
   - Activos Promedio
   - Patrimonio Promedio

4. **Observar resultados**: Los ratios se calculan automáticamente y se muestran en tiempo real.
5. **Explorar visualización 3D**: El prisma tridimensional se actualiza dinámicamente con los cambios.

## 📊 Modelo DuPont

El modelo descompone el ROE en tres componentes:

```
ROE = Margen Neto × Rotación de Activos × Apalancamiento Financiero
```

### Componentes:

- **Margen Neto** = Utilidad Neta / Ventas
- **Rotación de Activos** = Ventas / Activos Promedio  
- **Apalancamiento Financiero** = Activos Promedio / Patrimonio Promedio

## 📁 Estructura del Proyecto

```
roe-dupont/
├── app.py                    # Aplicación principal de Streamlit
├── calculadora_ratios.py     # Módulo de cálculo de ratios
├── visualizacion_3d.py       # Módulo de visualización 3D del prisma
├── estados_financieros.py    # Módulo de estados financieros simplificados
├── requirements.txt          # Dependencias del proyecto
├── README.md                # Este archivo
└── documentos/
    └── funcionalidades_proyecto.md  # Especificaciones del proyecto
```

## 🔧 Funcionalidades Implementadas

### ✅ Funcionalidad 1: Cálculo de Ratios Financieros Básicos

- [x] Sliders para 4 variables financieras
- [x] Cálculo automático de Margen Neto
- [x] Cálculo automático de Rotación de Activos
- [x] Cálculo automático de Apalancamiento Financiero
- [x] Cálculo del ROE
- [x] Visualización de resultados en métricas

### ✅ Funcionalidad 2: Visualización 3D del Prisma ROE

- [x] Prisma tridimensional interactivo
- [x] Representación visual de los tres componentes DuPont
- [x] Actualización dinámica con cambios en variables
- [x] Ejes de colores para cada componente
- [x] Etiquetas explicativas y anotaciones
- [x] Punto ROE que muestra la combinación exacta
- [x] Interpretación pedagógica del modelo
- [x] Guía de interpretación expandible

### ✅ Funcionalidad 3: Estados Financieros Simplificados

- [x] Estado de Resultados simplificado con gráfico de barras horizontal
- [x] Balance General simplificado con gráfico apilado
- [x] Cálculo dinámico de gastos (Ventas - Utilidad Neta)
- [x] Cálculo dinámico de deuda (Activos - Patrimonio)
- [x] Visualizaciones con colores específicos para cada elemento
- [x] Coherencia contable entre inputs y resultados
- [x] Actualización dinámica con cambios en variables

## 📈 Interpretación de Resultados

### Margen Neto
- **> 10%**: Excelente rentabilidad
- **5-10%**: Rentabilidad aceptable
- **< 5%**: Rentabilidad baja

### Rotación de Activos
- **> 1.5x**: Uso eficiente de activos
- **1.0-1.5x**: Uso moderado
- **< 1.0x**: Baja eficiencia

### Apalancamiento Financiero
- **> 2.0x**: Alto apalancamiento (mayor riesgo)
- **1.5-2.0x**: Apalancamiento moderado
- **< 1.5x**: Bajo apalancamiento (menor riesgo)

### ROE
- **> 15%**: Excelente rentabilidad del patrimonio
- **10-15%**: Buena rentabilidad
- **5-10%**: Rentabilidad moderada
- **< 5%**: Baja rentabilidad

## 🎯 Visualización 3D del Prisma ROE

La **Funcionalidad 2** introduce una visualización tridimensional que representa gráficamente la descomposición del ROE:

### Características del Prisma 3D:

- **🔵 Eje X (Margen Neto)**: Ancho del prisma representa la eficiencia en generación de utilidades
- **🟠 Eje Y (Rotación de Activos)**: Profundidad del prisma representa la eficiencia en uso de activos  
- **🟢 Eje Z (Apalancamiento Financiero)**: Altura del prisma representa el uso de deuda
- **🔴 Punto ROE**: Muestra la combinación exacta de los tres factores
- **📦 Volumen**: Es proporcional al ROE total calculado

### Interpretación Visual:

- **Prisma equilibrado**: Los tres componentes contribuyen de manera balanceada
- **Prisma alargado**: Un componente domina sobre los otros
- **Prisma pequeño**: Todos los componentes son bajos
- **Prisma grande**: Todos los componentes son altos

### Funcionalidades Interactivas:

- **Actualización dinámica**: El prisma se modifica en tiempo real al cambiar las variables
- **Etiquetas explicativas**: Anotaciones que muestran los valores exactos
- **Ejes de colores**: Cada componente tiene su color distintivo
- **Guía de interpretación**: Sección expandible con consejos pedagógicos

## 📊 Estados Financieros Simplificados

La **Funcionalidad 3** complementa el análisis con un contexto contable básico:

### Estado de Resultados:
- **📈 Gráfico de barras horizontal** con tres elementos:
  - 🔵 **Ventas** (celeste): Ingresos totales
  - 🌸 **Gastos** (rosado): Costos operativos (calculados como Ventas - Utilidad Neta)
  - 🟢 **Utilidad Neta** (verde suave): Beneficio final

### Balance General:
- **⚖️ Gráfico apilado** que muestra la estructura financiera:
  - 🟢 **Activos** (verde): Recursos de la empresa
  - 🌸 **Deuda** (rosado): Obligaciones con terceros (calculada como Activos - Patrimonio)
  - 🔵 **Patrimonio** (celeste): Capital propio

### Características:
- **Cálculos dinámicos**: Los valores se actualizan automáticamente con los inputs
- **Coherencia contable**: Ventas = Gastos + Utilidad Neta; Activos = Deuda + Patrimonio
- **Visualización clara**: Dos columnas con gráficos interactivos
- **Colores consistentes**: Esquema de colores coherente en toda la aplicación

## 🤝 Contribución

Este proyecto forma parte de un enfoque pedagógico para enseñar análisis financiero y desarrollo de aplicaciones con Python.

## 📄 Licencia

Este proyecto es de uso educativo y está disponible bajo licencia MIT.
