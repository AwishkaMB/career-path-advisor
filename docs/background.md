# Background & Problem Statement
### AI-Based Personalized Career Path Advisor

## 1. Background

Choosing a career path is one of the most important decisions a student makes during their degree, yet most students get very little personalized guidance in making it. University career units are usually understaffed relative to the number of students they serve, so guidance tends to come through generic workshops, brief advising sessions, or informal advice from friends and seniors — none of which is tailored to an individual student's actual academic strengths, skills, or interests.

At the same time, the range of careers open to a single degree has grown wider. A Computer Science graduate, for example, might reasonably move toward software engineering, data science, cybersecurity, UI/UX design, DevOps, or project management — each requiring a different mix of skills and knowledge. Matching every student to the direction that actually fits them is not something that scales well with traditional, manual advising.

**Who is affected:**
- Undergraduate students, especially in Computing/IT programmes, who must choose specializations, electives, and eventually apply for jobs.
- Academic advisors and career guidance staff, who are expected to advise large numbers of students with limited time per student.
- Employers, who benefit when graduates land in roles that genuinely match their competencies.

**Why it matters:** A poor career-path match leads to disengaged students, higher rates of switching subjects, longer job searches after graduation, and mismatched hires from an employer's side. Getting this right earlier — with more consistent, evidence-based guidance — has a real effect on student outcomes.

**How it's handled today, and the limitations:**
- One-to-one advising sessions — infrequent, and dependent on the availability and judgment of whichever advisor a student happens to see.
- Generic career fairs/orientation talks — not personalized to the individual at all.
- Self-directed research — students piecing together advice from online articles, forums, and anecdotes from seniors, with no structured use of their own academic or skill data.

**How AI can help:** AI can process a student's grades, self-rated skills, and interests far more consistently than a manual process, and compare that profile against patterns learned from historical student/career-outcome data. Clustering and classification can recognize which student "archetype" a given profile resembles; rule-based reasoning keeps the recommendations grounded in real prerequisites rather than pure statistical guesswork. The result is guidance that's faster, more consistent, and transparent about why it's suggesting what it's suggesting.

## 2. Problem Statement

There is currently no scalable, data-driven system available to undergraduate students that personally analyses their academic performance, skills, and interests to recommend suitable career paths — along with the specific skill gaps they'd need to close to pursue each one. Existing academic advising is manual, inconsistent, and cannot realistically be personalized to every student, which leaves many making career decisions on incomplete or generic information.

## 3. Objectives of the Proposed AI Solution

1. Collect and structure student profile data — academic performance, technical/soft skills, and interests — into a format suitable for machine learning analysis.
2. Classify a student's profile into the most compatible career category using a trained classification model.
3. Group students into peer clusters via unsupervised learning, enabling a "students similar to you tend to succeed in…" insight.
4. Apply rule-based eligibility checks so recommendations respect minimum prerequisite knowledge for each career path.
5. Rank and recommend the top career paths for a student using content-based filtering, with a plain-language explanation for each.
6. Generate a personalized development roadmap (skills to build, suggested courses) for the student's top recommendation.
7. Test the system against sample student profiles and evaluate whether the outputs are reasonable and explainable.
8. Identify and discuss the ethical implications of using AI to influence student career decisions.

## 4. Target Users

- **Primary:** Undergraduate students (particularly Computing/IT) choosing specializations, electives, or planning post-graduation applications.
- **Secondary:** Academic advisors and career guidance staff, who can use the system's output as a structured starting point rather than starting each session from scratch.
