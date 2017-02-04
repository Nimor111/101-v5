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


def get_mentor(mentor_name):
    mentor = session.query(Mentors).filter(mentor_name == Mentors.name).one()
    return mentor


def get_team(team_name):
    team = session.query(PublicTeam).filter(team_name == PublicTeam.name).one()
    return team


def insert_team(name, idea_desc, repo, need_members, members_needed_desc,
                room, techs, place="null"):
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
    mentor = Mentors(name=name, description=description, picture=picture)
    for team in teams:
        t = get_team(team['name'])
        mentor.teams.append(t)
    session.add(mentor)
    session.commit()


def get_teams_in_room(room):
    teams = session.query(PublicTeam).filter(room == PublicTeam.room).count()
    return teams


def get_teams_for_technology(tech):
    skill = get_skill(tech)
    return [t.name for t in skill.teams]


def get_mentor_teams(mentor_name):
    mentor = get_mentor(mentor_name)
    for team in mentor.teams:
        print("name: {}, \nidea_description: {}, \nrepository: {}, \
              \nmore members?: {}, \nwhat members needed?: {},\
              \nroom: {}, \nskills: {}".format(team.name,
                                               team.idea_description,
                                               team.repository,
                                               team.need_more_members,
                                               team.members_needed_desc,
                                               team.room,
                                               [skill.name for skill in
                                                team.skills]))
