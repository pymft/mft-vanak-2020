text = """Baden-Powell House is a Scouting hostel and conference 
centre in South Kensington, London. Built as a tribute 
to Lord Baden-Powell, the founder of Scouting, it is 
owned by The Scout Association. The house was designed 
in 1956 in the modern architectural style by Ralph 
Tubbs, whose works included the Dome of Discovery,
 the highlight of the 1951 Festival of Britain. 
 Olave Baden-Powell laid the foundation stone in 1959, 
 and the building was opened by Queen Elizabeth II in 1961. 
 A granite statue of Baden-Powell, sculpted by Don Potter, 
 was unveiled at the opening. The building has been 
 refurbished several times, and now provides lodging 
 for Scouts, Girl Guides and the general public. 
 A collection of Baden-Powell memorabilia formerly 
 displayed at the site, including several first 
 editions of his books and many of his drawings 
 and letters, has been moved to the headquarters 
 for Scouting in the UK at Gilwell Park. 
"""

words = text.lower().replace(".", " ").split()
print(words)
ans = words.count("london")
print(ans)

