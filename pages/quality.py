import streamlit as st
import pandas as pd
import plotly.express as px

from utils.metrics import Metrics


def show(df):

    metrics = Metrics(df)

    st.title("🚨 Risk Intelligence Dashboard")

    st.caption("Executive Delivery Risk Analytics")

    st.divider()

    # -----------------------------------------
    # Risk Calculations
    # -----------------------------------------

    blocked = df[
        df["State"].astype(str)
        .str.contains("Blocked", case=False, na=False)
    ]

    unassigned = df[
        df["Assigned To"].astype(str).str.strip() == ""
    ]

    no_story_points = pd.DataFrame()

    if "Story Points" in df.columns:

        no_story_points = df[
            pd.to_numeric(
                df["Story Points"],
                errors="coerce"
            ).fillna(0) == 0
        ]

    completed = metrics.completed_items()

    total = metrics.total_work_items()

    progress = 0

    if total > 0:
        progress = round(completed / total * 100)

    # -----------------------------------------
    # KPI Row
    # -----------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🚫 Blocked", len(blocked))

    c2.metric("👤 Unassigned", len(unassigned))

    c3.metric("📝 No Story Points", len(no_story_points))

    c4.metric("📊 Progress", f"{progress}%")

    st.divider()

    # -----------------------------------------
    # Risk Score
    # -----------------------------------------

    risk_score = 100

    risk_score -= len(blocked) * 5
    risk_score -= len(unassigned) * 3
    risk_score -= len(no_story_points)

    risk_score = max(risk_score, 0)

    st.subheader("Overall Risk Score")

    st.progress(risk_score / 100)

    if risk_score >= 85:

        st.success(f"🟢 Low Risk ({risk_score}/100)")

    elif risk_score >= 60:

        st.warning(f"🟡 Medium Risk ({risk_score}/100)")

    else:

        st.error(f"🔴 High Risk ({risk_score}/100)")

    st.divider()

    # -----------------------------------------
    # Risk Charts
    # -----------------------------------------

    chart = pd.DataFrame({

        "Category": [

            "Blocked",

            "Unassigned",

            "No Story Points"

        ],

        "Count": [

            len(blocked),

            len(unassigned),

            len(no_story_points)

        ]

    })

    fig = px.bar(

        chart,

        x="Category",

        y="Count",

        text="Count"

    )

    st.plotly_chart(

        fig,

        width="stretch"

    )

    st.divider()

    # -----------------------------------------
    # Blocked Items
    # -----------------------------------------

    st.subheader("🚫 Blocked Work Items")

    if len(blocked):

        st.dataframe(

            blocked[

                [

                    "ID",

                    "Title",

                    "Assigned To",

                    "State"

                ]

            ],

            width="stretch"

        )

    else:

        st.success("No blocked work items.")

    st.divider()

    # -----------------------------------------
    # Unassigned
    # -----------------------------------------

    st.subheader("👤 Unassigned Work")

    if len(unassigned):

        st.dataframe(

            unassigned[

                [

                    "ID",

                    "Title",

                    "State"

                ]

            ],

            width="stretch"

        )

    else:

        st.success("No unassigned work.")

    st.divider()

    # -----------------------------------------
    # AI Recommendation
    # -----------------------------------------

    st.subheader("🤖 Executive Recommendations")

    recommendations = []

    if len(blocked):

        recommendations.append(
            f"Resolve {len(blocked)} blocked work items."
        )

    if len(unassigned):

        recommendations.append(
            f"Assign owners to {len(unassigned)} work items."
        )

    if len(no_story_points):

        recommendations.append(
            f"Estimate {len(no_story_points)} work items."
        )

    if progress < 70:

        recommendations.append(
            "Sprint progress is behind plan."
        )

    if not recommendations:

        recommendations.append(
            "No major delivery risks detected."
        )

    for item in recommendations:

        st.info(item)