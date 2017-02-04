from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

import settings

engine = create_engine(settings.DB_NAME)

Base = declarative_base()


# relationship("PublicTeam", secondary=team_skills, back_populates="skill")
class PublicTeam(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    idea_description = Column(String(255))
    repository = Column(String(255))
    need_more_members = Column(String(255))
    members_needed_desc = Column(String(255))
    room = Column(String(255))
    place = Column(String(255), nullable=True)
    skills = relationship(
            'SkillList',
            secondary='team_skills',
            back_populates='teams'
            )
    mentors = relationship(
                'Mentors',
                secondary='team_mentors',
                back_populates='teams'
                )


class SkillList(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    teams = relationship(
            PublicTeam,
            secondary='team_skills',
            back_populates='skills'
            )


class Mentors(Base):
    __tablename__ = 'mentors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    picture = Column(String(255))
    teams = relationship(
            PublicTeam,
            secondary='team_mentors',
            back_populates='mentors'
            )


class TeamSkills(Base):
    __tablename__ = 'team_skills'
    skill_id = Column(Integer, ForeignKey('skills.id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), primary_key=True)


class TeamMentors(Base):
    __tablename__ = 'team_mentors'
    mentor_id = Column(Integer, ForeignKey('mentors.id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), primary_key=True)
