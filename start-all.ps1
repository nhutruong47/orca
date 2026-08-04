$ErrorActionPreference = "Continue"
$ProjectRoot = $PSScriptRoot

Write-Host "Attempting to start PostgreSQL via Docker Compose..."
try {
    Push-Location "$ProjectRoot\orca-backend-main"
    docker-compose up -d postgres
    Pop-Location
} catch {
    Write-Warning "Failed to start Postgres. Please ensure Docker Desktop is running."
}

Write-Host "Starting Backend in a new window..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$ProjectRoot\orca-backend-main\backend'; Write-Host 'Starting Backend...'; .\mvnw.cmd spring-boot:run `"-Dspring-boot.run.profiles=local`""

Write-Host "Starting AI Service in a new window..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$ProjectRoot\ai-service'; Write-Host 'Starting AI Service...'; .\run-local.ps1"

Write-Host "Starting Frontend in a new window..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$ProjectRoot\frontend-web-main'; Write-Host 'Installing dependencies and starting Frontend...'; npm install; npm run dev"

Write-Host "All services have been initiated!"
