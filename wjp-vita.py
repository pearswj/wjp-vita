#!/usr/local/bin/python2

from Cheetah.Template import Template
import time
import git
import os
import sys

# Input information

displaytypes = ['civil'] # civil, misc

personal = {
    'name':'Will Pearson',
    'email':'pearswj@gmail.com',
    'telephone':'+44(0)7882161421',
    'address':'56 Thomas More Street, London, UK. E1W 1YJ',
    'statement':''
}


education = []
education.append({
    'title':'MPhil Digital Architectonics',
    'qualification':'',
    'location':'University of Bath',
    'start':'October 2012',
    'end':'present',
    'summary':'''My studies investigate the design and application of computational tools in the fields of structural engineering and architectural design. For my thesis project I am currently exploring the use of manifold mesh operators (Conway, subdivision, etc.) in the design of efficient, free-form, structural systems. This is implemented as a suite of custom data types and components in Grasshopper's parametric framework (C\#). For a previous project I wrote a Processing library (Java) for modelling orientable, manifold meshes. I used this exercise to explore mesh operators and analysis methods and to further develop my skills in object oriented programming.'''
})
education.append({
    'title':'MEng Structural Engineering with Architectural Studies',
    'qualification':'2.I (hons)',
    'location':'University of Sheffield',
    'start':'September 2008',
    'end':'June 2012',
    'summary':'My undergraduate studies covered many topics from structural mechanics and dynamics, through structural design and drawing to fire engineering and statistics. I also attended lectures in the Architecture department and completed studio projects alongside first-year architecture students. During my time at Sheffield I gained an appreciation for the potential computing holds in the evolution of engineering and design. I also invloved myself in the running of the University\'s ice hockey club, building a website to help promote the club and invite sponsorship.'
})
education.append({
    'title':'A/AS levels',
    'qualification':'AABa (Maths, Art, Physics, Computing)',
    'location':'Beechen Cliff School Sixth Form, Bath',
    'start':'2006',
    'end':'2008',
    'summary':''
})


employment = []
employment.append({
    'position':'Graduate Engineer',
    'date':'September 2013 to present',
    'company':'Ramboll UK / Ramboll Computational Design',
    'location':'London',
    'type': 'civil',
    'description':''
})
employment.append({
    'position':'Work Placement (part-time)',
    'date':'May 2013 to August 2013',
    'company':'Ramboll Computational Design',
    'location':'Bristol',
    'type': 'civil',
    'description':'''I assisted the Bristol RCD team with the design of a pavilion at Oxford Brookes University. The project involved many aspects of computational design -- from the rationalisation and analysis of complex forms through to digital fabrication techniques.'''
})
employment.append({
    'position':'Ice Marshall (part-time)',
    'date':'November 2012 to January 2013',
    'company':'Bath On Ice',
    'location':'Bath',
    'type': 'misc',
    'description':'I recently spend the winter months working at a temporary outdoor ice rink in Bath. '
})
employment.append({
    'position':'Graduate Internship',
    'date':'June 2012 to August 2012',
    'company':'LimitState Ltd.',
    'location':'Sheffield',
    'type': 'civil',
    'description':'Upon completion of my undergraduate studies I returned to LimitState to continue my previous work. I was part of a small team developing a commercial geotechnical software package (C++, Qt). I investigated and fixed issues with the software as well as extending its functionality. I was fully integrated within the team and gained a great understanding of how version control (Subversion) and issue/feature tracking software (Trac) can be used to increase productivity in a collaborative development environment.'
})
employment.append({
    'position':'Internship (part-time)',
    'date':'January 2012 to April 2012',
    'company':'LimitState Ltd.',
    'location':'Sheffield',
    'type': 'civil',
    'description':'I joined LimitState Ltd.\ for three months on a part-time basis as part of the Sheffield Internship Scheme. I was responsible for the design and prototyping of a new software feature as well as general testing and documentation editing.'
})
employment.append({
    'position':'Research Assistant',
    'date':'July 2011 to October 2011',
    'company':'Computational Mechanics and Design Research Group, Department of Civil and Structural Engineering',
    'location':'University of Sheffield',
    'type': 'civil',
    'description':'My initial role was to format research papers for submission (using the \LaTeX~typesetting language) as well as drawing figures and graphs (using Asymptote and Adobe Illustrator) to be included within. I also had the chance to engage with some of the ongoing research in the department, assisting with the building and processing of data from Finite Element models (using LS-DYNA/LS-PrePost) and documenting this process (including any automation scripts used) in the project\'s wiki.'
})


