import pandas as pd


class DataLoader:

    def __init__(self):

        self.df = pd.read_csv(
            "data/ado_export.csv"
        )

        self.clean_data()

    # ---------------------------------------

    def clean_data(self):

        self.df.columns = self.df.columns.str.strip()

        # Convert Story Points first
        if "Story Points" in self.df.columns:

            self.df["Story Points"] = pd.to_numeric(
                self.df["Story Points"],
                errors="coerce"
            ).fillna(0)

        # Fill text columns only
        text_columns = self.df.select_dtypes(include=["object"]).columns

        self.df[text_columns] = self.df[text_columns].fillna("")

        # Convert important columns to string
        for column in [
            "Work Item Type",
            "State",
            "Area Path",
            "Iteration Path",
            "Assigned To",
            "Title",
            "Tags"
        ]:

            if column in self.df.columns:
                self.df[column] = self.df[column].astype(str)

    # ---------------------------------------

    def get_dataframe(self):

        return self.df