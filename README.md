# M2 Projects (Master 2)

A consolidated repository for Master 2 (M2) academic research projects, presentations, and coursework.

---

## Repository Overview

This repository hosts graduate-level projects covering machine learning, data science, decision analytics, and empirical research:

1. [**Prescriptive Analytics**](prescriptive-analytics/) — Comprehensive seminar materials on prescriptive analytics, decision optimization, mathematical modeling, and enterprise applications.
2. [**Student Burnout & Continuation Risk Research**](ResearchBurnout/) — An explainable machine learning research project investigating early prediction of academic burnout and continuation risk in small-sample regimes.

---

## Directory Structure

```text
M2-Projects/
├── .gitignore                                      # Global git ignore rules (data protection, caches, temp files)
├── README.md                                       # Repository documentation and navigation guide
│
├── prescriptive-analytics/                         # Prescriptive Analytics Seminar & Presentation
│   ├── prescriptive-analytics-presentation.md      # Marp presentation slides source (Gaia theme)
│   ├── prescriptive-analytics-presentation.pptx    # Exported PowerPoint presentation deck
│   ├── prescriptive-analytics-presentation-hallmark.pptx # Alternative styled presentation deck
│   ├── prescriptive-analytics-script.md            # Slide-by-slide spoken presentation script
│   └── Big Data Infographics by Slidesgo.pptx      # Visual reference and infographics assets
│
└── ResearchBurnout/                                # M2 Research Project: Student Burnout Prediction
    ├── .gitignore                                  # Subdirectory rules protecting participant-level records
    ├── Academic_Habits_Lifestyle_and_Burnout_Survey.md # Survey instruments, scales, and candidate predictors
    ├── Burnout_Assessment_Tool_English_Questionnaire.md # Structured transcription of BAT-S (Student version)
    ├── PaperMetadata.csv                           # Curated literature review (100+ academic papers & DOIs)
    └── Research_Project_Handoff.md                 # Complete research project blueprint & methodology
```

---

## Project 1: Prescriptive Analytics

*Module: Decision Support Systems & Advanced Analytics*

### Overview
Prescriptive analytics shifts analytical focus from *what happened* (descriptive) and *what will happen* (predictive) to **"what action should we take given our goals and constraints?"**

### Core Topics Covered
- **Decision Architecture:** Objectives, decision levers, forecasts, and real-world operational constraints.
- **Analytics Maturity:** Comparison across Descriptive, Diagnostic, Predictive, and Prescriptive paradigms.
- **Optimization Methodologies:** Linear Programming (LP), Integer & Mixed-Integer Programming (MIP), Monte Carlo simulation, heuristic search, and Reinforcement Learning (RL).
- **Domain Applications:** Healthcare scheduling, supply chain route optimization, dynamic pricing, and grid energy dispatch.
- **Implementation Challenges:** Data quality sensitivity, computational tractability, model drift, and human-in-the-loop governance.

### Resources
- [prescriptive-analytics-presentation.md](prescriptive-analytics/prescriptive-analytics-presentation.md): Marp Markdown deck formatted for modern slide rendering.
- [prescriptive-analytics-script.md](prescriptive-analytics/prescriptive-analytics-script.md): Slide-by-slide speaking script with talking points, transitions, and timing.
- [prescriptive-analytics-presentation.pptx](prescriptive-analytics/prescriptive-analytics-presentation.pptx): Ready-to-present PowerPoint slide deck.

---

## Project 2: Student Burnout & Continuation Risk Research

*Project Title: Predicting Academic Burnout and Academic Continuation Risk in Low-Sample Regimes Using Explainable Machine Learning*

### Overview
Institutional early warning systems frequently rely on backward-looking administrative metrics (such as historical GPA and attendance) while failing to capture real-time psychological, behavioral, and lifestyle determinants. This study develops an explainable machine learning framework to identify early signs of academic burnout and assess continuation risk under low-sample constraints.

### Key Dimensions & Instruments
- **Burnout Assessment Tool (BAT-S Student Version):** Measures primary burnout dimensions (Exhaustion, Mental Distance, Cognitive Impairment, Emotional Impairment) and secondary symptoms (Depressive Symptoms, Psychological Distress, Psychosomatic Complaints).
- **Academic Habits & Lifestyle Survey:** Collects candidate feature variables including perceived workload intensity, procrastination, sleep duration and satisfaction, screen time, Generative AI reliance, and academic self-efficacy.
- **Explainable AI (XAI):** Uses SHAP (Shapley Additive Explanations) and feature attribution to ensure transparent, actionable insights for academic advising.
- **Literature Review:** 100+ curated research papers indexing student attrition, educational data mining, and explainable AI in higher education.

### Resources
- [Research_Project_Handoff.md](ResearchBurnout/Research_Project_Handoff.md): Full research blueprint, hypotheses, modeling strategies, validation protocols, and ethics standards.
- [Academic_Habits_Lifestyle_and_Burnout_Survey.md](ResearchBurnout/Academic_Habits_Lifestyle_and_Burnout_Survey.md): Structured questionnaire schema and variable mapping.
- [Burnout_Assessment_Tool_English_Questionnaire.md](ResearchBurnout/Burnout_Assessment_Tool_English_Questionnaire.md): Standardized BAT-S transcription.
- [PaperMetadata.csv](ResearchBurnout/PaperMetadata.csv): Filtered literature database containing abstracts, citations, and DOI links.

---

## Data Privacy & Research Ethics

Participant confidentiality is strictly preserved:
- Raw survey responses (`data.csv`, `data.xlsx`, `Responses*.csv`) contain individual student submissions and are **excluded from version control** via `.gitignore`.
- No personally identifiable information (PII) is committed to this repository.

---

## Tools & Usage

### Marp Slides (Prescriptive Analytics)
To view or export the presentation slides locally:
```bash
# Using VS Code Marp extension:
# Open prescriptive-analytics/prescriptive-analytics-presentation.md and click preview

# Or using Marp CLI:
npx @marp-team/marp-cli@latest prescriptive-analytics/prescriptive-analytics-presentation.md --pdf
```

---

## Author

- **Ali Omar** — Master 2 (M2)  
- GitHub: [@aliomar139](https://github.com/aliomar139)
