from models import SkillList, Mentors, PublicTeam, Base, engine

from controllers import insert_skill, insert_team, insert_mentor

from reqs import skills, teams, mentors


def insert_all_skills(skills):
    for elem in skills.json():
        insert_skill(elem['name'])


def insert_all_teams(teams):
    for elem in teams.json():
        insert_team(elem['name'], elem['idea_description'], elem['repository'],
                    elem['need_more_members'], elem['members_needed_desc'],
                    elem['room'], elem['technologies_full'])


def insert_all_mentors(mentors):
    for elem in mentors.json():
        insert_mentor(elem['name'], elem['description'],
                      elem['picture'], elem['teams'])


def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    insert_all_skills(skills)
    insert_all_teams(teams)
    insert_all_mentors(mentors)


if __name__ == '__main__':
    main()
