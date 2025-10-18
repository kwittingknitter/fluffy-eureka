"""SQLAlchemy Models"""

from __future__ import annotations

from typing import List
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base model"""
    pass


class Legislator(Base):
    """Legislator database model"""
    __tablename__ = "legislators"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[ str | None ] = mapped_column(String(50))
    leg_code: Mapped[str] = mapped_column(String(50))
    district_number: Mapped[int] = mapped_column(Integer)
    state: Mapped[str] = mapped_column(String(15))
    party: Mapped[str] = mapped_column(String(50))
    begin_date: Mapped[datetime] = mapped_column(DateTime)
    end_date: Mapped[ datetime | None ] = mapped_column(DateTime, nullable=True)
    politician_id: Mapped[int] = mapped_column(Integer, ForeignKey("politicians.id"))
    politician = relationship("Politician", back_populates="legislators")
    session_id: Mapped[int] = mapped_column(Integer, ForeignKey("sessions.id"))
    session = relationship("Session", back_populates="legislators")

    def __hash__(self):
        return hash(self.leg_code)

    def __eq__(self, other):
        if not isinstance(other, Legislator):
            return NotImplemented
        return self.leg_code == other.leg_code and self.begin_date == other.begin_date

    def __repr__(self):
        return f'<{self.leg_code}>'

    def __iter__(self):
        yield self


class Committee(Base):
    """Committee database model"""
    __tablename__ = "committees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    committee_type: Mapped[str] = mapped_column(Text)
    session_id: Mapped[int] = mapped_column(Integer, ForeignKey("sessions.id"))
    session = relationship("Session", back_populates="committees")

    def __repr__(self):
        return f'<{self.name}>'

    def __iter__(self):
        yield self

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Committee):
            return NotImplemented
        return self.name == other.name and self.committee_type == other.committee_type


class Politician(Base):
    """Politician database model"""
    __tablename__ = "politicians"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    legislators: Mapped[List["Legislator"]] = relationship(
        back_populates="politician")

    def __repr__(self):
        return f'<{self.first_name} {self.last_name}>'

    def __iter__(self):
        yield self

    def __hash__(self):
        return hash((self.first_name, self.last_name))

    def __eq__(self, other):
        if not isinstance(other, Politician):
            return NotImplemented
        return self.first_name == other.first_name and self.last_name == other.last_name


class Session(Base):
    """Session database model"""
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    begin_date: Mapped[datetime] = mapped_column(DateTime)
    end_date: Mapped[ datetime | None ] = mapped_column(DateTime)
    committees: Mapped[List["Committee"]] = relationship(back_populates="session")
    legislators: Mapped[List["Legislator"]] = relationship(back_populates="session")

    def __repr__(self):
        return f'<{self.name}>'

    def __iter__(self):
        yield self

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Session):
            return NotImplemented
        return self.name == other.name


db = SQLAlchemy(model_class=Base)
