class ProjectManager:
    def create_timeline(self, tasks):
        timeline = {}
        for task in tasks:
            timeline[task["name"]] = f"Start: {task['start_date']}, End: {task['end_date']}"
        return timeline

if __name__ == "__main__":
    tasks = [
        {"name": "Market Analysis", "start_date": "2024-11-21", "end_date": "2024-11-25"},
        {"name": "Content Creation", "start_date": "2024-11-26", "end_date": "2024-12-01"}
    ]
    manager = ProjectManager()
    timeline = manager.create_timeline(tasks)
    print("Project Timeline:\n", timeline)
