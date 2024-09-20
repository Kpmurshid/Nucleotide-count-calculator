def nucleotide_counts(sequence):
    # Convert the sequence to uppercase to handle case sensitivity
    sequence = sequence.upper()

    # Count A, T, G, C
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    g_count = sequence.count('G')
    c_count = sequence.count('C')

    # Calculate total length
    total_length = len(sequence)

    # Calculate GC percentage
    gc_content = (g_count + c_count) / total_length * 100 if total_length > 0 else 0.0

    return {
        "A": a_count,
        "T": t_count,
        "G": g_count,
        "C": c_count,
        "GC Percentage": gc_content
    }


# Example usage

dna_sequence = "AGCTAGCTAGCGATCGATTCCTGGAGATTCACACAAGACAATCGATCGGCTAGCTAGCTAG"
counts = nucleotide_counts(dna_sequence)
print(f"Nucleotide Counts: {counts}")
