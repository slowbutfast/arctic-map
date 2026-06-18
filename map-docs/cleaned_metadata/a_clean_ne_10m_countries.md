# **Administrative Country Boundaries**

**Theme:** Socioeconomic
**Subtheme:** Administrative & Geographic Boundaries
**Layer Name in Database:** `a_clean_ne_10m_countries`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Administrative & Geographic Boundaries** subcategory.
3. Check the box next to **Administrative Country Boundaries** to display it on the map.

--- 

**Title:** ne_10m_countries  
**Abstract:** This dataset represents country boundaries. It includes information on the population, sovereignty, GDP, development stage, and region of the world of each country.  
**Purpose:**The dataset aims to provide an overview of the demographics of each country and each country's recognized borders, as opposed to those of nations or states.  
**Keywords:** countries, GDP, population, GIS  
**Temporal Extent:**

* **Date**: \[Date of data collection\]  
* **Time Period**: \[Start date \- End date\]

**Geographic Extent:** 

* Bounding Box: Top: 83.634101 deg; Bottom: \-90.000000 deg; Left: \-180.000000 deg; Right: 180.000000 deg

**Spatial Resolution**: XY resolution: 0.000000000899322046075566 Degree  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
The attributes of Featurecla, scalerank, LABELRANK, ADMO_DIF, LEVEL, TLC, ADMIN, ADM0_A3, GEOU_DIF, GEOUNIT, GU_A3, SU_DIF, SUBUNIT, SU_A3, BRK_DIFF, NAME, NAME_LONG, BRK_A3, BRK_NAME, BRK_GROUP, ABBREV, POSTAl, FORMAL_EN, FORMAL_FR, NAME_CIAWF, NOTE_ADM0, NOTE_BRK, NAME_SORT, NAME_ALT, MAPCOLOR7, MAPCOLOR8, MAPCOLOR9, MAPCOLOR13, GDP_MD, WOE_ID_EH, as well as country names and abbreviations in a vast array of languages, have been deleted from the original dataset to create this cleaned dataset.   
**Quality Information:**

* Accuracy:  
* Completeness: Each row has each attribute, creating a very complete dataset.   
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
| ne_10m_admin_0_countries.shp | WGS 1984 | polygon | 258 | 169 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | SOVEREIGNT | Text (15) | Country it is |
|  |  |  |  |  | SOV_A3 | Text (3) | 3- letter country abbreviation |
|  |  |  |  |  | TYPE | Text (17) | Status of sovereignty  |
|  |  |  |  |  | POP_EST | Double (11, 1\) | Estimation of population |
|  |  |  |  |  | POP_RANK | Short | Number in the 0’s and 10’s |
|  |  |  |  |  | POP_YEAR | Short | Year population was recorded: 2020 or 201964 |
|  |  |  |  |  | GDP_YEAR | Short | Year GDP_MD was recorded |
|  |  |  |  |  | ECONOMY | Text (16) | Ranked from 1-7 with how developed the economy is  |
|  |  |  |  |  | INCOME_GRP | Text (23) | Ranked from 1-5 with high-low income  |
|  |  |  |  |  | WOE_ID | Long | 32-bit ID that corresponds to a feature on earth |
|  |  |  |  |  | WOE_NOTE | Text (167) | Whether the WOE_ID is an exact match or not |
|  |  |  |  |  | REGION_UN | Text (10) |  |
|  |  |  |  |  | SUBREGION | Text (25) |  |
|  |  |  |  |  | WIKIDATAID | Text (8) |  |
|  |  |  |  |  | FCLASS_TLC | Text (21) | Dependency, country etc |

#