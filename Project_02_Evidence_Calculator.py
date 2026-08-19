# PROJECT 02: FORENSIC EVIDENCE CALCULATOR

print("============FORENSIC EVIDENCE CALCULATOR============")

# PART 01: input
evidence_ID = int(input("Enter Evidence ID: "))
evidence_type = input("Enter Evidence Type:")
sample_mass = float(input("Enter Sample Mass: "))
containers = int(input("Enter number of evidence containers: "))
investigators = int(input("Number of investigators: "))
evidence_items = int(input("Enter number of evidence items: "))

# PART 02: Calculations
sample_mass_mg = sample_mass * 1000
# print(sample_mass_mg)
sample_mass_kg = sample_mass / 1000
print(sample_mass_kg)
average_container_per_investigator = containers / investigators
average_container_per_investigator = round(average_container_per_investigator, 2)
avg_mass_per_container = sample_mass / containers
avg_mass_per_container = round(avg_mass_per_container,2)
evidence_to_investigator_ratio = evidence_items / investigators
evidence_to_investigator_ratio = round(evidence_to_investigator_ratio,2)


# PART 03: Output
print("Evidence ID of the investigation:", evidence_ID)
print("Evidence Type                   :", evidence_type)
print("Sample Mass in kg               :", sample_mass_kg)
print("Number of evidence containers   :", containers)
print("No. of Investigators            :", investigators)
print("Average container per investigator :" , average_container_per_investigator)
print("Average Mass per container      :", avg_mass_per_container)
print("Evidence to investigator ratio  :", evidence_to_investigator_ratio)