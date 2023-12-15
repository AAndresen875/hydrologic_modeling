# Hydrologic Modeling of Small watersheds

This repo is meant to back up the work related to hydrologic modeling of small watersheds. 

Much of this repo is guided by Bruce N. Wilson Hydrologic Modeling of Small Watersheds and the class BBE 8513 at the University of Minnesota Twin Cities.

```mermaid
---
title: Hydrologic models water balance
---
flowchart TD
    A{air} --> |Precipitation|B[Vegetative Interception]
    B[Vegetative Interception] --> |Evapotranspiration|A
    B -->|Throughfall| C[Surface Detention and Depressional Storage]
    C --> |Evapotranspiration| B
    C --> |Overland Flow|D[Channel Storage]
    A --> |Precipitation|D
    C ---->|Infiltration| E[Soil Storage]
    E-->|percolation|G[Groundwater Storage]
    G --> |Transpiration|A
    G--> |Base Flow|D
    E-->|Evaporation/ Transpiration|A
    E-->|Interflow|D
    D-->|Evaporation|A
    D-->F{Watershed Hydrograph}
```

