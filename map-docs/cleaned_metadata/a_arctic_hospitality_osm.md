# **Arctic Hospitality**

**Theme:** Socioeconomic
**Subtheme:** Human Settlements
**Layer Name in Database:** `a_arctic_hospitality_osm`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Human Settlements** subcategory.
3. Check the box next to **Arctic Hospitality** to display it on the map.

--- 

**Title:** a_Arctic_Hospitality_OSM  
**Abstract:** This dataset represents the locations of buildings relating to hospitality in the Arctic.   
**Purpose:** The dataset aims to provide the locations and identities of hospitality buildings in the Arctic to aid with spatial reference.   
**Keywords:** Arctic, Hospitality, OSM  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box:  
  * Top	78.655175	deg  
  * Bottom	51.482985	deg  
  * Left	\-174.203331	deg  
  * Right	177.740687	deg

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
| a_Arctic_Hospitality_OSM.shp | WGS 1984 | Point | 2867 | 13 | FID | OID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID_Arctic | Integer |  |
|  |  |  |  |  | osm_id | String |  |
|  |  |  |  |  | code | SmallInteger |  |
|  |  |  |  |  | fclass | String | Type of building (e.g. guesthouse, hostel, hotel, motel) |
|  |  |  |  |  | name | String | Name of the building |
|  |  |  |  |  | type | String | Type of building (e.g. guesthouse, hostel, hotel, motel) |
|  |  |  |  |  | ORIG_FID | Integer |  |
|  |  |  |  |  | FID_arct_1 | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape_Leng | Double |  |
|  |  |  |  |  | Shape_Area | Double |  |