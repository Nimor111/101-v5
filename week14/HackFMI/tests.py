import unittest
from controllers import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import PublicTeam, SkillList, Mentors

import settings


class StatTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_remove_skill_deletes_skills(self):
        remove_skill('Pests', 'Java')
        team = get_team('Pests')
        self.assertEqual(len(team.skills), 4)
        session.rollback()

    def test_add_skills_works_correctly(self):
        add_skill_to_team('Pests', ['Unity', 'GO'])
        team = get_team('Pests')
        self.assertEqual(len(team.skills), 7)
        session.rollback()

    def test_update_attr_works(self):
        update_team_attr('Pests', 'room', '405')
        team = get_team('Pests')
        self.assertEqual(team.room, '405')
        session.rollback()


if __name__ == '__main__':
    unittest.main()
