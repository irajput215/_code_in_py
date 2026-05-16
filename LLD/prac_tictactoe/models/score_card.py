from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from LLD.prac_tictactoe.models.player import Player

# SQLAlchemy Base class for models
Base = declarative_base()

class ScoreEntry(Base):
    """Database model for storing win counts."""
    __tablename__ = "scores"

    player_name = Column(String, primary_key=True)
    wins = Column(Integer, default=0)

    def __repr__(self):
        return f"<ScoreEntry(player='{self.player_name}', wins={self.wins})>"

class ScoreCard:
    def __init__(self, db_url: str = "sqlite:///tictactoe_scores.db"):
        # 1. Setup Engine and Session
        self._engine = create_engine(db_url)
        # Create tables if they don't exist
        Base.metadata.create_all(self._engine)
        
        self._Session = sessionmaker(bind=self._engine)

    def update_win(self, player: Player) -> None:
        """Increment win count using SQLAlchemy ORM."""
        session = self._Session()
        try:
            # Find existing entry or create a new one
            entry = session.query(ScoreEntry).filter_by(player_name=player.name).first()
            if entry:
                entry.wins += 1
            else:
                entry = ScoreEntry(player_name=player.name, wins=1)
                session.add(entry)
            
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error updating wins: {e}")
        finally:
            session.close()

    def display_scores(self) -> None:
        """Fetch and display scores using SQLAlchemy."""
        print("\n" + "="*20)
        print("🏆 SCORE CARD (ORM) 🏆")
        print("="*20)
        
        session = self._Session()
        try:
            entries = session.query(ScoreEntry).order_by(ScoreEntry.wins.desc()).all()
            if not entries:
                print("No wins recorded in database yet.")
            else:
                for entry in entries:
                    print(f"{entry.player_name:10}: {entry.wins} wins")
        finally:
            session.close()
        
        print("="*20 + "\n")

    def reset_scores(self) -> None:
        """Reset all scores to 0 using SQLAlchemy."""
        session = self._Session()
        try:
            session.query(ScoreEntry).delete()
            session.commit()
            print("✅ ScoreCard has been reset to default state (0).")
        except Exception as e:
            session.rollback()
            print(f"Error resetting scores: {e}")
        finally:
            session.close()
