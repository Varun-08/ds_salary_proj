import glassdoor_scraper as gs
import pandas as pd

path = "/home/varun/Varun/Workspace/CONRAD/DS_Project_from_scratch/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)