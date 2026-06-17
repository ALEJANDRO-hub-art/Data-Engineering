# Converted from: 03_enhanced_mock_data_generator(2).ipynb
# Auto-generated Python script from Jupyter Notebook

# %% [markdown] Cell 1
# # =============================================================================
# # UPI TRANSACTIONS CDC FEED PROJECT - ENHANCED MOCK DATA GENERATOR
# # =============================================================================
# # This notebook generates realistic mock data for UPI transactions with CDC operations
# # Purpose: Creates test data for development, testing, and demonstration of CDC streaming
# # Features: INSERT, UPDATE, DELETE operations with realistic UPI transaction patterns
# # Output: Continuous CDC operations to test real-time streaming pipeline

# %% Cell 2
# =============================================================================
# LIBRARY IMPORTS AND CONFIGURATION
# =============================================================================
# Import required libraries for mock data generation and CDC operations
# Purpose: Set up environment for generating realistic UPI transaction test data

import random
import uuid
from datetime import datetime, timedelta
from pyspark.sql import functions as F
from pyspark.sql.types import *
from delta.tables import DeltaTable
import time

# =============================================================================
# CONFIGURATION SETUP
# =============================================================================
# Configure Unity Catalog and target table for mock data generation
# catalog_name: Unity Catalog for data governance
# schema_name: Target schema for UPI transaction tables
# raw_table: Target table for inserting mock transaction data

catalog_name = "`gds_de_bootcamp_new`"
schema_name = "default"
raw_table = f"{catalog_name}.{schema_name}.raw_upi_transactions_v1"

print(f"Using catalog: {catalog_name}, schema: {schema_name}")
print(f"Target table: {raw_table}")

# %% Cell 3
# Mock data constants
MERCHANTS = [
    {"merchant_id": "M001", "merchant_name": "Amazon India", "merchant_category": "E-commerce"},
    {"merchant_id": "M002", "merchant_name": "Swiggy", "merchant_category": "Food Delivery"},
    {"merchant_id": "M003", "merchant_name": "Uber", "merchant_category": "Transportation"},
    {"merchant_id": "M004", "merchant_name": "Netflix", "merchant_category": "Entertainment"},
    {"merchant_id": "M005", "merchant_name": "BigBasket", "merchant_category": "Grocery"},
    {"merchant_id": "M006", "merchant_name": "Flipkart", "merchant_category": "E-commerce"},
    {"merchant_id": "M007", "merchant_name": "Zomato", "merchant_category": "Food Delivery"},
    {"merchant_id": "M008", "merchant_name": "Ola", "merchant_category": "Transportation"}
]

UPI_IDS = ["user123@paytm", "user456@phonepe", "user789@googlepay", "user101@amazonpay", "user202@mobikwik"]
CUSTOMER_IDS = ["CUST001", "CUST002", "CUST003", "CUST004", "CUST005"]
PAYMENT_METHODS = ["UPI", "QR Code", "Mobile Number"]
DEVICE_TYPES = ["Mobile", "Tablet"]
OPERATING_SYSTEMS = ["Android", "iOS"]
CITIES = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune", "Ahmedabad"]
STATES = ["Maharashtra", "Delhi", "Karnataka", "Tamil Nadu", "West Bengal", "Telangana", "Gujarat"]
AGE_GROUPS = ["18-25", "26-35", "36-45", "46-55", "55+"]
GENDERS = ["Male", "Female", "Other"]

# Transaction ID counter for unique IDs
transaction_counter = 1

