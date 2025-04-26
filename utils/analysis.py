
def analyze_evaluator(scores):
    mean_score = scores.mean()
    if mean_score > 4.0:
        return "관대화 경향", "평가 점수가 전반적으로 높은 편입니다. 더 객관적인 평가를 위해 평가 기준을 재검토해보세요."
    elif mean_score < 2.0:
        return "가혹화 경향", "평가 점수가 전반적으로 낮은 편입니다. 피평가자의 긍정적인 면도 함께 고려해보세요."
    else:
        return "균형적 평가", "비교적 균형잡힌 평가를 하고 있습니다. 지금의 객관성을 유지하세요."
