import pandas as pd
import streamlit as st


class DataLoader:

    def __init__(self, uploaded_file):

        try:

            self.df = pd.read_csv(uploaded_file)

        except Exception as ex:

            st.error(f"Unable to read CSV file.\n\n{ex}")

            st.stop()

        self.clean_data()

    # ---------------------------------------

    def clean_data(self):

        self.df.columns = self.df.columns.str.strip()

        # ---------------------------------------
        # Story Points
        # ---------------------------------------

        if "Story Points" in self.df.columns:

            self.df["Story Points"] = pd.to_numeric(

                self.df["Story Points"],

                errors="coerce"

            ).fillna(0)

        # ---------------------------------------
        # Text Columns
        # ---------------------------------------

        text_columns = self.df.select_dtypes(

            include=["object"]

        ).columns

        self.df[text_columns] = self.df[text_columns].fillna("")

        # ---------------------------------------
        # Standard Columns
        # ---------------------------------------

        columns = [

            "ID",

            "Title",

            "Work Item Type",

            "State",

            "Area Path",

            "Iteration Path",

            "Assigned To",

            "Tags"

        ]

        for column in columns:

            if column in self.df.columns:

                self.df[column] = (

                    self.df[column]

                    .astype(str)

                    .str.strip()

                )

        # ---------------------------------------
        # Validate Required Columns
        # ---------------------------------------

        required = [

            "ID",

            "Title",

            "Work Item Type",

            "State"

        ]

        missing = [

            c for c in required

            if c not in self.df.columns

        ]

        if missing:

            st.error(

                "Invalid Azure DevOps CSV.\n\nMissing columns:\n\n"

                + "\n".join(missing)

            )

            st.stop()

    # ---------------------------------------

    def get_dataframe(self):

        return self.df