import csv

input_file = input_file = r"E:\_DAIBIK\__ISI\DAA Project\Travelling-Salesman_DAA\dataset\UK_Cities.csv"
  # your CSV file

# Read the data, remove quotes and last column
with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = []
    for row in reader:
        if row:  # skip empty rows
            # Remove last column (Population)
            new_row = row[:-1]
            # Strip quotes from each element
            new_row = [cell.strip('"') for cell in new_row]
            rows.append(new_row)

# Write back to the same file
with open(input_file, "a", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"{len(rows)} rows processed and saved without quotes and population.")
