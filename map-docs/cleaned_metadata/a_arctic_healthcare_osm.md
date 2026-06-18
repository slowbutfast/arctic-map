# **Arctic Healthcare**

**Theme:** Socioeconomic
**Subtheme:** Human Settlements
**Layer Name in Database:** `a_arctic_healthcare_osm`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Human Settlements** subcategory.
3. Check the box next to **Arctic Healthcare** to display it on the map.

--- 

**Title:** a_Arctic_Healthcare_OSM  
**Abstract:** This dataset represents the locations of buildings relating to healthcare in the Arctic.   
**Purpose:** The dataset aims to provide the locations and identities of healthcare buildings in the Arctic to aid with spatial reference.   
**Keywords:** Arctic, Healthcare, OSM  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box:   
  * Top	78.654815	deg  
  * Bottom	51.485214	deg  
  * Left	\-179.122174	deg  
  * Right	177.693895	deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
Data is in original format.  
**Quality Information:**

* Accuracy:  
* Completeness: Every row except for “name”, in which many rows are blank, has each attribute filled, creating a nearly complete dataset.   
* Consistency: 

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: N/A  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: OpenStreetMap (OSM)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| a_Arctic_Healthcare_OSM.shp | WGS 1984 | Point | 1763 | 13 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID_Arctic | Integer |  |
|  |  |  |  |  | osm_id | String |  |
|  |  |  |  |  | code | SmallInteger |  |
|  |  |  |  |  | fclass | String | Type of building (e.g. clinic, dentist, doctors, hospital) |
|  |  |  |  |  | name | String | Name of the building |
|  |  |  |  |  | type | String | Type of building (e.g. clinic, dentist, doctors, hospital) |
|  |  |  |  |  | ORIG_FID | Integer |  |
|  |  |  |  |  | FID_arct_1 | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape_Leng | Double |  |
|  |  |  |  |  | Shape_Area | Double |  |