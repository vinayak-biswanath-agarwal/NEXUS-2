import streamlit as st
import plotly.express as px

from utils.metrics import Metrics


def show(df):

    metrics = Metrics(df)

    st.title("🚀 Sprint Intelligence")

    st.caption("Sprint Delivery Dashboard")

    st.divider()

    # ---------------------------------------------------
    # KPI Row
    # ---------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📦 Work Items", metrics.total_work_items())
    c2.metric("📋 Stories", metrics.total_user_stories())
    c3.metric("🚫 Blocked", metrics.blocked_items())
    c4.metric("✅ Completed", metrics.completed_items())

    st.divider()

    # ---------------------------------------------------
    # Sprint Progress
    # ---------------------------------------------------

    completed = metrics.completed_items()

    total = metrics.total_work_items()

    progress = 0

    if total > 0:
        progress = round(completed / total * 100)

    st.subheader("Sprint Progress")

    st.progress(progress / 100)

    st.metric("Completion", f"{progress}%")

    st.divider()

    # ---------------------------------------------------
    # State Distribution
    # ---------------------------------------------------

    left, right = st.columns(2)

    with left:

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

    with right:

        st.subheader("Sprint Work")

        chart = (
            df["Iteration Path"]
            .value_counts()
            .reset_index()
        )

        chart.columns = ["Iteration", "Count"]

        fig = px.pie(
            chart,
            names="Iteration",
            values="Count",
            hole=0.55
        )

        st.plotly_chart(fig, width="stretch")

    st.divider()

    # ---------------------------------------------------
    # Team Workload
    # ---------------------------------------------------

    st.subheader("👥 Team Workload")

    workload = (
        df["Assigned To"]
        .value_counts()
        .reset_index()
    )

    workload.columns = [
        "Engineer",
        "Work Items"
    ]

    fig = px.bar(
        workload,
        x="Engineer",
        y="Work Items",
        text="Work Items"
    )

    st.plotly_chart(fig, width="stretch")

    st.divider()

    # ---------------------------------------------------
    # Sprint Summary
    # ---------------------------------------------------

    st.subheader("🤖 Sprint Intelligence")

    if progress >= 90:

        st.success(
            "Sprint execution is excellent. Delivery confidence is HIGH."
        )

    elif progress >= 70:

        st.warning(
            "Sprint is progressing well. Monitor blocked work items."
        )

    else:

        st.error(
            "Sprint completion is behind plan. Immediate attention recommended."
        )

    st.info(f"""

Current Sprint Completion : **{progress}%**

Completed Work Items : **{completed}**

Remaining Work Items : **{total-completed}**

Blocked Items : **{metrics.blocked_items()}**

Story Points : **{metrics.total_story_points()}**

""")