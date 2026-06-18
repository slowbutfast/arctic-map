# **SSP 126 Low Emission Scenario for 2019**

**Theme:** Infrastructure
**Subtheme:** Shipping Routes
**Layer Name in Database:** `route_ssp126_2019`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Shipping Routes** subcategory.
3. Check the box next to **SSP 126 Low Emission Scenario for 2019** to display it on the map.

--- 

**Title:** route_ssp126_2019  
**Abstract:** This dataset represents daily navigable Arctic marine shipping routes simulated under the SSP126 emissions scenario specifically for the year **2019**. It is a subset of the master low-emissions scenario dataset, derived from CMIP6 model projections. The routes were generated assuming a non-ice-strengthened vessel traveling between Rotterdam and the Bering Strait. Each route is based on sea ice conditions modeled by one of 14 CMIP6 general circulation models (GCMs) and spans multiple years and days. The dataset includes attributes for date and contributing climate model. These routes reflect potential Arctic accessibility patterns under a specific climate future scenario.  
**Purpose:** To assess Arctic marine accessibility under a **low-emissions**, sustainable development scenario (SSP1-2.6), where rapid global cooperation, renewable energy transition, and climate mitigation limit future warming and sea ice loss.  
**Keywords:** shipping routes, climate model  
**Temporal Extent:**

* **Date**: 2021  
* **Time Period**: 2015-2065

**Geographic Extent:** 

* Bounding Box:   
  * Top	2,635,762.186500	m  
  * Bottom	\-3,321,766.612412	m  
  * Left	\-2,439,534.585600	m  
  * Right	2,011,649.433400	m

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** 

* Projected Coordinate System: North_Pole_Lambert_Azimuthal_Equal_Area

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: 

**Metadata Contact:**

* Organization:   
  * Li, X., & Lynch, A. H. (2023). New insights into projected Arctic sea road: Operational risks, economic values, and policy implications. Climatic Change, 176(30). https://doi.org/10.1007/s10584-023-03505-4  
  * Lynch, A. H., Norchi, C. H., & Li, X. (2022). The interaction of ice and law in Arctic marine accessibility. Proceedings of the National Academy of Sciences, 119(26), e2202720119. https://doi.org/10.1073/pnas.2202720119  
  * Li, X., Stephenson, S. R., Lynch, A. H., Goldstein, M. A., Bailey, D. A., & Veland, S. (2021). Arctic shipping guidance from the CMIP6 ensemble on operational and infrastructural timescales. Climatic Change, 167(1), 23\. https://doi.org/10.1007/s10584-021-03172-3  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| route_ssp126_2019.shp | North_Pole_Lambert_Azimuthal_Equal_Area | Shapefile | 64,094 | 7 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Year | String |  |
|  |  |  |  |  | Month | String |  |
|  |  |  |  |  | Day | String |  |
|  |  |  |  |  | Model | String |  |