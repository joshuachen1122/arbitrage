from bs4 import BeautifulSoup

# HTML TAG CLASS CONSTANTS
TBODY_CLASS = 'OddsGridstyles__TableBody-sc-1y5q2eg-3 bSORPE'
TR_CLASS_0 = 'OddsGridstyles__ParticipantRow-sc-1y5q2eg-0 bMsszi'
TR_CLASS_1 = 'OddsGridstyles__ParticipantRow-sc-1y5q2eg-0 dBhgZY'
SPAN_TEAM = 'teamName blueHover'
SPAN_BEST_LINE = 'best-line'

def parse_html_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    tbody_tags = soup.find_all('tbody', class_=TBODY_CLASS)
    if len(tbody_tags) == 0:
        print("No table found. Check the defined class name.")
        return
    print(tbody_tags[0])
    tr_tags_0 = tbody_tags[0].find_all('tr', TR_CLASS_0)
    tr_tags_1 = tbody_tags[0].find_all('tr', TR_CLASS_1)

    # TR_CLASS_0 holds road teams, TR_CLASS_1 holds home teams
    # interweave elements to get a stream of games
    tr_tags = []
    for elem1, elem2 in zip(tr_tags_0, tr_tags_1):
        tr_tags.append(elem1)
        tr_tags.append(elem2)

    for tr_tag in tr_tags:
        print(tr_tag)
        #print(tr_tag.find('span', SPAN_TEAM).text)
        #print(tr_tag.find('div', 'TeamContainerstyles__ConsensusOrScore-sc-9qm24l-3 lcveoM'))
        break