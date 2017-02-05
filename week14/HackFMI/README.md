## HackFMI version Programming101-Python-2016

HackFMI application has an API, which you need to consume today.

With the data from the API you will have to represent the three days of the latest hackathon.

You have to use SQLAlchemy and requests library to create HackFMI version Programming101-Python-2016. All of the data from HackFMI API must be represented by models.

Your tasks is to give an information to your users about the hackathon.
- How many teams are in room X?
- Which teams are using technology X?
- Add team members to the teams
- Add different skills to the team
- Give information about a mentor's teams
- Give your mentors information to which rooms they need to go(DES/ASC)
- Add new mentors, teams, skills, rooms, etc.

### HackFMI API

Use the HackFMI API to collect the needed information.

```python
https://hackbulgaria.com/hackfmi/api/mentors/
https://hackbulgaria.com/hackfmi/api/public-teams/
https://hackbulgaria.com/hackfmi/api/skills/
```

After you have the whole information, it's time to create the schedule for the last day.

```python
===========================================
   Hour   ||  Team   ||  Team Description
===========================================
   19:30  ||  Далеци || Търсене на подобни
          ||         || книги в база от
          ||         || книги на български
------------------------------------------
  19:40   ||  .....  || ......
```

Once the teams present their ideas and project, the mentors will give evaluate them.

### Have fun and create your hackathon!
