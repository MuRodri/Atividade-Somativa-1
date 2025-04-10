$excludePaths = @("env", ".git", ".github")

Get-ChildItem -Recurse -Include *.py | Where-Object {
    $shouldInclude = $true
    foreach ($exclude in $excludePaths) {
        if ($_.FullName -match "\\$exclude\\") {
            $shouldInclude = $false
            break
        }
    }
    $shouldInclude
} | ForEach-Object {
    python -m black --config pyproject.toml --check $_.FullName
}