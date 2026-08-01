"""
rules.py — Rule-Based Reasoning Engine
AI-Based Personalized Career Path Advisor

This module applies explicit prerequisite/eligibility rules to a student profile.
It exists so the system never recommends a career path the student clearly isn't
academically or skill-ready for, regardless of what the classifier predicts.

Each rule is a simple, explainable IF-THEN condition — matching the
"Rule-Based Reasoning (Knowledge-Based System)" technique described in the report.
"""

# Minimum thresholds required to be considered ELIGIBLE for each career path.
# Adjust these numbers if your dataset's distributions suggest different cutoffs.
ELIGIBILITY_RULES = {
    "Software Engineering": {
        "skill_programming": 4,
    },
    "Data Science & Analytics": {
        "skill_data_analysis": 4,
        "gpa_core_modules": 2.5,
    },
    "Cybersecurity": {
        "skill_programming": 3,
        "interest_security": 3,
        "gpa_core_modules": 2.5,
    },
    "UI/UX Design": {
        "skill_design": 4,
    },
    "DevOps & Cloud Engineering": {
        "skill_programming": 3,
        "gpa_core_modules": 2.5,
    },
    "Database Administration": {
        "skill_data_analysis": 3,
        "skill_programming": 2,
    },
    "IT Project Management": {
        "skill_communication": 4,
    },
    "Quality Assurance/Testing": {
        "skill_programming": 2,
        "skill_communication": 3,
    },
}


def check_eligibility(student_profile: dict) -> dict:
    """
    Given a student profile (dict of feature_name -> value), check eligibility
    for every career path in ELIGIBILITY_RULES.

    Returns a dict like:
    {
        "Software Engineering": {"eligible": True, "reasons": []},
        "UI/UX Design": {"eligible": False, "reasons": ["skill_design (2) is below required minimum (4)"]},
        ...
    }
    """
    results = {}

    for career, requirements in ELIGIBILITY_RULES.items():
        reasons = []
        for feature, min_required in requirements.items():
            student_value = student_profile.get(feature)
            if student_value is None:
                reasons.append(f"{feature} is missing from the student profile")
                continue
            if student_value < min_required:
                reasons.append(
                    f"{feature} ({student_value}) is below required minimum ({min_required})"
                )

        results[career] = {
            "eligible": len(reasons) == 0,
            "reasons": reasons,
        }

    return results


def get_eligible_careers(student_profile: dict) -> list:
    """Convenience function: returns just the list of career names the student is eligible for."""
    results = check_eligibility(student_profile)
    return [career for career, info in results.items() if info["eligible"]]


# ---- Quick self-test when run directly (also works if pasted into a Colab cell) ----
if __name__ == "__main__":
    sample_students = {
        "Strong programmer, weak design": {
            "gpa_core_modules": 3.4,
            "skill_programming": 8,
            "skill_data_analysis": 4,
            "skill_design": 2,
            "skill_communication": 5,
            "interest_security": 2,
        },
        "Design-focused, low programming": {
            "gpa_core_modules": 3.0,
            "skill_programming": 2,
            "skill_data_analysis": 3,
            "skill_design": 9,
            "skill_communication": 6,
            "interest_security": 1,
        },
        "Low GPA across the board": {
            "gpa_core_modules": 1.9,
            "skill_programming": 3,
            "skill_data_analysis": 2,
            "skill_design": 2,
            "skill_communication": 4,
            "interest_security": 2,
        },
    }

    for name, profile in sample_students.items():
        print(f"\n=== {name} ===")
        results = check_eligibility(profile)
        for career, info in results.items():
            status = "ELIGIBLE" if info["eligible"] else "NOT eligible"
            print(f"  {career}: {status}")
            for reason in info["reasons"]:
                print(f"      - {reason}")