def insert_new_transactions(num_transactions=5):
    """Insert new transactions using simple createDataFrame approach"""
    global transaction_counter
    try:
        print(f"INSERT: Adding {num_transactions} new transactions...")
        
        # Generate transaction data as tuples (following your pattern)
        transaction_data = []
        
        for i in range(num_transactions):
            merchant = random.choice(MERCHANTS)
            upi_id = random.choice(UPI_IDS)
            customer_id = random.choice(CUSTOMER_IDS)
            
            # Generate realistic transaction amounts based on merchant category
            if merchant["merchant_category"] == "E-commerce":
                amount = round(random.uniform(100, 5000), 2)
            elif merchant["merchant_category"] == "Food Delivery":
                amount = round(random.uniform(50, 500), 2)
            elif merchant["merchant_category"] == "Transportation":
                amount = round(random.uniform(20, 200), 2)
            elif merchant["merchant_category"] == "Entertainment":
                amount = round(random.uniform(100, 1000), 2)
            elif merchant["merchant_category"] == "Grocery":
                amount = round(random.uniform(200, 1000), 2)
            else:
                amount = round(random.uniform(50, 1000), 2)
            
            # Generate timestamp (recent for CDC testing)
            transaction_time = datetime.now() - timedelta(minutes=random.randint(1, 60))
            
            # Generate transaction status
            status_weights = {"completed": 0.75, "failed": 0.15, "initiated": 0.05, "refunded": 0.03, "cancelled": 0.02}
            status = random.choices(list(status_weights.keys()), weights=list(status_weights.values()))[0]
            
            # Calculate processing fee and commission
            processing_fee = round(amount * 0.005, 2)
            commission = round(amount * 0.01, 2)
            
            # Generate unique transaction ID
            transaction_id = f"TXN_{datetime.now().strftime('%Y%m%d')}_{transaction_counter:06d}"
            transaction_counter += 1
            
            # Create tuple with all required fields (following your simple pattern)
            transaction_tuple = (
                transaction_id,
                upi_id,
                merchant["merchant_id"],
                merchant["merchant_name"],
                merchant["merchant_category"],
                float(amount),  # Use float/double as in your working example
                "INR",
                transaction_time,
                status,
                random.choice(PAYMENT_METHODS),
                random.choice(DEVICE_TYPES),  # device_type
                random.choice(OPERATING_SYSTEMS),  # device_os
                f"v{random.randint(1, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}",  # app_version
                round(random.uniform(8.0, 37.0), 6),  # latitude
                round(random.uniform(68.0, 97.0), 6),  # longitude
                random.choice(CITIES),  # city
                random.choice(STATES),  # state
                "India",  # country
                customer_id,  # customer_id
                random.choice(AGE_GROUPS),  # age_group
                random.choice(GENDERS),  # gender
                float(processing_fee),  # Use float/double as in your working example
                float(commission),  # Use float/double as in your working example
                datetime.now(),  # created_at
                datetime.now()   # updated_at
            )
            
            transaction_data.append(transaction_tuple)
        
        # Create DataFrame using simple createDataFrame (following your pattern)
        transaction_df = spark.createDataFrame(transaction_data, [
            "transaction_id", "upi_id", "merchant_id", "merchant_name", "merchant_category",
            "transaction_amount", "transaction_currency", "transaction_timestamp", "transaction_status",
            "payment_method", "device_type", "device_os", "app_version", "latitude", "longitude",
            "city", "state", "country", "customer_id", "age_group", "gender",
            "processing_fee", "commission", "created_at", "updated_at"
        ])
        
        transaction_df.write.format("delta").mode("append").saveAsTable(raw_table)
        
        print(f"INSERT: Successfully added {num_transactions} transactions")
        return True
        
    except Exception as e:
        print(f"INSERT failed: {str(e)}")
        return False

def update_existing_transactions(num_updates=3):
    """Update existing transactions using merge pattern with correct column names"""
    try:
        print(f"UPDATE: Updating {num_updates} existing transactions...")
        
        # Get existing transactions to update - FIXED COLUMN NAMES
        existing_transactions = spark.sql(f"""
            SELECT transaction_id, upi_id, merchant_id, merchant_name, merchant_category,
                   transaction_amount, transaction_currency, transaction_timestamp,
                   transaction_status, payment_method, device_type, device_os, app_version,
                   latitude, longitude, city, state, country, customer_id, age_group, gender,
                   processing_fee, commission, created_at
            FROM {raw_table}
            ORDER BY created_at DESC
            LIMIT {num_updates}
        """).collect()
        
        if len(existing_transactions) == 0:
            print("No existing transactions to update")
            return False
        
        # Prepare update data as tuples (following your pattern)
        update_data = []
        
        for row in existing_transactions:
            # Update the transaction status and amount
            new_status = random.choice(["completed", "failed", "refunded"])
            new_amount = round(row["transaction_amount"] * random.uniform(0.8, 1.2), 2)
            new_processing_fee = round(new_amount * 0.005, 2)
            new_commission = round(new_amount * 0.01, 2)
            
            # Create tuple for update (following your pattern) - FIXED COLUMN NAMES
            update_tuple = (
                row["transaction_id"],
                row["upi_id"],
                row["merchant_id"],
                row["merchant_name"],
                row["merchant_category"],
                float(new_amount),  # Use float/double as in your working example
                row["transaction_currency"],
                row["transaction_timestamp"],
                new_status,
                row["payment_method"],
                row["device_type"],  # FIXED: was device_info
                row["device_os"],    # FIXED: was device_info
                row["app_version"],  # FIXED: was device_info
                row["latitude"],     # FIXED: was location_info
                row["longitude"],    # FIXED: was location_info
                row["city"],         # FIXED: was location_info
                row["state"],        # FIXED: was location_info
                row["country"],      # FIXED: was location_info
                row["customer_id"],  # FIXED: was customer_info
                row["age_group"],    # FIXED: was customer_info
                row["gender"],       # FIXED: was customer_info
                float(new_processing_fee),  # Use float/double as in your working example
                float(new_commission),  # Use float/double as in your working example
                row["created_at"],
                datetime.now()  # Update timestamp
            )
            
            update_data.append(update_tuple)
        
        # Create DataFrame for updates (following your pattern) - FIXED COLUMN NAMES
        update_df = spark.createDataFrame(update_data, [
            "transaction_id", "upi_id", "merchant_id", "merchant_name", "merchant_category",
            "transaction_amount", "transaction_currency", "transaction_timestamp", "transaction_status",
            "payment_method", "device_type", "device_os", "app_version", "latitude", "longitude",
            "city", "state", "country", "customer_id", "age_group", "gender",
            "processing_fee", "commission", "created_at", "updated_at"
        ])
        
        # Use merge pattern (following your approach)
        delta_table = DeltaTable.forName(spark, raw_table)
        delta_table.alias("target").merge(
            update_df.alias("source"),
            "target.transaction_id = source.transaction_id"
        ).whenMatchedUpdateAll().execute()
        
        print(f"UPDATE: Successfully updated {len(existing_transactions)} transactions")
        return True
        
    except Exception as e:
        print(f"UPDATE failed: {str(e)}")
        return False

