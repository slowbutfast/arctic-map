# **Sweden Geonames (human settlements and natural features)**

**Theme:** Socioeconomic
**Subtheme:** Human Settlements
**Layer Name in Database:** `sweden_geonames`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Human Settlements** subcategory.
3. Check the box next to **Sweden Geonames (human settlements and natural features)** to display it on the map.

--- 

**Title**: Sweden Geonames   
**Abstract**: This dataset includes various types of geographic features such as cities, towns, natural features (like mountains, lakes, and rivers), and other significant landmarks. The "Sweden Geonames" shapefile serves as an essential reference for mapping, navigation, and geographical analysis, providing a detailed catalog of named locations throughout the country.  
**Purpose**: The shapefile is to provide an authoritative and standardized geospatial representation of geographic names across Sweden. This dataset aims to support a wide range of applications, including mapping and cartography and geospatial analysis.   
**Keywords:** Sweden Geography, Place Names, Cartography   
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 69.050000 degree Bottom: 55.050000 degree Left: 10.816670 degree Right: 24.166670 degree**

**Spatial Resolution:** 0.00000000000000233146835171283 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The field cc2 (alternate country codes) is removed because these attributes are blank. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 7554 records.   
- **Consistency**: The dataset is consistent with 19 attributes. 

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
| SE_Geonames | WGS 1984  | Point | 7554 | 19 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | geonameid | Long | Long numeric code |
|  |  |  |  |  | name | Text | Name of location, such as “Kap Wynn” |
|  |  |  |  |  | asciiname | Text | Seems to be exactly the same as Field2, but without any umlauts, other special letter forms |
|  |  |  |  |  | alternatenames | Text | alternate names for the locations. Most rows are blank |
|  |  |  |  |  | latitude | Double | Latitude in decimal degrees |
|  |  |  |  |  | longitude | Double | Longitude in decimal degrees |
|  |  |  |  |  | Feature class | Text | see http://www.geonames.org/export/codes.html |
|  |  |  |  |  | Feature code | Text | Defines the location as the type of country, state, region….stream, lake…see http://www.geonames.org/export/codes.html |
|  |  |  |  |  | Admin1 code | Long | Fipscode, A number 0-28 |
|  |  |  |  |  | Admin2 code | Long | Code for the second administrative division, a county in the US |
|  |  |  |  |  | Admin3 code | Long | Code for the third level administrative division |
|  |  |  |  |  | Admin4 code | Long | Code for the fourth level administrative division, many rows say 0 |
|  |  |  |  |  | population | Long |  |
|  |  |  |  |  | elevation | Text | In meters |
|  |  |  |  |  | dem | Long | Digital elevation model, srtm3 or gtopo30, average |
|  |  |  |  |  | timezone | Text | The iana timezone id |
|  |  |  |  |  | Modification date | Date | Date of last modification in yyyy-MM-dd format |

#