# **Global Mineral Resource Occurrences**

**Theme:** Environmental
**Subtheme:** Natural Resources
**Layer Name in Database:** `global_mineral_resource_occurrences`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Environmental** category.
2. Expand the **Natural Resources** subcategory.
3. Check the box next to **Global Mineral Resource Occurrences** to display it on the map.

--- 

**Title:** global_mineral_resource_occurrences  
**Abstract:** This dataset consolidates global mineral resource occurrence information, primarily focusing on the United States, by integrating records from the [USGS's Mineral Resource Data System (MRDS)](https://mrdata.usgs.gov/mrds/) and the U.S. Bureau of Mines' (now USGS) Mineral Availability System/Mineral Industry Locator System (MAS/MILS). Developed over decades, the MRDS aimed for complete U.S. coverage, making its international data less comprehensive. Critically, the information's currency is limited to the original source reports, some of which are no longer available, meaning operational statuses, ownership, production figures, and resource estimates are likely outdated; however, geological characteristics of the mineral resources generally remain accurate.  
**Purpose:** This digest of the complex mineral resources database is intended for use as reference material supporting mineral resource and environmental assessments on local to regional scale worldwide.  
**Keywords:** mine site, mineral deposit areas, mineral resources  
**Temporal Extent:**

* **Date**: 3/15/2016  
* **Time Period**: 

**Geographic Extent:** 

* Bounding Box:   
  * Top	85.003744	deg  
  * Bottom	51.255673	deg  
  * Left	\-180.002618	deg  
  * Right	180.001993	deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** 

* Projected Coordinate System: WGS 1984

**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: All features have values for each of the attributes.  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: none  
* Use Constraints: Haddaway, N.R., Smith, A., Taylor, J.J., Andrews, C., Cooke, S.J., Nilsson, A.E. and Lesser, P., 2022\. Evidence of the impacts of metal mining and the effectiveness of mining mitigation measures on social–ecological systems in Arctic and boreal regions: a systematic map. Environmental Evidence, 11(1), 30

**Metadata Contact:**

* Organization: USGS Geology, Energy, and Minerals Science Center  
* Position: Peter N Schweitzer, Geologist  
* Email: pschweitzer@usgs.gov

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| global_mineral_resource_occurrences.shp | WGS 1984 | Point | 13,141 | 5 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | SITE_NAME | String | Name of the site, deposit, or operation. |
|  |  |  |  |  | DEV_STAT | String | Status of development of the resource or operation. |
|  |  |  |  |  | CODE_LIST | String |  |