experience = []
"""
experience.append({
    'date':'19th August 2010',
    'title':'Bath Riverside Development meetings',
    'place':'Buro Happold, Bath office'
})
experience.append({
    'date':'18th August 2010',
    'title':'London 2012 Team Stadium design office inc. site visit',
    'place':'Buro Happold'
})
experience.append({
    'date':'May 2008',
    'title':'Site visit to St. David\'s 2 Development, Cardiff',
    'place':'Whitbybird'
})
experience.append({
    'date':'June 2007',
    'title':'3 day intro placement',
    'place':'Buro Happold, Bath Office'
})
"""


skillsblurb = 'I have experience in a number of software tools and programming languages as well as an aptitude for learning something new when necessary.'
skills = [] # escape '&' symbols!
skills.append({'name':'C++, Visual Studio, Qt', 'ability':'120'})
skills.append({'name':'Java, Processing, Eclipse', 'ability':'138'})
skills.append({'name':'Bash, Python, Ruby, Matlab', 'ability':'150'})
skills.append({'name':'\LaTeX, \BibTeX, Adobe CS', 'ability':'148'})
skills.append({'name':'Git, Subversion', 'ability':'130'})
skills.append({'name':'Rhino/Grasshopper, C\#', 'ability':'142'})
skills.append({'name':'AutoCAD, ANSYS, Robot, GSA', 'ability':'80'})
skills.append({'name':'GenerativeComponents, DesignScript', 'ability':'30'})
skills.append({'name':'HTML, CSS, PHP, SQL', 'ability':'118'})

skills.sort(key=lambda x: int(x['ability'])) # sort by ability
skills.reverse()

for skill in skills:
    skill["ability"] = int(skill["ability"]) / 8


interests = []
interests.append('building, riding and maintaining bicycles')
interests.append('playing for a local recreational ice hockey team')
interests.append('exploring opensource software projects on Github')


# Git

def TryRepoIsDirty(repo):
    try:
        dirty = repo.is_dirty()
    except:
        dirty = False
    return dirty

repo = git.Repo(os.getcwd())
head = repo.head.commit
dirty = TryRepoIsDirty(repo)
date = time.time() if dirty else head.authored_date
git = {
    'date':time.strftime("%d/%m/%Y", time.gmtime(date)),
    'hash':head.hexsha[:7],
    'dirty':dirty
}

# Call template

t = Template(file='template.tex')
t.personal = personal
t.education = education
t.employment = employment
t.experience = experience
t.skillsblurb = skillsblurb
t.skills = skills
t.achievements = None
t.interests = interests
t.git = git
t.displaytypes = displaytypes

if os.name == 'nt':
    t.font = 'Garamond'
else:
    t.font = 'Helvetica Neue Light'

# Write .tex file

name = os.path.basename(__file__)[:-2] + 'tex'

f = open(name, 'w')
f.write(str(t))
f.close()

try:
    import pexpect
except ImportError as e:
    print 'Pexpect module doesn\'t like Windows'
    print 'run `latexmk -xelatex ' + name + '` to finish'
    sys.exit()

pexpect.run('latexmk -xelatex ' + name, logfile=sys.stdout)
pexpect.run('latexmk -c', logfile=sys.stdout)
os.remove(name)
