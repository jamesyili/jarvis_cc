# DataKind Singapore’s Latest Project Accelerator

**Source:** https://eugeneyan.com//writing/datakind-sg-project-accelerator/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

> Originally posted on DataKind’s [blog](https://www.datakind.org/blog/report-from-datakind-singapores-latest-project-accelerator).

From providing clean water and sanitation to fighting human trafficking to improving the lives of the underserved, nonprofits in our region are collecting a lot of useful data that could help inform their work and better serve their communities. However, many don’t have the time or staff expertise to clean, analyze, and visualize the data to take advantage of this powerful resource.

During DataKind Singapore’s third Project Accelerator, over 40 volunteer data scientists came together for a night of brainstorming and consulting to help four local organizations do just this.

Representatives from [Lien AID](http://www.lienaid.org), [Phandeeyar](https://www.phandeeyar.org), Walk Strong, and [Liberty Asia](https://libertyshared.org) briefly talked about the challenges they face and how they hoped to use data to tackle them. Participants then broke up into different focus groups to frame the problems and suggest solutions to the most pressing issues.

Briefing before starting the project accelerator

## Lien AID

Lien AID is a nonprofit that aims to improves the lives of rural communities in Asia by making clean water and sanitation accessible and affordable to them. In developing countries, about 80% of illnesses are linked to poor water and sanitation, and one out of every five deaths under five is due to a water-related disease. Furthermore, the burden of collecting clean water—usually on women and children—reduces time spent in an income-generating job or attending school. To provide sustainable access to clean water, Lien AID partners with local governments and organizations to build water treatment plants that provide bottled and piped water.

**Problem Statement:** To understand the consumption of clean drinking water in a community, Lien AID tracks households that buy bottled water by collecting data through phone calls to local operators. However, this data can be unreliable, making it difficult to get an accurate picture of bottled water consumption and its related benefits. In addition, Lien AID has collected significant data from its needs assessment surveys and other sources, but much of this is free text. They requested guidance on how to begin analyzing the data, especially unstructured free text data.

**Proposed Solutions:** To improve the accuracy of tracking bottled water sales, we suggested providing each household with identification cards and/or numbering the reusable water bottles. Purchases of bottled water can then be tracked by recording the numbers of incoming and outgoing bottles, with transaction data stored in a centralized database. Depending on the tech comfort level of the local operators, the simple numbering could be replaced by barcodes or QR codes.

To better structure data in the collection phase (and reduce data cleanup after), we suggested replacing free text fields with multiple response questions. To better understand how Lien AID can analyze their existing data, we suggested Lien AID provide a data sample to assess how best to begin. It’s always important to first develop clear questions of the data before jumping into the analysis.

## Phandeeyar

Phandeeyar is a nonprofit tech hub that brings together the tech community to accelerate development in Myanmar. Myanmar has opened up recently, though the decades of isolation led to an information and communication technology deficit. Thus, there is great potential for Myanmar to harness technology and the internet to foster social change. With this in mind, Phandeeyar aims to foster collaboration between the tech community, civil society, and journalists to create positive social impact. Past activities include collaborating with Google to crowdsource the improvement of Google Translate for Myanmar and organizing data journalism workshops on data analysis and visualization.

**Problem Statement:** Phandeeyar aims to improve its capability in matching nonprofits’ needs with volunteers having the right skill sets. Currently, the process is largely manual and reliant on Phandeeyar team members’ knowledge of nonprofits and the tech community and there is no centralised database. In addition, being a relatively young group, Phandeeyar lacked an organized and efficient workflow. This limited its ability to collect data about its events and stakeholders that attend (e.g., needs, skills, contact information), making it difficult to link up civil society and nonprofits’ needs with members of the tech community that have the right skills.

**Proposed Solutions:** To automate the collection of data on nonprofits (and their needs) and the tech community (and their skill sets), the use of Google forms was proposed. Well structured Google forms with multi response options for needs and skill sets (e.g., data cleaning, analysis, visualisation, etc) would help match nonprofits with specific needs to volunteers with the right skill set. To improve Phandeeyar’s workflow, we suggested forming internal teams for each aspect (e.g., outreach, logistics, etc) as well as coordinating work using project management tools such as Trello.

## Walk Strong

Walk Strong, directly translated from “Jalan Kukoh,” is a movement dedicated to improving the lives of the underserved Jalan Kukoh community. Comprising nine rental blocks (approximately 4,000 residents), Jalan Kukoh is one of the poorest neighbourhoods in Singapore. The community consists largely of elderly people living alone and includes single mothers, ex-convicts, and the homeless. To improve the lives of the community, Walk Strong intends to better understand the needs of the estate and its residents. With its deeper understanding, it aims to design target programs to meet community needs and advise other organisations on how best to help the community.

**Problem Statement:** Walk Strong shared that they had some data on the Jalan Kukoh community, though it was stored in an inconsistent and ad-hoc manner. To better understand the needs of the community and complement their existing data, Walk Strong aimed to conduct a survey to collect information on income, education, food sources, incarceration rates, etc. Walk Strong also wanted help designing a comprehensive data platform to consolidate, clean, and analyze their data. Insights from the data analysis could then be used to guide programs for the community.

**Proposed Solutions:** We suggested to first implement a simple case management system (e.g., Google Sheets) to store Walk Strong’s existing data in a structured manner; additional data from the survey could also be added to it. For the survey, we suggested starting with households that were already familiar with and trusted Walk Strong. The quick collection of initial data could then be used for analysis and guide further tweaking of the survey if necessary. Some of the questions may be sensitive and respondents may not be willing to answer them. To address this, we suggested ordering easy-to-answer factual questions at the start before following up with more sensitive questions (e.g., criminal history) possibly at a later phase.

## Liberty Asia

Liberty Asia works with anti-trafficking organizations to fill gaps in data, technology, and legal expertise. Often, data is collected via hardcopy forms, making it difficult to share and use victim and evidence data for conducting investigations. In addition, organizations using the data are vulnerable to accusations of defamation and violations of data privacy. To address these challenges, Liberty Asia provides a cloud-based case management platform (based on Salesforce) to frontline organizations, facilitating the storage, sharing, and analysis of data. It also provides a platform to facilitate knowledge sharing and cooperation between anti-trafficking organizations, as well as legal expertise and training.

**Problem Statement:** As Liberty Asia did not have any specific problems, the focus group discussion was centred around its platform, data collected, and how it is currently being used by its partners. With a greater understanding of its platform and data, we shared possible visualization use cases and text mining techniques to analyze their documents (e.g., NLP, topic modeling).

**Collaboration with other nonprofits:** Some areas for collaboration between Liberty Asia and other nonprofits were noted while preparing for the Project Accelerator. For one, Xinyi and Duncan from Liberty Asia had previously conducted a survey with a nonprofit in a low-income neighborhood in Hong Kong. The survey aimed to identify root-causes of social immobility and ways to adjust the nonprofit’s programs to enable disadvantaged youth to reach their full potential. This was relevant to Walk Strong and its endeavour to conduct a survey. Immediately after the Project Accelerator, representatives of Liberty Asia and Walk Strong had a fruitful discussion over dinner, which included suggestions on how to ask sensitive questions. For example, rather than asking if the respondent had ever been incarcerated, it was more likely to get response if they asked how many of the respondent’s acquaintances had been incarcerated. In addition, Liberty Asia’s case management platform appeared relevant to an existing DataCorps project—the DataCorps team had a follow-up discussion with Liberty Asia to evaluate the platform.

## Get Involved

After the intense focus group sessions, each group shared a summary of discussions with the rest of the participants. Each nonprofit was able to access data science experts to get feedback and left with clear next steps on how to tackle their data challenges. It also allowed volunteers to apply their experience with data and data analysis to help nonprofits that are working to make our local communities stronger. We can’t wait to see what happens next with these organizations!

Big shoutout to [ThoughtWorks Singapore](https://www.thoughtworks.com) for providing a wonderful space for the event and a huge thanks all the participants that made the Project Accelerator a success.

If you’re interested in lending your skills to help local organizations start their data science journeys, sign up for your local DataKind Chapter’s Meetup group to stay up to date on [future events](https://www.datakind.org/community-events/)!

> Originally posted on DataKind’s [blog](https://www.datakind.org/blog/report-from-datakind-singapores-latest-project-accelerator).

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Sep 2015). DataKind Singapore’s Latest Project Accelerator. eugeneyan.com.
> https://eugeneyan.com/writing/datakind-sg-project-accelerator/.

or

```
@article{yan2015datakind,
  title   = {DataKind Singapore’s Latest Project Accelerator},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2015},
  month   = {Sep},
  url     = {https://eugeneyan.com/writing/datakind-sg-project-accelerator/}
}
```

  
Share on:
