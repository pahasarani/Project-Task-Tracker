import pandas as pd
from datetime import datetime

# Step 1: Sample Data (Tasks, Resources, Status)
data = {
    'Task_ID': [1, 2, 3, 4, 5],
    'Task_Name': ['Design UI', 'Develop Backend', 'Write Documentation', 'Testing', 'Deployment'],
    'Assigned_Resource': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Start_Date': ['2025-03-01', '2025-03-02', '2025-03-05', '2025-03-10', '2025-03-12'],
    'End_Date': ['2025-03-10', '2025-03-15', '2025-03-07', '2025-03-14', '2025-03-18'],
    'Status': ['Completed', 'In Progress', 'Completed', 'Not Started', 'In Progress'],
    'Priority': ['High', 'Medium', 'Low', 'High', 'Medium']
}

# Step 2: Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Step 3: Convert date columns to datetime
df['Start_Date'] = pd.to_datetime(df['Start_Date'])
df['End_Date'] = pd.to_datetime(df['End_Date'])

# Step 4: Analysis - Calculate overdue tasks
current_date = datetime.now()
df['Overdue'] = df['End_Date'] < current_date

# Step 5: Task Status Summary
status_summary = df['Status'].value_counts()

# Step 6: Percentage of tasks completed
completed_percentage = (df['Status'] == 'Completed').sum() / len(df) * 100

# Step 7: Tasks by each team member
tasks_by_member = df.groupby('Assigned_Resource')['Task_ID'].count()

# Step 8: Remaining days for each task
df['Remaining_Days'] = (df['End_Date'] - current_date).dt.days

# Display the DataFrame and results
print("Project Task Tracker:")
print(df)
print("\nStatus Summary:")
print(status_summary)
print(f"\nCompleted Tasks Percentage: {completed_percentage:.2f}%")
print("\nTasks by Team Member:")
print(tasks_by_member)
print("\nRemaining Days for Each Task:")
print(df[['Task_Name', 'Remaining_Days']])
