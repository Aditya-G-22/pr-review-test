import os

def run_backup(filename):
    os.system("tar -czf backup.tar.gz " + filename)
