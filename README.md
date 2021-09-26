# shellU
It's still a work in progress.
Inspired by "Algoexpert" Obviosly not as good as that lol
The Final Result Would Look Like This:
![dashboard](https://user-images.githubusercontent.com/64773992/134801061-67b0797d-36c9-4871-8475-de3bc4182fb6.png)
The current project is about 90% complete then my exams started and I had to pause it.
just have to polish some things, the backend is pretty much done, only need to work on the CSS and HTML part 

## Stack:
- Front-End:
  - Angular, Bootstrap
- Back-End:
  - Django, Django REST-api, and for compiling user code I use PISTON-API from Engineerman

and for sql obviosly right now it use sqlite3, but I was thinking about MYSql.

## Features:
- Fully Functioning Compiler using Piston-API:
  - Currently It Only Supports a few languages (In theory it can support any but I've not implemented that as of yet)
- User Profiles
  - You can manage your own and view other user's profile too
      - Set Your own Profile
      - Your Prefered Languages
      - Etc.
  - View your global ranking
  - A highly sophisticated ranking System
- A "Hall Of Fame" for a quick TOP-10 Users and a "King Of The Room" for the Highest Ranking User
- Every Puzzle Has Many different Attributes
  - Hints
  - Score
  - Solution
  - Difficulty
  
## Working:
- User's who are not logged in, would see the landing page (Completely Designed)
- Their they can Either Register or Log in (Everything till now is hosted on Django's side)
- After Logging in, they are redirected to port 4200 and everything "frontend" from here is handled by Angular
- I use Django-Rest-Api to handle data transfer from server side django and angular
