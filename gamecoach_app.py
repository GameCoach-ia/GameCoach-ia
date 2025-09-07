# gamecoach_app.py
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="GameCoach.ia - Fortnite", layout="wide", page_icon="🎮")
st.title("🎮 GameCoach.ia — Coach para Fortnite (MVP)")
st.markdown("Entrenador legal y educativo para mejorar en Fortnite. Planes, rutinas y checklist de VOD.")

# ---------- Sidebar: perfil ----------
st.sidebar.header("Tu perfil")
game = st.sidebar.selectbox("Juego (MVP):", ["Fortnite (BR)"])
rank = st.sidebar.selectbox("Rango actual:", ["Nuevo","Bronce","Plata","Oro","Platino","Diamante+"])
hours = st.sidebar.slider("Horas/semana disponibles:", 1, 40, 8)
goals = st.sidebar.multiselect("Objetivos (elige hasta 3):",
                               ["Mejorar puntería","Mejorar posicionamiento","Rotaciones / Macro","Aim consistency","Decisiones bajo presión","Subir rango"],
                               default=["Mejorar puntería","Subir rango"])
st.sidebar.markdown("---")
st.sidebar.header("Herramientas")
st.sidebar.markdown("[Únete al Discord](https://discord.gg/tu-enlace-aqui)")
st.sidebar.markdown("[Deja feedback](https://forms.gle/tu-form-aqui)")

# ---------- Plan semanal ----------
def gen_week_plan(hours_per_week:int, goals:list):
    daily_minutes = max(30, min(240, int(hours_per_week * 60 / 5)))
    blocks = []
    if "Mejorar puntería" in goals or "Aim consistency" in goals:
        blocks.append(("Entreno Aim (Creativo/Aim trainer)", int(daily_minutes * 0.4)))
    if "Mejorar posicionamiento" in goals or "Rotaciones / Macro" in goals:
        blocks.append(("Rotaciones / Macro / Scrims", int(daily_minutes * 0.3)))
    blocks.append(("Ranked / Pubs prácticos", max(20, daily_minutes - sum(t for _, t in blocks))))
    days = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    plan = []
    for i,d in enumerate(days):
        if i < 5:
            entry = {"Día": d}
            for name,mins in blocks:
                entry[name] = mins
            plan.append(entry)
        else:
            plan.append({"Día": d, "Review VOD / Repaso (min)": int(daily_minutes*0.4), "Jugar libre (min)": int(daily_minutes*0.6)})
    return pd.DataFrame(plan)

st.subheader("📅 Plan de 7 días personalizado")
if st.button("Generar plan semanal"):
    df_plan = gen_week_plan(hours, goals)
    st.dataframe(df_plan, use_container_width=True)

# ---------- Rutinas específicas para Fortnite ----------
st.subheader("🧪 Rutinas y checklist para Fortnite (por sesión)")
st.markdown("**Mini-sesión de 60 min sugerida:** 10' creativo (edición) + 20' aim maps + 20' pubs/práctica + 10' revisión VOD corta.")
fortnite_checklist = [
    "Drop seguro vs. hot drop (elige 2 spots y repite)",
    "Ruta de loot: prioridad AR/SMG + curas + movilidad",
    "Coger altura y cobertura dura antes del mid game",
    "Evitar peleas 3rd-party sin recursos",
    "Controlar la zona final: rotar con cobertura"
]
st.write("- " + "\n- ".join(fortnite_checklist))

# ---------- VOD tagging ----------
st.subheader("📼 VOD Review (sube clip corto .mp4/.mov) - Manual/Guiado")
vod = st.file_uploader("Sube un clip 20–60s para organizar tags (demo)", type=["mp4","mov"])
if vod is not None:
    st.success("Clip subido — aún no hay análisis automático. Usa la checklist y etiqueta manualmente.")
    tag_input = st.text_input("Añade tus etiquetas separadas por comas (ej: endgame,rotación,tilt)")
    if st.button("Guardar etiquetas"):
        st.success("Etiquetas guardadas (demo). Revisa tu Discord para feedback.")

# ---------- Plan de progresión ----------
st.subheader("📈 Estimación de progreso")
target = st.selectbox("Meta de rango:", ["Bronce","Plata","Oro","Platino","Diamante+"])
def estimate_weeks(current, target, hours_per_week):
    order = ["Nuevo","Bronce","Plata","Oro","Platino","Diamante+"]
    i_current = order.index(current)
    i_target = order.index(target)
    gap = max(0, i_target - i_current)
    weeks = max(1, int((gap * 20) / max(1, hours_per_week)))
    return weeks

if st.button("Calcular semanas aproximadas"):
    w = estimate_weeks(rank, target, hours)
    st.info(f"Con {hours}h/semana, podrías tardar ~{w} semanas (estimación).")

st.markdown("---")
st.caption("Nota: App educativa. Sin hacks ni overlays. Cumple ToS.")
