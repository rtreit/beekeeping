import csv

# Define the inventory data: each dictionary represents an equipment-location record.
inventory_data = [
    # Hive Components
    {
        "Item Name": "Deep Boxes (Deeps)",
        "Category": "Hive Component",
        "Location": "Bee Yard",
        "Quantity": "3",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Essential for brood rearing"
    },
    {
        "Item Name": "Deep Boxes (Deeps)",
        "Category": "Hive Component",
        "Location": "Storage",
        "Quantity": "3",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Extra spares"
    },
    {
        "Item Name": "Medium Boxes (Supers)",
        "Category": "Hive Component",
        "Location": "Bee Yard",
        "Quantity": "5",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "For honey storage"
    },
    {
        "Item Name": "Bottom Boards",
        "Category": "Hive Component",
        "Location": "Bee Yard",
        "Quantity": "3",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Base of hive for ventilation and pest management"
    },
    {
        "Item Name": "Inner Covers",
        "Category": "Hive Component",
        "Location": "Bee Yard",
        "Quantity": "3",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Protects hive and aids ventilation"
    },
    {
        "Item Name": "Outer Covers (Telescoping Covers)",
        "Category": "Hive Component",
        "Location": "Bee Yard",
        "Quantity": "3",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Provides weather protection"
    },
    {
        "Item Name": "Queen Excluder",
        "Category": "Hive Component",
        "Location": "Bee Yard",
        "Quantity": "2",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Keeps queen from entering honey supers"
    },
    {
        "Item Name": "Frames & Foundation",
        "Category": "Hive Component",
        "Location": "Bee Yard",
        "Quantity": "30",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Used to build comb"
    },
    # Tools & Equipment
    {
        "Item Name": "Smoker",
        "Category": "Tool",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Calms bees during inspections"
    },
    {
        "Item Name": "Hive Tool",
        "Category": "Tool",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Used to pry apart hive components and scrape off excess wax"
    },
    {
        "Item Name": "Bee Brush",
        "Category": "Tool",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Gently removes bees from frames"
    },
    {
        "Item Name": "Feeder",
        "Category": "Tool",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Provides supplemental feeding"
    },
    {
        "Item Name": "Entrance Reducer",
        "Category": "Tool",
        "Location": "Bee Yard",
        "Quantity": "2",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Helps control hive entrance size"
    },
    # Protective Gear
    {
        "Item Name": "Beekeeping Suit or Jacket",
        "Category": "Protective Gear",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Full body protection"
    },
    {
        "Item Name": "Veil",
        "Category": "Protective Gear",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Protects face and neck"
    },
    {
        "Item Name": "Gloves",
        "Category": "Protective Gear",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Hand protection"
    },
    {
        "Item Name": "Boots",
        "Category": "Protective Gear",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Safety and comfort during hive work"
    },
    # Maintenance & Miscellaneous
    {
        "Item Name": "Spare Parts",
        "Category": "Maintenance/Miscellaneous",
        "Location": "Storage",
        "Quantity": "Varies",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Extra parts for quick replacements"
    },
    {
        "Item Name": "Cleaning Supplies",
        "Category": "Maintenance/Miscellaneous",
        "Location": "Storage",
        "Quantity": "Varies",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Used for regular hive maintenance"
    },
    {
        "Item Name": "Pollen Trap",
        "Category": "Maintenance/Miscellaneous",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Collects pollen from returning foragers"
    },
    {
        "Item Name": "Mite Treatments/Medications",
        "Category": "Maintenance/Miscellaneous",
        "Location": "Storage",
        "Quantity": "Varies",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "For managing hive health"
    },
    # Additional Common Equipment
    {
        "Item Name": "Honey Extractor",
        "Category": "Processing Equipment",
        "Location": "Storage",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Used to extract honey from frames"
    },
    {
        "Item Name": "Uncapping Knife or Fork",
        "Category": "Processing Equipment",
        "Location": "Bee Yard",
        "Quantity": "1",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "Used to remove wax cappings from frames"
    },
    {
        "Item Name": "Bottling Equipment",
        "Category": "Processing Equipment",
        "Location": "Storage",
        "Quantity": "Set",
        "Condition": "",
        "Purchase Date": "",
        "Notes": "For packaging honey"
    }
]

# Define the CSV file column names
fieldnames = ["Item Name", "Category", "Location", "Quantity", "Condition", "Purchase Date", "Notes"]

# Write data to CSV file
with open('beekeeping_inventory.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in inventory_data:
        writer.writerow(record)

print("CSV file 'beekeeping_inventory.csv' generated successfully!")
