# **Global Power Plants**

**Theme:** Infrastructure
**Subtheme:** Energy
**Layer Name in Database:** `a_globalpowerplant`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Energy** subcategory.
3. Check the box next to **Global Power Plants** to display it on the map.

--- 

**Title**: GlobalPowerPlant  
**Abstract**: The database aims to illustrate how World Resources Institute (WRI) experts and their partners created the Global Power Plant Database from official government data and independent sources around the world, integrated them with crowdsourced data such as analysis of satellite images, and delivered the final database as an open data resource.   
**Purpose**: The database explains how the experts addressed three challenges: matching plants across databases, keeping the database up to date, and delivering information on the accuracy of the data.   
**Keywords:** sustainability, power plant, technology, fuel, ownership   
**Temporal Extent:** 

* **Date: NA**  
* **Time Period: NA**

**Geographic Extent:** 

* **Bounding Box: Top: 71.292 Bottom: \-77.847 Left: \-179.9777 Right: 179.3887**

**Spatial Resolution:** 0.0000000000000888178419700125 Degree  
**Coordinate Reference System:** WGS 1984  
**Lineage:** The attributes: wepp_id, year_of_ca, generation, other_fuel, generation_1, generation_2, generation_3, generation_4, generation_5 are removed from the original dataset because most of these attributes are blank. If not, they are also not very informative for the audience.  

**Quality Information:** 

* **Accuracy**: NA  
* **Completeness:** The dataset is complete with 34936 records.   
* **Consistency**: The dataset is consistent with 31 attributes. 

**Distribution Information:** 

* **Format:** Shapefile  
* **Access Constraints**: No constraints   
* **Use Constraints**: No constraints 

**Metadata Contact:** 

* **Organization:** World Resource Institute   
* **Position:**   
* **Email:** logan.byers@wri.org  
* **Phone:**

**Data Dictionary:** 

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| a_globalpowerplant.shp | WGS 1984 | Point | 34936 | 31 |  |  |  |
|  |  |  |  |  | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | country | Text | 3-letter abbreviation |
|  |  |  |  |  | country_lo | Text | Full country name |
|  |  |  |  |  | name | Text | Name of power plant |
|  |  |  |  |  | gppd_idnr | Text | “10 or 12 character identifier for the power plant” |
|  |  |  |  |  | capacity_mw | Double | “electrical generating capacity in megawatts” |
|  |  |  |  |  | latitude | Double |  |
|  |  |  |  |  | longitude | Double |  |
|  |  |  |  |  | primary_fu | Text | “energy source used in primary electricity generation or export” |
|  |  |  |  |  | commission | Double | When it started operating |
|  |  |  |  |  | owner | Text | Who owns power plant |
|  |  |  |  |  | source | Text | Information source |
|  |  |  |  |  | url | Text | Website for power plant |
|  |  |  |  |  | geolocatio | Text |  |
|  |  |  |  |  | wepp_id | Long | “a reference to a unique plant identifier in the widely-used PLATTS-WEPP database” (from README file) |
|  |  |  |  |  | year_of_ca | Long | Many say 0 but others have actual years like 2019 so doesnt seem useful, but data that is there is year capacity data was reported |
|  |  |  |  |  | generation | Text | Empty: *Also not empty if sorted by descending but does not seem to be useful, unless it’s how much energy is generated:* From what i’ve pieced together, this is gWh generated in 2013 |
|  |  |  |  |  | Generati_7 *Should be generation_data_source* | Text | Seems to be source for energy generation  |
|  |  |  |  |  | estimated_ | Double | estimated electricity generation in gigawatt-hours for the year 2013 |
|  |  |  |  |  | estimated1 | Double | estimated electricity generation in gigawatt-hours for the year 2014 |
|  |  |  |  |  | estimate_1 | Double | estimated electricity generation in gigawatt-hours for the year 2015 |
|  |  |  |  |  | estimate_2 | Double | estimated electricity generation in gigawatt-hours for the year 2016 |
|  |  |  |  |  | estimate_3 | Double | estimated electricity generation in gigawatt-hours for the year 2017 |
|  |  |  |  |  | estimate_4 | Text | label of the model/method used to estimate generation for the year 2013 |
|  |  |  |  |  | estimate_5 | Text | label of the model/method used to estimate generation for the year 2014 |
|  |  |  |  |  | estimate_6 | Text | label of the model/method used to estimate generation for the year 2015 |
|  |  |  |  |  | estimate_7 | Text | label of the model/method used to estimate generation for the year 2016 |
|  |  |  |  |  | estimate_8 | Text | label of the model/method used to estimate generation for the year 2017 |

# 

# 

# 

#