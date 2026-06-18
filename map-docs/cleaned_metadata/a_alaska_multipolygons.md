# **Alaska Multipolygons (geographic and administrative boundaries) **

**Theme:** Socioeconomic
**Subtheme:** Administrative & Geographic Boundaries
**Layer Name in Database:** `a_alaska_multipolygons`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Socioeconomic** category.
2. Expand the **Administrative & Geographic Boundaries** subcategory.
3. Check the box next to **Alaska Multipolygons (geographic and administrative boundaries) ** to display it on the map.

--- 

**Title**: Alaska multipolygons  
**Abstract**: The "Alaska_multipolygons" shapefile is a detailed geospatial dataset that contains multipolygon geometries representing various geographic and administrative boundaries within the state of Alaska. This dataset includes multiple types of polygons such as land parcels, protected areas, municipal boundaries, and other significant regions.  
**Purpose**: The purpose of the "Alaska_multipolygons" shapefile is to provide a comprehensive geospatial representation of various multipolygonal boundaries within Alaska. This dataset aims to support a wide range of applications, including land management and planning, environmental conservation.   
**Keywords:** Alaska multipolygons, administrative boundaries  
**Temporal Extent:** 

- **Date:** NA  
- **Time Period:** NA

**Geographic Extent:** 

- **Bounding Box: Top: 66.900787 degree Bottom: 55.205761 degree Left: \-165.398375 degree Right: \-134.632787 degree**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The fields: addr_unit, building_l, operator etc are removed because these attributes are blank and do not serve any useful purpose. 

**Quality Information:** 

- **Accuracy**: NA  
- **Completeness:** The dataset is complete with 14 records.   
- **Consistency**: The dataset is consistent with 22 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** NordRegio   
* **Position:** NA  
* **Email:** NA  
* **Phone:**  NA

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Alaska_multipolygons.shp | WGS 1984 | Polygon | 14 | 22 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | full_id  | String | If osm_type is relation, full_id starts with r. If osm_type is way, full_id starts with w.  |
|  |  |  |  |  | osm_id  | String  | Open Street Map ID, the only difference is that osm_id doesn’t start with a letter.  |
|  |  |  |  |  | osm_type  | String | Open Street Map Type. It’s either relation or way.  |
|  |  |  |  |  | amenity  | String  | All the amenity type is university.  |
|  |  |  |  |  | phone  | String  |  |
|  |  |  |  |  | layer  | String |  |
|  |  |  |  |  | building  | String  | Only contains two datapoint: university, yes.  |
|  |  |  |  |  | wikipedia  | String |  |
|  |  |  |  |  | wikidata  | String |  |
|  |  |  |  |  | website  | String |  |
|  |  |  |  |  | operator_t  | String  | Two datapoints say public.  |
|  |  |  |  |  | addr_stree  | String | street |
|  |  |  |  |  | addr_state  | String  | state |
|  |  |  |  |  | addr_postc  | String | Postal code |
|  |  |  |  |  | addr_house | String | House Number |
|  |  |  |  |  | addr_city  | String  | City |
|  |  |  |  |  | type  | String | Geometric types: multipolygons |
|  |  |  |  |  | name  | String |  |

#