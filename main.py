# main.py
from src.detect_players import detect_players
from src.match_players import map_players
import json

def main():
    broadcast_video = "data/broadcast.mp4"
    tacticam_video = "data/tacticam.mp4"
    model_path = "models/player_detection_model.pt"

    # Detect players in both videos
    broadcast_players = detect_players(broadcast_video, model_path)
    tacticam_players = detect_players(tacticam_video, model_path)

    # Map players
    mapping = map_players(broadcast_players, tacticam_players)

    # Save results
    with open("outputs/mapped_players.json", "w") as f:
        json.dump(mapping, f, indent=4)

if __name__ == "__main__":
    main()
