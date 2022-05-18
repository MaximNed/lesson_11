

import json


def load_candidates_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_candidate(candidate_id):
    candidates = load_candidates_from_json('candidates.json')
    for c in candidates:
        if c.get('id') == candidate_id:
            return c
    return False

def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json('candidates.json')
    return [c for c in candidates if candidate_name in c.get('name')]



def get_candidates_by_skill(skill_name):
    candidates = load_candidates_from_json('candidates.json')
    skill_candidates = [c for c in candidates if skill_name.lower() in c.get('skills').lower().split(', ')]
    return skill_candidates



if __name__ == '__main__':
    print(get_candidates_by_skill('flask'))
    print(get_candidates_by_name('Austin'))
    print(load_candidates_from_json('candidates.json'))