import streamlit as st


class Sidebar:

    def __init__(self, df):

        self.df = df.copy()

    # ----------------------------------------------------
    # Sidebar Filters
    # ----------------------------------------------------

    def show(self):

        st.sidebar.title("📊 NEXUS")

        st.sidebar.caption("Executive PMO Dashboard")

        st.sidebar.divider()

        # ----------------------------------------
        # Area Path
        # ----------------------------------------

        area_options = ["All"]

        if "Area Path" in self.df.columns:

            area_options += sorted(
                self.df["Area Path"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

        area = st.sidebar.selectbox(
            "Area",
            area_options
        )

        # ----------------------------------------
        # Iteration
        # ----------------------------------------

        iteration_options = ["All"]

        if "Iteration Path" in self.df.columns:

            iteration_options += sorted(
                self.df["Iteration Path"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

        iteration = st.sidebar.selectbox(
            "Iteration",
            iteration_options
        )

        # ----------------------------------------
        # Work Item Type
        # ----------------------------------------

        type_options = ["All"]

        if "Work Item Type" in self.df.columns:

            type_options += sorted(
                self.df["Work Item Type"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

        work_item_type = st.sidebar.selectbox(
            "Work Item Type",
            type_options
        )

        # ----------------------------------------
        # State
        # ----------------------------------------

        state_options = ["All"]

        if "State" in self.df.columns:

            state_options += sorted(
                self.df["State"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

        state = st.sidebar.selectbox(
            "State",
            state_options
        )

        # ----------------------------------------
        # Assigned To
        # ----------------------------------------

        assigned_options = ["All"]

        if "Assigned To" in self.df.columns:

            assigned_options += sorted(
                self.df["Assigned To"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

        assigned_to = st.sidebar.selectbox(
            "Assigned To",
            assigned_options
        )

        st.sidebar.divider()

        st.sidebar.success("CSV Connected")

        # ----------------------------------------
        # Apply Filters
        # ----------------------------------------

        filtered = self.df.copy()

        if area != "All":

            filtered = filtered[
                filtered["Area Path"] == area
            ]

        if iteration != "All":

            filtered = filtered[
                filtered["Iteration Path"] == iteration
            ]

        if work_item_type != "All":

            filtered = filtered[
                filtered["Work Item Type"] == work_item_type
            ]

        if state != "All":

            filtered = filtered[
                filtered["State"] == state
            ]

        if assigned_to != "All":

            filtered = filtered[
                filtered["Assigned To"] == assigned_to
            ]

        return filtered