def delete_transactions(num_deletes=2):
    """Delete some transactions"""
    try:
        print(f"DELETE: Deleting {num_deletes} transactions...")
        
        # Get transactions to delete
        transactions_to_delete = spark.sql(f"""
            SELECT transaction_id
            FROM {raw_table}
            ORDER BY created_at DESC
            LIMIT {num_deletes}
        """).collect()
        
        if len(transactions_to_delete) == 0:
            print("No transactions to delete")
            return False
        
        # Delete transactions using DeltaTable
        target_table = DeltaTable.forName(spark, raw_table)
        
        transaction_ids = [row["transaction_id"] for row in transactions_to_delete]
        
        for transaction_id in transaction_ids:
            target_table.delete(f"transaction_id = '{transaction_id}'")
        
        print(f"DELETE: Successfully deleted {len(transaction_ids)} transactions")
        return True
        
    except Exception as e:
        print(f"DELETE failed: {str(e)}")
        return False

print("UPDATE and DELETE functions defined with fixed column names")
print("Transaction data generation functions defined")

# %% Cell 4
def continuous_cdc_data_generation(duration_minutes=20):
    """Generate data continuously with CDC operations every 2 minutes"""
    global transaction_counter
    
    try:
        print(f"Starting continuous CDC data generation for {duration_minutes} minutes")
        print("Operations will run every 2 minutes")
        print("Operations: INSERT (70%), UPDATE (20%), DELETE (10%)")
        
        end_time = datetime.now() + timedelta(minutes=duration_minutes)
        batch_count = 0
        
        while datetime.now() < end_time:
            batch_count += 1
            print(f"Batch {batch_count} - {datetime.now().strftime('%H:%M:%S')}")
            
            # Determine operation type based on weights
            operation_weights = {"INSERT": 0.7, "UPDATE": 0.2, "DELETE": 0.1}
            operation = random.choices(list(operation_weights.keys()), weights=list(operation_weights.values()))[0]
            
            if operation == "INSERT":
                success = insert_new_transactions(random.randint(3, 8))
            elif operation == "UPDATE":
                success = update_existing_transactions(random.randint(1, 4))
            elif operation == "DELETE":
                success = delete_transactions(random.randint(1, 2))
            
            if success:
                print(f"Batch {batch_count} completed successfully")
            else:
                print(f"Batch {batch_count} had issues")
            
            # Wait for next batch (2 minutes)
            if datetime.now() < end_time:
                print(f"Waiting 2 minutes for next batch...")
                time.sleep(120)  # 2 minutes
        
        print(f"Continuous CDC data generation completed!")
        print(f"Total batches processed: {batch_count}")
        
    except KeyboardInterrupt:
        print("Continuous data generation stopped by user")
    except Exception as e:
        print(f"Error in continuous data generation: {str(e)}")
        raise

print("Continuous CDC data generation function defined")

# %% Cell 5
# Set up initial data
print("Setting up initial data...")
success = insert_new_transactions(20)
if success:
    print("Initial data setup completed successfully!")
    print("You can now run: continuous_cdc_data_generation(duration_minutes=30)")
    continuous_cdc_data_generation(duration_minutes=20)
else:
    print("Initial data setup failed")

# %% Cell 6
# Uncomment this if manually we want to run upate

# update_existing_transactions(3)

# %% Cell 7
# Uncomment this if manually we want to run delete

# delete_transactions(2)
