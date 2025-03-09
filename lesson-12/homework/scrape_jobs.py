import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

DB_FILE = "jobs.db"
URL = "https://realpython.github.io/fake-jobs"

def create_database():
    """Creates an SQLite database and jobs table if not exists."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(title, company, location)
        )
    ''')
    conn.commit()
    conn.close()

def scrape_jobs():
    """Scrapes job listings from the website."""
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for job_card in soup.find_all("div", class_="card-content"):
        title = job_card.find("h2", class_="title").text.strip()
        company = job_card.find("h3", class_="company").text.strip()
        location = job_card.find("p", class_="location").text.strip()
        description = job_card.find("div", class_="description").text.strip()
        application_link = job_card.find("a", text="Apply")["href"]
        jobs.append((title, company, location, description, application_link))
    
    return jobs

def save_jobs(jobs):
    """Stores or updates job listings in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(title, company, location) DO UPDATE SET
                description=excluded.description,
                application_link=excluded.application_link
        """, job)
    
    conn.commit()
    conn.close()

def filter_jobs(location=None, company=None):
    """Retrieves job listings filtered by location or company."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    if location:
        query += " AND location = ?"
        params.append(location)
    if company:
        query += " AND company = ?"
        params.append(company)
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def export_to_csv(filename, jobs):
    """Exports job listings to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(jobs)

def main():
    """Run the script."""
    create_database()
    jobs = scrape_jobs()
    save_jobs(jobs)
    print("Job listings updated.")

if __name__ == "__main__":
    main()