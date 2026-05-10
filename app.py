import streamlit as st

from src.parser import load_logs
from src.detector import detect_threats
from src.ai_analyzer import analyze_threat

st.set_page_config(
    page_title="ObscuarAI",
    layout="wide"
)

st.title("🛡️ ObscuraAI")
st.subheader("AI-Powered SOC Analysis Dashboard")

logs = load_logs("data/sample_logs.csv")
threats = detect_threats(logs)

st.metric("Total Logs", len(logs))
st.metric("Detected Threats", len(threats))

st.divider()

st.write("## Detected Threats")

for _, threat in threats.iterrows():

    severity = threat.get("severity", "Unknown")

    if severity.lower() == "critical":
        st.error(f"🚨{threat.get('event_type', 'Unknown Event')}")
    elif severity.lower() == "high":
        st.warning(f"⚠️{threat.get('event_type', 'Unknown Event')}")
    else:
        st.info(f"ℹ️{threat.get('event_type', 'Unknown Event')}")

st.write(f"**User:** {threat.get('username', 'Unknow')}")
st.write(f"**Source IP:** {threat.get('source_ip', 'Unknown')}")
st.write(f"**Severity:** {severity}")

st.write(
    f"**AI Analyst Summary:** "
    f"{analyze_threat(threat)}"
)

st.divider()