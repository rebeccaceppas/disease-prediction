SYMPTOMS = ['sweating',
 'pain',
 'f17.210',
 'fatigue_ext',
 'fever',
 'sore_throat',
 'lesions',
 'muscle_pain',
 'lost_appetite',
 'cough',
 'trav1',
 'z92.25',
 'runny_nose',
 'heart_valves',
 'cortico',
 'gained_weight',
 'i50',
 'i80',
 'k74',
 'lymph_surg',
 'swelling',
 'sahs',
 'synd_nephro',
 'nsaids',
 'swollen_nodes',
 'std',
 'diarrhea',
 'unprotected_sex',
 'weight_loss',
 'sex_hiv',
 'convulsion',
 'short_breath',
 'e66',
 'agri',
 'itchy_nose',
 'eye_itching',
 'urban1',
 'z84.89',
 'HIV',
 'cough_blood',
 'IV_drugs',
 'f10.129',
 'ca_blockers',
 'I30',
 'fatigue',
 'high_bp',
 'menarche_12',
 'ulcers',
 'red_eye',
 'vag_discharge',
 'nausea',
 'severe_allergy',
 'contact_allergy',
 'wheezing_exhale',
 'fam_allergies',
 'fam_j45',
 'j45',
 'dizziness',
 'lost_consciousness',
 'chills',
 'e10_e11',
 'v85.0',
 'stridor',
 'patho_endo',
 'confusion',
 'contact',
 'ebolacase',
 'bruising',
 'breastfed_9',
 'anorexia',
 'new_fatigue',
 'vomiting_cough',
 'coughing_fits',
 'vaccination',
 'cont_pertussis',
 'wheezing_inhale']

aux = {
    'pain': [
 'pain_char',
 'pain_somewhere',
 'pain_intensity',
 'pain_precise',
 'pain_sudden',
 ],
  'lesions': [
 'lesion_color',
 'lesion_pain_swollen',
 'lesion_location',
 'lesion_pain_intense',
 'lesion_larger_than_1cm',
 'itching_severity',
 ],
  'swelling': [
 'swelling_location',
]
}

SYMPTOM_PHRASES = {
    #'pain_char': 'pain can be characterized as',
    #'lesion_color': 'rash color',
    #'pain_somewhere': 'pain',
    #'lesion_location': 'affected region location',
    #'swelling_location': 'swelling location',
    'swollen_nodes': 'swollen lymph nodes',
    'sweating': 'increased sweating',
    'diarrhea': 'diarrhea',
    'pain': 'pain',
    #'pain_intensity': 'pain intensity',
    #'pain_precise': 'pain precision',
    #'pain_sudden': 'pain onset speed',
    'fever': 'fever presence',
    'lesions': 'skin lesions or rashes',
    #'lesion_pain_swollen': 'swollen rash',
    #'lesion_pain_intense': 'rash pain intensity',
    #'itching_severity': 'itching severity',
    'nausea': 'nausea or vomiting',
    'weight_loss': 'weight loss',
    'itchy_nose': 'itchy nose or throat',
    'eye_itching': 'eye itching',
    'runny_nose': 'nasal congestion or runny nose',
    'short_breath': 'shortness of breath',
    'swelling': 'swelling',
    'lost_consciousness': 'loss of consciousness or fainting',
    'stridor': 'high-pitched breathing sound',
    'cough': 'cough presence',
    'cough_blood': 'coughing up blood',
    'ulcers': 'mouth ulcers or sores',
    'anorexia': 'unintentional weight loss or appetite loss',
    'new_fatigue': 'new fatigue or muscle aches',
    'convulsion': 'muscle contractions or absence episodes',
    'red_eye': 'redness in eyes',
    'gained_weight': 'recent weight gain',
    'dizziness': 'lightheadedness or faint feeling',
    'wheezing_exhale': 'wheezing on exhale',
    'fatigue_ext': 'extreme fatigue affecting activities',
    'sore_throat': 'sore throat',
    'muscle_pain': 'diffuse muscle pain',
    'lost_appetite': 'loss of appetite or early fullness',
    'vomiting_cough': 'vomiting after coughing',
    'coughing_fits': 'intense coughing fits',
    'chills': 'chills or shivers',
    'vag_discharge': 'vaginal discharge',
    'wheezing_inhale': 'wheezing on inhale or after coughing',
    'fatigue': 'constant fatigue or non-restful sleep',
    'confusion': 'confusion or disorientation',
    'bruising': 'unusual bleeding or bruising',
    'contact_allergy': 'had an allergic reaction',
}

SYMPTOMS_IN_ORDER = ['AGE', 'SEX', 'INITIAL_EVIDENCE', 'swollen_nodes', 'std',
       'sweating', 'diarrhea', 'pain', 'pain_char', 'pain_somewhere',
       'pain_intensity', 'pain_precise', 'pain_sudden', 'fever',
       'unprotected_sex', 'lesions', 'lesion_color',
       'lesion_pain_swollen', 'lesion_location', 'lesion_pain_intense',
       'lesion_larger_than_1cm', 'itching_severity', 'nausea',
       'weight_loss', 'sex_hiv', 'trav1', 'fam_allergies', 'fam_j45',
       'j45', 'itchy_nose', 'eye_itching', 'runny_nose', 'urban1',
       'severe_allergy', 'contact_allergy', 'short_breath', 'swelling',
       'swelling_location', 'lost_consciousness', 'stridor', 'z84.89',
       'HIV', 'cortico', 'IV_drugs', 'e10_e11', 'f10.129', 'cough',
       'cough_blood', 'v85.0', 'I30', 'f17.210', 'high_bp', 'ulcers',
       'anorexia', 'new_fatigue', 'nsaids', 'i50', 'i80', 'lymph_surg',
       'synd_nephro', 'convulsion', 'e66', 'red_eye', 'agri',
       'gained_weight', 'k74', 'patho_endo', 'dizziness',
       'wheezing_exhale', 'fatigue_ext', 'sore_throat', 'muscle_pain',
       'lost_appetite', 'heart_valves', 'sahs', 'cont_pertussis',
       'vomiting_cough', 'coughing_fits', 'vaccination', 'chills',
       'z92.25', 'ca_blockers', 'vag_discharge', 'wheezing_inhale',
       'fatigue', 'menarche_12', 'breastfed_9', 'confusion', 'contact',
       'ebolacase', 'bruising']