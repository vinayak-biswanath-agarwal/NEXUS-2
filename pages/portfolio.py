import streamlit as st
import plotly.express as px

from utils.metrics import Metrics


def show(df):

    metrics = Metrics(df)

    st.title("📁 Portfolio Analytics")

    st.caption("Executive Portfolio Health Dashboard")

    st.divider()

    # -------------------------------------------------
    # KPI Row
    # -------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📁 Epics", metrics.total_epics())
    c2.metric("⭐ Features", metrics.total_features())
    c3.metric("📋 Stories", metrics.total_user_stories())
    c4.metric("📦 Work Items", metrics.total_work_items())

    st.divider()

    # -------------------------------------------------
    # Charts
    # -------------------------------------------------

    left, right = st.columns(2)

    with left:

        st.subheader("Work Item Distribution")

        chart = (
            df["Work Item Type"]
            .value_counts()
            .reset_index()
        )

        chart.columns = ["Type", "Count"]

        fig = px.pie(
            chart,
            names="Type",
            values="Count",
            hole=0.55
        )

        st.plotly_chart(fig, width="stretch")

    with right:

        st.subheader("State Distribution")

        chart = (
            df["State"]
            .value_counts()
            .reset_index()
        )

        chart.columns = ["State", "Count"]

        fig = px.bar(
            chart,
            x="State",
            y="Count",
            text="Count"
        )

        st.plotly_chart(fig, width="stretch")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Area Path")

        chart = (
            df["Area Path"]
            .value_counts()
            .reset_index()
        )

        chart.columns = ["Area", "Count"]

        fig = px.treemap(
            chart,
            path=["Area"],
            values="Count"
        )

        st.plotly_chart(fig, width="stretch")

    with right:

        st.subheader("Iteration Distribution")

        chart = (
            df["Iteration Path"]
            .value_counts()
            .reset_index()
        )

        chart.columns = ["Iteration", "Count"]

        fig = px.bar(
            chart,
            x="Iteration",
            y="Count",
            text="Count"
        )

        st.plotly_chart(fig, width="stretch")

    st.divider()

    # -------------------------------------------------
    # Statistics Table
    # -------------------------------------------------

    st.subheader("📊 Portfolio Statistics")

    stats = {
        "Metric": [
            "Total Work Items",
            "Total Epics",
            "Total Features",
            "Total Stories",
            "Completed",
            "Blocked",
            "Story Points"
        ],
        "Value": [
            metrics.total_work_items(),
            metrics.total_epics(),
            metrics.total_features(),
            metrics.total_user_stories(),
            metrics.completed_items(),
            metrics.blocked_items(),
            metrics.total_story_points()
        ]
    }

    st.dataframe(
        stats,
        width="stretch",
        hide_index=True
    )

    st.divider()

    # -------------------------------------------------
    # AI Summary
    # -------------------------------------------------

    st.subheader("🤖 Portfolio Insights")

    st.success(
        f"""
• Portfolio contains **{metrics.total_epics()}** Epics.

• Portfolio contains **{metrics.total_features()}** Features.

• Portfolio contains **{metrics.total_user_stories()}** User Stories.

• **{metrics.completed_items()}** work items are completed.

• **{metrics.blocked_items()}** work items require attention.

• Delivery Health: **{metrics.delivery_health()}**
"""
    )