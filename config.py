import os

class Config:
    # LinkedIn credentials (use environment variables)
    LINKEDIN_EMAIL = os.getenv('LINKEDIN_EMAIL')
    LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
    
    # Database settings
    DATABASE_URI = 'sqlite:///companies.db'
