import plotly.express as px
import streamlit as st


class Charts:

    def __init__(self, df):

        self.df = df.copy()

    # ---------------------------------------

    def work_item_types(self):

        st.subheader("📊 Work Item Distribution")

        if "Work Item Type" not in self.df.columns:
            return

        chart = (
            self.df["Work Item Type"]
            .value_counts()
            .reset_index()
        )

        chart.columns = [
            "Work Item Type",
            "Count"
        ]

        fig = px.pie(
            chart,
            names="Work Item Type",
            values="Count",
            hole=.55
        )

        fig.update_layout(height=450)

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # ---------------------------------------

    def state_distribution(self):

        st.subheader("📌 State Distribution")

        if "State" not in self.df.columns:
            return

        chart = (
            self.df["State"]
            .value_counts()
            .reset_index()
        )

        chart.columns = [
            "State",
            "Count"
        ]

        fig = px.bar(
            chart,
            x="State",
            y="Count",
            text="Count"
        )

        fig.update_layout(height=450)

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # ---------------------------------------

    def area_distribution(self):

        st.subheader("🏢 Area Path")

        if "Area Path" not in self.df.columns:
            return

        chart = (
            self.df["Area Path"]
            .value_counts()
            .reset_index()
        )

        chart.columns = [
            "Area",
            "Count"
        ]

        fig = px.treemap(
            chart,
            path=["Area"],
            values="Count"
        )

        fig.update_layout(height=500)

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # ---------------------------------------

    def iteration_distribution(self):

        st.subheader("🚀 Iterations")

        if "Iteration Path" not in self.df.columns:
            return

        chart = (
            self.df["Iteration Path"]
            .value_counts()
            .reset_index()
        )

        chart.columns = [
            "Iteration",
            "Count"
        ]

        fig = px.bar(
            chart,
            x="Iteration",
            y="Count",
            text="Count"
        )

        fig.update_layout(height=500)

        st.plotly_chart(
            fig,
            width="stretch"
        )

    # ---------------------------------------

    def assignee_distribution(self):

        st.subheader("👤 Work Items by Assignee")

        if "Assigned To" not in self.df.columns:
            return

        chart = (
            self.df["Assigned To"]
            .value_counts()
            .head(15)
            .reset_index()
        )

        chart.columns = [
            "Assigned To",
            "Count"
        ]

        fig = px.bar(
            chart,
            x="Assigned To",
            y="Count",
            text="Count"
        )

        fig.update_layout(height=500)

        st.plotly_chart(
            fig,
            width="stretch"
        )