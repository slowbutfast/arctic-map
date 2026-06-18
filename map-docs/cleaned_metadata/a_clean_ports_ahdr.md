# **AHDR Ports**

**Theme:** Infrastructure
**Subtheme:** Transportation
**Layer Name in Database:** `a_clean_ports_ahdr`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Transportation** subcategory.
3. Check the box next to **AHDR Ports** to display it on the map.

--- 

**Title:** AHDR_Ports  
**Abstract:** This dataset represents Airport locations throughout the Arctic. It includes information on the name, Natural Earth ID, and in some cases the website of the port.  
**Purpose:**The dataset aims to provide information on Arctic port locations to assist in transportation decisions in the Arctic while dealing with Arctic development.  
**Keywords:** Ports, Arctic, ne_id, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 78.226111 deg; Bottom: 53.384444 deg; Left: \-165.425147 deg; Right: 177.538634 deg

**Spatial Resolution**: XY Resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: Considering the high spatial resolution and low tolerance of 0.00000000898315284119521 Degree, this is an accurate dataset.   
* Completeness: Data set lacks an attribute for the nation or area of the Port.   
* Consistency: Not every Port has a website, leading to inconsistent amounts of information for each one. 

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
| AHDR_Ports.shp | WGS 1984 | point | 52 | 8 | FID | Object ID |  |
|  |  |  |  |  | scalerank | Short |  |
|  |  |  |  |  | featurecla | Text (80) | Each one says “Port” |
|  |  |  |  |  | name | Text (50) | Appears to be name of port |
|  |  |  |  |  | website | Text (254) |  |
|  |  |  |  |  | ne_id | Long | Natural earth id |

# 

#