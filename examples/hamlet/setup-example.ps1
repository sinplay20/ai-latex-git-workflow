param(
    [string]$Destination = (Join-Path $PSScriptRoot "hamlet-history-work")
)

$ErrorActionPreference = "Stop"
$Bundle = Join-Path $PSScriptRoot "hamlet-history.bundle"

if (-not (Test-Path $Bundle)) {
    throw "Bundle not found: $Bundle. Run build-example.py first."
}

if (Test-Path $Destination) {
    throw "Destination already exists: $Destination"
}

git clone $Bundle $Destination
if ($LASTEXITCODE -ne 0) { throw "git clone failed" }

git -C $Destination remote remove origin
if ($LASTEXITCODE -ne 0) { throw "failed to remove bundle origin" }

git -C $Destination switch main
if ($LASTEXITCODE -ne 0) { throw "failed to switch to main" }

Write-Host "Created Hamlet course repository:" -ForegroundColor Green
Write-Host $Destination
Write-Host ""
git -C $Destination status --short --branch
git -C $Destination log -3 --oneline --decorate
