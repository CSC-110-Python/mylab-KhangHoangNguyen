import math

# Constants
earth_g = 9.81  # gravitational acceleration on Earth in m/s^2
mars_g = 3.71   # gravitational acceleration on Mars in m/s^2

# Input height from the user
height = float(input('Height in meters: '))  # Meters from planet

# Calculate and print the time it takes to fall from the given height on Earth and Mars
if __name__ == '__main__':
    time_earth = math.sqrt(2 * height / earth_g)
    time_mars = math.sqrt(2 * height / mars_g)
    
    print('Earth:', time_earth, 'seconds')
    print('Mars:', time_mars, 'seconds')
