# west-africa-rainfall-shear-analysis
This repository contains code and data for analyzing the relationship between boundary layer vertical wind shear and rainfall onset over West Africa. The project aims to investigate how atmospheric conditions, specifically wind shear in the boundary layer, influence the initiation of rainfall in the West African region.


# West Africa Rainfall and Wind Shear Analysis

## Overview

This repository contains code and data for a research project exploring the relationship between boundary layer vertical wind shear and rainfall onset over West Africa. Understanding these atmospheric dynamics is crucial for predicting and managing weather patterns in the region.

## Project Structure

- **data**: Contains datasets used for the analysis.
- **scripts**: Holds the Python scripts and Jupyter notebooks for data processing, analysis, and visualization.
- **results**: Stores the results and visualizations obtained from the analysis.

## Requirements

- Python 3.x
- Jupyter Notebooks
- Required Python packages can be installed using: `pip install -r requirements.txt`

## Usage

1. Clone the repository: `git clone https://github.com/your-username/west-africa-rainfall-shear-analysis.git`
2. Navigate to the project directory: `cd west-africa-rainfall-shear-analysis`
3. Install dependencies: `pip install -r requirements.txt`
4. Explore the Jupyter notebooks in the `scripts` directory for data analysis and visualization.

## Data Sources

### ERA5 Datasets:

#### Data - 1: Total Precipitation

- **Product Type:** Monthly averaged reanalysis by hour of day
- **Variable:** Total precipitation
- **Pressure Level:** Not specified
- **Sub-region Extraction:** North 20°, West -20°, South -5°, East 25°
- **Format:** NetCDF (experimental)

#### Data - 2: V-component of Wind

- **Product Type:** Monthly averaged reanalysis by hour of day
- **Variable:** V-component of wind
- **Pressure Level:** 200 hPa, 800 hPa
- **Sub-region Extraction:** North 20°, West -20°, South -5°, East 25°
- **Format:** NetCDF (experimental)

#### Data - 3: U-component of Wind

- **Product Type:** Monthly averaged reanalysis by hour of day
- **Variable:** U-component of wind
- **Pressure Level:** 200 hPa, 800 hPa
- **Sub-region Extraction:** North 20°, West -20°, South -5°, East 25°
- **Format:** NetCDF (experimental)

### CMIP5 Datasets:

#### Data - 1: Mean Precipitation Flux

- **Experiment:** RCP 4.5
- **Variable:** Mean precipitation flux
- **Model:** GFDL-CM2p1 (NOAA, USA)
- **Ensemble Member:** r10i1p1
- **Period:** 200601-201012, 201101-201512, 201601-202012
- **Format:** Zip file (.zip)

#### Data - 2: V-component of Wind

- **Experiment:** RCP 4.5
- **Variable:** V-component of wind
- **Model:** GFDL-CM2p1 (NOAA, USA)
- **Ensemble Member:** r10i1p1
- **Period:** 200601-201012, 201101-201512, 201601-202012
- **Format:** Zip file (.zip)

#### Data - 3: U-component of Wind

- **Experiment:** RCP 4.5
- **Variable:** U-component of wind
- **Model:** GFDL-CM2p1 (NOAA, USA)
- **Ensemble Member:** r10i1p1
- **Period:** 200601-201012, 201101-201512, 201601-202012
- **Format:** Zip file (.zip)


## Results

### Key Findings

Both detailed results and key findings can be found in the following Jupyter Notebooks:

- [CMIPS Analysis](./CMIPS_Analysis.ipynb)
- [ERA5 Analysis](./ERA5_Analysis.ipynb)

Navigate to these notebooks to explore in-depth analyses, visualizations, and insights into the relationship between boundary layer vertical wind shear and rainfall onset over West Africa.

Feel free to open the notebooks in a Jupyter environment to interact with the code and explore the findings in detail.

### Visualizations

Charts and graphs from the analysis can be found in the `figures` folder in this repository. Navigate to the [`figures`](./figures) directory to view visual representations of the data.

Feel free to explore the visualizations to gain insights into the relationship between boundary layer vertical wind shear and rainfall onset over West Africa.


## Contribution Guidelines

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`
3. Make your changes and commit: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature/new-feature`
5. Create a pull request.


