import pysam
import matplotlib.pyplot as plt
from collections import defaultdict

def find_reads_with_secondary_mapping(bam_file):
    primary_positions = {}
    secondary_positions = defaultdict(list)
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam.fetch():
            # Check if the read has a secondary alignment (i.e., supplementary alignment)
            if read.is_secondary:
                secondary_positions[read.query_name].append(read.reference_start+((read.reference_end-read.reference_start)/2))
        for read in bam.fetch():
            if read.query_name in secondary_positions.keys():
                if not read.is_secondary:
                    primary_positions[read.query_name]=read.reference_start+((read.reference_end-read.reference_start)/2)

    return primary_positions, secondary_positions

def get_points(pp,sp):
    points=[]
    for name,secondary_mappings in sp.items():
        for secondary_mapping in secondary_mappings:
            points.append((pp[name],secondary_mapping))
    return points


if __name__ == "__main__":
    # Replace 'your_file.bam' with the path to your BAM file
    bam_file_path = 'results/EM60/mapping/new_chemistry/new_chemistry.bam'
    primary_positions, secondary_positions = find_reads_with_secondary_mapping(bam_file_path)
    points = get_points(primary_positions,secondary_positions)
    
    x=[]
    y=[]
    for p in points:
        x.append(p[0])
        y.append(p[1])

    plt.scatter(x,y)
    plt.ylabel('secondary mapping')
    plt.xlabel('primary mapping')
    plt.show()