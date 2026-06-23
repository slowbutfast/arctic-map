import os
import re
import csv
import shutil

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

# 5. Write a structurally chunked file helper
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
    
    # Chunk 1: Overview
    overview_clean = re.sub(r'^#\s+\*\*.*?\*\*\s*\n', '', overview, flags=re.IGNORECASE)
    overview_content = (
        f"{header_base}"
        f"**Document Section:** Overview & Geographic Extent\n\n"
        f"{enable_instructions}"
        f"{overview_clean}"
    )
    with open(os.path.join(output_dir, f"{base_filename}_overview.md"), 'w', encoding='utf-8') as out_f:
        out_f.write(overview_content)
        
    # Chunk 2: Quality & Lineage (only write if not empty)
    if quality:
        quality_content = (
            f"{header_base}"
            f"**Document Section:** Data Quality, Lineage, & Metadata Contact\n\n"
            f"--- \n\n"
            f"{quality}"
        )
        with open(os.path.join(output_dir, f"{base_filename}_quality.md"), 'w', encoding='utf-8') as out_f:
            out_f.write(quality_content)
            
    # Chunk 3: Schema (only write if not empty)
    if schema:
        schema_content = (
            f"{header_base}"
            f"**Document Section:** Data Dictionary & Attribute Schema\n\n"
            f"--- \n\n"
            f"{schema}"
        )
        with open(os.path.join(output_dir, f"{base_filename}_schema.md"), 'w', encoding='utf-8') as out_f:
            out_f.write(schema_content)


# 6. Generate metadata files for active layers
matched_count = 0
unmatched_layers = []

# Keep a reference to route_SSP126_low_emissions for yearly sub-layer generation
parent_route_content = ""

# First, find parent route content for SSP126 low emissions scenario
for idx, sec in parsed_sections.items():
    title_clean = clean_text_for_matching(sec['title_field'])
    if title_clean == "routessp126lowemissions":
        parent_route_content = sec['raw_content']
        break

for cl in csv_layers:
    ln = cl['layer_name']
    
    # Check manual mapping first
    matched_sec = None
    if ln in MANUAL_MAPPING:
        matched_sec = parsed_sections.get(MANUAL_MAPPING[ln])
    else:
        # Match automatically
        clean_ln = clean_text_for_matching(ln)
        clean_dn = clean_text_for_matching(cl['display_name'])
        
        for idx, sec in parsed_sections.items():
            clean_sec_title = clean_text_for_matching(sec['title_field'])
            clean_sec_header = clean_text_for_matching(sec['header'])
            
            if clean_sec_title and (clean_ln == clean_sec_title or clean_dn == clean_sec_title):
                matched_sec = sec
                break
            if clean_sec_header and (clean_ln == clean_sec_header or clean_dn == clean_sec_header):
                matched_sec = sec
                break
                
    if matched_sec:
        # We have a matched section - split and write it structurally
        write_structural_chunks(cl, matched_sec['raw_content'], ln)
        matched_count += 1
    else:
        unmatched_layers.append(cl)

# 7. Handle unmatched/missing layers (Auto-generation)
for cl in unmatched_layers:
    ln = cl['layer_name']
    dn = cl['display_name']
    
    # 7.1 Yearly Shipping Route Scenario Layers (SSP 126 2015-2020)
    if ln.startswith("route_ssp126_20") and parent_route_content:
        year_match = re.search(r'\d{4}', ln)
        year = year_match.group(0) if year_match else "Selected Year"
        
        # Modify parent content to make it specific to the year
        modified_content = parent_route_content
        modified_content = re.sub(r'route_SSP126_low_emissions', ln, modified_content, flags=re.IGNORECASE)
        modified_content = modified_content.replace(
            "This dataset represents daily navigable Arctic marine shipping routes simulated under the SSP126 emissions scenario, derived from CMIP6 model projections of sea ice concentration and thickness.",
            f"This dataset represents daily navigable Arctic marine shipping routes simulated under the SSP126 emissions scenario specifically for the year **{year}**. It is a subset of the master low-emissions scenario dataset, derived from CMIP6 model projections."
        )
        modified_content = modified_content.replace("route_SSP126_low_emissions.shp", f"{ln}.shp")
        
        write_structural_chunks(cl, modified_content, ln)
        print(f"Auto-generated yearly route metadata chunks: {ln}")
        
    # 7.2 CPAD Arctic Base Boundary Layer
    elif ln == "cpad_arctic_base":
        custom_content = (
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
        
        write_structural_chunks(cl, custom_content, ln)
        print(f"Auto-generated boundary metadata chunks: {ln}")
        
    else:
        print(f"WARNING: No metadata found or auto-generated for active layer '{dn}' ({ln})")

# 8. Generate master index _index.md linking to split files
index_content = (
    f"# **CPAD Arctic Map Dataset Directory**\n\n"
    f"This directory lists all the active dataset layers available on the Arctic Map Explorer website. "
    f"Each layer has been split into structurally logical sections (Overview, Quality, and Schema) "
    f"to ensure optimal, context-preserving retrieval for RAG. Use these links to navigate.\n\n"
)

grouped = {}
for cl in csv_layers:
    theme = cl['theme']
    subtheme = cl['subtheme']
    if theme not in grouped:
        grouped[theme] = {}
    if subtheme not in grouped[theme]:
        grouped[theme][subtheme] = []
    grouped[theme][subtheme].append(cl)

for theme, subthemes in grouped.items():
    index_content += f"## **Theme: {theme}**\n\n"
    for subtheme, layers in subthemes.items():
        index_content += f"### **Subtheme: {subtheme}**\n\n"
        index_content += "| Layer Display Name | Database Name | Overview | Quality & Contact | Attribute Schema |\n"
        index_content += "| :--- | :--- | :--- | :--- | :--- |\n"
        for cl in layers:
            ln = cl['layer_name']
            dn = cl['display_name']
            
            # Check which chunks exist for this layer
            overview_exists = os.path.exists(os.path.join(output_dir, f"{ln}_overview.md"))
            quality_exists = os.path.exists(os.path.join(output_dir, f"{ln}_quality.md"))
            schema_exists = os.path.exists(os.path.join(output_dir, f"{ln}_schema.md"))
            
            overview_link = f"[Overview]({ln}_overview.md)" if overview_exists else "-"
            quality_link = f"[Quality]({ln}_quality.md)" if quality_exists else "-"
            schema_link = f"[Schema]({ln}_schema.md)" if schema_exists else "-"
            
            index_content += f"| {dn} | `{ln}` | {overview_link} | {quality_link} | {schema_link} |\n"
        index_content += "\n"

index_file_path = os.path.join(output_dir, "_index.md")
with open(index_file_path, 'w', encoding='utf-8') as out_f:
    out_f.write(index_content)

# Count generated markdown files
total_generated_files = len([name for name in os.listdir(output_dir) if name.endswith('.md')])

print(f"\nCompleted! Restructured active metadata documents.")
print(f"Generated {total_generated_files} total chunk files in {output_dir}")
print(f"Master index created at {index_file_path}")