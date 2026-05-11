# Análisis de Datos Climáticos Globales

## Descripción del Proyecto

Este proyecto forma parte del Trabajo Práctico de la materia Organización Empresarial de la Tecnicatura Universitaria en Programación (UTN). Se desarrolló bajo el paradigma de Aprendizaje Basado en Problemas (ABP), aplicando herramientas de control de versiones, gestión de tareas y análisis de datos.

## Integrantes

| Nombre | Rol |
|--------|-----|
| Agustin Fassi | P1 - Líder y Organizador (Hugo) |
| Agustin Fassi | P2 - Desarrollador Técnico (Paco) |
| Agustin Fassi | P3 - Revisor y QA (Luis) |

## Escenario Elegido

**Escenario A – Análisis de Datos Climáticos**

Se procesaron datos históricos de temperatura global para generar indicadores estadísticos básicos y visualizar la evolución de las anomalías de temperatura a lo largo del tiempo.

## Dataset Utilizado

- **Fuente:** GCAG (Global Climate at a Glance) vía datahub.io
- **URL:** https://datahub.io/core/global-temp
- **Formato:** CSV
- **Cobertura temporal:** 1850 - actualidad
- **Licencia:** Dominio público

## Estructura del Repositorio

```
analisis-climatico-tup/
│
├── datos/
│   └── dataset.csv
├── scripts/
│   └── analisis_datos.py
├── resultados/
│   └── grafico_temperatura.png
├── README.md
└── .gitignore
```

## Indicadores Generados

| Indicador | Valor |
|-----------|-------|
| Temperatura promedio (anomalía) | -0.0650 °C |
| Temperatura máxima registrada | 1.1755 °C |
| Temperatura mínima registrada | -0.5975 °C |

## Instrucciones para Ejecutar el Script

1. Clonar el repositorio:

```
git clone https://github.com/agusfassi/analisis-climatico-tup.git
```

2. Abrir Google Colab y montar el entorno

3. Descargar el dataset en la carpeta /datos:

```python
import urllib.request
urllib.request.urlretrieve('https://datahub.io/core/global-temp/r/annual.csv', 'datos/dataset.csv')
```

4. Ejecutar el script:

```python
exec(open('scripts/analisis_datos.py').read())
```

## Gestión del Proyecto

Las tareas fueron gestionadas mediante **Jira** bajo el proyecto *Análisis Climático TUP*, utilizando Conventional Commits para garantizar la trazabilidad entre cada tarea y su correspondiente cambio en el repositorio.

| Issue | Descripción |
|-------|-------------|
| SCRUM-5 | Inicialización del repositorio y estructura de carpetas |
| SCRUM-6 | Desarrollo del script de análisis climático |
| SCRUM-7 | Revisión, documentación y merge final |

## Tecnologías Utilizadas

- Python 3
- Pandas
- Matplotlib
- Git / GitHub
- Google Colab
- Jira
