import sys

print("=== Player Score Analytics ===")
if (len(sys.argv) == 1):
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    scores = []
    i = 1
    while i < len(sys.argv):
        try :
            score[i] = int(sys.argv[i])
            scores.append(score)
        except ValueError:
            print("Invalid score ignored:", sys.argv[i])
        i += 1

    if len(scores) == 0:
        print("No valid scores to process.")
    else:
        print("Scores processed:", scores)
        print("Total players:", len(scores))
        print("Total score:", sum(scores))
        print("Average score:", sum(scores) / len(scores))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))
