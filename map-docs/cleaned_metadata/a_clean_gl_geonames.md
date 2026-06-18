# **Greenland Geonames (human settlements and natural features)**

**Theme:** Socioeconomic
**Subtheme:** Human Settlements
**Layer Name in Database:** `a_clean_gl_geonames`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Human Settlements** subcategory.
3. Check the box next to **Greenland Geonames (human settlements and natural features)** to display it on the map.

--- 

**Title**: GreenLand Geonames   
**Abstract**: This dataset includes various types of geographic features such as cities, towns, natural features (like mountains, lakes, and rivers), and other significant landmarks. The "Greenland Geonames" shapefile serves as an essential reference for mapping, navigation, and geographical analysis, providing a detailed catalog of named locations throughout the country.  
**Purpose**: The shapefile is to provide an authoritative and standardized geospatial representation of geographic names across Greenland. This dataset aims to support a wide range of applications, including mapping and cartography and geospatial analysis.   
**Keywords:** GreenLand Geography, Place Names, Cartography   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 83.666670 degree Bottom: 59.723060 degree Left: \-73.167570 degree Right: \-12.133330 degree**

**Spatial Resolution:** 0.0000000000000101642427807746 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: Field 9, 10, 12, 13,14,15,16,17 etc are removed because these attributes are blank, and some numbers are random. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 7527 records.   
- **Consistency**: The dataset is consistent with 13 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** [GeoNames](https://www.geonames.org/export/)  
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| GL_Geonames | WGS 1984  | Point | 7527 | 13 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Field1 | Long | Long numeric code |
|  |  |  |  |  | Field2 | Text | Name of location, such as “Kap Wynn” |
|  |  |  |  |  | Field3 | Text | Seems to be exactly the same as Field2 |
|  |  |  |  |  | Field4 | Text | Seems to be alternate names for field1. Most rows are blank |
|  |  |  |  |  | Field5 | Double | Seems to be latitude |
|  |  |  |  |  | Field6 | Double | Seems to be longitude |
|  |  |  |  |  | Field7 | Text | Is a letter A, H, T, V, L, P, R, or S not defined anywhere |
|  |  |  |  |  | Field8 | Text | Defines the location as the type of country, state, region….steam, lake…with codes defined in the GeoNames_CODES file located in the GeoNames section of settlements file |
|  |  |  |  |  | Field11 | Long | An undefined number 0-7, or one of two obscure long numbers |
|  |  |  |  |  | Field18 | Text | Seems to say the region, such as “America/Thule” |
|  |  |  |  |  | Field19 | Date | An unspecified date..maybe when data was collected |

#