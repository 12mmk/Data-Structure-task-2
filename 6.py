# a company accepts  an application only if a applicant if 

applicant = {"name":"priya", "skills": ["java", "sql"], "experience": 1}
required_skills = {"python", "java"}

# the candidate knows python or java and has at least 2 years of experiece. 
# check if at least one skill in appliccant skills is required skills and experience >=2. 
# print priya qualifes or priya does not.


present_skills = set(applicant["skills"])
skills = present_skills.intersection(required_skills)


if skills and applicant["experience"] >= 2:
    print(f"{applicant['name']} qualifies.")
else:
    print(f"{applicant['name']} does not qualify.")

