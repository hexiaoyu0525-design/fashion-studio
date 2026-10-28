<#
.SYNOPSIS
fashion-web-scraper 新环境初始化：检查 Node/npx、验证 @playwright/cli、冒烟测试浏览器、按需安装内核。

.DESCRIPTION
换新电脑 / 首次使用通道①（本地 playwright-cli 批量采集）前运行。
只做"检查 -> 验证 -> 冒烟 -> 按需安装"，不写死任何本地路径，保持技能可移植。
内核装不上不影响功能：自动落回通道②（Agent 内置浏览器）或通道③（手动放图）。

.PARAMETER InstallBrowser
加 -InstallBrowser 才会下载 chromium 内核（约 440MB，一次下载永久复用）。
不带则只检查/验证/冒烟，不下载。

.PARAMETER HeadlessOnly
与 -InstallBrowser 同用：只装无头内核 chromium_headless_shell（约 280MB），适合纯无头批量截图。

.EXAMPLE
pwsh -NoProfile -File setup.ps1
pwsh -NoProfile -File setup.ps1 -InstallBrowser
pwsh -NoProfile -File setup.ps1 -InstallBrowser -HeadlessOnly
#>

param(
    [switch]$InstallBrowser,
    [switch]$HeadlessOnly
)

$ErrorActionPreference = 'Stop'

function Step($msg) { Write-Host "==> $msg" -ForegroundColor Cyan }
function Ok($msg)   { Write-Host "    OK: $msg" -ForegroundColor Green }
function Warn($msg) { Write-Host "    提示: $msg" -ForegroundColor Yellow }

# --- 1/4 检查 Node.js 与 npx ---
Step '1/4 检查 Node.js 与 npx'
$nodeVer = & node --version 2>$null
if ($LASTEXITCODE -ne 0 -or -not $nodeVer) {
    throw '未找到 node。请先安装 Node.js LTS：winget install OpenJS.NodeJS.LTS（或 https://nodejs.org 下载）后重跑本脚本。'
}
Ok "node $nodeVer"
if (-not (Get-Command npx -ErrorAction SilentlyContinue)) {
    throw '未找到 npx（随 npm 提供），请确认 Node.js 安装完整。'
}
Ok 'npx 可用'

# --- 2/4 验证 @playwright/cli（npx 自动拉取，无需全局安装） ---
Step '2/4 验证 @playwright/cli'
$cliOut = npx --yes @playwright/cli --help 2>&1 | Select-Object -First 1
if ($LASTEXITCODE -ne 0 -or -not $cliOut) {
    throw "playwright-cli 启动失败：$cliOut  （检查网络后重试）"
}
Ok '@playwright/cli 可用'

# --- 3/4 冒烟测试：真实启动一次浏览器（open + close） ---
Step '3/4 冒烟测试浏览器内核'
npx --yes @playwright/cli open about:blank *> $null
if ($LASTEXITCODE -ne 0) {
    if ($InstallBrowser) {
        Warn '冒烟失败——内核可能仍未就绪，见下方安装步骤结果。'
    } else {
        Warn '未检测到可用浏览器内核。两种选择：'
        Warn '  a) 需要本地批量：pwsh -NoProfile -File setup.ps1 -InstallBrowser'
        Warn '  b) 不装内核：直接走通道②（Agent 内置浏览器）或通道③（手动放图），功能不受影响'
    }
} else {
    npx --yes @playwright/cli close *> $null
    Ok '浏览器内核可用'
}

# --- 4/4 按需安装内核 ---
if ($InstallBrowser) {
    Step '4/4 安装浏览器内核（一次下载，永久复用）'
    if ($HeadlessOnly) {
        npx --yes playwright@latest install chromium --only-shell
    } else {
        npx --yes playwright@latest install chromium
    }
    if ($LASTEXITCODE -ne 0) {
        Warn '内核下载失败（网络/代理受限）。功能不受影响：改用通道②（Agent 内置浏览器）或通道③（手动放图）。'
    } else {
        Ok '内核安装完成'
        # 再冒烟一次
        Step '    复核冒烟'
        npx --yes @playwright/cli open about:blank *> $null
        if ($LASTEXITCODE -eq 0) {
            npx --yes @playwright/cli close *> $null
            Ok '通道① 就绪：可用 playwright-cli 批量采集'
        } else {
            Warn '复核未通过：若 cli 提示缺少特定内核版本，按提示补装（如 npx playwright@latest install chromium）。仍不行则落回通道②/③。'
        }
    }
} else {
    Step '4/4 跳过内核安装'
    Write-Host '    日常任务走通道②/③ 即可；需要本地批量时再跑: pwsh -NoProfile -File setup.ps1 -InstallBrowser' -ForegroundColor DarkGray
}

Write-Host ''
Write-Host '完成。规则：内核装不上 ≠ 功能不可用；任务流程始终可继续。' -ForegroundColor Green
