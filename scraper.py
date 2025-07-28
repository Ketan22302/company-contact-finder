from linkedin_api import Linkedin
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config
import datetime

# Database setup
Base = declarative_base()
engine = create_engine(Config.DATABASE_URI)
Session = sessionmaker(bind=engine)

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    website = Column(String)
    emails = Column(String)
    phones = Column(String)
    address = Column(String)
    vat = Column(String)
    linkedin = Column(String)
    last_updated = Column(String)

Base.metadata.create_all(engine)

class EnhancedScraper:
    def __init__(self):
        self.linkedin = Linkedin(
            Config.LINKEDIN_EMAIL,
            Config.LINKEDIN_PASSWORD
        )
    
    def get_linkedin_data(self, company_name):
        try:
            results = self.linkedin.search_companies(company_name)
            if results:
                company_id = results[0]['urn_id']
                return self.linkedin.get_company(company_id)
        except Exception as e:
            print(f"LinkedIn Error: {str(e)}")
        return None
    
    def cache_results(self, data):
        session = Session()
        company = session.query(Company).filter_by(name=data['name']).first()
        
        if company:
            # Update existing record
            for key, value in data.items():
                setattr(company, key, value)
            company.last_updated = datetime.datetime.now()
        else:
            # Create new record
            new_company = Company(
                **data,
                last_updated=datetime.datetime.now()
            )
            session.add(new_company)
        
        session.commit()
        session.close()
