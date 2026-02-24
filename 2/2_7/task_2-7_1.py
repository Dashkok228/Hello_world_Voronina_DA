files = ["seq1", "seq2", "seq3", "seq4"]
sample_date = "2025-02-10"
for name in files:

   new_name = f"{name}_{sample_date}.fasta"

   print(f"{new_name}")