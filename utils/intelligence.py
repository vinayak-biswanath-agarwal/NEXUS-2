class Intelligence:

    def __init__(self, metrics):

        self.metrics = metrics

    # ---------------------------------------
    # Portfolio Health
    # ---------------------------------------

    def portfolio_health(self):

        completed = self.metrics.completed_items()

        total = self.metrics.total_work_items()

        if total == 0:
            return 0

        return round((completed / total) * 100)

    # ---------------------------------------
    # Delivery Confidence
    # ---------------------------------------

    def delivery_confidence(self):

        blocked = self.metrics.blocked_items()

        bugs = self.metrics.total_bugs()

        score = 100

        score -= blocked * 5

        score -= bugs * 2

        return max(score, 0)

    # ---------------------------------------
    # Executive Score
    # ---------------------------------------

    def executive_score(self):

        portfolio = self.portfolio_health()

        confidence = self.delivery_confidence()

        return round(
            (portfolio + confidence) / 2
        )

    # ---------------------------------------
    # Executive Status
    # ---------------------------------------

    def executive_status(self):

        score = self.executive_score()

        if score >= 90:
            return "🟢 Excellent"

        if score >= 75:
            return "🟡 Good"

        if score >= 60:
            return "🟠 Needs Attention"

        return "🔴 Critical"

    # ---------------------------------------
    # Executive Message
    # ---------------------------------------

    def executive_message(self):

        status = self.executive_status()

        if status == "🟢 Excellent":
            return "Portfolio is progressing extremely well."

        if status == "🟡 Good":
            return "Portfolio is healthy with minor risks."

        if status == "🟠 Needs Attention":
            return "Executive monitoring recommended."

        return "Immediate leadership intervention required."