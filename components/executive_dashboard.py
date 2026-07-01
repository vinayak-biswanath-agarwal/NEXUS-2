import streamlit as st
from utils.intelligence import Intelligence


class ExecutiveDashboard:

    def __init__(self, metrics):

        self.metrics = metrics
        self.ai = Intelligence(metrics)

    def show(self):

        st.header("🏢 Executive Intelligence Dashboard")

        st.divider()

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "🏆 Executive Score",
                f"{self.ai.executive_score()}/100"
            )

        with c2:

            st.metric(
                "📈 Portfolio Health",
                f"{self.ai.portfolio_health()}%"
            )

        with c3:

            st.metric(
                "🚀 Delivery Confidence",
                f"{self.ai.delivery_confidence()}%"
            )

        with c4:

            st.metric(
                "🟢 Status",
                self.ai.executive_status()
            )

        st.divider()

        st.subheader("🤖 Executive Recommendation")

        status = self.ai.executive_status()

        if "Excellent" in status:

            st.success(
                self.ai.executive_message()
            )

        elif "Good" in status:

            st.info(
                self.ai.executive_message()
            )

        elif "Attention" in status:

            st.warning(
                self.ai.executive_message()
            )

        else:

            st.error(
                self.ai.executive_message()
            )

        st.divider()

        st.subheader("📊 Executive Scorecard")

        st.progress(
            self.ai.executive_score() / 100
        )

        st.write(
            f"Overall Executive Score : **{self.ai.executive_score()} / 100**"
        )

        st.progress(
            self.ai.portfolio_health() / 100
        )

        st.write(
            f"Portfolio Health : **{self.ai.portfolio_health()}%**"
        )

        st.progress(
            self.ai.delivery_confidence() / 100
        )

        st.write(
            f"Delivery Confidence : **{self.ai.delivery_confidence()}%**"
        )