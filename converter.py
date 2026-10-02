import pandas as pd
import argparse
import logging
import os

# Logging Setup


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


# Read CSV File


def read_csv_file(input_file):
    try:
        logging.info("Reading CSV file...")

        if not os.path.exists(input_file):
            raise FileNotFoundError("Input file was not found.")

        if not input_file.lower().endswith(".csv"):
            raise ValueError("Input file must be a CSV file.")

        df = pd.read_csv(input_file)

        if df.empty:
            raise ValueError("The CSV file is empty.")

        logging.info("CSV file loaded successfully.")
        logging.info(f"Rows: {len(df)}, Columns: {len(df.columns)}")

        return df

    except FileNotFoundError as error:
        logging.error(error)
        return None

    except pd.errors.EmptyDataError:
        logging.error("The CSV file contains no data.")
        return None

    except pd.errors.ParserError:
        logging.error("Could not read the CSV file. Please check its format.")
        return None

    except Exception as error:
        logging.error(f"Something went wrong: {error}")
        return None

# Clean Column Names

def clean_column_names(df):
    logging.info("Cleaning column names...")

    # Remove extra spaces
    df.columns = df.columns.str.strip()

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Replace spaces with underscores
    df.columns = df.columns.str.replace(" ", "_")

    return df


# Handle Missing Values

def handle_missing_values(df):
    logging.info("Handling missing values...")

    for column in df.columns:

        # If column contains numbers
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].fillna(df[column].mean())

        # If column contains text
        else:
            df[column] = df[column].fillna("Unknown")

    return df

# Parse Date Columns

def parse_dates(df):
    logging.info("Checking for date columns...")

    for column in df.columns:

        if "date" in column:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    return df

# Rename Columns

def rename_columns(df):
    logging.info("Renaming columns...")

    column_names = {
        "student_name": "name",
        "student_id": "id",
        "phone_number": "phone"
    }

    df.rename(
        columns=column_names,
        inplace=True
    )

    return df

# Export to Excel

def export_to_excel(df, output_file):

    try:
        logging.info("Exporting data to Excel...")

        # Create output folder if it doesn't exist
        output_directory = os.path.dirname(output_file)

        if output_directory:
            os.makedirs(output_directory, exist_ok=True)

        df.to_excel(
            output_file,
            index=False,
            engine="openpyxl"
        )

        logging.info(
            f"Excel file created successfully: {output_file}"
        )

        return True

    except PermissionError:
        logging.error(
            "Permission denied. Please close the Excel file if it is open."
        )
        return False

    except Exception as error:
        logging.error(
            f"Could not create Excel file: {error}"
        )
        return False

# Main Program

def main():

    parser = argparse.ArgumentParser(
        description="Convert and clean a CSV file and export it to Excel."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path of the input CSV file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path of the output Excel file"
    )

    args = parser.parse_args()

    # Step 1: Read CSV
    df = read_csv_file(args.input)

    if df is None:
        return

    # Step 2: Clean column names
    df = clean_column_names(df)

    # Step 3: Handle missing values
    df = handle_missing_values(df)

    # Step 4: Parse dates
    df = parse_dates(df)

    # Step 5: Rename columns
    df = rename_columns(df)

    # Step 6: Export Excel
    success = export_to_excel(
        df,
        args.output
    )

    if success:
        logging.info("CSV to Excel conversion completed!")

# Program Entry Point

if __name__ == "__main__":
    main()