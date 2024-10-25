# Causal Modeling of Juvenile Criminal Justice Involvement
This repository contains code and data for a research project studying the intergenerational impacts of parental criminal justice system (CJS) involvement on children’s behaviors. The project uses causal discovery and structural equation modeling to identify factors influencing children’s involvement with the CJS and potential intervention targets.

# Table of Contents
Background
Data
Methodology
Causal Discovery
Structural Equation Modeling
Simulated Interventions
Results
Installation
Usage

# Background
The study explores the impact of parental CJS involvement on juvenile delinquency and other behavioral outcomes. Using data from families involved with the CJS, the project aims to provide clinical insights and to identify potential intervention targets that could mitigate the risk of children’s future CJS involvement.

# Data
Data was collected from a two-wave study of 762 children (ages 9-15) and their parents, primarily from the South Bronx, NYC. The sample includes:

CJS-involved families: Families where parents have CJS involvement.
Control group: Families with no history of CJS involvement, matched by demographics.
Variables: Data includes 62 variables across categories such as psychiatric disorders, delinquent behaviors, personality disorders, and functional impairments.

Note: Due to privacy concerns, the dataset is not publicly available. Please contact the project PI for access.

# Methodology
Causal Discovery
The study uses the Greedy Recursive Sparse Projection in Fast Causal Inference (GRaSP-FCI) algorithm to estimate causal relationships. GRaSP-FCI allows for the detection of direct causal links and identifies confounding variables using partial ancestral graphs (PAGs).

# Structural Equation Modeling
We used Lavaan in R to estimate causal effects based on the identified relationships. Structural equation modeling was used to calculate standardized causal effects, and model fit was assessed using SRMR and CFI scores.

# Simulated Interventions
A simulated intervention was applied to assess the effect of decreasing symptoms of Conduct Disorder. The analysis quantifies both direct and indirect effects on juvenile outcomes using the causal pathways identified by the model.

# Results
Key findings include:

Juvenile CJS involvement tends to act as a negative turning point, contributing to higher conduct disorder severity and future CJS involvement.
Interventions that target Conduct Disorder symptoms have the potential to reduce juvenile CJS engagement.

# Installation
## Clone the repository:

```
git clone https://github.com/yourusername/juvenile-cjs-causal-modeling.git
cd juvenile-cjs-causal-modeling
```

## Install dependencies:

### Ensure you have Python 3.8+ and R 4.0+ installed.
### Install Python dependencies:
```
pip install -r requirements.txt
```

### Install R dependencies:
#### Inside an R environment, run:
```
install.packages("lavaan")
```

# Usage
## Data Preprocessing: Run the data_preprocessing.py script to process raw data for analysis.

```
python data_preprocessing.py
```


## Causal Discovery: Use causal_discovery_grasp_fci.py to apply GRaSP-FCI to the dataset.
```
python causal_discovery_grasp_fci.py
```

## Structural Equation Modeling: Run the R script structural_equation_modeling.R to estimate causal effects.

```
Rscript structural_equation_modeling.R
```

## Simulated Intervention: Simulate the impact of modifying Conduct Disorder symptoms by running simulate_intervention.py.

```
python simulate_intervention.py
```
