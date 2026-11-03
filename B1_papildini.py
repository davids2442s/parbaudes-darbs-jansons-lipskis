# ----------------------------------------------------------------------
# B1. Python — kļūdas pa diennakts stundām
# ----------------------------------------------------------------------

# Saskaiti, cik ERROR rindu ir katrā diennakts stundā, un izvadi tās no 00 līdz 23. Aizpildi abas vietas, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Vārdnīcu, kurā skaita, nosauc par stundu_tabula.

stundas = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        dalas = rinda.split()
        if dalas[2] == "ERROR":
            stunda = dalas[1][:2]
            # TODO: saskaiti, cik ERROR rindu ir katrā stundā
            error_skaits = stundas.get(stunda, 0)
            stundas[stunda] = error_skaits + 1

# TODO: izvadi rezultātu, sakārtotu pēc stundas no 00 līdz 23
for stunda in range(24):
    stunda_str = f"{stunda:02d}"
    error_skaits = stundas.get(stunda_str, 0)
    print(f"{stunda_str}: {error_skaits}")
