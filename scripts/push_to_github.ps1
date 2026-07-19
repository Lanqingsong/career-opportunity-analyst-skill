param(
    [string]$Remote = "origin",
    [string]$Branch = "main",
    [string]$Message = "docs: update skill",
    [switch]$NoCommit,
    [switch]$SkipFetch,
    [switch]$NoPush
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Invoke-Git {
    param([Parameter(Mandatory = $true)][string[]]$GitArgs)

    Write-Host ""
    Write-Host "git $($GitArgs -join ' ')" -ForegroundColor Cyan
    & git @GitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Git command failed: git $($GitArgs -join ' ')"
    }
}

function Get-GitText {
    param([Parameter(Mandatory = $true)][string[]]$GitArgs)

    $output = & git @GitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Git command failed: git $($GitArgs -join ' ')"
    }
    return @($output)
}

function Get-ItemCount {
    param([AllowNull()][object]$Items)

    if ($null -eq $Items) {
        return 0
    }

    return @($Items | Where-Object { $null -ne $_ -and "$_".Length -gt 0 }).Count
}

function Get-GitDir {
    $gitDir = (Get-GitText @("rev-parse", "--git-dir") | Select-Object -First 1)
    if ([System.IO.Path]::IsPathRooted($gitDir)) {
        return $gitDir
    }
    return Join-Path (Get-Location) $gitDir
}

function Test-RebaseInProgress {
    $gitDir = Get-GitDir
    return (Test-Path (Join-Path $gitDir "rebase-merge")) -or (Test-Path (Join-Path $gitDir "rebase-apply"))
}

function Get-UnmergedFiles {
    return @(Get-GitText @("diff", "--name-only", "--diff-filter=U") | Where-Object { $_ })
}

function Stop-WithConflictHelp {
    param([string[]]$Files)

    Write-Host ""
    Write-Host "Push stopped because Git has unresolved conflicts:" -ForegroundColor Yellow
    foreach ($file in $Files) {
        Write-Host "  - $file"
    }
    Write-Host ""
    Write-Host "Fix the files above, then run:" -ForegroundColor Yellow
    Write-Host "  git add <fixed-files>"
    Write-Host "  scripts\push_to_github.ps1 -Message `"$Message`""
    exit 2
}

function New-NoopEditor {
    $gitDir = Get-GitDir
    $editor = Join-Path $gitDir "codex-noop-editor.cmd"
    Set-Content -LiteralPath $editor -Encoding ASCII -Value @(
        "@echo off",
        "exit /b 0"
    )
    return $editor
}

function Continue-RebaseIfNeeded {
    while (Test-RebaseInProgress) {
        $unmerged = Get-UnmergedFiles
        if ((Get-ItemCount $unmerged) -gt 0) {
            Stop-WithConflictHelp $unmerged
        }

        $env:GIT_EDITOR = New-NoopEditor
        Invoke-Git @("rebase", "--continue")
    }
}

function Ensure-OnBranch {
    $current = (Get-GitText @("branch", "--show-current") | Select-Object -First 1)
    if ($current -eq $Branch) {
        return
    }

    if ([string]::IsNullOrWhiteSpace($current)) {
        if (Test-RebaseInProgress) {
            Continue-RebaseIfNeeded
            $current = (Get-GitText @("branch", "--show-current") | Select-Object -First 1)
        }
    }

    if ($current -ne $Branch) {
        Invoke-Git @("switch", $Branch)
    }
}

function Ensure-SafeDirectory {
    param([string]$RepoRoot)

    $existing = @(& git config --global --get-all safe.directory 2>$null)
    if ($existing -notcontains $RepoRoot) {
        Invoke-Git @("config", "--global", "--add", "safe.directory", $RepoRoot)
    }
}

function Commit-WorkingTreeIfNeeded {
    if ($NoCommit) {
        return
    }

    $changes = @(Get-GitText @("status", "--porcelain") | Where-Object { $_ })
    if ((Get-ItemCount $changes) -eq 0) {
        return
    }

    $unmerged = Get-UnmergedFiles
    if ((Get-ItemCount $unmerged) -gt 0) {
        Stop-WithConflictHelp $unmerged
    }

    Invoke-Git @("add", "-A")
    & git diff --cached --quiet
    if ($LASTEXITCODE -eq 1) {
        Invoke-Git @("commit", "-m", $Message)
    }
    elseif ($LASTEXITCODE -ne 0) {
        throw "Git command failed: git diff --cached --quiet"
    }
}

function Rebase-OnRemoteIfNeeded {
    if (-not $SkipFetch) {
        Invoke-Git @("fetch", $Remote)
    }

    $remoteRef = "$Remote/$Branch"
    & git rev-parse --verify --quiet $remoteRef *> $null
    if ($LASTEXITCODE -ne 0) {
        return
    }

    $localSha = (Get-GitText @("rev-parse", $Branch) | Select-Object -First 1)
    $remoteSha = (Get-GitText @("rev-parse", $remoteRef) | Select-Object -First 1)
    $baseSha = (Get-GitText @("merge-base", $Branch, $remoteRef) | Select-Object -First 1)

    if ($localSha -eq $remoteSha) {
        return
    }

    if ($baseSha -ne $remoteSha) {
        Invoke-Git @("rebase", $remoteRef)
        Continue-RebaseIfNeeded
    }
}

try {
    $repoRoot = (Get-GitText @("rev-parse", "--show-toplevel") | Select-Object -First 1)
    Set-Location $repoRoot

    Ensure-SafeDirectory $repoRoot
    Continue-RebaseIfNeeded
    Ensure-OnBranch
    Commit-WorkingTreeIfNeeded
    Rebase-OnRemoteIfNeeded
    Continue-RebaseIfNeeded

    if ($NoPush) {
        Write-Host ""
        Write-Host "Ready to push. NoPush was set, so nothing was uploaded." -ForegroundColor Green
        exit 0
    }

    Invoke-Git @("push", "-u", $Remote, $Branch)
    Write-Host ""
    Write-Host "Push completed." -ForegroundColor Green
}
catch {
    Write-Host ""
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}
