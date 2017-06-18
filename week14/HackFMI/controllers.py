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


def get_all_teams():
    teams = [(team.name, team.idea_description) for team in session.query(
        PublicTeam).all()]
    return teams


def insert_team(name, idea_desc, repo, need_members, members_needed_desc,
                room, techs, place="null"):
    team = PublicTeam(name=name, idea_description=idea_desc, repository=repo,
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


def get_mentor_rooms(mentor_name):
    mentor = get_mentor(mentor_name)
    rooms = []
    for team in mentor.teams:
        rooms.append(team.room)

    sorted_rooms = sorted([int(room) for room in rooms if room != 'mazata'])
    if 'mazata' in rooms:
        sorted_rooms.append('mazata')

    return sorted_rooms


def remove_skill(team_name, skill_name):
    team = get_team(team_name)
    for skill in team.skills:
        if skill.name == skill_name:
            team.skills.remove(skill)


def add_skill_to_team(team_name, skills):
    team = get_team(team_name)
    for skill in skills:
        s = get_skill(skill)
        if s not in team.skills:
            team.skills.append(s)


def update_team_attr(team_name, attr, new_value):
    team = get_team(team_name)
    setattr(team, attr, new_value)
