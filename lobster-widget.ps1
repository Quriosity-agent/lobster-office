# Lobster Office - Desktop Widget
# Opens as a small always-on-top-like Chrome window
Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList @(
    "--app=http://127.0.0.1:18891",
    "--window-size=360,300",
    "--window-position=1520,720"
)
