def nucleotide_counts(seq):
    # Handle case sensitivity
    seq = seq.upper()

    # Count A, T, G, C
    a_count = seq.count('A')
    t_count = seq.count('T')
    g_count = seq.count('G')
    c_count = seq.count('C')

    # Calculate the total length
    total_length = len(seq)

    # Calculate GC percentage
    gc_content = (g_count + c_count) / total_length * 100 if total_length > 0 else 0.0

    return {
        "A": a_count,
        "T": t_count,
        "G": g_count,
        "C": c_count,
        "GC Percentage": gc_content
    }


# Example
dna_sequence = "AGCTAGCTAGCGATCGATTCCTGGAGATTCACACAAGACAATCGATCGGCTAGCTAGCTAG"
counts = nucleotide_counts(dna_sequence)
print(f"Nucleotide Counts: {counts}")
