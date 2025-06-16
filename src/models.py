from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from enum import Enum

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    favorites: Mapped[List["Favorites"]] = relationship(back_populates="user")

class Favorites(db.Model):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character_id: Mapped[Optional[int]] = mapped_column(ForeignKey("characters.id"), nullable=True)
    film_id: Mapped[Optional[int]] = mapped_column(ForeignKey("films.id"), nullable=True)
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planets.id"), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="favorites")
    character: Mapped[Optional["Characters"]] = relationship("Characters", back_populates="favorited_by")
    film: Mapped[Optional["Films"]] = relationship("Films", back_populates="favorited_by")
    planet: Mapped[Optional["Planets"]] = relationship("Planets", back_populates="favorited_by")


    

class Characters(db.Model):
    __tablename__ = "characters"
    id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    birth_year: Mapped[int] = mapped_column(nullable=True)
    homeworld: Mapped[str] = mapped_column(String(120), nullable=False)
    skin_color: Mapped[Optional[str]] = mapped_column(String(120))
    favorited_by: Mapped[List["Favorites"]] = relationship("Favorites", back_populates="character")

class Films(db.Model):
    __tablename__ = "films"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    episode_id:Mapped[int] = mapped_column(nullable=True)
    director: Mapped[str] = mapped_column(String(120), nullable=True)
    favorited_by: Mapped[List["Favorites"]] = relationship("Favorites", back_populates="film")


class Planets(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    diameter: Mapped[Optional[str]] = mapped_column(String(500))
    gravity: Mapped[Optional[int]] = mapped_column(nullable=True)
    population: Mapped[Optional[int]] = mapped_column(nullable=True)
    terrain: Mapped[Optional[str]] = mapped_column(String(500))
    favorited_by: Mapped[List["Favorites"]] = relationship("Favorites", back_populates="planet")

