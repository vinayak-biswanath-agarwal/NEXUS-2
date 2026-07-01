import streamlit as st


class KPICards:

    def __init__(self, metrics):

        self.metrics = metrics

    # ----------------------------------------------------
    # Executive KPI Row
    # ----------------------------------------------------

    def executive(self):

        # ====================================================
        # Work Item Summary
        # ====================================================

        st.subheader("📊 Work Item Summary")

        summary = {

            "Work Item": [

                "📁 Epics",

                "⭐ Features",

                "📋 User Stories",

                "🐞 Bugs"

            ],

            "Total": [

                self.metrics.total_epics(),

                self.metrics.total_features(),

                self.metrics.total_user_stories(),

                self.metrics.total_bugs()

            ],

            "Active": [

                self.metrics.active_by_type("Epic"),

                self.metrics.active_by_type("Feature"),

                self.metrics.active_by_type("User Story"),

                self.metrics.active_by_type("Bug")

            ],

            "Closed": [

                self.metrics.closed_by_type("Epic"),

                self.metrics.closed_by_type("Feature"),

                self.metrics.closed_by_type("User Story"),

                self.metrics.closed_by_type("Bug")

            ]

        }

        st.dataframe(

            summary,

            width="stretch",

            hide_index=True

        )

        st.divider()

        # ====================================================
        # Portfolio KPIs
        # ====================================================

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(

                "📦 Total Work Items",

                self.metrics.total_work_items()

            )

        with c2:

            st.metric(

                "📝 Story Points",

                self.metrics.total_story_points()

            )

        with c3:

            st.metric(

                "🚫 Blocked",

                self.metrics.blocked_items()

            )

        with c4:

            st.metric(

                "✅ Completed",

                self.metrics.completed_items()

            )

        st.divider()

        # ====================================================
        # Executive Health
        # ====================================================

        c5, c6, c7 = st.columns(3)

        with c5:

            health = self.metrics.delivery_health()

            if "GREEN" in health:

                st.success(

                    f"Delivery Health\n\n{health}"

                )

            elif "AMBER" in health:

                st.warning(

                    f"Delivery Health\n\n{health}"

                )

            else:

                st.error(

                    f"Delivery Health\n\n{health}"

                )

        with c6:

            readiness = self.metrics.release_readiness()

            st.metric(

                "🚀 Release Readiness",

                f"{readiness}%"

            )

            st.progress(

                readiness / 100

            )

        with c7:

            st.metric(

                "⚡ Active Work Items",

                self.metrics.active_items()

            )

    # ----------------------------------------------------
    # Executive Summary
    # ----------------------------------------------------

    def executive_summary(self):

        st.subheader("📊 Executive Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.info(

                f"""

### Portfolio Overview

**📦 Total Work Items:** {self.metrics.total_work_items()}

**⚡ Active Work Items:** {self.metrics.active_items()}

**✅ Completed Items:** {self.metrics.completed_items()}

**📝 Story Points:** {self.metrics.total_story_points()}

"""

            )

        with col2:

            st.info(

                f"""

### Delivery Status

**🟢 Delivery Health:** {self.metrics.delivery_health()}

**🚀 Release Readiness:** {self.metrics.release_readiness()}%

**🚫 Blocked Items:** {self.metrics.blocked_items()}

**🐞 Open Bugs:** {self.metrics.total_bugs()}

"""

            )