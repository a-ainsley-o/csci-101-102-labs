# Addison Olstad
# CSCI 102 - Section H
# Assessment04-amino_acids
# References:
# Time:

print("Input the chemical elements of the amino acid:")
car = input("CARBON> ")
hydro = input("HYDROGEN> ")
nitro = input("NITROGEN> ")
oxy = input("OXYGEN> ")
sul = input("SULFUR> ")

aa_string = car + hydro + nitro + oxy + sul
#aa_string = str(aa_string)

def translate(seq):
    aa_dict = {"37120":"Alanine",
           "614420":"Arginine",
           "48230":"Asparagine",
           "37121":"Cysteine",
           "69320":"Histidine",
           "510230":"Glutamine"}
    aa_name = " "
    aa_name = aa_dict.get(str(seq))
    return aa_name

new_aa = translate(aa_string)

print("The amino acid for {}C--{}H--{}N--{}O--{}S is {}".format(car, hydro, nitro, oxy, sul, new_aa))
print("OUTPUT {}C--{}H--{}N--{}O--{}S".format(car, hydro, nitro, oxy, sul))
print("OUTPUT {}".format(new_aa))
