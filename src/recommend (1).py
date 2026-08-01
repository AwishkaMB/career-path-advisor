"""
recommend.py — Recommendation Ranking Engine
AI-Based Personalized Career Path Advisor

Combines three pieces already built:
  1. The trained classifier (career_classifier.pkl) — gives a probability/confidence
     score for each career category, based on patterns learned from historical data.
  2. The rule-based eligibility engine (rules.py) — filters out any career the
     student doesn't meet minimum prerequisites for, regardless of what the
     classifier predicts.
  3. Content-based similarity — used as a tie-breaker/secondary score, comparing
     the student's feature vector to each career's "ideal" profile.

Final output: a ranked Top-N list of ELIGIBLE careers, each with a confidence
score and a plain-language explanation.
"""

import numpy as np
import joblib
from rules import check_eligibility

# Feature order MUST match the order used when training the classifier in Week 5.
FEATURE_ORDER = [
    "gpa_core_modules", "skill_programming", "skill_data_analysis",
    "skill_design", "skill_communication", "interest_software",
    "interest_data", "interest_security", "interest_design", "interest_management",
]

# "Ideal" feature profile for each career — used for the content-based similarity
# score. These are rough midpoints based on what a strong candidate for each path
# typically looks like; tune later using your actual cluster averages from Week 3.
CAREER_IDEAL_PROFILES = {
    "Software Engineering":            [3.2, 8, 5, 3, 5, 8, 5, 3, 2, 4],
    "Data Science & Analytics":        [3.4, 6, 9, 3, 6, 6, 9, 4, 2, 4],
    "Cybersecurity":                   [3.3, 6, 5, 3, 5, 5, 5, 9, 2, 4],
    "UI/UX Design":                    [3.0, 3, 3, 9, 6, 4, 3, 2, 9, 4],
    "DevOps & Cloud Engineering":      [3.1, 7, 4, 3, 5, 8, 4, 5, 2, 4],
    "Database Administration":         [3.2, 6, 7, 2, 5, 5, 7, 3, 2, 4],
    "IT Project Management":           [3.1, 4, 3, 3, 9, 4, 3, 3, 3, 9],
    "Quality Assurance/Testing":       [3.0, 5, 4, 3, 6, 5, 4, 3, 2, 4],
}


def cosine_similarity(vec_a, vec_b):
    a, b = np.array(vec_a, dtype=float), np.array(vec_b, dtype=float)
    denom = (np.linalg.norm(a) * np.linalg.norm(b))
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)


def recommend_careers(student_profile: dict, model_path="career_classifier.pkl",
                       scaler=None, top_n=3):
    """
    student_profile: dict with all FEATURE_ORDER keys present.
    model_path: path to the saved classifier from Week 5.
    scaler: the fitted StandardScaler from Week 5 (pass it in if you have it saved;
            otherwise this function will skip classifier scoring and rely on
            similarity + eligibility only).
    top_n: how many recommendations to return.

    Returns a list of dicts, ranked best-first:
      [{"career": ..., "confidence": ..., "similarity": ..., "reason": ...}, ...]
    """
    # --- Step 1: Rule-based eligibility filtering ---
    eligibility = check_eligibility(student_profile)
    eligible_careers = [c for c, info in eligibility.items() if info["eligible"]]

    if not eligible_careers:
        return []  # No career meets prerequisites — flag this case in your UI/report

    # --- Step 2: Classifier confidence scores (if model + scaler available) ---
    feature_vector = [student_profile.get(f, 0) for f in FEATURE_ORDER]
    class_probs = {}
    try:
        model = joblib.load(model_path)
        x = np.array(feature_vector).reshape(1, -1)
        if scaler is not None:
            x = scaler.transform(x)
        probs = model.predict_proba(x)[0]
        class_probs = dict(zip(model.classes_, probs))
    except Exception:
        # If the model/scaler isn't available in this environment, fall back to
        # similarity-only ranking rather than crashing.
        class_probs = {}

    # --- Step 3: Content-based similarity score for each eligible career ---
    results = []
    for career in eligible_careers:
        ideal = CAREER_IDEAL_PROFILES.get(career)
        similarity = cosine_similarity(feature_vector, ideal) if ideal else 0.0
        confidence = class_probs.get(career, 0.0)

        # Combined score: weight classifier confidence higher, similarity as support
        combined_score = (0.7 * confidence) + (0.3 * similarity) if class_probs else similarity

        results.append({
            "career": career,
            "confidence": round(confidence, 3),
            "similarity": round(similarity, 3),
            "combined_score": round(combined_score, 3),
            "reason": (
                f"Meets all prerequisites for {career}; "
                f"profile similarity score {round(similarity, 2)}"
                + (f", classifier confidence {round(confidence, 2)}" if class_probs else "")
            ),
        })

    # --- Step 4: Rank and return top N ---
    results.sort(key=lambda r: r["combined_score"], reverse=True)
    return results[:top_n]


# ---- Quick self-test ----
if __name__ == "__main__":
    sample_student = {
        "gpa_core_modules": 3.4,
        "skill_programming": 8,
        "skill_data_analysis": 4,
        "skill_design": 2,
        "skill_communication": 5,
        "interest_software": 8,
        "interest_data": 5,
        "interest_security": 2,
        "interest_design": 1,
        "interest_management": 3,
    }

    recommendations = recommend_careers(sample_student, top_n=3)
    print("Top recommendations:")
    for i, rec in enumerate(recommendations, start=1):
        print(f"{i}. {rec['career']}  (score: {rec['combined_score']})")
        print(f"   {rec['reason']}")
