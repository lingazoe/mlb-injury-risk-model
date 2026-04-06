import pandas as pd
import re

def extract_data(injury_comment):

    if pd.isna(injury_comment) or injury_comment == "":
        return "Unknown", "Unknown", False
    
    injury_comment = injury_comment.lower()

    injury_side = "Unknown"

    if "left" in injury_comment: injury_side = "Left"
    elif "right" in injury_comment: injury_side = "Right"

    injured_body_part = "Other"

    injury_patterns = {
        'Elbow': r'elbow|ucl|tommy john',
        'Shoulder': r'shoulder|labrum|rotator|capsule',
        'Oblique': r'oblique|abdominal|core',
        'Hamstring': r'hamstring|quad|thigh|groin',
        'Knee': r'knee|acl|mcl|meniscus',
        'Hand/Wrist': r'hand|finger|wrist|thumb',
        'Back': r'back|spine|lumbar',
        'Foot/Ankle': r'foot|ankle|toe|achilles'
    }

    # check each comment for pattern
    for part, regex in injury_patterns.items():
        if re.search(regex, injury_comment):
            injured_body_part = part
            break

    accidental_injury = any(accident_term in injury_comment for accident_term in ['fracture', 'hit by pitch', 'hbp', 'contusion', 'bruise'])
    
    return injured_body_part, injury_side, accidental_injury

