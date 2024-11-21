import json

class FinanceAgent:
    def analyze_budget(self, budget_path):
        with open(budget_path, 'r') as f:
            budget = json.load(f)
        
        # Calculate total budget and percentage allocation for each department
        total_budget = sum(budget.values())
        allocation = {key: (value / total_budget) * 100 for key, value in budget.items()}
        
        return allocation

if __name__ == "__main__":
    agent = FinanceAgent()
    allocation = agent.analyze_budget('data/sample_budget.json')
    print("Budget Allocation:\n", allocation)
