# **Arctic Regions**

**Theme:** Socioeconomic
**Subtheme:** Administrative & Geographic Boundaries
**Layer Name in Database:** `a_clean_arctic_regions`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Administrative & Geographic Boundaries** subcategory.
3. Check the box next to **Arctic Regions** to display it on the map.

--- 

**Title:** Arctic Regions  
**Abstract:** This dataset represents regions in the Arctic. It includes information on the name of the region, and for some of the regions, the classification of the territory and the country it resides in.   
**Purpose:**The dataset aims to outline the regions of the Arctic visually while providing name information.   
**Keywords:** Arctic, Territory, Russia, Greenland  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 83.658333 deg; Bottom: 83.658333 deg; Left: 51.209721 deg; Right: 180.000000 deg

**Spatial Resolution**: XY resolution: 0.0000000000000888178419700125 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
“ID”, “Shape_Leng”, “Shape_Area”, “GID_1”, “NAME_1”, “NL_NAME_1”, “GID_2”, “NAME_2”, “NL_NAME_2”, “GID_3”, “NAME_3”, “VARNAME_3”, “NL_NAME_3”, TYPE_3, “ENGTYPE_3”, “CC_3”, “HASC_3”, “VARNAME_1”, “TYPE_1”, “CC_1”, “HASC_1”, and “path” attributes were deleted.   
**Quality Information:**

* Accuracy:  
* Completeness: For the GID_0, NAME_0, and ENGTYPE_1 attributes, only a few rows have data.   
* Consistency: 

**Distribution Information:**

* Format: Shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: \[Describe any restrictions on usage\]

**Metadata Contact:**

* Organization: Tingstad, A., Van Abel, K., Bennett, M.M. *et al.* Divergent trajectories of Arctic change: Implications for future socio-economic patterns. *Ambio* 54, 239–255 (2025). https://doi.org/10.1007/s13280-024-02080-x  
* Position: \[Position of the contact person\]  
* Email: \[Contact email address\]  
* Phone: \[Contact phone number\]

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of record | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| ArcticRegions.shp | WGS 1984 | Polygon  | 19 | 28 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | GID_0 | Text (80) | 3-letter code abbreviation of NAME_0 attribute, or blank |
|  |  |  |  |  | NAME_0 | Text (80) | Name of region, or blank |
|  |  |  |  |  | ENGTYPE_1 | Text (80) | “Territory”, “Region”, or blank |
|  |  |  |  |  | layer | Text (254) | Says nation/region place is in |

#