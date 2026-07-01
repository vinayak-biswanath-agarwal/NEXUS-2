import streamlit as st
from utils.metrics import Metrics
from utils.intelligence import Intelligence


def show(df):

    metrics = Metrics(df)

    intelligence = Intelligence(metrics)

    st.title("🤖 AI Executive Command Center")

    st.caption("AI Powered Executive PMO Dashboard")

    st.divider()

    # -----------------------------------------
    # Executive Score Cards
    # -----------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🏆 Executive Score",
        f"{intelligence.executive_score()}/100"
    )

    c2.metric(
        "📈 Portfolio Health",
        f"{intelligence.portfolio_health()}%"
    )

    c3.metric(
        "🚀 Delivery Confidence",
        f"{intelligence.delivery_confidence()}%"
    )

    c4.metric(
        "🟢 Status",
        intelligence.executive_status()
    )

    st.divider()

    # -----------------------------------------
    # Executive Summary
    # -----------------------------------------

    st.subheader("📋 Executive Summary")

    st.info(

f"""
Portfolio contains **{metrics.total_work_items()}** work items.

Current Portfolio Health is **{intelligence.portfolio_health()}%**

Delivery Confidence is **{intelligence.delivery_confidence()}%**

Overall Executive Score is **{intelligence.executive_score()}/100**

Current Status is **{intelligence.executive_status()}**
"""

    )

    st.divider()

    # -----------------------------------------
    # Delivery Snapshot
    # -----------------------------------------

    st.subheader("📊 Delivery Snapshot")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📁 Epics",
            metrics.total_epics()
        )

        st.metric(
            "⭐ Features",
            metrics.total_features()
        )

        st.metric(
            "📋 Stories",
            metrics.total_user_stories()
        )

        st.metric(
            "🐞 Bugs",
            metrics.total_bugs()
        )

    with col2:

        st.metric(
            "🚫 Blocked",
            metrics.blocked_items()
        )

        st.metric(
            "✅ Completed",
            metrics.completed_items()
        )

        st.metric(
            "⚡ Active",
            metrics.active_items()
        )

        st.metric(
            "📝 Story Points",
            metrics.total_story_points()
        )

    st.divider()

    # -----------------------------------------
    # Executive Recommendations
    # -----------------------------------------

    st.subheader("🎯 AI Recommendations")

    recommendations = []

    if metrics.blocked_items() > 0:

        recommendations.append(
            f"Resolve {metrics.blocked_items()} blocked work items."
        )

    if intelligence.portfolio_health() < 80:

        recommendations.append(
            "Portfolio health requires executive review."
        )

    if intelligence.delivery_confidence() < 80:

        recommendations.append(
            "Delivery confidence is below target."
        )

    if metrics.completed_items() < (
        metrics.total_work_items() * 0.50
    ):

        recommendations.append(
            "Focus on improving completion rate."
        )

    if metrics.total_story_points() == 0:

        recommendations.append(
            "Story Points are missing for planning."
        )

    if len(recommendations) == 0:

        recommendations.append(
            "Portfolio is progressing well."
        )

    for rec in recommendations:

        st.success(rec)

    st.divider()

    # -----------------------------------------
    # Executive Focus Today
    # -----------------------------------------

    st.subheader("🔥 Executive Focus Today")

    st.warning(

"""
1. Review blocked work items.

2. Review work items without Story Points.

3. Validate Sprint Progress.

4. Review Delivery Risks.

5. Review Team Capacity.

6. Review upcoming Release Readiness.

"""

    )

    st.divider()

    # -----------------------------------------
    # AI Executive Message
    # -----------------------------------------

    st.subheader("🤖 AI Executive Narrative")

    st.success(

f"""
NEXUS has analysed the Azure DevOps portfolio.

Current Executive Score is **{intelligence.executive_score()}/100**.

Portfolio Health is **{intelligence.portfolio_health()}%**.

Delivery Confidence is **{intelligence.delivery_confidence()}%**.

Based on current delivery data, the portfolio is **{intelligence.executive_status()}**.

Immediate focus should be on blocked work, completion rate and release readiness.
"""

    )