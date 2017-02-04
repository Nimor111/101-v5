from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import PublicTeam, SkillList, Mentors

import settings

engine = create_engine(settings.DB_NAME)

Session = sessionmaker(bind=engine)

session = Session()


def insert_skill(name):
    s = SkillList(name=name)
    session.add(s)
    session.commit()


def get_skills():
    skillies = [s.name for s in session.query(SkillList).all()]
    return skillies


def get_skill(skill_name):
    skill = session.query(SkillList).filter(skill_name == SkillList.name).one()
    return skill


def get_team(team_name):
    team = session.query(PublicTeam).filter(team_name == PublicTeam.name).one()
    return team


def insert_team(name, idea_desc, repo, need_members, members_needed_desc,
                room, place, techs):
    team = PublicTeam(name=name, idea_description=idea_desc,   repository=repo,
                      need_more_members=need_members,
                      members_needed_desc=members_needed_desc, room=room,
                      place=place)
    for tech in techs:
        skill = get_skill(tech['name'])
        team.skills.append(skill)
    session.add(team)
    session.commit()


def insert_mentor(name, description, picture, teams):
    mentor = Mentor(name=name, description=description, picture=picture)
    for team in teams:
        t = get_team(team['name'])
        mentor.teams.append(t)
    session.add(mentor)
    session.commit()
