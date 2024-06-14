# week-10 -> student_gpa.py

def calculate_average_gpa(gpas):
    return sum(gpas) / len(gpas)

def main():
    filename = "students.txt"
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                age = int(data[1])
                gpas = list(map(float, data[2:]))
                average_gpa = calculate_average_gpa(gpas)
                
                print(f"Student: {name}, Age: {age}, Average GPA: {average_gpa:.2f}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
