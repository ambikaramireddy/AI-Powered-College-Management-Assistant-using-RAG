import re
from langsmith import traceable

# ---------------------------------------------------
# QUERY CATEGORIES
# ---------------------------------------------------

GREETING_KEYWORDS = {
    "hi",
    "hello",
    "hey",
    "good morning",
    "good afternoon",
    "good evening",
    "thanks",
    "thank you",
    "bye"
}

ADMISSION_KEYWORDS = {
    "admission",
    "apply",
    "application",
    "eligibility",
    "scholarship",
    "fee",
    "fees",
    "payment",
    "tuition",
    "hostel fee",
    "transport fee",
    "registration"
}

ACADEMIC_KEYWORDS = {
    "course",
    "courses",
    "department",
    "syllabus",
    "semester",
    "subject",
    "subjects",
    "attendance",
    "exam",
    "exams",
    "results",
    "marks",
    "credits",
    "curriculum",
    "faculty",
    "hod",
    "lab",
    "labs",
    "library",
    "academic"
}

CAMPUS_KEYWORDS = {
    "hostel",
    "transport",
    "bus",
    "canteen",
    "wifi",
    "campus",
    "sports",
    "placement",
    "placements",
    "internship",
    "club",
    "facilities",
    "infrastructure"
}

GENERAL_COLLEGE_KEYWORDS = {
    "college",
    "principal",
    "rules",
    "timings",
    "office",
    "contact",
    "location",
    "information"
}

# ---------------------------------------------------
# QUERY CLASSIFICATION
# ---------------------------------------------------

@traceable(name="Query Classification", run_type="chain")
def classify_query(query: str):

    q = query.lower().strip()

    # ---------------------------------------------------
    # GREETINGS
    # ---------------------------------------------------

    if q in GREETING_KEYWORDS:
        return "GENERAL"

    # ---------------------------------------------------
    # ADMISSION RELATED
    # ---------------------------------------------------

    if any(word in q for word in ADMISSION_KEYWORDS):
        return "ADMISSION"

    # ---------------------------------------------------
    # ACADEMICS
    # ---------------------------------------------------

    if any(word in q for word in ACADEMIC_KEYWORDS):
        return "ACADEMICS"

    # ---------------------------------------------------
    # CAMPUS / FACILITIES
    # ---------------------------------------------------

    if any(word in q for word in CAMPUS_KEYWORDS):
        return "CAMPUS"

    # ---------------------------------------------------
    # GENERAL COLLEGE INFO
    # ---------------------------------------------------

    if any(word in q for word in GENERAL_COLLEGE_KEYWORDS):
        return "COLLEGE_INFO"

    # ---------------------------------------------------
    # QUESTION PATTERNS
    # ---------------------------------------------------

    if re.search(r"\b(when|where|how|what|which)\b", q):
        return "COLLEGE_INFO"

    # ---------------------------------------------------
    # DEFAULT
    # ---------------------------------------------------

    return "GENERAL"