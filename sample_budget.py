import json

# Budget data (simplified for this example)
budget_data = {
    "Marketing": 50000,
    "Development": 75000,
    "Operations": 60000,
    "HR": 40000,
    "R&D": 50000
}

# Save to JSON
with open("sample_budget.json", "w") as f:
    json.dump(budget_data, f, indent=4)

print("Budget data saved to sample_budget.json")
