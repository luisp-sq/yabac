# YABAC (yet another bad actors client)

## Overview

This project is a simple Python script for processing customer actions specified in a CSV file and interacting with a gRPC service using Protocol Buffers (Protobuf). The actions include disabling a customer (`remove`) and initiating an initial screen (`screen`) both actions supported by BadActors

## Features

- **CSV File Processing:** Read and process a CSV file with columns 'customer_token' and 'action'.
- **Action Execution:** Call appropriate gRPC functions based on the specified action in the CSV file.
- **Protobuf Integration:** Utilize Protocol Buffers for efficient serialization and communication with the gRPC service.

## Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Place your csv file under the data folder**

3. **Run the Script:**
   ```bash
   python main.py --csv_file_path data/csv_file.csv
   ```

   Replace `csv_file.csv` with your file name.

## Configuration

- **CSV File:** Ensure your CSV file contains columns 'customer_token' and 'action'.
- **gRPC Service Address:** Provide the address of your gRPC service in the format `host:port`.

## Logging

- Log messages are recorded in the `logs` directory under `main.log`
