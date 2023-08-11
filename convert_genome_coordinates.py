
def convert_coordinates(phage,assembly_site,offset,genome_length):

    if assembly_site<(genome_length-offset):
        reference_site=offset+assembly_site
    else:
        reference_site=assembly_site-(genome_length-offset)

    return reference_site

offset_dictionary={'EM11':94975}
genome_length_dictionary={'EM11':142668}

phage='EM11'
assembly_site=58828
reference_site=convert_coordinates(phage,assembly_site,offset_dictionary[phage],genome_length_dictionary[phage])
print(reference_site)