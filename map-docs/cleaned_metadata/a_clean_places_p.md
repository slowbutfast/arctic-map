# **Wilson Center Infrastructure Projects**

**Theme:** Infrastructure
**Subtheme:** General
**Layer Name in Database:** `a_clean_places_p`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **General** subcategory.
3. Check the box next to **Wilson Center Infrastructure Projects** to display it on the map.

--- 

**Title**: Places_P  
**Abstract**: This dataset includes critical infrastructure such as buildings, utilities, along with significant locations that are relevant to the Wilson Center's scope of work and influence. The shapefile serves as an essential tool for visualizing and analyzing the distribution and characteristics of these infrastructural elements and places, facilitating research, planning, and decision-making processes.   
**Purpose**: The purpose of the "Infrastructure Wilson Center/Places_P" shapefile is to provide a detailed geospatial representation of infrastructure and notable places associated with the Wilson Center. This dataset aims to support a variety of applications, including policy analysis, urban and regional planning.   
**Keywords:** significant places, urban planning, policy analysis, wilson center   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 3,305,034.338342 m  Bottom: 226,939.278930 m  Left: \-2,061,714.468956 m  Right: 3,336,654.810682 m**

**Spatial Resolution:** 0.00000000305360181585002 Meters  
**Coordinate Reference System:** Alaska Albers Equal Area Conic  
**Lineage:** The fields: NAMEPAR, NAMEALT, NAMEASCII, ADM0CAP, CAPIN, WORLDCITY, ADM0NAME, ADM0_A3, ISO_A2, NOTE, RANK_MAX, RANK_MIN, MEGANAME, LS_NAME, MIN_ZOOM, CAPALT, NAME_EN, NAME_DE, NAME_ES, NAME_FR, NAME_PT, NAME_RU, NAME_ZH, LABEL, NAME_AR, NAME_BN, NAME_EL, NAME_HI, NAME_HU, NAME_ID, NAME_IT, NAME_JA, NAME_KO, NAME_NL, NAME_PL, NAME_SV, NAME_TR, NAME_VI, NAME_FA, NAME_HE, NAME_UK, NAME_UR, NAME_ZHT, GEONAMESID, FCLASS_ISO, FCLASS_US, FCLASS_FR, FCLASS_RU, FCLASS_ES, FCLASS_CN, FCLASS_TW, FCLASS_IN, FCLASS_NP, FCLASS_PK, FCLASS_DE, FCLASS_GB, FCLASS_BR, FCLASS_IL, FCLASS_PS, FCLASS_SA, FCLASS_EG, FCLASS_MA, FCLASS_PT, FCLASS_AR, FCLASS_JP, FCLASS_KO, FCLASS_VN, FCLASS_TR, FCLASS_ID, FCLASS_PL, FCLASS_GR, FCLASS_IT, FCLASS_NL,  FCLASS_SE, FCLASS_BD, FCLASS_UA, FCLASS_TLC, Cntr, ST, X, Y are removed because most of these attributes are blank. If not, these attributes are not very understandable for the audience.  

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 151 records.   
- **Consistency**: The dataset is consistent with 55 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:**   
**Organization:** Wilson Center  
**Position:** NA  
**Email:** NA  
**Phone:**  NA

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Places_P.shp | Alaska Albers Equal Area Conic | Point | 854 | 55 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | FID_clean_ | Integer |  |
|  |  |  |  |  | OBJECTID | Long |  |
|  |  |  |  |  | SCALERANK | Long | 0-8 |
|  |  |  |  |  | NATSCALE | Long | 0-300, seems to be multiples |
|  |  |  |  |  | LABELRANK | Long | 0-2 |
|  |  |  |  |  | FEATURECLA | Text | Blank, Admin-1 capital, Historic place, or Populated place |
|  |  |  |  |  | NAME | Text | Name of place, or blank |
|  |  |  |  |  | MEGACITY | Long | 0 or 1 |
|  |  |  |  |  | SOV0NAME | Text | United States, Russia, Canada, or blank |
|  |  |  |  |  | SOV_A3 | Text | 3-letter country abbreviation |
|  |  |  |  |  | ADM1NAME | Text | State name  |
|  |  |  |  |  | LATITUDE | Double |  |
|  |  |  |  |  | POP_MAX | Double |  |
|  |  |  |  |  | POP_MIN | Double |  |
|  |  |  |  |  | POP_OTHER | Double |  |
|  |  |  |  |  | MAX_POP10 | Double |  |
|  |  |  |  |  | MAX_POP20 | Double |  |
|  |  |  |  |  | MAX_POP50 | Double |  |
|  |  |  |  |  | MAX_POP300 | Double |  |
|  |  |  |  |  | MAX_POP310 | Double |  |
|  |  |  |  |  | TIMEZONE | Text |  |
|  |  |  |  |  | UN_FID | Long |  |
|  |  |  |  |  | POP1950 | Double |  |
|  |  |  |  |  | POP1955 | Double |  |
|  |  |  |  |  | POP1960 | Double |  |
|  |  |  |  |  | POP1965 | Double |  |
|  |  |  |  |  | POP1970 | Double |  |
|  |  |  |  |  | POP1975 | Double |  |
|  |  |  |  |  | POP1980 | Double |  |
|  |  |  |  |  | POP1985 | Double |  |
|  |  |  |  |  | POP1990 | Double |  |
|  |  |  |  |  | POP1995 | Double |  |
|  |  |  |  |  | POP2000 | Double |  |
|  |  |  |  |  | POP2005 | Double |  |
|  |  |  |  |  | POP2010 | Double |  |
|  |  |  |  |  | POP2015 | Double |  |
|  |  |  |  |  | POP2020 | Double |  |
|  |  |  |  |  | POP2025 | Double |  |
|  |  |  |  |  | POP2050 | Double |  |
|  |  |  |  |  | WIKIDATAID | Text |  |
|  |  |  |  |  | WOF_ID | Double | Long iD |
|  |  |  |  |  | NE_ID | Double | Cant see how this would be useful |
|  |  |  |  |  | Region | Text | Region, or blank |
|  |  |  |  |  | Code | Text | Many Empty |
|  |  |  |  |  | Sett | Text | Not sure what thjis means |
|  |  |  |  |  | Pop_2017 | Long | Many are 0 but rest have pop |
|  |  |  |  |  | On_Perma | Long | 0 or 1 |
|  |  |  |  |  | State | Text | Alaska or Empty |
|  |  |  |  |  | Name2 | Text | Area name or Empty |
|  |  |  |  |  | FID_arctic | Integer |  |
|  |  |  |  |  | Id | Integer |  |
|  |  |  |  |  | Shape_Leng | Doublee |  |
|  |  |  |  |  | Shape_Area | Douuble |  |

#