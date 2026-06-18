# **Arctic Monthly Average Sea Ice Area**

**Theme:** Environmental
**Subtheme:** Water Resources
**Layer Name in Database:** `arctic_sea_ice_time_series`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Environmental** category.
2. Expand the **Water Resources** subcategory.
3. Check the box next to **Arctic Monthly Average Sea Ice Area** to display it on the map.

--- 

**Title:** arctic_sea_ice_time_series  
**Abstract:** This dataset contains average monthly sea ice area for 1978 to present (2025), in square kilometers, by region of the Arctic Ocean. The Arctic is broken up into 14 regions with boundaries defined by the ASINA team using Meier et al. (2007): Baffin Bay, Barents Sea, Beaufort Sea, Bering Sea, Canadian Archipelago, Central Arctic Ocean, Chukchi Sea, East Siberian Sea, Greenland Sea, Hudson Bay, Kara Sea, Laptev Sea, Sea of Okhotsk, and Gulf of St. Lawrence. The data is sourced from the [NSIDC Sea Ice Index](https://nsidc.org/data/seaice_index), which uses passive microwave remote sensing from the DMSP and JAXA Advanced Microwave Scanning Radiometer 2 (AMSR2) satellites.  
**Purpose:** This dataset provides a long-term, consistent record of average monthly sea ice area in specific regions of the Arctic. It allows for the analysis and tracking of changes in Arctic sea ice over time, which is critical for climate research, environmental monitoring, and understanding the impacts of climate change.  
**Keywords:**   
**Temporal Extent:**

* **Date**:   
* **Time Period**: 1978-2025

**Geographic Extent:** 

* Bounding Box:   
  * Top	89.836816	deg  
  * Bottom	39.169437	deg  
  * Left	\-180.000000	deg  
  * Right	179.763242	deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** 

* Projected Coordinate System: WGS 1984

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: Values for 10 months in 1978 and 11 months in 2025 are missing.  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: Fetterer, F., Knowles, K., Meier, W. N., Savoie, M., Windnagel, A. K. & Stafford, T. (2025). Sea Ice Index. (G02135, Version 4). \[Data Set\]. Boulder, Colorado USA. National Snow and Ice Data Center. https://doi.org/10.7265/a98x-0f50. \[describe subset used if applicable\]. Date Accessed 08-13-2025.

**Metadata Contact:**

* Organization: [National Snow and Ice Data Center](https://nsidc.org/sea-ice-today/sea-ice-tools)  
* Position: NSIDC User Services  
* Email: [nsidc@nsidc.org](mailto:nsidc@nsidc.org) 

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| arctic_sea_ice_time_series.shp | WGS 1984 | Point | 14 | 579 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | region_nam | String | 1/14 Arctic regions:  Baffin Bay, Barents Sea, Beaufort Sea, Bering Sea, Canadian Archipelago, Central Arctic Ocean, Chukchi Sea, East Siberian Sea, Greenland Sea, Hudson Bay, Kara Sea, Laptev Sea, Sea of Okhotsk, Gulf of St. Lawrence |
|  |  |  |  |  | Jan_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Feb_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Mar_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Apr_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | May_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Jun_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Jul_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Aug_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Sep_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Oct_1978 | String | Data unavailable for this month and year |
|  |  |  |  |  | Nov_1978 | Double |  |
|  |  |  |  |  | Dec_1978 | Double |  |
|  |  |  |  |  | Jan_1979 | Double |  |
|  |  |  |  |  | Feb_1979 | Double |  |
|  |  |  |  |  | Mar_1979 | Double |  |
|  |  |  |  |  | Apr_1979 | Double |  |
|  |  |  |  |  | May_1979 | Double |  |
|  |  |  |  |  | Jun_1979 | Double |  |
|  |  |  |  |  | Jul_1979 | Double |  |
|  |  |  |  |  | Aug_1979 | Double |  |
|  |  |  |  |  | Sep_1979 | Double |  |
|  |  |  |  |  | Oct_1979 | Double |  |
|  |  |  |  |  | Nov_1979 | Double |  |
|  |  |  |  |  | Dec_1979 | Double |  |
|  |  |  |  |  | ... | Double |  |
|  |  |  |  |  | Jan_2025 | Double |  |
|  |  |  |  |  | Feb_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Mar_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Apr_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | May_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Jun_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Jul_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Aug_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Sep_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Oct_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Nov_2025 | String | Data unavailable for this month and year |
|  |  |  |  |  | Dec_2025 | String | Data unavailable for this month and year |