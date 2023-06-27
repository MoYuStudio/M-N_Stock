
import csv

lookup_table = [
    # 2
    ['AB'], ['AC'], ['AD'], ['AE'], ['AF'], ['AG'], ['AH'],
    ['BC'], ['BD'], ['BE'], ['BF'], ['BG'], ['BH'],
    ['CD'], ['CE'], ['CF'], ['CG'], ['CH'],
    ['DE'], ['DF'], ['DG'], ['DH'],
    ['EF'], ['EG'], ['EH'],
    ['FG'], ['FH'],
    ['GH'],

    # 3
    ['ABC'], ['ABD'], ['ABE'], ['ABF'], ['ABG'], ['ABH'], ['ACD'], ['ACE'], ['ACF'], ['ACG'], ['ACH'], ['ADE'], ['ADF'], ['ADG'], ['ADH'], ['AEF'], ['AEG'], ['AEH'], ['AFG'], ['AFH'], ['AGH'],
    ['BCD'], ['BCE'], ['BCF'], ['BCG'], ['BCH'], ['BDE'], ['BDF'], ['BDG'], ['BDH'], ['BEF'], ['BEG'], ['BEH'], ['BFG'], ['BFH'], ['BGH'],
    ['CDE'], ['CDF'], ['CDG'], ['CDH'], ['CEF'], ['CEG'], ['CEH'], ['CFG'], ['CFH'], ['CGH'],
    ['DEF'], ['DEG'], ['DEH'], ['DFG'], ['DFH'], ['DGH'],
    ['EFG'], ['EFH'], ['EGH'],
    ['FGH'],

    # 4
    ['ABCD'], ['ABCE'], ['ABCF'], ['ABCG'], ['ABCH'], ['ABDE'], ['ABDF'], ['ABDG'], ['ABDH'], ['ABEF'], ['ABEG'], ['ABEH'],
    ['ABFG'], ['ABFH'], ['ABGH'],
    ['ACDE'], ['ACDF'], ['ACDG'], ['ACDH'], ['ACEF'], ['ACEG'], ['ACEH'], ['ACFG'], ['ACFH'], ['ACGH'],
    ['ADEF'], ['ADEG'], ['ADEH'], ['ADFG'], ['ADFH'], ['ADGH'],
    ['AEFG'], ['AEFH'], ['AEGH'],
    ['AFGH'],

    ['BCDE'], ['BCDF'], ['BCDG'], ['BCDH'], ['BCEF'], ['BCEG'], ['BCEH'], ['BCFG'], ['BCFH'], ['BCGH'],
    ['BDEF'], ['BDEG'], ['BDEH'], ['BDFG'], ['BDFH'], ['BDGH'],
    ['BEFG'], ['BEFH'], ['BEGH'],
    ['BFGH'],

    ['CDEF'], ['CDEG'], ['CDEH'], ['CDFG'], ['CDFH'], ['CDGH'],
    ['CEFG'], ['CEFH'], ['CEGH'],
    ['CFGH'],

    ['DEFG'], ['DEFH'], ['DEGH'],
    ['DFGH'],

    # 5
    ['ABCDE'], ['ABCDF'], ['ABCDG'], ['ABCDH'], ['ABCEF'], ['ABCEG'], ['ABCEH'], ['ABCFG'], ['ABCFH'], ['ABCGH'], ['ABDEF'], ['ABDEG'], ['ABDEH'],
    ['ABDFG'], ['ABDFH'], ['ABDGH'],
    ['ABEFG'], ['ABEFH'], ['ABEGH'],
    ['ABFGH'],

    ['ACDEF'], ['ACDEG'], ['ACDEH'], ['ACDFG'], ['ACDFH'], ['ACDGH'],
    ['ACEFG'], ['ACEFH'], ['ACEGH'],
    ['ACFGH'],

    ['ADEFG'], ['ADEFH'], ['ADEGH'],
    ['ADFGH'],

    ['AEFGH'],

    ['BCDEF'], ['BCDEG'], ['BCDEH'], ['BCDFG'], ['BCDFH'], ['BCDGH'],
    ['BCEFG'], ['BCEFH'], ['BCEGH'],
    ['BCFGH'],

    ['BDEFG'], ['BDEFH'], ['BDEGH'],
    ['BDFGH'],

    ['BEFGH'],

    ['CDEFG'], ['CDEFH'], ['CDEGH'], ['CDFGH'],
    ['CEFGH'],

    ['DEFGH'],

    # 6
    ['ABCDEF'], ['ABCDEG'], ['ABCDEH'], ['ABCDFG'], ['ABCDFH'], ['ABCDGH'],
    ['ABCEFG'], ['ABCEFH'], ['ABCEGH'], ['ABCFGH'],
    ['ABDEFG'], ['ABDEFH'], ['ABDEGH'],
    ['ABDFGH'], ['ABEFGH'],
    ['ACDEFG'], ['ACDEFH'], ['ACDEGH'], ['ACDFGH'],
    ['ACEFGH'],
    ['ADEFGH'],
    ['BCDEFG'], ['BCDEFH'], ['BCDEGH'], ['BCDFGH'],
    ['BCEFGH'],
    ['BDEFGH'],
    ['CDEFGH'],

    # 7
    ['ABCDEFG'], ['ABCDEFH'], ['ABCDEGH'], ['ABCDFGH'],
    ['ABCEFGH'],
    ['ACDEFGH'],
    ['BCDEFGH'],

    # 8
    ['ABCDEFGH']
]

