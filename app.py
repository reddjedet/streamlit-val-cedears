import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Título de la aplicación
st.title("📈 Análisis de Valoración de Cedear/Acción")

# Carga de los datos
@st.cache_data
def load_data(file_path):
    """
    Carga los datos desde un archivo CSV.
    """
    df = pd.read_csv(file_path)
    return df

try:
    df = load_data("data.csv")

    # Crea un gráfico de figuras sin subplots iniciales
    fig = go.Figure()

    # Añade el OCF por Acción (eje Y principal)
    fig.add_trace(
        go.Scatter(
            x=df["trimestre"],
            y=df["ocf_por_accion"],
            name="OCF por Acción",
            mode="lines+markers",
            line=dict(color="purple"),
        )
    )

    # Añade el Precio de la Acción (eje Y secundario)
    fig.add_trace(
        go.Scatter(
            x=df["trimestre"],
            y=df["precio_de_la_accion"],
            name="Precio de la Acción",
            mode="lines+markers",
            line=dict(color="goldenrod"),
            yaxis="y2",
        )
    )

    # Añade el Buyback Yield (tercer eje Y)
    fig.add_trace(
        go.Scatter(
            x=df["trimestre"],
            y=df["buyback_yield"],
            name="Buyback Yield (%)",
            mode="lines+markers",
            line=dict(color="deepskyblue", dash="dot"),
            yaxis="y3",
        )
    )

    # Configura los ejes y títulos, incluyendo la rotación del eje X
    fig.update_layout(
        # Línea modificada para añadir el nombre del cedear
        title_text="Evolución de Métricas de la Acción: $GOOGL",
        xaxis=dict(
            domain=[0.1, 0.9],
            tickangle=45,
        ),
        yaxis=dict(
            title="OCF por Acción",
            title_font=dict(color="purple"),
            tickfont=dict(color="purple"),
            side="left",
            position=0.0,
        ),
        yaxis2=dict(
            title="Precio de la Acción",
            title_font=dict(color="goldenrod"),
            tickfont=dict(color="goldenrod"),
            anchor="x",
            overlaying="y",
            side="right",
            position=1.0,
        ),
        yaxis3=dict(
            title="Buyback Yield (%)",
            title_font=dict(color="deepskyblue"),
            tickfont=dict(color="deepskyblue"),
            anchor="free",
            overlaying="y",
            side="right",
            position=0.95,
        ),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode="x unified",
    )

    # Muestra el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Muestra los datos sin procesar
    if st.checkbox("Mostrar datos sin procesar"):
        st.subheader("Datos sin procesar")
        st.dataframe(df)

except FileNotFoundError:
    st.error(
        "El archivo `data.csv` no se encontró. Asegúrate de que está en el mismo directorio."
    )
except Exception as e:
    st.error(f"Ocurrió un error: {e}")
