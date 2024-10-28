#!/bin/bash

# Update system packages
echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

# Install Python and pip
echo "Installing Python and pip..."
sudo apt-get install -y python3
sudo apt-get install -y python3-pip

# Install PostgreSQL and its dependencies
echo "Installing PostgreSQL..."
sudo apt-get install -y postgresql postgresql-contrib libpq-dev

# Install Git
echo "Installing Git..."
sudo apt-get install -y git

# Install Python packages
echo "Installing Python packages..."
pip3 install django psycopg2-binary

# Clone the repository
echo "Cloning the repository..."
git clone https://github.com/nathy-cpu/Cyber-Vanguard.git
cd Cyber-Vanguard

# Create PostgreSQL user and database
echo "Setting up PostgreSQL..."
sudo -u postgres psql <<EOF
CREATE USER vanguard WITH PASSWORD '12345678';
ALTER ROLE vanguard SET client_encoding TO 'utf8';
ALTER ROLE vanguard SET default_transaction_isolation TO 'read committed';
ALTER ROLE vanguard SET timezone TO 'UTC';
CREATE DATABASE vanguard OWNER vanguard;
\q
EOF

# Make migrations and migrate
echo "Setting up Django database..."
python3 manage.py makemigrations
python3 manage.py migrate

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Create superuser (optional, commented out)
# echo "Creating superuser..."
# python3 manage.py createsuperuser

# Set proper permissions
echo "Setting permissions..."
chmod +x manage.py

echo "Setup complete! You can now run the server with:"
echo "python3 manage.py runserver"

# Optional: Start the development server
# python3 manage.py runserver
