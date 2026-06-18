# **Alaskan Airports**

**Theme:** Infrastructure
**Subtheme:** Transportation
**Layer Name in Database:** `a_clean_alaskan_airports`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Transportation** subcategory.
3. Check the box next to **Alaskan Airports** to display it on the map.

--- 

**Title:** Alaskan Airports  
**Abstract:** This dataset represents Airport locations throughout the state of Alaska. It includes information on the location, owner, status, and identifying codes of the airport. .  
**Purpose:**The dataset aims to provide information on Alaskan Airport locations and ownership to assist in transportation decisions in Alaska while dealing with Arctic development.  
**Keywords:** Alaska, Airports, Arctic, FAA_ID, GIS  
**Temporal Extent:**

* **Date**: March 2025  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 71.284889 deg; Bottom: 51.877963 deg; Left: \-176.646046 deg; Right: \-130.010426 deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: [Alaska Department of Transportation](https://dot.alaska.gov/)  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of record | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Airports.shp | WGS 1984 | point | 289 | 12 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | NAME | Text (43) | Full name of airport |
|  |  |  |  |  | OWNER | Text (17) | Who controlls/owns airport |
|  |  |  |  |  | STATUS | Text (20) | Standard or Substandard |
|  |  |  |  |  | REGION | Text (10) | Region of alaska |
|  |  |  |  |  | LAT_DD | Double (23,15) | latitude |
|  |  |  |  |  | LONG_DD | Double (23,15) | longitude |
|  |  |  |  |  | FAA_ID | Text (3) | Identifies airport |

#