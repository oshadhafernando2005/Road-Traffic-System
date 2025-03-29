import csv
import os

def get_valid_input(prompt, valid_range, input_type=int):
    while True:
        try:
            value = input_type(input(prompt))
            if value not in valid_range:
                print(f"Out of range - values must be in the range {valid_range.start} to {valid_range.stop - 1}.")
            else:
                return value
        except ValueError:
            print("Integer required.")

def load_csv_file(day, month, year):
    filename = f"data_{day:02d}{month:02d}{year}.csv"  # Example CSV file format: data_01_10_2024.csv
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return None
    return filename

def process_csv_file(filename):
    outcomes = {
        "total_vehicles": 0,
        "total_trucks": 0,
        "total_ev": 0,
        "two_wheeled": 0,
        "buses_north": 0,
        "straight_vehicles": 0,
        "trucks_percentage": 0,
        "avg_bicycles_hour": 0,
        "over_speed_limit": 0,
        "elm_only": 0,
        "hanley_only": 0,
        "scooter_percentage": 0,
        "peak_hour_vehicles": 0,
        "peak_hour_times": "Between 18:00 and 19:00",
        "hours_of_rain": 0
    }
    
    # Placeholder for CSV reading logic (Assumes structure with vehicle types and counts)
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                outcomes["total_vehicles"] += int(row['TotalVehicles'])
                outcomes["total_trucks"] += int(row['Trucks'])
                outcomes["total_ev"] += int(row['EV'])
                outcomes["two_wheeled"] += int(row['TwoWheeled'])
                # Additional processing based on fields
    except Exception as e:
        print(f"Error reading the file: {e}")
    
    return outcomes

def display_outcomes(outcomes):
    print("\n--- Survey Results ---")
    for key, value in outcomes.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

def save_results_to_file(outcomes):
    with open("results.txt", 'a') as file:
        file.write("\n--- Survey Results ---\n")
        for key, value in outcomes.items():
            file.write(f"{key.replace('_', ' ').title()}: {value}\n")

def main():
    while True:
        print("\nPlease enter the date of the survey:")
        day = get_valid_input("Day (DD): ", range(1, 32))
        month = get_valid_input("Month (MM): ", range(1, 13))
        year = get_valid_input("Year (YYYY): ", range(2000, 2025))

        filename = load_csv_file(day, month, year)
        if filename:
            outcomes = process_csv_file(filename)
            display_outcomes(outcomes)
            save_results_to_file(outcomes)
        
        # Loop control
        continue_choice = input("\nLoad new dataset? (Y/N): ").strip().upper()
        if continue_choice != 'Y':
            print("Exiting program.")
            break

if _name_ == "_main_":
    main()
