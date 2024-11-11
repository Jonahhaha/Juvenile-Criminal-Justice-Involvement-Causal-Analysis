# Juvenile Criminal Justice Involvement Causal Analysis
This repository contains code and data for a research project studying the intergenerational impacts of parental criminal justice system (CJS) involvement on children’s behaviors. The project uses causal discovery and structural equation modeling to identify factors influencing children’s involvement with the CJS and potential intervention targets.

# Table of Contents
## Background
## Data
## Methodology
## Causal Discovery
## Structural Equation Modeling
## Simulated Interventions
## Results
## [Final_reporting](https://drive.google.com/file/d/1y5kgZv0gUOj8djgkkQgtCayH816bdGLU/view?usp=sharing)

# Background
The study explores the impact of parental CJS involvement on juvenile delinquency and other behavioral outcomes. Using data from families involved with the CJS, the project aims to provide clinical insights and to identify potential intervention targets that could mitigate the risk of children’s future CJS involvement.

# [Data](https://github.com/Jonahhaha/Intervetion/tree/main/dataset)
Data was collected from a two-wave study of 762 children (ages 9-15) and their parents, primarily from the South Bronx, NYC. The sample includes:

CJS-involved families: Families where parents have CJS involvement.
Control group: Families with no history of CJS involvement, matched by demographics.
Variables: Data includes 62 variables across categories such as psychiatric disorders, delinquent behaviors, personality disorders, and functional impairments.

# [Methodology](https://github.com/Jonahhaha/Intervetion/tree/main/Testing_for_different_version_of_tetrad_and_different_algorthim)
Causal Discovery
The study uses the Greedy Recursive Sparse Projection in Fast Causal Inference (GRaSP-FCI) algorithm to estimate causal relationships. GRaSP-FCI allows for the detection of direct causal links and identifies confounding variables using partial ancestral graphs (PAGs). Also since the Tetrad has different version, so I test with all of the versions for testing it out which version will be the best. So there is all of these versions of testing and Python, and R version too. 

1. I use [Tetrad](https://github.com/cmu-phil/tetrad) to generate a graph which include all the causal relationships within the database.
I. Load the data and knowledge file
II. Chose the algorthim and variables to generate the graph
2. I use R to bootstrape to [generate 100 datasets](https://github.com/Jonahhaha/Intervetion/blob/main/Bootstrpe_Final_Result/bootstrap%20result%20final.xlsx), where I also run the [Causal_CMD](https://github.com/bd2kccd/causal-cmd) to produce the accuracy for my dataset.
3. I use [Python](https://github.com/Jonahhaha/Intervetion/blob/main/Bootstrpe_Final_Result/GET_THE_CASUAL_RELATIONSHIPS.ipynb) to generate the right format for the causal relationships, and write it down in txt file. 
4. I use [R Lavvan](https://github.com/Jonahhaha/Intervetion/blob/main/Final%20result%20copy/labforLavaan.Rmd) to numeric the causal relationships.
5. I use [R](https://github.com/Jonahhaha/Intervention_of_CJS/blob/main/Lavaan/CODE_labforLavaan.pdf) to check should we standlized the dataset and is Causal_CMD and Tetrad has any difference. 
6. I use [Python to do intervations for the dataset](https://github.com/Jonahhaha/Intervetion/blob/main/Lavaan/CODE_Lavaan%20Data%20Result.ipynb), since we think Y0_CD will be the main variable, how much [Y0_CD changes](https://github.com/Jonahhaha/Intervetion/blob/main/Fomal_Result_Summary/final_variable_change_output.txt) will impact other variable which is the important for us for this project. 

Sorry the Python code is still a little bit messy. I will keep working on the code. 

# [Structural Equation Modeling](https://github.com/Jonahhaha/Intervetion/tree/main/Bootstrpe_Final_Result)
We used Lavaan in R to estimate causal effects based on the identified relationships. Structural equation modeling was used to calculate standardized causal effects, and model fit was assessed using SRMR and CFI scores.

# Simulated Interventions
A simulated intervention was applied to assess the effect of decreasing symptoms of Conduct Disorder. The analysis quantifies both direct and indirect effects on juvenile outcomes using the causal pathways identified by the model.

# [Results](https://github.com/Jonahhaha/Intervetion/tree/main/Final%20result%20copy)
Key findings include:

Juvenile CJS involvement tends to act as a negative turning point, contributing to higher conduct disorder severity and future CJS involvement.
Interventions that target Conduct Disorder symptoms have the potential to reduce juvenile CJS engagement.

