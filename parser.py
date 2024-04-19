import csv
import sys

# Function to parse version information and extract subfields
def parse_version_info(version_info):
    subfields = {
        "product": "",
        "version": "",
        "ostype": "",
        "hostname": "",
        "extrainfo": "",
        "protocol": "",
        "distribution": "",
        "patchlevel": "",
        "architecture": ""
    }

    # Split version information by space
    parts = version_info.split()

    # Iterate over parts and identify subfields
    current_subfield = None
    for part in parts:
        part_lower = part.lower()
        for subfield in subfields.keys():
            if subfield + ":" in part_lower:
                current_subfield = subfield
                subfields[subfield] = part.replace(subfield + ":", "").strip()
                break
        else:
            if current_subfield:
                subfields[current_subfield] += " " + part

    return subfields


# Read the CSV file
csv_file = sys.argv[1]
with open(csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ip_address = row['IP Address']
        port = row['Port']
        service = row['Service']
        version_info = row['Version']
        
        # Parse version information and extract subfields
        version_subfields = parse_version_info(version_info)
        
        # Output the extracted information
        print(f"IP Address: {ip_address}")
        print(f"Port: {port}")
        print(f"Service: {service}")
        print("Version Information:")
        for subfield, value in version_subfields.items():
            print(f"  {subfield}: {value}")
        print()

