# **Canada Geonames (human settlements and natural features)**

**Theme:** Socioeconomic
**Subtheme:** Human Settlements
**Layer Name in Database:** `a_clean_ca_geonames`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Human Settlements** subcategory.
3. Check the box next to **Canada Geonames (human settlements and natural features)** to display it on the map.

--- 

**Title**: CA Geonames   
**Abstract**: This dataset includes various types of geographic features such as cities, towns, natural features (like mountains, lakes, and rivers), and other significant landmarks. The "Canada Geonames" shapefile serves as an essential reference for mapping, navigation, and geographical analysis, providing a detailed catalog of named locations throughout the country.  
**Purpose**: The shapefile is to provide an authoritative and standardized geospatial representation of geographic names across Canada. This dataset aims to support a wide range of applications, including mapping and cartography and geospatial analysis.   
**Keywords:** Canadian Geography, Place Names, Cartography   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 83.122240 degree Bottom: 41.654440 degree Left: \-141.005420 degree Right: \-48.500000 degree**

**Spatial Resolution:** 0.0000000000000154052470779931 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: Field 1, 7, 19 etc are removed because these attributes are blank. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 314328 records.   
- **Consistency**: The dataset is consistent with 18 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:**   
**Organization:** [GeoNames](https://www.geonames.org/export/)  
**Position:** NA  
**Email:** NA  
**Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| CA_Geonames | WGS 1984  | Point | 314328 | 18  | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | Field2 | Text | Name of location, such as “Aarons Hill” |
|  |  |  |  |  | Field3 | Text | Seems to be exactly the same as Field2 |
|  |  |  |  |  | Field4 | Text | Seems to be alternate names for field1. Most rows are blank |
|  |  |  |  |  | Field5 | Double | Seems to be latitude |
|  |  |  |  |  | Field6 | Double | Seems to be longitude |
|  |  |  |  |  | Field8 | Text | Defines the location as the type of country, state, region….steam, lake…with codes defined in the GeoNames_CODES file located in the GeoNames section of settlements file |
|  |  |  |  |  | Field9 | Text | All say “CA” |
|  |  |  |  |  | Field10 | Text | Only 14 rows have data saying US or CA,US |
|  |  |  |  |  | Field11 | Long | An undefined value 0-14 |
|  |  |  |  |  | Field12 | Long | An undefined long numerical value |
|  |  |  |  |  | Field13 | Long | Another long undefined numerical value |
|  |  |  |  |  | Field14 | Text | Either a two digit number or a two letter code, or blank. 2 letter codes are undefined in the GeoNames_CODES database.  |
|  |  |  |  |  | Field15 | Long | Long number, or 0 |
|  |  |  |  |  | Field16 | Long | Up to a 4 digit numeric code, or 0 |
|  |  |  |  |  | Field17 | Long | Up to a 4 digit numeric code, or 0 |
|  |  |  |  |  | Field18 | Text | States region, or is blank |

# 

#