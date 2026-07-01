import pandas as pd

class Metrics:
    def __init__(self, df):
        self.df = df.copy()

        # Remove duplicate work items
        if "ID" in self.df.columns:
            self.df = self.df.drop_duplicates(subset=["ID"])

        # Clean text columns
        for column in self.df.columns:
            if self.df[column].dtype == "object":
                self.df[column] = self.df[column].astype(str).str.strip()

    # ------------------------------------------
    # Generic Count
    # ------------------------------------------
    def count_by_type(self, work_item_type):
        if "Work Item Type" not in self.df.columns:
            return 0
        return len(
            self.df[
                self.df["Work Item Type"].str.casefold() == work_item_type.casefold()
            ]
        )

    # ------------------------------------------
    # Total Work Items
    # ------------------------------------------
    def total_work_items(self):
        return len(self.df)

    # ------------------------------------------
    # Epics
    # ------------------------------------------
    def total_epics(self):
        return self.count_by_type("Epic")

    # ------------------------------------------
    # Features
    # ------------------------------------------
    def total_features(self):
        return self.count_by_type("Feature")

    # ------------------------------------------
    # User Stories
    # ------------------------------------------
    def total_user_stories(self):
        if "Work Item Type" not in self.df.columns:
            return 0

        values = self.df["Work Item Type"].str.casefold().unique()

        if "user story" in values:
            return self.count_by_type("User Story")
        if "product backlog item" in values:
            return self.count_by_type("Product Backlog Item")

        return 0

    # ------------------------------------------
    # Tasks
    # ------------------------------------------
    def total_tasks(self):
        return self.count_by_type("Task")

    # ------------------------------------------
    # Bugs
    # ------------------------------------------
    def total_bugs(self):
        return self.count_by_type("Bug")

    # ------------------------------------------
    # Story Points
    # ------------------------------------------
    def total_story_points(self):
        if "Story Points" not in self.df.columns:
            return 0
        return round(
            pd.to_numeric(self.df["Story Points"], errors="coerce").fillna(0).sum(),
            1
        )

    # ------------------------------------------
    # Active Items
    # ------------------------------------------
    def active_items(self):
        if "State" not in self.df.columns:
            return 0

        closed = ["done", "closed", "completed", "removed"]

        return len(
            self.df[~self.df["State"].str.casefold().isin(closed)]
        )

    # ------------------------------------------
    # Completed Items
    # ------------------------------------------
    def completed_items(self):
        if "State" not in self.df.columns:
            return 0

        completed = ["done", "closed", "completed"]

        return len(
            self.df[self.df["State"].str.casefold().isin(completed)]
        )

    # ------------------------------------------
    # Blocked
    # ------------------------------------------
    def blocked_items(self):
        if "State" not in self.df.columns:
            return 0
        return len(
            self.df[
                self.df["State"].str.contains("blocked", case=False, na=False)
            ]
        )

    # ------------------------------------------
    # Delivery Health
    # ------------------------------------------
    def delivery_health(self):
        bugs = self.total_bugs()
        blocked = self.blocked_items()

        if bugs <= 5 and blocked == 0:
            return "🟢 GREEN"
        if bugs <= 20:
            return "🟡 AMBER"
        
        return "🔴 RED"

    # ------------------------------------------
    # Release Readiness
    # ------------------------------------------
    def release_readiness(self):
        total = self.total_work_items()
        if total == 0:
            return 0

        completed = self.completed_items()
        return round(completed / total * 100, 1)

    # ------------------------------------------
    # Top Assignees
    # ------------------------------------------
    def top_assignees(self):
        if "Assigned To" not in self.df.columns:
            return pd.DataFrame()

        return (
            self.df["Assigned To"]
            .value_counts()
            .head(10)
            .rename_axis("Assigned To")
            .reset_index(name="Work Items")
        )

    # ------------------------------------------
    # State Summary
    # ------------------------------------------
    def state_summary(self):
        if "State" not in self.df.columns:
            return pd.DataFrame()

        return (
            self.df["State"]
            .value_counts()
            .rename_axis("State")
            .reset_index(name="Count")
        )

    # ------------------------------------------
    # Work Item Summary
    # ------------------------------------------
    def work_item_summary(self):
        if "Work Item Type" not in self.df.columns:
            return pd.DataFrame()

        return (
            self.df["Work Item Type"]
            .value_counts()
            .rename_axis("Type")
            .reset_index(name="Count")
        )

    # ------------------------------------------
    # Active By Type
    # ------------------------------------------
    def active_by_type(self, work_item_type):
        closed_states = ["Done", "Closed", "Completed", "Removed"]
        return len(
            self.df[
                (self.df["Work Item Type"] == work_item_type) &
                (~self.df["State"].isin(closed_states))
            ]
        )

    # ------------------------------------------
    # Closed By Type
    # ------------------------------------------
    def closed_by_type(self, work_item_type):
        closed_states = ["Done", "Closed", "Completed", "Removed"]
        return len(
            self.df[
                (self.df["Work Item Type"] == work_item_type) &
                (self.df["State"].isin(closed_states))
            ]
        )