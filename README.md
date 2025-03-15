# Automating Clash Detection Resolution
This Dynamo workflow automates the process of detecting and visualizing clashes in Revit based on Navisworks XML reports. It extracts clash data, categorizes priorities, applies dynamic materials, and tracks resolution status—allowing for an efficient clash review process inside Revit. 

#  Automated Clash Detection in Revit with Dynamo & Navisworks

## 🔹 What This Project Does
This **Dynamo script** automates clash detection in **Revit** using **Navisworks XML reports**. It:
- Extracts clash data from XML files.
- Categorizes clashes (High: MEP vs. Structure, Medium: MEP vs. Architecture).
- Creates 3D spheres in Revit at clash locations.
- Uses colors (Red, Yellow, Green) to show resolution status.
- Updates clash colors automatically when resolved!

##  Files in This Repository
- `workflow.dyn` → Dynamo script
- `clash_processing.py` → Python script for processing clash data
- `example_clash_report.xml` → Sample Navisworks clash report
- `workflow_screenshot.png` → Screenshot of the workflow

##  Requirements
- **Revit 2023+**
- **Dynamo 2.12+**
- **Navisworks Manage 2023+**


##  How to Use
1. Download `workflow.dyn` and open it in **Dynamo**.
2. Import a **Navisworks clash report** (`.xml` file).
3. Run the script to generate clash spheres in Revit.
4. Review clashes and resolve them—the color updates automatically!

