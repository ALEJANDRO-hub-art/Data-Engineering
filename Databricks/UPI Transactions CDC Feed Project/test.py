# Converted from: test(2).ipynb
# Auto-generated Python script from Jupyter Notebook

# %% Cell 1
# Read CDC stream
cdc_stream = spark.readStream.format("delta") \
    .option("readChangeFeed", "true") \
    .table("`gds_de_bootcamp_new`.default.raw_upi_transactions")

# Display CDC changes
query = cdc_stream.select(
    "transaction_id",
    "upi_id",
    "merchant_id",
    "transaction_amount",
    "transaction_timestamp",
    "transaction_status",
    "_change_type",  # CDC change type
    "_commit_version",
    "_commit_timestamp"
).writeStream.format("console") \
    .outputMode("append") \
    .start()

query.awaitTermination()
