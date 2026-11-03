# ----------------------------------------------------------------------
# C1. Python — kopsavilkuma atskaite
# ----------------------------------------------------------------------

# Uzraksti skriptu, kas izveido atskaites failu par visu žurnālu. Atskaitē jābūt: kopējam rindu skaitam, rindu skaitam katram līmenim, servisu sarakstam, kas sakārtots pēc ERROR skaita, un tā servisa nosaukumam, kuram kļūdu ir visvairāk. Skripts neko neprasa no lietotāja.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Atskaites failu nosauc par kopsavilkums_atskaite.txt.

# Uzraksti skriptu, kas izveido atskaites failu par visu žurnālu. Atskaitē jābūt: kopējam rindu skaitam, rindu skaitam katram līmenim, servisu sarakstam, kas sakārtots pēc ERROR skaita, un tā servisa nosaukumam, kuram kļūdu ir visvairāk. Skripts neko neprasa no lietotāja.
zurnals = "sistema.log"
kopa = 0



error_skaits = {}
with open(zurnals, "r") as f:
    for rinda in f:
        if "ERROR" in rinda:
            serviss = rinda.split(" ")[1]
            error_skaits[serviss] = error_skaits.get(serviss, 0) + 1




info_skaits = {}
with open(zurnals, "r") as f:
    for rinda in f:
        if "INFO" in rinda:
            serviss = rinda.split(" ")[1]
            info_skaits[serviss] = info_skaits.get(serviss, 0) + 1


warning_skaits = {}
with open(zurnals, "r") as f:
    for rinda in f:
        if "WARNING" in rinda:
            serviss = rinda.split(" ")[1]
            warning_skaits[serviss] = warning_skaits.get(serviss, 0) + 1

critical_skaits = {}
with open(zurnals, "r") as f:
    for rinda in f:
        if "CRITICAL" in rinda:
            serviss = rinda.split(" ")[1]
            critical_skaits[serviss] = critical_skaits.get(serviss, 0) + 1

kopa = len(error_skaits) + len(info_skaits) + len(warning_skaits) + len(critical_skaits)

print(f"kopējais rinidu skaits: {kopa}")
print(f"WARNING skaiti: {len(warning_skaits)}")
print(f"INFO skaiti: {len(info_skaits)}")

print(f"ERROR skaiti: {len(error_skaits)}")
print(f"CRITICAL skaiti: {len(critical_skaits)}")
