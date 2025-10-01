from .database import create_tables

def init_db():
    """Initialize database tables"""
    create_tables()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")