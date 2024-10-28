@echo off
setlocal

echo Setting up Vanguard project...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/
    exit /b 1
)

:: Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please install pip.
    exit /b 1
)

:: Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed. Please install Git from https://git-scm.com/downloads
    exit /b 1
)

:: Check if PostgreSQL is installed
pg_config --version >nul 2>&1
if %errorlevel% neq 0 (
    echo PostgreSQL is not installed. Please install PostgreSQL from https://www.postgresql.org/download/windows/
    exit /b 1
)

:: Install required Python packages
echo Installing Python packages...
pip install django psycopg2-binary

:: Clone the repository
echo Cloning the repository...
git clone https://github.com/yourusername/Vanguard.git
cd Vanguard

:: Set up PostgreSQL
echo Setting up PostgreSQL database...
:: Store the PostgreSQL commands in a temporary file
echo CREATE USER vanguard WITH PASSWORD '12345678'; > db_setup.sql
echo ALTER ROLE vanguard SET client_encoding TO 'utf8'; >> db_setup.sql
echo ALTER ROLE vanguard SET default_transaction_isolation TO 'read committed'; >> db_setup.sql
echo ALTER ROLE vanguard SET timezone TO 'UTC'; >> db_setup.sql
echo CREATE DATABASE vanguard OWNER vanguard; >> db_setup.sql

:: Run the PostgreSQL commands
:: Note: This assumes PostgreSQL bin directory is in PATH
:: and that the default superuser is 'postgres'
psql -U postgres -f db_setup.sql

:: Clean up the temporary file
del db_setup.sql

:: Make and apply migrations
echo Setting up Django database...
python manage.py makemigrations
python manage.py migrate

:: Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput

:: Optional: Create superuser
:: echo Creating superuser...
:: python manage.py createsuperuser

echo Setup complete! You can now run the server with:
echo python manage.py runserver

:: Optional: Start the development server
:: python manage.py runserver

endlocal
