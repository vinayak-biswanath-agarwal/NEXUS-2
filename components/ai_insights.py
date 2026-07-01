import streamlit as st


class AIInsights:

    def __init__(self, metrics):

        self.metrics = metrics

    def show(self):

        st.subheader("🤖 AI Executive Insights")

        epics = self.metrics.total_epics()
        features = self.metrics.total_features()
        stories = self.metrics.total_user_stories()
        bugs = self.metrics.total_bugs()
        blocked = self.metrics.blocked_items()
        readiness = self.metrics.release_readiness()

        insights = []

        if readiness >= 90:
            insights.append("🟢 Release readiness is excellent. Project appears on track.")

        elif readiness >= 75:
            insights.append("🟡 Release readiness is good but requires monitoring.")

        else:
            insights.append("🔴 Release readiness is low. Executive attention recommended.")

        if bugs == 0:
            insights.append("✅ No open bugs detected.")

        elif bugs < 10:
            insights.append(f"🐞 {bugs} bugs are currently open.")

        else:
            insights.append(f"🚨 High bug count detected ({bugs}).")

        if blocked == 0:
            insights.append("✅ No blocked work items.")

        else:
            insights.append(f"⚠ {blocked} blocked work items require action.")

        if features < epics:
            insights.append("⚠ Some Epics may not yet contain Features.")

        if stories < features:
            insights.append("⚠ Some Features may not yet contain User Stories.")

        st.info("\n\n".join(insights))

        st.subheader("📌 Executive Recommendation")

        if readiness >= 90 and blocked == 0:
            st.success(
                "Recommendation : Continue execution. Delivery confidence is HIGH."
            )

        elif readiness >= 75:
            st.warning(
                "Recommendation : Monitor delivery closely during upcoming sprint."
            )

        else:
            st.error(
                "Recommendation : Immediate PMO review is advised."
            )