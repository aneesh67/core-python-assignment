def manage_patients(patients, disease):
    return [p["Name"] for p in patients if p["Disease"] == disease]

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = "Flu"
result = manage_patients(patients, search_disease)
print(f"Patients with {search_disease}: {result}")
