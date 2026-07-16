from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

from config import DB_CONFIG
from etl.mapping import TABLE_MAPPING, PRELOAD_SCHEMA


def get_engine():
    """
    Create and return a SQLAlchemy engine.
    """

    connection_url = URL.create(
        drivername="mysql+pymysql",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"]
    )

    engine = create_engine(
        connection_url,
        echo=False,
        pool_pre_ping=True
    )

    # Verify connection
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    print(" MySQL Connected Successfully")

    return engine


def apply_mapping(table_name, dataframe):
    """
    Apply table-specific mapping before loading.
    """

    dataframe = dataframe.copy()

    if table_name not in TABLE_MAPPING:
        return dataframe

    mapping = TABLE_MAPPING[table_name]

    if "drop_columns" in mapping:
        dataframe = dataframe.drop(
            columns=mapping["drop_columns"],
            errors="ignore"
        )

    if "type_conversion" in mapping:
        for column, dtype in mapping["type_conversion"].items():
            dataframe[column] = dataframe[column].astype(dtype)

    return dataframe


def validate_schema(table_name, dataframe):
    """
    Validate DataFrame schema before loading.
    """

    expected_columns = PRELOAD_SCHEMA[table_name]
    actual_columns = dataframe.columns.tolist()

    if expected_columns != actual_columns:
        raise ValueError(
            f"\nSchema mismatch in '{table_name}'\n"
            f"Expected : {expected_columns}\n"
            f"Found    : {actual_columns}"
        )


def load_table(engine, table_name, dataframe):
    """
    Load one row at a time for debugging.
    """

    for index, row in dataframe.iterrows():

        try:

            row.to_frame().T.to_sql(
                name=table_name,
                con=engine,
                if_exists="append",
                index=False
            )

        except Exception as e:

            print("\n" + "=" * 60)
            print(f"FAILED ROW : {index}")
            print(f"TABLE      : {table_name}")
            print("=" * 60)

            print(row)

            print("\nERROR:")
            print(e)

            raise


def truncate_tables(engine):
    """
    Remove existing data before loading.
    """

    table_order = [

        "order_items",
        "reviews",
        "returns",
        "shipping",
        "payments",
        "orders",
        "inventory",
        "products",
        "customers",
        "categories"

    ]

    with engine.begin() as connection:

        connection.execute(text("SET FOREIGN_KEY_CHECKS = 0"))

        for table in table_order:
            connection.execute(
                text(f"TRUNCATE TABLE {table}")
            )

        connection.execute(text("SET FOREIGN_KEY_CHECKS = 1"))

    print(" Existing data cleared.")


def load_data(datasets):
    """
    Load all datasets.
    """

    engine = get_engine()

    truncate_tables(engine)

    loading_order = [

        "categories",
        "customers",
        "products",
        "inventory",
        "orders",
        "payments",
        "shipping",
        "returns",
        "reviews",
        "order_items"

    ]

    successful = []
    failed = []

    for table in loading_order:

        try:

            dataframe = apply_mapping(
                table,
                datasets[table]
            )

            validate_schema(
                table,
                dataframe
            )

            load_table(
                engine,
                table,
                dataframe
            )

            print(f" {table} loaded successfully")

            successful.append(table)

        except Exception as e:

            print("\n" + "=" * 60)
            print(f"FAILED TABLE : {table}")
            print("=" * 60)

            print("Error Type :", type(e).__name__)
            print("Error      :", str(e))

            if hasattr(e, "orig"):
                print("\nOriginal MySQL Error:")
                print(e.orig)

            failed.append(table)

    print("\n==============================")
    print("LOAD SUMMARY")
    print("==============================")

    print(f"Successful Tables : {len(successful)}")
    print(f"Failed Tables     : {len(failed)}")

    print("\nLoaded Tables")
    print(successful)

    print("\nFailed Tables")
    print(failed)