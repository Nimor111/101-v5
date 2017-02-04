from models import SkillList, Mentors, PublicTeam, Base, engine

from controllers import insert_skill, insert_team, get_skills, get_skill

from reqs import skills


def insert_all_skills(skills):
    for elem in skills.json():
        insert_skill(elem['name'])


def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    insert_all_skills(skills)
    insert_team("Ne znam", "Soon", "", "true", "", "2", "null",
                [{"name": "HTML / CSS / JavaScript "}, {"name": "Java"}])
    insert_team("Oshte po ne znam", "Soon", "", "true", "", "2", "null",
                [{"name": "HTML / CSS / JavaScript "}, {"name": "Java"}])
    # get_skills()
    skill = get_skill('HTML / CSS / JavaScript ')
    import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    main()
