'''
NOTE: 
    Major changes in the refactored code:
        1. Three functions added (get_average, get_max, get_min)
        2. Dictionary format changed to single dictionary with 3 key value pairs and list as values
        3. Error handling implemented
        4. Displaying was moved to the main function

'''
import csv 

def get_average(values: list) -> float:
    '''Return the average of all the values in the list'''
    return sum(values)/len(values)

def get_max(values: list) -> float:
    '''Return the maximum value in the list'''
    return max(values)

def get_min(values: list) -> float:
    '''Return the minimum value in the list'''
    return min(values)

def process_weather_data(file_path: str) -> dict: 
    '''Store csv data into dictionary format and return the dictionary'''
    data = {}
    
    try:
        with open(file_path, 'r') as f: 
            reader = csv.DictReader(f) 
            
            for row in reader: 
                for key, value in row.items():
                    match (key):
                        case 'temperature':
                            data.setdefault(key, []).append(float(value))
                        case 'humidity':
                            data.setdefault(key, []).append(int(value))
                        case _:
                            data.setdefault(key, []).append(value)

    except FileNotFoundError:
        print("Error: CSV file not found in the specified directory!")

    return data

# main function
if __name__ == "__main__":
    data = process_weather_data('Lab Activity 4/weather_data.csv')

    avg_temp = get_average(data["temperature"])
    avg_humidity = get_average(data["humidity"])
    max_temp = get_max(data["temperature"])
    min_temp = get_min(data["temperature"])

    print(f"Average Temperature: {avg_temp:.2f}°C") 
    print(f"Average Humidity: {avg_humidity:.2f}%") 
    print(f"Maximum Temperature: {max_temp:.2f}°C") 
    print(f"Minimum Temperature: {min_temp:.2f}°C") 

    # Bonus tasks
    