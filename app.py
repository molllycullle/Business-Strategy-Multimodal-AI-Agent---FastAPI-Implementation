from fastapi import FastAPI
from pydantic import BaseModel
from data_analyst import DataAnalyst
from project_manager import ProjectManager
from content_writer import ContentWriter
from finance_agent import FinanceAgent
import json
import os

app = FastAPI()

# Initialize the agents
analyst = DataAnalyst()
manager = ProjectManager()
writer = ContentWriter()
finance = FinanceAgent()

# Request models
class Task(BaseModel):
    name: str
    start_date: str
    end_date: str

class Prompt(BaseModel):
    prompt: str

# Endpoint to analyze market data
@app.post("/analyze-market-data/")
async def analyze_market_data():
    region_summary, category_summary, plot_path = analyst.analyze_market_data('data/sample_market_data.csv')
    # Return data as JSON response
    return {
        "region_summary": region_summary.to_dict(),
        "category_summary": category_summary.to_dict(),
        "plot_path": plot_path
    }

# Endpoint to create project timeline
@app.post("/create-timeline/")
async def create_timeline(tasks: list[Task]):
    task_data = [task.dict() for task in tasks]
    timeline = manager.create_timeline(task_data)
    return {"project_timeline": timeline}

# Endpoint to generate content
@app.post("/generate-content/")
async def generate_content(prompt: Prompt):
    content = writer.generate_content(prompt.prompt)
    return {"generated_content": content}

# Endpoint to analyze budget
@app.post("/analyze-budget/")
async def analyze_budget():
    allocation = finance.analyze_budget('data/sample_budget.json')
    return {"budget_allocation": allocation}


# Run the FastAPI server using Uvicorn
# uvicorn filename:app --reload

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
