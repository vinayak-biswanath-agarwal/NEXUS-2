import streamlit as st

from components.kpi_cards import KPICards
from components.executive_dashboard import ExecutiveDashboard
from components.charts import Charts
from components.ai_insights import AIInsights
from utils.metrics import Metrics


def show(df):

    metrics = Metrics(df)

    cards = KPICards(metrics)

    cards.executive()

    st.divider()

    cards.executive_summary()

    st.divider()

    executive = ExecutiveDashboard(metrics)

    executive.show()

    st.divider()

    charts = Charts(df)

    c1, c2 = st.columns(2)

    with c1:

        charts.work_item_types()

    with c2:

        charts.state_distribution()

    st.divider()

    c3, c4 = st.columns(2)

    with c3:

        charts.area_distribution()

    with c4:

        charts.iteration_distribution()

    st.divider()

    charts.assignee_distribution()

    st.divider()

    ai = AIInsights(metrics)

    ai.show()