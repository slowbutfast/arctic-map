# **10m Scale Roads**

**Theme:** Infrastructure
**Subtheme:** Transportation
**Layer Name in Database:** `a_clean_ne_10m_roads`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Transportation** subcategory.
3. Check the box next to **10m Scale Roads** to display it on the map.

--- 

**Title:** ne_10m_roads  
**Abstract:** This dataset represents road locations throughout the world at a 10m scale. It includes information on the type of road, country, length, toll information, expressway status, continent, and for many the name of the roads as well.  
**Purpose:**The dataset aims to provide an overview of the global road network to assist with mapping the transit routes for both people and goods.  
**Keywords:** roads, country, expressway GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.177684 deg; Bottom: \-55.112124 deg; Left: \-166.532488 deg; Right: 178.419079 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
“Edited”, “namealt”, “routeraw”, “question”, “ne_part”, “label”, “label2”, “local”, “localtype” “localalt”, “ignore”, “add”, “rwdb_rd_id”, “orig_fid”, “min_zoom”, and “min_label” attributes were deleted.    
**Quality Information:**

* Accuracy:  
* Completeness: Not every road has a name, namealtt, note, level, or prefix  
* Consistency: 

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: Natural Earth  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ne_10m_roads.shp | WGS 1984 | Line | 56,600 | 33 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | scalerank | Long | From 3 to 10 |
|  |  |  |  |  | featurecla | Text (30) | “Road” or “ferry” |
|  |  |  |  |  | type | Text (50) | “Beltway”, “Bypass”, “Ferry Route”, “Ferry, seasonal”, “Major Highway”, “Road”, “Secondary Highway”, “Track”, or “Unknown” |
|  |  |  |  |  | sov_a3 | Text (3) | 3- letter country abbreviation |
|  |  |  |  |  | note | Text (50) | Almost all blank, just a select few talk about who operartes the ferry for example |
|  |  |  |  |  | name | Text (25) | Letters or number codes |
|  |  |  |  |  | namealtt | Text (30) | Almost all blank, some say federal, Interstate, State, or A1 |
|  |  |  |  |  | length_km | Long | Length in km |
|  |  |  |  |  | toll | Short | 1 or 0 |
|  |  |  |  |  | labelrank | Short | 1-8 |
|  |  |  |  |  | prefix | Text (5) | E, I, US, or blank |
|  |  |  |  |  | uident | Long | numbers |
|  |  |  |  |  | continent | Text (50) | continent |
|  |  |  |  |  | expressway | Short | 0 or 1 |
|  |  |  |  |  | level | Text (50) | Blank, “E”, “Federal”, “State”, “Ferry”, “Interstate”, “U/C”, or “Other” |

#