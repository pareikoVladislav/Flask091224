__all__ = (
    'engine',
    'Base'
)

import dotenv
import os

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


proj_path = Path(__file__).parent.parent

dotenv.load_dotenv(
    dotenv_path=proj_path / '.env.stage'
)

engine = create_engine(
    url=os.getenv('DB_URI'),
    echo=True
)

Base = declarative_base()
