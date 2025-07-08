# src/match_players.py
import numpy as np

def map_players(broadcast_players, tacticam_players):
    mapping = {}
    for player_b in broadcast_players:
        best_match = None
        best_distance = float("inf")
        
        for player_t in tacticam_players:
           
            dist = np.linalg.norm(np.array(player_b['bbox'][:2]) - np.array(player_t['bbox'][:2]))
            if dist < best_distance:
                best_distance = dist
                best_match = player_t
        
        mapping[player_b['frame']] = best_match
    return mapping
