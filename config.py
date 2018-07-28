from ics import current_time
class Config:
    params = [{
        'start_date': '20180707',
        'start_time': '000000',
        'end_date': '20180710',
        'end_time': '000000',
        'summary': 'Microsoft Q# Coding Contest - Summer 2018',
        'location': 'CodeForces',
        'url': 'http://codeforces.com/contests',
        'description': '''\
Microsoft's Quantum Team and Codeforces are excited to invite you to Microsoft Q# Coding Contest — Summer 2018!

The contest will run from July 6 — 9 and will consist of increasingly challenging tasks on introductory topics in quantum computing: superposition, measurement, oracles and simple algorithms. The top 50 ranked participants will receive a Microsoft Quantum T-shirt!

As a reminder, last weekend we help a warmup round with easier tasks which covered the same topics. The results were quite impressive: 167 participants solved all tasks! You can see the tasks here, and the solutions with explanations here.

Several useful reminders:

The contest is unrated.
Solutions are accepted in Q# only.
Participants are ranked according to the number of correctly solved tasks, with penalty time as a tiebreaker.
The tasks are grouped by topic, and the tasks within one topic are ordered in approximate order of increasing difficulty. If you find a problem too hard, don't forget to check the next problems in this topic and problems from different topics, they might turn out to be easier.
Unlike the warmup round, you're not allowed to discuss the tasks during the contest.
For tasks which require you to create a certain quantum state or to implement a unitary transformation, any kind of error gives verdict "Wrong Answer". For tasks which have classical return, I tried to differentiate verdicts "Wrong Answer" (your return value was incorrect) and "Runtime Error" (array index out of bounds, qubits released are not in zero state, oracle called too many times etc.).
You can find the discussion of the warmup round and pointers to Q#/quantum computing materials here.

For first time Codeforces users:

Create user account here.
Register for the contest here.
Once the contest starts on July 6, access the problems here.
Good luck! We hope you enjoy the contest!'''},
    
    ]

cfg = Config()