def range_fixer(ranges):
    overlapping_ranges = []
    
    for i in range(len(ranges) - 1):
        range1 = ranges[i]
        key1, values1 = list(range1.items())[0]
        
        for j in range(i + 1, len(ranges)):
            range2 = ranges[j]
            key2, values2 = list(range2.items())[0]
            
            # Compare each pair of ranges
            if key1 in key2 or key2 in key1:
                overlap = any(x <= values2[0] <= y or x <= values2[1] <= y for x, y in zip(values1[::2], values1[1::2]))
                
                if overlap:
                    overlapping_ranges.append([key1, values1, key2, values2])
    
    return overlapping_ranges


def save_overlapping_ranges_to_csv(file_path, overlapping_ranges):
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Range 1 Key', 'Range 1 Values', 'Range 2 Key', 'Range 2 Values'])
        
        for row in overlapping_ranges:
            writer.writerow(row)


def organize_data_from_csv(file_path, ranges):
    organized_data = {}
    
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        for row in reader:
            date = row[0]
            values = [float(value) for value in row[1:]]
            
            for i, key in enumerate(ranges.keys()):
                if key not in organized_data:
                    organized_data[key] = []
                organized_data[key].append(values[i])
    
    return organized_data


def generate_ranges_from_data(organized_data):
    ranges = []
    keys = list(organized_data.keys())
    num_days = len(organized_data[keys[0]])
    
    for day in range(num_days - 1):
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                range_key = keys[i] + keys[j]
                range_values = []
                
                for key in range_key:
                    range_values.append(organized_data[key][day])
                    range_values.append(organized_data[key][day + 1])
                
                ranges.append({range_key: range_values})
    
    return ranges


data_file = 'data/transformed_data/ecl_interactions.csv'
range_frame = {
    'A': [0, 0],
    'B': [0, 0],
    'C': [0, 0],
    'D': [0, 0],
    'E': [0, 0],
    'F': [0, 0],
    'G': [0, 0],
    'H': [0, 0]
}

organized_data = organize_data_from_csv(data_file, range_frame)
ranges = generate_ranges_from_data(organized_data)
overlapping_ranges = range_fixer(ranges)

output_file = 'data/transformed_data/overlapping_ranges.csv'
save_overlapping_ranges_to_csv(output_file, overlapping_ranges)