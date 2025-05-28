import sqlite3

def add_job(job_role, company, package, job_description):
    conn2 = sqlite3.connect('db/hireme.db')
    cursor2 = conn2.cursor()
    cursor2.execute('''INSERT INTO jobs (job_role, company, package, job_description) VALUES (?, ?, ?, ?)''', (job_role, company, package, job_description))
    conn2.commit()
    conn2.close()

if __name__ == '__main__':
    print("create_job.py loaded")
    print("Functions available:", [f for f in dir() if not f.startswith('_')])