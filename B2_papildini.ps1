# ----------------------------------------------------------------------
# B2. PowerShell — līmeņu kopsavilkums CSV failā
# ----------------------------------------------------------------------

# Saskaiti, cik žurnālā ir katra līmeņa rindu, un saglabā rezultātu CSV failā limeni.csv, ko var atvērt Excel. Aizpildi vietu, kur stāv TODO.
#
# Aizpildi vietu, kur stāv TODO. Tad palaid.
# ----------------------------------------------------------------------                                                                                                Pirms eksporta izvadi Write-Host rindu "Grupēts".

$rindas = Get-Content "sistema.log"
$limeni = $rindas | ForEach-Object { ($_ -split " ")[2] }

# TODO: saskaiti, cik reižu katrs līmenis parādās,
# TODO: un saglabā rezultātu failā limeni.csv
