import pysam
import matplotlib.pyplot as plt

def find_reads_with_secondary_mapping(bam_file):
    reads_positions = []
    with pysam.AlignmentFile(bam_file, "rb") as bam:
        for read in bam.fetch():
            # Check if the read has a secondary alignment (i.e., supplementary alignment)
            if read.is_secondary:
                read_name = read.query_name
                primary_position = read.reference_start
                secondary_position = read.next_reference_start
                reads_positions.append((primary_position, secondary_position))
    return reads_positions

if __name__ == "__main__":
    # Replace 'your_file.bam' with the path to your BAM file
    bam_file_path = 'your_file.bam'
    reads_positions = find_reads_with_secondary_mapping(bam_file_path)
    plt.plot(reads_positions[0], reads_positions[1])
    plt.show()

samfile = pysam.AlignmentFile("ex1.bam", "rb")
for read in samfile.fetch('chr1', 100, 120):
    print(read)
samfile.close()

