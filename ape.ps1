# APE Pipeline - Windows PowerShell Version
# Save as: ape.ps1

param(
    [Parameter(Position=0)]
    [string]$Command = "help",
    
    [Parameter(Position=1)]
    [string]$Arg1 = "",
    
    [Parameter(Position=2)]
    [string]$Arg2 = "",
    
    [Parameter(Position=3)]
    [string]$Arg3 = "",
    
    [Parameter(Position=4)]
    [string]$Arg4 = "",
    
    [Parameter(Position=5)]
    [string]$Arg5 = ""
)

function Show-Help {
    Write-Host "APE Pipeline - Windows PowerShell Version" -ForegroundColor Cyan
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Commands:" -ForegroundColor Yellow
    Write-Host "  .\ape.ps1 generate 'Question' [Method]           - Generate basic paper"
    Write-Host "  .\ape.ps1 generate-field 'Question' field method - Generate for specific field"
    Write-Host "  .\ape.ps1 generate-dir 'Question' field method data\ refs\ - With directories"
    Write-Host "  .\ape.ps1 review [paper_id]                      - Review paper"
    Write-Host "  .\ape.ps1 tournament [p1] [p2]                   - Compare papers"
    Write-Host "  .\ape.ps1 leaderboard                            - View rankings"
    Write-Host "  .\ape.ps1 fields                                 - List supported fields"
    Write-Host "  .\ape.ps1 setup                                  - Edit configuration"
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Green
    Write-Host '  .\ape.ps1 generate "Min wage effects" DiD'
    Write-Host '  .\ape.ps1 generate-field "Social media" psychology Survey'
    Write-Host '  .\ape.ps1 generate-dir "HSR pollution" economics DiD .\data .\refs'
}

function Show-Fields {
    Write-Host "Supported Academic Fields" -ForegroundColor Cyan
    Write-Host "=========================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1. economics (default)     - AER/QJE style, DiD/RDD/IV"
    Write-Host "2. psychology              - APA style, experiments/surveys"
    Write-Host "3. computer_science        - ACM style, algorithms"
    Write-Host "4. medicine                - NEJM style, RCTs"
    Write-Host "5. sociology               - ASR style, ethnography"
    Write-Host "6. political_science       - APSR style, quantitative"
    Write-Host "7. education               - AERA style, mixed methods"
    Write-Host "8. environmental_science   - Nature style, modeling"
}

function Edit-Config {
    $editor = $env:EDITOR
    if (-not $editor) { $editor = "notepad" }
    & $editor "config\.env"
}

function Invoke-Generate {
    param($Question, $Method = "DiD")
    python scripts\generate_paper.py "$Question" "economics" "$Method"
}

function Invoke-GenerateField {
    param($Question, $Field = "economics", $Method = "")
    python scripts\generate_paper.py "$Question" "$Field" "$Method"
}

function Invoke-GenerateDir {
    param($Question, $Field = "economics", $Method = "", $DataDir = "", $RefsDir = "")
    python scripts\generate_paper.py "$Question" "$Field" "$Method" "$DataDir" "$RefsDir"
}

function Invoke-Review {
    param($PaperId)
    python scripts\review_paper.py "$PaperId"
}

function Invoke-Tournament {
    param($P1, $P2)
    python scripts\tournament.py match "$P1" "$P2"
}

function Invoke-Leaderboard {
    python scripts\tournament.py leaderboard
}

# Main switch
switch ($Command) {
    "help" { Show-Help }
    "fields" { Show-Fields }
    "setup" { Edit-Config }
    "generate" { Invoke-Generate -Question $Arg1 -Method $Arg2 }
    "generate-field" { Invoke-GenerateField -Question $Arg1 -Field $Arg2 -Method $Arg3 }
    "generate-dir" { Invoke-GenerateDir -Question $Arg1 -Field $Arg2 -Method $Arg3 -DataDir $Arg4 -RefsDir $Arg5 }
    "review" { Invoke-Review -PaperId $Arg1 }
    "tournament" { Invoke-Tournament -P1 $Arg1 -P2 $Arg2 }
    "leaderboard" { Invoke-Leaderboard }
    default { Show-Help }
}
