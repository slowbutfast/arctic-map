# **Liquefied Natural Gas Terminals**

**Theme:** Infrastructure
**Subtheme:** Energy
**Layer Name in Database:** `liquefied_natural_gas_terminals`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Energy** subcategory.
3. Check the box next to **Liquefied Natural Gas Terminals** to display it on the map.

--- 

**Title:** liquefied_natural_gas_terminals  
**Abstract:** This dataset represents tracks liquefied natural gas (LNG) import and export terminals globally.  
**Purpose:**  
**Keywords:** gas infrastructure, liquefied natural gas, terminals  
**Temporal Extent:**

* **Date**: 9/2024  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box: Top: 73.153613 degree Bottom: \-41.576699 degree Left: \-151.388340 degree Right: 154.690296 degree

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** unknown  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefiles  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: Recommended Citation: “Global Oil Infrastructure Tracker, Global Energy Monitor, May 2024 release”.

**Metadata Contact:**

* Organization: [Global Energy Monitor](https://globalenergymonitor.org/projects/global-gas-infrastructure-tracker/download-data/​)  
* Position: Global Oil Infrastructure Tracker: Baird Langenbrunner   
* Email: baird.langenbrunner@globalenergymonitor.org  
* Phone: 415-206-0906


**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| liquefied_natural_gas_terminals.shp | unknown | Shapefile | 1,295 | 23 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | TerminalID | Text | Assigned ID number to every whole terminal. Unique to each distinct terminal. |
|  |  |  |  |  | ProjectID | Text | Assigned ID number to every project within a whole terminal. Unique within each distinct TerminalID. |
|  |  |  |  |  | ComboID | Text | Combined TerminalID and ProjectID to create unique index value for every observation. |
|  |  |  |  |  | Wiki | Text | Link to project's GEM.wiki page |
|  |  |  |  |  | TermName | Text | Terminal name |
|  |  |  |  |  | UnitName | Text | Smaller unit within a terminal (including trains T1, T2; phases Phase 1, Phase 2; expansions; project revivals/recommissions; etc.) |
|  |  |  |  |  | FacilType | Text | Type of facility (import or export terminal) |
|  |  |  |  |  | Status | Text | Operating, Proposed, Retired, Construction, Shelved, Cancelled, Idle, or Mothballed If there have been no development updates in the two years following the project's proposal, then the status is assumed to be "Shelved". If there have been no development updates in the 4 years following the project's proposal or longer, the status is assumed to be "Cancelled" |
|  |  |  |  |  | Country | Text | Country of location; note Hong Kong and Macao are considered separate countries so that their infrastructure can be tracked independently of China |
|  |  |  |  |  | OthLanName | Text | Terminal name in its local language (referring exactly to the OtherLanguageWikiPage) |
|  |  |  |  |  | OthEngName | Text | Alternate terminal names in English (note some Chinese terminals are also included, and these will eventually be moved to an OtherLanguageTerminalName column) |
|  |  |  |  |  | Owner | Text | Owner company name(s), percent ownership if available; here "owner" means lowest level of ownership that we're able to trace. |
|  |  |  |  |  | Parent | Text | Parent company name(s), percent ownership if available, taken from the Parent tab; here "parent" means highest level of ownership that we're able to trace (e.g., parent companies or ultimate shareholders). For state-owned enterprises, we prioritize the name of the company (e.g., PipeChina) or the ministry (e.g., Iran Ministry of Oil) rather than Government of China or Government of Iran. |
|  |  |  |  |  | ParHQCntry | Text | Parents' headquarters countries, listed in order of the parent companies. |
|  |  |  |  |  | Capac | Text | Maximum potential production capacity (if there's a range found in research, the maximum is recorded in the sheet and the range is added to the wiki page) |
|  |  |  |  |  | CapacUnits | Text | Unit that capacity is publicly reported in (mtpa, bcf/d, bcm/year, gal/day) |
|  |  |  |  |  | CapacMtpa | Text | Publicly reported capacity value, converted to mtpa |
|  |  |  |  |  | CapInBcmy | Text | Capacity in bcm/y |
|  |  |  |  |  | PropYr | Text | Year the project was first proposed |
|  |  |  |  |  | PropMo | Text | Month project was proposed |
|  |  |  |  |  | ConstYr | Text | Year construction began (only fill out if construction has already started or been completed, not the expected year of construction start) |

#