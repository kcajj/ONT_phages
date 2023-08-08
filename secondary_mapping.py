import pysam
import matplotlib.pyplot as plt

def find_reads_with_secondary_mapping(bam_file):
    primary_positions = []
    secondary_positions = []
    read_names = []
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam.fetch():
            # Check if the read has a secondary alignment (i.e., supplementary alignment)
            if read.is_secondary:
                read_names.append(read.query_name)
                secondary_positions.append(read.reference_start)

        while len(read_names)>0:
            for read in bam.fetch():
                if read.query_name in read_names:
                    if not read.is_secondary:
                        primary_positions.append(read.reference_start)
                        read_names.remove(read.query_name)

    return primary_positions, secondary_positions

if __name__ == "__main__":
    # Replace 'your_file.bam' with the path to your BAM file
    bam_file_path = 'results/EM60/mapping/new_chemistry/new_chemistry.bam'
    pp, sp = find_reads_with_secondary_mapping(bam_file_path)
    plt.scatter(pp,sp)
    plt.ylabel('secondary mapping')
    plt.xlabel('primary mapping')
    plt.show()
