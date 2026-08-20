# PART 01: INPUT

accident_case_ID = int(input("Enter Accident Case ID :"))
vehicle_type = input("Enter vehicle type :")
skid_mark_length_m = float(input("Enter skid mark length :"))
road_surface_condition = input("Enter road surface condition :")
vehicle_speed_kmph = float(input("Enter vehicle speed in kmph :"))
number_of_photographs = int(input("Enter number of photographs :"))
number_of_investigators = int(input("Enter number of investigators :"))

# PART 02: CALCULATIONS

skid_mark_length_cm = skid_mark_length_m * 100
vehicle_speed_mps = vehicle_speed_kmph / 3.6
photographs_per_investigator = number_of_photographs // number_of_investigators
skid_mark_length_cm_per_investigator = skid_mark_length_cm / number_of_investigators
print(skid_mark_length_cm)
print(vehicle_speed_mps)
print(photographs_per_investigator)
print(skid_mark_length_cm_per_investigator)

# PART 03: OUTPUT

print("==========CASE SUMMARY==========")
print("Accident Case ID               :", accident_case_ID)
print("Vehicle Type                   :", vehicle_type)
print("Skid Mark Length in metres     :", skid_mark_length_m)
print("Skid mark length in centimetres:", skid_mark_length_cm)
print("Road Surface Condition         : ", road_surface_condition)
print("Vehicle Speed in mps           :", vehicle_speed_mps)
print("Vehicle speed in kmph          :", vehicle_speed_kmph)
print("Photographs per investigator   :", photographs_per_investigator)
print("Number of investigators        :", number_of_investigators)


