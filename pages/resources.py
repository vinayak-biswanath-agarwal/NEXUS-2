import streamlit as st
import pandas as pd
import plotly.express as px

from utils.metrics import Metrics


def show(df):

    metrics = Metrics(df)

    st.title("👥 Resource Intelligence Dashboard")

    st.caption("Team Capacity & Workload Analytics")

    st.divider()

    # ---------------------------------------
    # Clean Assigned To
    # ---------------------------------------

    data = df.copy()

    data["Assigned To"] = (
        data["Assigned To"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    assigned = data[data["Assigned To"] != ""]

    # ---------------------------------------
    # KPI Row
    # ---------------------------------------

    engineers = assigned["Assigned To"].nunique()

    unassigned = len(data[data["Assigned To"] == ""])

    avg_work = round(len(assigned) / engineers, 1) if engineers else 0

    story_points = 0

    if "Story Points" in assigned.columns:

        story_points = pd.to_numeric(
            assigned["Story Points"],
            errors="coerce"
        ).fillna(0).sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("👨‍💻 Engineers", engineers)

    c2.metric("📦 Assigned Work", len(assigned))

    c3.metric("⚠ Unassigned", unassigned)

    c4.metric("📝 Story Points", round(story_points, 1))

    st.divider()

    # ---------------------------------------
    # Workload
    # ---------------------------------------

    workload = (

        assigned["Assigned To"]

        .value_counts()

        .reset_index()

    )

    workload.columns = [

        "Engineer",

        "Work Items"

    ]

    workload["Status"] = workload["Work Items"].apply(

        lambda x:
        "High"

        if x > avg_work * 1.5

        else "Balanced"

        if x >= avg_work * 0.75

        else "Low"

    )

    left, right = st.columns(2)

    with left:

        st.subheader("Workload Distribution")

        fig = px.bar(

            workload,

            x="Engineer",

            y="Work Items",

            color="Status",

            text="Work Items"

        )

        st.plotly_chart(

            fig,

            width="stretch"

        )

    with right:

        st.subheader("Engineer Distribution")

        fig = px.pie(

            workload,

            names="Engineer",

            values="Work Items",

            hole=.55

        )

        st.plotly_chart(

            fig,

            width="stretch"

        )

    st.divider()

    # ---------------------------------------
    # Workload Table
    # ---------------------------------------

    st.subheader("📋 Team Workload")

    st.dataframe(

        workload,

        width="stretch",

        hide_index=True

    )

    st.divider()

    # ---------------------------------------
    # Top Contributors
    # ---------------------------------------

    st.subheader("🏆 Top Contributors")

    st.dataframe(

        workload.sort_values(

            "Work Items",

            ascending=False

        ).head(10),

        width="stretch",

        hide_index=True

    )

    st.divider()

    # ---------------------------------------
    # AI Recommendations
    # ---------------------------------------

    st.subheader("🤖 Resource Insights")

    overloaded = len(

        workload[

            workload["Status"] == "High"

        ]

    )

    underloaded = len(

        workload[

            workload["Status"] == "Low"

        ]

    )

    if overloaded:

        st.warning(

            f"{overloaded} engineers appear overloaded."

        )

    else:

        st.success(

            "No overloaded engineers detected."

        )

    if underloaded:

        st.info(

            f"{underloaded} engineers have spare capacity."

        )

    else:

        st.success(

            "No underutilized engineers detected."

        )

    st.info(

        f"Average workload per engineer is **{avg_work}** work items."

    )

    st.info(

        "Consider balancing work across the team to reduce delivery risk."

    )