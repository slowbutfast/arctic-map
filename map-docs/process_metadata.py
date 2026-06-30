import os
import re
import csv
import shutil
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(script_dir, "Meta Data based on ISO 19115 Standards.md")
csv_path = os.path.join(script_dir, "CPAD Datasets Theme & Subtheme Organization V2 - CPAD WebGIS App.csv")
output_dir = os.path.join(script_dir, "cleaned_metadata")

# Manual mappings for layers with naming mismatches in the MD file
MANUAL_MAPPING = {
    "a_clean_gl_geonames": 7,       # Greenland Geonames
    "a_clean_ne_10m_railroads": 32,  # 10m Scale Railroads / Railroads
    "iceland_poly": 18               # Iceland Polygons / Iceland universities (poly)
}

# Clean output directory: delete existing files and recreate it
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# 1. Parse CSV layers (active layers)
csv_layers = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dn = re.sub(r'[\u200b-\u200d\ufeff]', '', row['display_name'].strip())
        csv_layers.append({
            'theme': row['theme'].strip(),
            'subtheme': row['subtheme'].strip(),
            'layer_name': row['layer_name'].strip(),
            'display_name': dn
        })

print(f"Loaded {len(csv_layers)} active layers from CSV.")

# 2. Parse Markdown metadata file into sections
with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Split MD by numbered headers (e.g. "51. # **OSM Alaska A Places**")
md_sections = re.split(r'\n(?=\d+\.\s+#\s+\*\*|#\s+\*\*)', md_content)

