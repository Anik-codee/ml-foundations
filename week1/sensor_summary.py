import csv
def load_sensor_data(sensor_data):
    my_list = []
    with open(sensor_data, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["temperature"] = float(row["temperature"])
                row["rotation_speed"] = float(row["rotation_speed"])
                row["torque"] = float(row["torque"])
                my_list.append(row)
            except ValueError as e:
                print(f"Skipping row due to conversion error: {e}")
                continue
    return my_list
sensor_data = load_sensor_data('sensor_data.csv')

def classify_temperature(temperature):
    if temperature<70:
        return "Normal"
    elif temperature<=89:
        return "Warning"
    else:
        return "Critical"

def calculate_statistics(data):
    total_machines=len(data)
    temp_sum=0
    speed_sum=0
    torque_sum=0
    highest_temp=data[0]['temperature']
    lowest_temp=data[0]['temperature']
    highest_risk_machine=data[0]['machine']
    warning_critical_machines=[]
    for row in data:
        temp=row['temperature']
        speed=row['rotation_speed']
        torque=row['torque']
        temp_sum+=temp
        speed_sum+=speed
        torque_sum+=torque
        if temp>highest_temp:
            highest_temp=temp
            highest_risk_machine=row['machine']
        if temp<lowest_temp:
            lowest_temp=temp
        status=classify_temperature(temp)
        if status in ["Warning","Critical"]:
            warning_critical_machines.append({'machine': row['machine'],'temperature':temp})
    avg_temp=temp_sum/total_machines
    avg_speed=speed_sum/total_machines
    avg_torque=torque_sum/total_machines
    return {
        'total_machines': total_machines,
        'avg_temp': avg_temp,
        'highest_temp': highest_temp,
        'lowest_temp': lowest_temp,
        'avg_speed': avg_speed,
        'avg_torque': avg_torque,
        'highest_risk_machine': highest_risk_machine,
        'warning_critical_machines': warning_critical_machines
    }

def display_report(data, statistics):
    print("MACHINE SENSOR SUMMARY")
    print(f"Machines analyzed: {statistics['total_machines']}")
    print(f"Average temperature: {statistics['avg_temp']} C")
    print(f"Highest temperature: {statistics['highest_temp']} C")
    print(f"Lowest temperature: {statistics['lowest_temp']} C")
    print(f"Average rotational speed: {statistics['avg_speed']} RPM")
    print(f"Average torque: {statistics['avg_torque']:.1f} Nm")
    print("\nWarning and critical machines:")
    
    for item in statistics['warning_critical_machines']:
        print(f"- {item['machine']}: {item['temperature']} C")
        
    print(f"Highest-risk machine: {statistics['highest_risk_machine']}")

stats = calculate_statistics(sensor_data)
display_report(sensor_data, stats)