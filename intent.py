import math

def compute_intent(actions):
    if not actions:
        return [0, 0, 0, 0]

    total_value = sum(a["value"] for a in actions)
    avg_value = total_value / len(actions)

    avg_time = sum(a["time_delta"] for a in actions) / len(actions)

    unique_actions = len(set(a["action"] for a in actions))
    entropy = unique_actions / len(actions)

    return [
        len(actions),                 # activity level
        math.log(avg_value + 1),       # value scale
        avg_time,                      # timing behavior
        entropy                        # diversity
    ]