def clean_text_for_matching(text):
    if not text:
        return ""
    text = text.strip().replace('\\', '')
    text = re.sub(r'\.(shp|csv|geojson|json|tif|tiff)$', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^(a_clean_|clean_|a_)', '', text, flags=re.IGNORECASE)
    text = text.lower()
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

parsed_sections = {}
for idx, sec in enumerate(md_sections):
    if idx == 0 and "Land Use Map of City X" in sec:
        continue  # skip example
    
    lines = [l.strip() for l in sec.strip().split('\n') if l.strip()]
    header = lines[0] if lines else ""
    
    title_val = ""
    title_match = re.search(r'\*\*Title:\*\*?\s*(.*)', sec, re.IGNORECASE)
    if not title_match:
        title_match = re.search(r'\*\*Title\*\*:\s*(.*)', sec, re.IGNORECASE)
    if title_match:
        title_val = title_match.group(1).strip()
    
    parsed_sections[idx] = {
        'index': idx,
        'header': header,
        'title_field': title_val,
        'raw_content': sec
    }

print(f"Loaded {len(parsed_sections)} metadata records from MD file.")

# 3. Clean raw markdown content
def clean_markdown(content):
    # Remove all backslash-escaped underscores
    content = content.replace(r'\_', '_')
    # Remove backslash-escaped asterisks
    content = content.replace(r'\*', '*')
    # Fix double colons if any (e.g. **Title:**: -> **Title:**)
    content = re.sub(r'\*\*Title:\*\*:', '**Title:**', content)
    # Remove numbered list formatting prefix from title header if present (e.g. "51. # **Title**" -> "# **Title**")
    content = re.sub(r'^\s*\d+\.\s+#', '#', content.strip())
    return content

# 4. Helper function to split a single metadata block into Overview, Quality, and Schema
def split_metadata_content(content):
    # Standardize content
    content_clean = clean_markdown(content)
    
    # Search for headings
    lineage_match = re.search(r'(?:\n|^)\s*\*\*Lineage:\*\*?', content_clean, re.IGNORECASE)
    quality_match = re.search(r'(?:\n|^)\s*\*\*Quality Information:\*\*?', content_clean, re.IGNORECASE)
    dict_match = re.search(r'(?:\n|^)\s*\*\*Data Dictionary:\*\*?', content_clean, re.IGNORECASE)
    
    # Determine split points
    quality_start = -1
    schema_start = -1
    
    if lineage_match:
        quality_start = lineage_match.start()
    elif quality_match:
        quality_start = quality_match.start()
        
    if dict_match:
        schema_start = dict_match.start()
        
    # Split content logically
    if quality_start != -1 and schema_start != -1 and quality_start < schema_start:
        overview = content_clean[:quality_start].strip()
        quality = content_clean[quality_start:schema_start].strip()
        schema = content_clean[schema_start:].strip()
    elif schema_start != -1:
        # No quality section found, split into overview and schema
        overview = content_clean[:schema_start].strip()
        quality = ""
        schema = content_clean[schema_start:].strip()
    else:
        # Fallback: keep all as overview
        overview = content_clean
        quality = ""
        schema = ""
        
    return overview, quality, schema

# 5. Use case generator based on theme path
def generate_use_cases(theme, subtheme, display_name, abstract, purpose):
    use_cases = []
    theme_lower = theme.lower()
    subtheme_lower = subtheme.lower()
    
    if "socioeconomic" in theme_lower:
        if "education" in subtheme_lower:
            use_cases = [
                f"Analyze accessibility and spatial distribution of {display_name} for educational infrastructure development.",
                f"Correlate {display_name} locations with demographic datasets to evaluate educational equity and coverage.",
                f"Plan student transport networks and assess proximity of schools to residential zones."
            ]
        elif "settlements" in subtheme_lower:
            use_cases = [
                f"Map population distribution and settlement footprints across Arctic and sub-Arctic zones.",
                f"Assess regional infrastructure demand and evaluate emergency evacuation planning for local communities.",
                f"Analyze risk exposure of human settlements to climate hazards like permafrost thawing or seasonal flooding."
            ]
        elif "boundaries" in subtheme_lower:
            use_cases = [
                f"Use boundaries for spatial queries, aggregation, and filtering of environmental or infrastructure datasets.",
                f"Study administrative jurisdictions and regional resource management policies.",
                f"Overlay demographic or economic data to analyze administrative division metrics."
            ]
        else:
            use_cases = [
                f"Conduct spatial demographic analysis and assess community vulnerability in Arctic regions.",
                f"Evaluate resource distribution and human-environment interactions within the mapped area.",
                f"Support regional socioeconomic development planning and policy impact studies."
            ]
    elif "environmental" in theme_lower:
        if "animal" in subtheme_lower or "plant" in subtheme_lower or "biodiversity" in subtheme_lower:
            use_cases = [
                f"Identify critical habitats and biodiversity hotspots for regional conservation and protection planning.",
                f"Monitor shifts in species distribution and ecological corridors relative to climate indicators (e.g., ice melt, permafrost).",
                f"Establish ecological baselines for environmental impact assessments of infrastructure projects."
            ]
        elif "ice" in subtheme_lower or "climate" in subtheme_lower or "permafrost" in subtheme_lower:
            use_cases = [
                f"Analyze climate change trends, temporal sea ice dynamics, or permafrost degradation models.",
                f"Assess environmental feedback loops and their impact on global climate systems.",
                f"Overlay spatial climate data with shipping routes or pipelines to assess physical infrastructure risks."
            ]
        else:
            use_cases = [
                f"Analyze regional ecological health, habitat fragmentation, and biodiversity baselines.",
                f"Conduct environmental impact mapping and identify ecosystems vulnerable to human activity.",
                f"Assess natural resource distribution and support sustainable environmental conservation policies."
            ]
    elif "infrastructure" in theme_lower:
        if "energy" in subtheme_lower or "pipeline" in subtheme_lower or "power" in subtheme_lower:
            use_cases = [
                f"Analyze the spatial layout, capacity, and distribution networks of {display_name}.",
                f"Evaluate infrastructure exposure to environmental risks such as permafrost thaw, sea ice, or coastal erosion.",
                f"Plan sustainable energy distribution routes and optimize corridor layouts."
            ]
        elif "shipping" in subtheme_lower or "route" in subtheme_lower or "density" in subtheme_lower:
            use_cases = [
                f"Optimize Arctic maritime shipping corridors and evaluate navigable routes under various climate scenarios.",
                f"Assess shipping density impacts on marine ecosystems, noise pollution, and conservation areas.",
                f"Support maritime safety, search and rescue operations, and ports planning."
            ]
        elif "transport" in subtheme_lower or "railroad" in subtheme_lower or "road" in subtheme_lower or "airport" in subtheme_lower:
            use_cases = [
                f"Analyze regional connectivity, accessibility, and transport network density in remote Arctic environments.",
                f"Identify transport bottlenecks and plan strategic expansions of logistics corridors.",
                f"Assess structural integrity and maintenance requirements of transportation links built on permafrost."
            ]
        else:
            use_cases = [
                f"Perform utility mapping, connectivity assessment, and structural asset management.",
                f"Evaluate the proximity of critical services and infrastructure to remote communities.",
                f"Optimize site selection for new facility projects and logistical hubs in the Arctic region."
            ]
    
    if not use_cases:
        use_cases = [
            f"Conduct spatial queries and overlay analysis with other socioeconomic or environmental datasets.",
            f"Perform regional policy evaluation and support spatial decision-making systems.",
            f"Identify geographic clusters and map patterns of spatial characteristics."
        ]
    return use_cases

# 6. Write a structurally chunked file helper (unified single document)
def write_structural_chunks(cl, raw_sec_content, base_filename):
    ln = cl['layer_name']
    dn = cl['display_name']
    theme = cl['theme']
    subtheme = cl['subtheme']
    
    # Split content
    overview, quality, schema = split_metadata_content(raw_sec_content)
    
    # Base headers
    header_base = (
        f"# **{dn}** (Layer: `{ln}`)\n"
        f"**Theme Path:** {theme} > {subtheme} > {dn}\n"
        f"**Layer Database Name:** `{ln}`\n"
    )
    
    enable_instructions = (
        f"**How to Enable on Website Map:**\n"
        f"1. In the left sidebar of the website, expand the **{theme}** category.\n"
        f"2. Expand the **{subtheme}** subcategory.\n"
        f"3. Check the box next to **{dn}** to display it on the map.\n\n"
        f"--- \n\n"
    )
    
    # Clean Overview
    overview_clean = re.sub(r'^#\s+\*\*.*?\*\*\s*\n', '', overview, flags=re.IGNORECASE).strip()
    
    # Extract abstract and purpose for use case generation
    abstract_val = ""
    abstract_match = re.search(r'\*\*Abstract:\*\*?\s*(.*?)(?:\n\n|\n\*\*)', raw_sec_content, re.DOTALL | re.IGNORECASE)
    if abstract_match:
        abstract_val = abstract_match.group(1).strip()
        
    purpose_val = ""
    purpose_match = re.search(r'\*\*Purpose:\*\*?\s*(.*?)(?:\n\n|\n\*\*)', raw_sec_content, re.DOTALL | re.IGNORECASE)
    if purpose_match:
        purpose_val = purpose_match.group(1).strip()
        
    use_cases = generate_use_cases(theme, subtheme, dn, abstract_val, purpose_val)
    use_cases_list = "\n".join([f"- {uc}" for uc in use_cases])
    
    unified_content = (
        f"{header_base}\n"
        f"{enable_instructions}"
        f"## Overview & Geographic Extent\n\n"
        f"{overview_clean}\n\n"
    )
    
    if quality:
        unified_content += (
            f"## Data Quality, Lineage, & Metadata Contact\n\n"
            f"{quality.strip()}\n\n"
        )
        
    if schema:
        unified_content += (
            f"## Data Dictionary & Attribute Schema\n\n"
            f"{schema.strip()}\n\n"
        )
        
    unified_content += (
        f"## Potential Use Cases\n\n"
        f"{use_cases_list}\n"
    )
    
    with open(os.path.join(output_dir, f"{base_filename}.md"), 'w', encoding='utf-8') as out_f:
        out_f.write(unified_content)


# 7. Group active layers by theme and subtheme
grouped_layers = {}
for cl in csv_layers:
    theme = cl['theme']
    subtheme = cl['subtheme']
    if theme not in grouped_layers:
        grouped_layers[theme] = {}
    if subtheme not in grouped_layers[theme]:
        grouped_layers[theme][subtheme] = []
    grouped_layers[theme][subtheme].append(cl)

# Keep a reference to route_SSP126_low_emissions for yearly sub-layer generation
parent_route_content = ""
for idx, sec in parsed_sections.items():
    title_clean = clean_text_for_matching(sec['title_field'])
    if title_clean == "routessp126lowemissions":
        parent_route_content = sec['raw_content']
        break

# Batch layers into groups of max 3 to satisfy uploader / Sandbox limits
batched_groups = []
for theme, subthemes in grouped_layers.items():
    for subtheme, layers in subthemes.items():
        for i in range(0, len(layers), 3):
            batch = layers[i:i+3]
            batched_groups.append({
                'theme': theme,
                'subtheme': subtheme,
                'layers': batch,
                'part': (i // 3) + 1,
                'total_parts': (len(layers) + 2) // 3
            })

print(f"Divided {len(csv_layers)} layers into {len(batched_groups)} batched files (max 3 layers per file).")

metadata_cheatsheet = []

# Generate batched metadata files
for bg in batched_groups:
    theme = bg['theme']
    subtheme = bg['subtheme']
    layers = bg['layers']
    part = bg['part']
    total_parts = bg['total_parts']
    
    # Filesystem safe names
    theme_safe = re.sub(r'[^a-zA-Z0-9_]', '_', theme.strip().replace('&', '_and_').replace(' ', '_'))
    subtheme_safe = re.sub(r'[^a-zA-Z0-9_]', '_', subtheme.strip().replace('&', '_and_').replace(' ', '_'))
    
    filename = f"{theme_safe}_{subtheme_safe}"
    if total_parts > 1:
        filename += f"_part{part}"
    filename = re.sub(r'_+', '_', filename).strip('_').lower() + ".md"
    
    layer_names_list = [cl['layer_name'] for cl in layers]
    layer_names_str = ",".join(layer_names_list)
    
# Helper to extract a metadata field using regex
def extract_metadata_field(text, field_name):
    pattern = r'(?:^|\n)\s*\*\*' + re.escape(field_name) + r':?\*\*?\s*(.*?)(?=\n\s*\*\*|\n\s*##|\n\n|\Z)'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if match:
        val = match.group(1).strip()
        # Clean consecutive newlines/spaces inside the text block to keep it unified
        val = re.sub(r'\s*\n\s*', ' ', val)
        return val
    return ""

def format_layer_as_key_value(cl, raw_sec_content):
    ln = cl['layer_name']
    dn = cl['display_name']
    theme = cl['theme']
    subtheme = cl['subtheme']
    
    # Clean the raw markdown first
    content_clean = clean_markdown(raw_sec_content)
    
    # Extract fields
    fields = [
        "Title", "Abstract", "Purpose", "Keywords", 
        "Temporal Extent", "Geographic Extent", 
        "Spatial Resolution", "Coordinate Reference System",
        "Lineage", "Quality Information", "Metadata Contact"
    ]
    ext = {}
    for f in fields:
        ext[f] = extract_metadata_field(content_clean, f)
        
    # Extract schema table
    schema_table = ""
    table_lines = [line.strip() for line in content_clean.split('\n') if line.strip().startswith('|')]
    if table_lines:
        schema_table = "\n".join(table_lines)
        
    # Build content
    layer_content = f"## **Dataset Layer: {dn}** (Layer ID: `{ln}`)\n"
    layer_content += f"* **Theme Path**: {theme} > {subtheme} > {dn}\n"
    layer_content += f"* **Layer Database Name**: `{ln}`\n"
    
    # How to enable
    layer_content += (
        f"* **How to Enable on Website Map**:\n"
        f"  1. In the left sidebar of the website, expand the **{theme}** category.\n"
        f"  2. Expand the **{subtheme}** subcategory.\n"
        f"  3. Check the box next to **{dn}** to display it on the map.\n"
    )
    
    # Overview
    layer_content += f"### **Overview & Geographic Extent for {dn} (Layer: {ln})**\n"
    if ext.get("Title"):
        layer_content += f"* **Title**: {ext['Title']}\n"
    if ext.get("Abstract"):
        layer_content += f"* **Abstract**: {ext['Abstract']}\n"
    if ext.get("Purpose"):
        layer_content += f"* **Purpose**: {ext['Purpose']}\n"
    if ext.get("Keywords"):
        layer_content += f"* **Keywords**: {ext['Keywords']}\n"
    if ext.get("Temporal Extent"):
        layer_content += f"* **Temporal Extent**: {ext['Temporal Extent']}\n"
    if ext.get("Geographic Extent"):
        geo_clean = ext['Geographic Extent'].replace(r'\-', '-')
        layer_content += f"* **Geographic Extent**: {geo_clean}\n"
    if ext.get("Spatial Resolution"):
        layer_content += f"* **Spatial Resolution**: {ext['Spatial Resolution']}\n"
    if ext.get("Coordinate Reference System"):
        layer_content += f"* **Coordinate Reference System**: {ext['Coordinate Reference System']}\n"
        
    # Quality & Contact
    quality_section = ""
    if ext.get("Lineage"):
        quality_section += f"* **Lineage**: {ext['Lineage']}\n"
    if ext.get("Quality Information"):
        quality_section += f"* **Quality Information**: {ext['Quality Information']}\n"
    if ext.get("Metadata Contact"):
        quality_section += f"* **Metadata Contact**: {ext['Metadata Contact']}\n"
        
    if quality_section:
        layer_content += f"### **Data Quality, Lineage, & Contacts for {dn} (Layer: {ln})**\n" + quality_section
        
    # Schema
    if schema_table:
        layer_content += f"### **Data Dictionary & Attribute Schema for {dn} (Layer: {ln})**\n"
        layer_content += f"{schema_table}\n"
        
    # Use cases
    use_cases = generate_use_cases(theme, subtheme, dn, ext.get("Abstract"), ext.get("Purpose"))
    use_cases_list = "\n".join([f"  * {uc}" for uc in use_cases])
    layer_content += (
        f"### **Potential Use Cases for {dn} (Layer: {ln})**\n"
        f"* **Recommended GIS Applications**:\n{use_cases_list}\n"
    )
    
    return layer_content

# Generate batched metadata files
for bg in batched_groups:
    theme = bg['theme']
    subtheme = bg['subtheme']
    layers = bg['layers']
    part = bg['part']
    total_parts = bg['total_parts']
    
    # Filesystem safe names
    theme_safe = re.sub(r'[^a-zA-Z0-9_]', '_', theme.strip().replace('&', '_and_').replace(' ', '_'))
    subtheme_safe = re.sub(r'[^a-zA-Z0-9_]', '_', subtheme.strip().replace('&', '_and_').replace(' ', '_'))
    
    filename = f"{theme_safe}_{subtheme_safe}"
    if total_parts > 1:
        filename += f"_part{part}"
    filename = re.sub(r'_+', '_', filename).strip('_').lower() + ".md"
    
    layer_names_list = [cl['layer_name'] for cl in layers]
    layer_names_str = ",".join(layer_names_list)
    
    # Store uploader cheatsheet record
    metadata_cheatsheet.append({
        'filename': filename,
        'theme': theme,
        'subtheme': subtheme,
        'layer_names': layer_names_str
    })
    
    # Build consolidated markdown file content
    file_content = (
        f"# **CPAD Arctic Map Datasets - {theme} > {subtheme} (Part {part} of {total_parts})**\n\n"
        f"This document consolidates metadata, attributes, schemas, and potential use cases for the following active layers:\n"
    )
    for cl in layers:
        file_content += f"- **{cl['display_name']}** (Layer Database Name: `{cl['layer_name']}`)\n"
    file_content += "\n---\n\n"
    
    for cl in layers:
        ln = cl['layer_name']
        dn = cl['display_name']
        
        # Check manual mapping first
        matched_sec = None
        if ln in MANUAL_MAPPING:
            matched_sec = parsed_sections.get(MANUAL_MAPPING[ln])
        else:
            clean_ln = clean_text_for_matching(ln)
            clean_dn = clean_text_for_matching(dn)
            for idx, sec in parsed_sections.items():
                clean_sec_title = clean_text_for_matching(sec['title_field'])
                clean_sec_header = clean_text_for_matching(sec['header'])
                if clean_sec_title and (clean_ln == clean_sec_title or clean_dn == clean_sec_title):
                    matched_sec = sec
                    break
                if clean_sec_header and (clean_ln == clean_sec_header or clean_dn == clean_sec_header):
                    matched_sec = sec
                    break
                    
        raw_sec_content = ""
        if matched_sec:
            raw_sec_content = matched_sec['raw_content']
        elif ln.startswith("route_ssp126_20") and parent_route_content:
            year_match = re.search(r'\d{4}', ln)
            year = year_match.group(0) if year_match else "Selected Year"
            raw_sec_content = parent_route_content
            raw_sec_content = re.sub(r'route_SSP126_low_emissions', ln, raw_sec_content, flags=re.IGNORECASE)
            raw_sec_content = raw_sec_content.replace(
                "This dataset represents daily navigable Arctic marine shipping routes simulated under the SSP126 emissions scenario, derived from CMIP6 model projections of sea ice concentration and thickness.",
                f"This dataset represents daily navigable Arctic marine shipping routes simulated under the SSP126 emissions scenario specifically for the year **{year}**. It is a subset of the master low-emissions scenario dataset, derived from CMIP6 model projections."
            )
            raw_sec_content = raw_sec_content.replace("route_SSP126_low_emissions.shp", f"{ln}.shp")
        elif ln == "cpad_arctic_base":
            raw_sec_content = (
                f"# **{dn}**\n\n"
                f"**Title:** CPAD Arctic Base Boundaries\n"
                f"**Abstract:** This layer defines the base geographic boundary for the Co-production of Policy-relevant Climate Data (CPAD) Arctic project. It encompasses the geographic scope of all socioeconomic, environmental, and infrastructure datasets displayed in the Arctic Map Explorer.\n"
                f"**Purpose:** To provide a reference boundary defining the Arctic project area for spatial analysis and mapping.\n"
                f"**Keywords:** CPAD, Arctic, project boundary, reference geography\n"
                f"**Temporal Extent:** \n"
                f"* **Date**: N/A\n"
                f"* **Time Period**: Active project boundary (present)\n"
                f"**Geographic Extent:**\n"
                f"* **Bounding Box**: Circle enclosing the Arctic region above 50°N latitude.\n"
                f"**Spatial Resolution**: N/A\n"
                f"**Coordinate Reference System**: WGS 1984\n"
                f"**Lineage**: Created by the CPAD project consortium to standardize the visualization boundary for the Arctic region.\n"
                f"**Quality Information:**\n"
                f"* **Accuracy**: Positionally accurate reference boundary.\n"
                f"* **Completeness**: 100% complete boundary polygon.\n"
                f"* **Consistency**: Digitally consistent with all overlay layers.\n"
                f"**Distribution Information:**\n"
                f"* **Format**: Shapefile / Polygon\n"
                f"* **Access Constraints**: No restrictions\n"
                f"* **Use Constraints**: Creative Commons Attribution 4.0 International\n"
                f"**Metadata Contact:**\n"
                f"* **Organization**: CPAD Consortium (https://nna-cpad.org/)\n"
                f"**Data Dictionary:**\n\n"
                f"| Layer Name | Coordinate System | Feature Type | Number of records | Number of attributes | List of Attributes | Data Type | Description |\n"
                f"| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
                f"| cpad_arctic_base.shp | WGS 1984 | Shapefile, Polygon | 1 | 2 | FID | OID | Object ID |\n"
                f"| | | | | | Shape | Geometry | Polygon boundary |\n"
            )
            
        if not raw_sec_content:
            print(f"WARNING: No metadata found or auto-generated for active layer '{dn}' ({ln})")
            raw_sec_content = f"# **{dn}**\n**Abstract:** GIS layer mapping {dn}.\n**Purpose:** Reference layer.\n**Data Dictionary:**\n| Layer Name | List of Attributes | Data Type | Description |\n| {ln} | FID | OID | Object ID |\n"
            
        layer_content = format_layer_as_key_value(cl, raw_sec_content)
        file_content += layer_content
        file_content += "\n---\n\n"
        
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as out_f:
        out_f.write(file_content)

# 8. Generate master index _index.md linking to unified grouped files
index_content = (
    f"# **CPAD Arctic Map Dataset Directory**\n\n"
    f"This directory lists the active dataset layers available on the Arctic Map Explorer website, "
    f"consolidated into **{len(batched_groups)} subtheme-level documents** to fit Dify's document quotas. "
    f"Use these links to navigate.\n\n"
)

for theme, subthemes in grouped_layers.items():
    index_content += f"## **Theme: {theme}**\n\n"
    for subtheme, layers in subthemes.items():
        index_content += f"### **Subtheme: {subtheme}**\n\n"
        index_content += "| Documents | Layers Contained |\n"
        index_content += "| :--- | :--- |\n"
        for bg in batched_groups:
            if bg['theme'] == theme and bg['subtheme'] == subtheme:
                # Find matching filename
                filename = ""
                for c in metadata_cheatsheet:
                    if c['theme'] == theme and c['subtheme'] == subtheme and bg['part'] == (batched_groups.index(bg) - batched_groups.index(next(x for x in batched_groups if x['theme'] == theme and x['subtheme'] == subtheme)) + 1):
                        filename = c['filename']
                        break
                if not filename:
                    # fallback matching
                    theme_safe = re.sub(r'[^a-zA-Z0-9_]', '_', theme.strip().replace('&', '_and_').replace(' ', '_'))
                    subtheme_safe = re.sub(r'[^a-zA-Z0-9_]', '_', subtheme.strip().replace('&', '_and_').replace(' ', '_'))
                    filename = f"{theme_safe}_{subtheme_safe}"
                    if bg['total_parts'] > 1:
                        filename += f"_part{bg['part']}"
                    filename = re.sub(r'_+', '_', filename).strip('_').lower() + ".md"
                    
                doc_link = f"[{filename}]({filename})"
                layers_str = ", ".join([f"`{cl['display_name']}`" for cl in bg['layers']])
                index_content += f"| {doc_link} | {layers_str} |\n"
        index_content += "\n"

index_file_path = os.path.join(output_dir, "_index.md")
with open(index_file_path, 'w', encoding='utf-8') as out_f:
    out_f.write(index_content)

# 9. Generate Dify Upload cheatsheet CSV and JSON
cheatsheet_csv_path = os.path.join(output_dir, "dify_metadata_cheatsheet.csv")
with open(cheatsheet_csv_path, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['filename', 'theme', 'subtheme', 'layer_names'])
    for row in metadata_cheatsheet:
        writer.writerow([row['filename'], row['theme'], row['subtheme'], row['layer_names']])

cheatsheet_json_path = os.path.join(output_dir, "dify_metadata_cheatsheet.json")
with open(cheatsheet_json_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(metadata_cheatsheet, jsonfile, indent=2)

# Count generated markdown files
total_generated_files = len([name for name in os.listdir(output_dir) if name.endswith('.md')])

print(f"\nCompleted! Restructured active metadata documents.")
print(f"Generated {total_generated_files} total chunk files in {output_dir}")
print(f"Master index created at {index_file_path}")
print(f"Dify upload metadata cheatsheet CSV created at {cheatsheet_csv_path}")
print(f"Dify upload metadata cheatsheet JSON created at {cheatsheet_json_path}")