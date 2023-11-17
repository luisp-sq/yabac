import csv
import logging

def validate_csv_columns(file_path):
    required_columns = ['customer_token', 'action']
    valid_actions = {'initial_screen', 'remove'}  # Using a set for faster membership testing

    success = False
    
    try:
        logging.info(f"START - Validation for file name: {file_path}")
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            
            if not all(column in reader.fieldnames for column in required_columns):
                print(f"Error: Missing columns in CSV file - {', '.join(set(required_columns) - set(reader.fieldnames))}")
                logging.error(f"Missing columns in CSV file - {', '.join(set(required_columns) - set(reader.fieldnames))}")
                return success
            
            token_count = {'initial_screen': 0, 'remove': 0}
            
            for row in reader:
                if row['action'] not in valid_actions:
                    print(f"Error: Invalid 'action' value in CSV file - {row['action']}")
                    logging.error(f"Invalid 'action' value in CSV file - {row['action']}")
                    return success
                
                token_count[row['action']] += 1
    
            print(f"Let's confirm the expected counts: {token_count}")
            
            confirmation = input("Do you want to proceed? (yes/y or no): ").lower()
            if confirmation not in ['yes', 'y']:
                print("Validation canceled. Exiting...")
                logging.info("END - Validation canceled by user.")
                return success

            logging.info(f"END - Token count: {token_count}")
            success = True

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid CSV file path.")
        logging.error("END - File not found. Please provide a valid CSV file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        logging.error(f"END - An unexpected error occurred: {str(e)}")

    return success

def disable (customer_token, reason_intent, service_address):
    # implementation to call DisableCustomerRequest
    print(f'disabling customer: {customer_token}')
    pass

def screen (customer_token, screen_intent, service_address):
    # implementation to call ScreenCustomerRequest
    print(f'screening customer: {customer_token}')
    pass

def process_csv(file_path, service_address):

    try:
        logging.info(f"START - Processing file: {file_path}")
        
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                customer_token = row.get('customer_token', '')
                action = row.get('action', '').lower()

                if action == 'remove':
                    disable(customer_token, 'product_intent_a', service_address)
                elif action == 'initial_screen':
                    screen(customer_token, 'product_intent_a', service_address)
                else:
                    logging.error(f"Invalid action '{action}' for customer {customer_token}")

        logging.info(f"END - Processing file: {file_path}")

    except FileNotFoundError:
        logging.error("File not found. Please provide a valid CSV file path.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    csv_file_path = 'data/test.csv'
    grpc_service_address = "localhost:50051"
    logging.basicConfig(filename='logs/main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    if validate_csv_columns(csv_file_path):
        # Proceed with further processing or API calls
        print("Data looks good, now...")
        process_csv(csv_file_path, grpc_service_address)
    else:
        # Halt execution or handle the error accordingly
        print("Validation failed. Exiting...")