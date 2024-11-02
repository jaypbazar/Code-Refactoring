'''
NOTE: 
    Major changes in the refactored code:
        1. Three functions added (get_average, get_max, get_min, and get_median)
            - This increases the reusability of the code making the program more flexible.

        2. Dictionary format changed to single dictionary with 3 key value pairs and list as values
            - The new data format makes it easier to access the data and use built-in functions to process them

        3. Error handling implemented
            - This increases the overall performance as well as the security of the program

        4. Additional features were added (median temperature and day with highest humidity)
            - Additional features were added as specified in the bonus tasks

        5. Argparse implemented
            - This makes the program more flexible by allowing users to run the program with different csv file

'''
import csv 
import argparse

def get_average(values: list) -> float:
    '''Return the average of all the values in the list'''
    return sum(values)/len(values)

def get_max(values: list) -> float:
    '''Return the maximum value in the list'''
    return max(values)

def get_min(values: list) -> float:
    '''Return the minimum value in the list'''
    return min(values)

def get_median(values: list) -> float:
    '''Return the median value of the list'''
    values = sorted(values)
    middle = len(values) // 2

    return ((values[middle - 1] + values[middle]) / 2.0) if len(values) % 2 == 0 else values[middle]

def process_weather_data(file_path: str) -> None: 
    '''Store csv data into dictionary format and display the processed data'''
    data = {}
    
    try:
        with open(file_path, 'r') as f: 
            reader = csv.DictReader(f) 

            # raise an error of file is empty
            if not any(reader): raise EOFError
            
            for row in reader: 
                for key, value in row.items():
                    if key == 'date':
                        data.setdefault(key, []).append(value)
                    else:
                        data.setdefault(key, []).append(float(value))

        # raise an error if any of the columns are missing
        if 'humidity' not in data or 'humidity' not in data or 'humidity' not in data:
            raise Exception  

        avg_temp = get_average(data["temperature"])
        avg_humidity = get_average(data["humidity"])
        max_temp = get_max(data["temperature"])
        min_temp = get_min(data["temperature"])

        print(f"Average Temperature: {avg_temp:.2f}°C") 
        print(f"Average Humidity: {avg_humidity:.2f}%") 
        print(f"Maximum Temperature: {max_temp:.2f}°C") 
        print(f"Minimum Temperature: {min_temp:.2f}°C") 
        
        # NOTE: Additional features
        median_temp = get_median(data['temperature'])
        max_humidity_date = data['date'][data['humidity'].index(get_max(data['humidity']))]

        print(f"\nMedian Temperature: {median_temp:.2f}°C") 
        print(f"Day with Highest Humidity: {max_humidity_date}") 

    except FileNotFoundError:
        print("Error: CSV file not found in the specified directory!")

    except EOFError:
        print("Error: CSV file is empty!")

    except Exception:
        print("Error: CSV data might not be in the right format.")

# main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Path to the CSV file containing weather data')

    args = parser.parse_args()

    process_weather_data(args.file_path)
