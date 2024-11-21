# Business-Strategy-Multimodal-AI-Agent---FastAPI-Implementation
This project is a FastAPI-based application that provides a set of endpoints to analyze market data, generate project timelines, create content, and analyze budgets. These functionalities are driven by a collection of AI agents for Data Analysis, Project Management, Content Writing, and Finance Management.

This API is designed for interacting with various aspects of a business strategy and is intended for use in environments where these tasks can be automated or analyzed using AI models.

Features
Market Data Analysis: Analyzes market data, summarizes sales by region and category, and generates a sales plot.
Project Timeline Creation: Accepts a list of tasks with start and end dates to generate a project timeline.
Content Generation: Uses a pre-trained model to generate content based on a provided prompt.
Budget Allocation: Analyzes a JSON budget file and returns the budget allocation as percentages.
Requirements
Before running the FastAPI server, make sure you have the following installed on your system:

Python 3.7 or higher
pip for managing Python packages
Python Libraries
FastAPI: Framework for building the web API.
Uvicorn: ASGI server for running the FastAPI application.
Pandas: Data analysis library for handling market data.
Matplotlib: Plotting library for generating graphs.
Transformers: Hugging Face library for loading pre-trained models (e.g., T5-small for content generation).
Pydantic: Data validation and settings management library.
To install the required libraries, you can use the following requirements.txt file or manually install the dependencies:

requirements.txt
txt

fastapi==0.95.2
uvicorn==0.22.0
pandas==1.5.3
matplotlib==3.7.1
transformers==4.33.0
pydantic==2.2.2
Installing Dependencies
To install the dependencies, run the following command:


pip install -r requirements.txt
Project Setup
Step 1: Clone the Repository
Clone the repository to your local machine using:


git clone https://github.com/your-username/business-strategy-ai-agent.git
cd business-strategy-ai-agent
Step 2: Prepare the Data
The FastAPI app requires data files for the Market Data and Budget:

Market Data (data/sample_market_data.csv): A CSV file containing market sales data with columns like Date, Sales, Region, and Category.
Budget Data (data/sample_budget.json): A JSON file containing the budget allocations for different categories.
Ensure that these data files exist in the data/ directory. Example content:

data/sample_market_data.csv
csv
Date,Sales,Region,Category
2024-11-01,1500,North,Tech
2024-11-02,1700,South,Fashion
2024-11-03,1600,East,Health
...
data/sample_budget.json
json
{
  "Marketing": 10000,
  "R&D": 5000,
  "Operations": 3000,
  "Salaries": 12000
}
Step 3: Running the FastAPI Server
After setting up the data, you can run the FastAPI server using Uvicorn:

uvicorn main:app --reload
This will start the server on http://localhost:8000 in development mode. The --reload flag ensures that the server reloads whenever you make changes to the code.

API Endpoints
Once the server is running, you can access the following endpoints using Postman or any HTTP client.

1. Market Data Analysis
Endpoint: /analyze-market-data/

Method: POST
Description: Analyzes the market data and returns region-wise and category-wise sales summaries along with a sales plot.
Response: JSON containing:
region_summary: Region-wise sales summary.
category_summary: Category-wise sales summary.
plot_path: Path to the saved sales plot image.
Example Request:

json
{
  "data_path": "data/sample_market_data.csv"
}
Example Response:

json
{
  "region_summary": {"North": 5000, "South": 4000, "East": 3000},
  "category_summary": {"Tech": 6000, "Fashion": 5000, "Health": 3000},
  "plot_path": "data/sales_plot.png"
}
2. Create Project Timeline
Endpoint: /create-timeline/

Method: POST

Description: Accepts a list of tasks and generates a project timeline with start and end dates.

Request Body:

json
[
  {
    "name": "Market Analysis",
    "start_date": "2024-11-21",
    "end_date": "2024-11-25"
  },
  {
    "name": "Content Creation",
    "start_date": "2024-11-26",
    "end_date": "2024-12-01"
  }
]
Response: JSON containing the project timeline with task names, start and end dates.

Example Response:

json
{
  "project_timeline": {
    "Market Analysis": "Start: 2024-11-21, End: 2024-11-25",
    "Content Creation": "Start: 2024-11-26, End: 2024-12-01"
  }
}
3. Generate Content
Endpoint: /generate-content/

Method: POST

Description: Accepts a prompt and generates content using a pre-trained model (T5-small).

Request Body:

json
{
  "prompt": "Write a blog introduction for a new tech product launch focusing on AI advancements."
}
Response: JSON containing the generated content.

Example Response:

json
{
  "generated_content": "Introducing the next big leap in AI technology, where innovation meets real-world applications..."
}
4. Analyze Budget
Endpoint: /analyze-budget/

Method: POST
Description: Analyzes the budget allocation and returns the percentage distribution of each category.
Response: JSON containing the budget allocation percentages.
Example Response:

json
{
  "budget_allocation": {
    "Marketing": 40.0,
    "R&D": 20.0,
    "Operations": 12.0,
    "Salaries": 48.0
  }
}
Testing the API with Postman
Once the server is up and running, you can test the endpoints using Postman:

Set the request type to POST.
Enter the appropriate endpoint URL: http://localhost:8000/analyze-market-data/, /create-timeline/, /generate-content/, or /analyze-budget/.
Set the request body according to the expected format (see examples above).
Send the request and observe the response in the Postman interface.
File Structure
graphql
business-strategy-ai-agent/
│
├── data/
│   ├── sample_market_data.csv   # Market data CSV file
│   └── sample_budget.json       # Budget data JSON file
│
├── main.py                     # FastAPI application code
├── data_analyst.py             # Data analysis agent code
├── project_manager.py          # Project management agent code
├── content_writer.py           # Content generation agent code
├── finance_agent.py            # Finance management agent code
├── requirements.txt            # List of dependencies
└── README.md                   # This file
Troubleshooting
Issue: The server doesn't start.
Solution: Ensure that you have installed all the dependencies correctly by running pip install -r requirements.txt.
Issue: The request to /analyze-market-data/ or /generate-content/ returns an error.
Solution: Verify that your data files (sample_market_data.csv and sample_budget.json) exist in the data/ directory and are properly formatted.
