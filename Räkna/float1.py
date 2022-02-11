pris_utan_moms = float(input("Mata in ett pris: "))
moms = float(input("Mata in moms: "))

pris_med_moms = pris_utan_moms * (1 + moms)

print(f"Priset med moms är {pris_med_moms}")