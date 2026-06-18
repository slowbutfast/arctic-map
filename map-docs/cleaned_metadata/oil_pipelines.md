# **Oil Pipelines**

**Theme:** Infrastructure
**Subtheme:** Energy
**Layer Name in Database:** `oil_pipelines`

**How to Enable on Website Map:**
1. In the left sidebar of the website, expand the **Infrastructure** category.
2. Expand the **Energy** subcategory.
3. Check the box next to **Oil Pipelines** to display it on the map.

--- 

**Title:** oil_pipelines  
**Abstract:** This dataset represents tracks Oil Infrastructure globally.  
**Purpose:**  
**Keywords:** oil infrastructure  
**Temporal Extent:**

* **Date**: 5/2024  
* **Time Period**: \[Start date \- End date\]


**Geographic Extent:** 

* Bounding Box: \[Coordinates defining the geographic extent of the dataset\]

**Spatial Resolution**: \[Resolution of the land use classification, e.g., 5 meters\]  
**Coordinate Reference Systems:** WGS 1984  
**Lineage:** The dataset was created using aerial imagery captured in \[year\], classified using \[specific classification methodology\], and validated against ground truth data from \[source\].  
**Quality Information:**

* Accuracy: \[Describe accuracy measures, e.g., positional accuracy\]  
* Completeness: \[Describe completeness of the dataset\]  
* Consistency: \[Describe consistency measures\]

**Distribution Information:**

* Format: shapefile  
* Access Constraints: \[Describe any restrictions on access\]  
* Use Constraints: Recommended Citation: “Global Oil Infrastructure Tracker, Global Energy Monitor, May 2024 release”.

**Metadata Contact:**

