# PROJECT 01: FORENSIC CASE INTAKE SYSTEM

print("===============================================")
print("WELCOME TO THE MOCK INVESTIGATORS PROJECT 2026")
print("================================================")

# PART 01: Input
case_number = int(input("Enter case number: "))
victim_name = input("Enter victim name: ")
victim_age = int(input("Enter victim age (years): "))
evidence_items = int(input("Enter number of evidence items: "))
sample_weight = float(input("Enter sample weight (g): "))
investigators = int(input("Enter number of investigators: "))

# PART 02: Calculations
sample_weight_mg = sample_weight * 1000
average_evidence = evidence_items // investigators
# print("Sample weight in mg" , sample_weight_mg)
sample_weight_kg = sample_weight / 1000
print("Sample weight in Kg", sample_weight_kg)


# PART 03: Output
print("=========CASE SUMMARY=========")
print("Average evidence items per investigators" , average_evidence)
# Keep lines 18 & 19 in mind to show output data clearly.
print("Case Number", case_number)
print("Victim Name", victim_name)
print("Victim Age in years", victim_age)
print("Evidence Items", evidence_items)
print("Sample Weight", sample_weight)
print("Investigators", investigators)