* Organization: [Global Energy Monitor](https://globalenergymonitor.org/projects/global-oil-infrastructure-tracker/)  
* Position: Global Oil Infrastructure Tracker: Baird Langenbrunner   
* Email: baird.langenbrunner@globalenergymonitor.org  
* Phone: 415-206-0906

**Data Dictionary:**

| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| oil_pipelines.shp | WGS 1984 | Shapefile | 1,639 | 48 | FID | Object ID |  |
|  |  |  |  |  | Shape | Geometry |  |
|  |  |  |  |  | ProjectID | Text | A unique ID for each project (all the phases, segments, expansions, etc. belonging to the same overall pipeline do not necesssarily share a ProjectID, but they should share the same PipelineName) |
|  |  |  |  |  | Fuel | Text | Oil, Gas, or NGL |
|  |  |  |  |  | StartCntry | Text | Country the pipeline starts in |
|  |  |  |  |  | EndCntry | Text | Country the pipeline ends in |
|  |  |  |  |  | Countries | Text | Countries that the pipeline passes through, in order from beginning to end (where possible); note Hong Kong and Macao are recognized as sovereign states here |
|  |  |  |  |  | Wiki | Text | Link to project's GEM.wiki page |
|  |  |  |  |  | PipeName | Text | Name of the pipeline (or pipeline system, when it has multiple pieces, phases, segments, or expansions) |
|  |  |  |  |  | SegName | Text | Name of the pipeline segment (which can be a segment of a bigger pipeline system/network, or an expansion project) |
|  |  |  |  |  | OthEngName | Text | Alternate pipeline names in English, if applicable; if there are multiple, separate by a semicolon (;) |
|  |  |  |  |  | Status | Text | Operating, Proposed, Retired, Construction, Shelved, Cancelled, Idle, or Mothballed If there have been no development updates in the two years following the project's proposal, then the status is assumed to be "Shelved". If there have been no development updates in the 4 years following the project's proposal or longer, the status is assumed to be "Cancelled". If Shelved, Cancelled, or Retired, these are associated with ShelvedYear, CancelledYear, and StopYear |
|  |  |  |  |  | Owner | Text | Auto-filled: direct owner name(s), percent ownership if available; here "owner" means lowest level of ownership that we're able to find in our research. |
|  |  |  |  |  | Parent | Text | Parent company name(s), percent ownership if available; here "parent" means highest level of ownership that we're able to trace (e.g., parent companies or ultimate shareholders). |
|  |  |  |  |  | ParHQCntry | Text | First year operations initiated, or expected to initiate |
|  |  |  |  |  | StartYr1 | Text | Year operations initiated for first expansion project, or expected to initiate, if expansion not listed as separate observation |
|  |  |  |  |  | StartYr2 | Text | Year operations initiated for second expansion project, or expected to initiate, if expansion not listed as separate observation |
|  |  |  |  |  | StartYr3 | Text | Year operations ended (if Status="Mothballed", Status="Idle", or Status="Retired") or the year the project was cancelled (if Status="Cancelled"). If Status="Cancelled" due to 4-year rule* (as opposed to a formal cancellation), then StopYear="presumed" |
|  |  |  |  |  | StopYr | Text | If Status=Shelved, the year this became true |
|  |  |  |  |  | ShelvedYr | Text | Maximum potential capacity |
|  |  |  |  |  | Capac | Text | If Status=Cancelled, the year this became true |
|  |  |  |  |  | CancelldYr | Text | Units that "Capacity" is reported in (bpd, bcm/year, mtpa, MMcf/d, or TJ/d) |
|  |  |  |  |  | CapacUnits | Text | Capacity converted to billion cubic meters (bcm) per year |
|  |  |  |  |  | CapacBOEd | Text | Capacity converted to barrels of oil equivalent (BOE) per day |
|  |  |  |  |  | LenKwnKm | Text | Publicly available length, converted to km |
|  |  |  |  |  | LenEstKm | Text | Estimated length in km, calulated using route coordinates with Geopandas Python package and taken from "Length Estimates by Pipeline" tab) |
|  |  |  |  |  | LenMergdKm | Text | Merge between LengthKnownKm and LengthEstimateKm (LengthKnownKm is priotized when available; otherwise LengthEstimateKm is used). |
|  |  |  |  |  | Diam | Text | Pipeline's diameter (without units); when multiple values are reported, they are separated by a comma |
|  |  |  |  |  | DiamUnits | Text | Pipeline's diameter units |
|  |  |  |  |  | FuelSource | Text | Name of oil or gas field, or pipeline, the fuel is sourced from |
|  |  |  |  |  | StartLoc | Text | Town, city, or village the pipeline starts in |
|  |  |  |  |  | StartDist | Text | Prefecture or district the pipeline starts in |
|  |  |  |  |  | StartState | Text | State or province pipeline starts in |
|  |  |  |  |  | StartReg | Text | Pipeline's start region. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | EndLoc | Text | Town, city, or village the pipeline ends in |
|  |  |  |  |  | StartSubRe | Text | Pipeline's start subregion. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | EndDist | Text | Prefecture or district the pipeline ends in |
|  |  |  |  |  | EndState | Text | State or province the pipeline ends in |
|  |  |  |  |  | EndReg | Text | Pipeline's end region. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | FID_1 | Text | Has the project received its Final Investment Decision (FID) yet? (if Status="Proposed" then option: "Pre-FID"/"FID", if Status is anything other than "Proposed", then leave blank) |
|  |  |  |  |  | EndSubRe | Text | Pipeline's end subregion. Regions and subregions are as defined by the United Nations Statistics Division, in their M49 specification. |
|  |  |  |  |  | FIDYr | Text | If Pre-FID status, then enter the year FID is expected; if FID already made, then enter year of decision. |
|  |  |  |  |  | OthLanName | Text | Primary name in other relevant search language. |
|  |  |  |  |  | OthLanSeg | Text | Pipeline segment/expansion name in other relevant search languages. |
|  |  |  |  |  | Cost | Text | Cost of the project (either estimated or actual) |
|  |  |  |  |  | CostUnits | Text | Cost units/currency 3-letter code name (USD, EUR, etc.) |
|  |  |  |  |  | CostUSD | Text | Cost of construction converted to USD |
|  |  |  |  |  | LastUpdate | Text | Date this was last checked/updated (filled in by Researcher) |